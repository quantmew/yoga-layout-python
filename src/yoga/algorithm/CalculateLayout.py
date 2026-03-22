# cython: infer_types=False
"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from math import isnan

from .._cython_compat import cython
from ..algorithm.AbsoluteLayout import layoutAbsoluteDescendants
from ..algorithm.Align import fallbackAlignment, resolveChildAlignment
from ..algorithm.Baseline import calculateBaseline, isBaselineLayout
from ..algorithm.BoundAxis import boundAxis, boundAxisWithinMinAndMax, paddingAndBorderForAxis
from ..algorithm.Cache import canUseCachedMeasurement
from ..algorithm.FlexDirection import (
    dimension,
    flexStartEdge,
    isRow,
    resolveCrossDirection,
    resolveDirection,
)
from ..algorithm.FlexLine import calculateFlexLine
from ..algorithm.PixelGrid import roundLayoutResultsToPixelGrid
from ..algorithm.SizingMode import SizingMode
from ..algorithm.TrailingPosition import needsTrailingPosition, setChildTrailingPosition
from ..event.event import (
    Event,
    EventData,
    LayoutData,
    LayoutPassEndData,
    LayoutPassReason,
    LayoutType,
    MeasureCallbackEndData,
    NodeLayoutData,
)
from ..node.LayoutResults import LayoutResults
from ..node.Node import Node
from ..numeric.Comparison import inexactEquals, isDefined, isUndefined, maxOrDefined, minOrDefined
from ..numeric.FloatMath import float32, floatDivision
from ..numeric.FloatOptional import FloatOptional
from ..numeric.FloatOptional import maxOrDefined as maxOrDefinedFloatOptional
from ..YGEnums import (
    YGAlign,
    YGDimension,
    YGDirection,
    YGDisplay,
    YGEdge,
    YGErrata,
    YGExperimentalFeature,
    YGFlexDirection,
    YGJustify,
    YGMeasureMode,
    YGOverflow,
    YGPositionType,
    YGWrap,
)

gCurrentGenerationCount = 0


@cython.locals(size=cython.double, margin=cython.double)
def constrainMaxSizeForMode(
    node: Node,
    direction: YGDirection,
    axis: YGFlexDirection,
    ownerAxisSize: float,
    ownerWidth: float,
    mode: SizingMode,
    size: float,
) -> tuple[SizingMode, float]:
    nodeStyle = node.style()
    dimensionValue = YGDimension.YGDimensionWidth if isRow(axis) else YGDimension.YGDimensionHeight
    maxDimension = nodeStyle.resolvedMaxDimension(
        direction,
        dimensionValue,
        ownerAxisSize,
        ownerWidth,
    )
    margin = nodeStyle.computeMarginForAxis(axis, ownerWidth)
    maxSize = maxDimension + FloatOptional(margin)
    if mode in (SizingMode.StretchFit, SizingMode.FitContent):
        size = size if maxSize.isUndefined() or size < maxSize.unwrap() else maxSize.unwrap()
    elif mode == SizingMode.MaxContent and maxSize.isDefined():
        mode = SizingMode.FitContent
        size = maxSize.unwrap()
    return mode, size


@cython.locals(
    mainAxisSize=cython.double,
    mainAxisOwnerSize=cython.double,
    childWidth=cython.double,
    childHeight=cython.double,
    marginRow=cython.double,
    marginColumn=cython.double,
    hasExactWidth=cython.bint,
    childWidthStretch=cython.bint,
    hasExactHeight=cython.bint,
    childHeightStretch=cython.bint,
    alignStretch=cython.bint,
)
def computeFlexBasisForChild(
    node: Node,
    child: Node,
    width: float,
    widthMode: SizingMode,
    height: float,
    ownerWidth: float,
    ownerHeight: float,
    heightMode: SizingMode,
    direction: YGDirection,
    layoutMarkerData: LayoutData,
    depth: int,
    generationCount: int,
) -> None:
    nodeStyle = node.style()
    childStyle = child.style()
    childLayout = child.getLayout()
    childConfig = child.getConfig()
    mainAxis = resolveDirection(nodeStyle.flexDirection(), direction)
    isMainAxisRow = isRow(mainAxis)
    mainAxisSize = width if isMainAxisRow else height
    mainAxisOwnerSize = ownerWidth if isMainAxisRow else ownerHeight
    childWidth = float("nan")
    childHeight = float("nan")
    resolvedFlexBasis = child.resolveFlexBasis(direction, mainAxis, mainAxisOwnerSize, ownerWidth)
    isRowStyleDimDefined = child.hasDefiniteLength(YGDimension.YGDimensionWidth, ownerWidth)
    isColumnStyleDimDefined = child.hasDefiniteLength(YGDimension.YGDimensionHeight, ownerHeight)
    overflow = nodeStyle.overflow()
    alignStretch = resolveChildAlignment(node, child) == YGAlign.YGAlignStretch

    if resolvedFlexBasis.isDefined() and isDefined(mainAxisSize):
        if childLayout.computedFlexBasis.isUndefined() or (
            childConfig.isExperimentalFeatureEnabled(YGExperimentalFeature.YGExperimentalFeatureWebFlexBasis)
            and childLayout.computedFlexBasisGeneration != generationCount
        ):
            paddingAndBorder = FloatOptional(paddingAndBorderForAxis(child, mainAxis, direction, ownerWidth))
            child.setLayoutComputedFlexBasis(
                maxOrDefinedFloatOptional(resolvedFlexBasis, paddingAndBorder)
            )
    elif isMainAxisRow and isRowStyleDimDefined:
        # The width is definite, so use that as the flex basis.
        paddingAndBorder = FloatOptional(paddingAndBorderForAxis(child, YGFlexDirection.YGFlexDirectionRow, direction, ownerWidth))
        child.setLayoutComputedFlexBasis(
            FloatOptional(
                maxOrDefined(
                    child.getResolvedDimension(direction, YGDimension.YGDimensionWidth, ownerWidth, ownerWidth).unwrap(),
                    paddingAndBorder.unwrap(),
                )
            )
        )
    elif (not isMainAxisRow) and isColumnStyleDimDefined:
        # The height is definite, so use that as the flex basis.
        paddingAndBorder = FloatOptional(paddingAndBorderForAxis(child, YGFlexDirection.YGFlexDirectionColumn, direction, ownerWidth))
        child.setLayoutComputedFlexBasis(
            FloatOptional(
                maxOrDefined(
                    child.getResolvedDimension(direction, YGDimension.YGDimensionHeight, ownerHeight, ownerWidth).unwrap(),
                    paddingAndBorder.unwrap(),
                )
            )
        )
    else:
        # Compute the flex basis and hypothetical main size (i.e. the clamped flex
        # basis).
        childWidthSizingMode = SizingMode.MaxContent
        childHeightSizingMode = SizingMode.MaxContent
        marginRow = childStyle.computeMarginForAxis(YGFlexDirection.YGFlexDirectionRow, ownerWidth)
        marginColumn = childStyle.computeMarginForAxis(YGFlexDirection.YGFlexDirectionColumn, ownerWidth)
        if isRowStyleDimDefined:
            childWidth = child.getResolvedDimension(direction, YGDimension.YGDimensionWidth, ownerWidth, ownerWidth).unwrap() + marginRow
            childWidthSizingMode = SizingMode.StretchFit
        if isColumnStyleDimDefined:
            childHeight = child.getResolvedDimension(direction, YGDimension.YGDimensionHeight, ownerHeight, ownerWidth).unwrap() + marginColumn
            childHeightSizingMode = SizingMode.StretchFit
        # The W3C spec doesn't say anything about the 'overflow' property, but all
        # major browsers appear to implement the following logic.
        if ((not isMainAxisRow) and overflow == YGOverflow.YGOverflowScroll) or (
            overflow != YGOverflow.YGOverflowScroll
        ):
            if isUndefined(childWidth) and isDefined(width):
                childWidth = width
                childWidthSizingMode = SizingMode.FitContent
        if (isMainAxisRow and overflow == YGOverflow.YGOverflowScroll) or (
            overflow != YGOverflow.YGOverflowScroll
        ):
            if isUndefined(childHeight) and isDefined(height):
                childHeight = height
                childHeightSizingMode = SizingMode.FitContent
        childAspectRatio = childStyle.aspectRatio()
        if childAspectRatio.isDefined():
            if (not isMainAxisRow) and childWidthSizingMode == SizingMode.StretchFit:
                childHeight = marginColumn + (childWidth - marginRow) / childAspectRatio.unwrap()
                childHeightSizingMode = SizingMode.StretchFit
            elif isMainAxisRow and childHeightSizingMode == SizingMode.StretchFit:
                childWidth = marginRow + (childHeight - marginColumn) * childAspectRatio.unwrap()
                childWidthSizingMode = SizingMode.StretchFit
        # If child has no defined size in the cross axis and is set to stretch, set
        # the cross axis to be measured exactly with the available inner width
        hasExactWidth = isDefined(width) and widthMode == SizingMode.StretchFit
        childWidthStretch = alignStretch and childWidthSizingMode != SizingMode.StretchFit
        if (not isMainAxisRow) and (not isRowStyleDimDefined) and hasExactWidth and childWidthStretch:
            childWidth = width
            childWidthSizingMode = SizingMode.StretchFit
            if childAspectRatio.isDefined():
                childHeight = (childWidth - marginRow) / childAspectRatio.unwrap()
                childHeightSizingMode = SizingMode.StretchFit
        hasExactHeight = isDefined(height) and heightMode == SizingMode.StretchFit
        childHeightStretch = alignStretch and childHeightSizingMode != SizingMode.StretchFit
        if isMainAxisRow and (not isColumnStyleDimDefined) and hasExactHeight and childHeightStretch:
            childHeight = height
            childHeightSizingMode = SizingMode.StretchFit
            if childAspectRatio.isDefined():
                childWidth = (childHeight - marginColumn) * childAspectRatio.unwrap()
                childWidthSizingMode = SizingMode.StretchFit
        childWidthSizingMode, childWidth = constrainMaxSizeForMode(
            child, direction, YGFlexDirection.YGFlexDirectionRow, ownerWidth, ownerWidth, childWidthSizingMode, childWidth
        )
        childHeightSizingMode, childHeight = constrainMaxSizeForMode(
            child, direction, YGFlexDirection.YGFlexDirectionColumn, ownerHeight, ownerWidth, childHeightSizingMode, childHeight
        )
        # Measure the child
        calculateLayoutInternal(
            child,
            childWidth,
            childHeight,
            direction,
            childWidthSizingMode,
            childHeightSizingMode,
            ownerWidth,
            ownerHeight,
            False,
            LayoutPassReason.kMeasureChild,
            layoutMarkerData,
            depth,
            generationCount,
        )
        child.setLayoutComputedFlexBasis(
            FloatOptional(
                maxOrDefined(
                    child.getLayout().measuredDimension(
                        YGDimension.YGDimensionWidth if isMainAxisRow else YGDimension.YGDimensionHeight
                    ),
                    paddingAndBorderForAxis(child, mainAxis, direction, ownerWidth),
                )
            )
        )
    child.setLayoutComputedFlexBasisGeneration(generationCount)


def measureNodeWithMeasureFunc(
    node: Node,
    direction: YGDirection,
    availableWidth: float,
    availableHeight: float,
    widthSizingMode: SizingMode,
    heightSizingMode: SizingMode,
    ownerWidth: float,
    ownerHeight: float,
    layoutMarkerData: LayoutData,
    reason: LayoutPassReason,
) -> None:
    if widthSizingMode == SizingMode.MaxContent:
        availableWidth = float("nan")
    if heightSizingMode == SizingMode.MaxContent:
        availableHeight = float("nan")
    layout = node.getLayout()
    paddingAndBorderAxisRow = (
        layout.padding(YGEdge.YGEdgeLeft)
        + layout.padding(YGEdge.YGEdgeRight)
        + layout.border(YGEdge.YGEdgeLeft)
        + layout.border(YGEdge.YGEdgeRight)
    )
    paddingAndBorderAxisColumn = (
        layout.padding(YGEdge.YGEdgeTop)
        + layout.padding(YGEdge.YGEdgeBottom)
        + layout.border(YGEdge.YGEdgeTop)
        + layout.border(YGEdge.YGEdgeBottom)
    )
    innerWidth = availableWidth if isnan(availableWidth) else maxOrDefined(0.0, availableWidth - paddingAndBorderAxisRow)
    innerHeight = availableHeight if isnan(availableHeight) else maxOrDefined(0.0, availableHeight - paddingAndBorderAxisColumn)
    if widthSizingMode == SizingMode.StretchFit and heightSizingMode == SizingMode.StretchFit:
        node.setLayoutMeasuredDimension(boundAxis(node, YGFlexDirection.YGFlexDirectionRow, direction, availableWidth, ownerWidth, ownerWidth), YGDimension.YGDimensionWidth)
        node.setLayoutMeasuredDimension(boundAxis(node, YGFlexDirection.YGFlexDirectionColumn, direction, availableHeight, ownerHeight, ownerWidth), YGDimension.YGDimensionHeight)
    else:
        Event.publish(node, Event.MeasureCallbackStart, EventData())
        measuredSize = node.measure(innerWidth, YGMeasureMode.YGMeasureModeExactly if widthSizingMode == SizingMode.StretchFit else (YGMeasureMode.YGMeasureModeAtMost if widthSizingMode == SizingMode.FitContent else YGMeasureMode.YGMeasureModeUndefined), innerHeight, YGMeasureMode.YGMeasureModeExactly if heightSizingMode == SizingMode.StretchFit else (YGMeasureMode.YGMeasureModeAtMost if heightSizingMode == SizingMode.FitContent else YGMeasureMode.YGMeasureModeUndefined))
        layoutMarkerData.measureCallbacks += 1
        layoutMarkerData.measureCallbackReasonsCount[int(reason)] += 1
        Event.publish(
            node,
            Event.MeasureCallbackEnd,
            MeasureCallbackEndData(
                width=innerWidth,
                widthMeasureMode=YGMeasureMode.YGMeasureModeExactly if widthSizingMode == SizingMode.StretchFit else (YGMeasureMode.YGMeasureModeAtMost if widthSizingMode == SizingMode.FitContent else YGMeasureMode.YGMeasureModeUndefined),
                height=innerHeight,
                heightMeasureMode=YGMeasureMode.YGMeasureModeExactly if heightSizingMode == SizingMode.StretchFit else (YGMeasureMode.YGMeasureModeAtMost if heightSizingMode == SizingMode.FitContent else YGMeasureMode.YGMeasureModeUndefined),
                measuredWidth=measuredSize.width,
                measuredHeight=measuredSize.height,
                reason=reason,
            ),
        )
        node.setLayoutMeasuredDimension(
            boundAxis(
                node,
                YGFlexDirection.YGFlexDirectionRow,
                direction,
                measuredSize.width + paddingAndBorderAxisRow if widthSizingMode in (SizingMode.MaxContent, SizingMode.FitContent) else availableWidth,
                ownerWidth,
                ownerWidth,
            ),
            YGDimension.YGDimensionWidth,
        )
        node.setLayoutMeasuredDimension(
            boundAxis(
                node,
                YGFlexDirection.YGFlexDirectionColumn,
                direction,
                measuredSize.height + paddingAndBorderAxisColumn if heightSizingMode in (SizingMode.MaxContent, SizingMode.FitContent) else availableHeight,
                ownerHeight,
                ownerWidth,
            ),
            YGDimension.YGDimensionHeight,
        )


def measureNodeWithoutChildren(
    node: Node,
    direction: YGDirection,
    availableWidth: float,
    availableHeight: float,
    widthSizingMode: SizingMode,
    heightSizingMode: SizingMode,
    ownerWidth: float,
    ownerHeight: float,
) -> None:
    layout = node.getLayout()
    width = availableWidth
    if widthSizingMode in (SizingMode.MaxContent, SizingMode.FitContent):
        width = layout.padding(YGEdge.YGEdgeLeft) + layout.padding(YGEdge.YGEdgeRight) + layout.border(YGEdge.YGEdgeLeft) + layout.border(YGEdge.YGEdgeRight)
    node.setLayoutMeasuredDimension(boundAxis(node, YGFlexDirection.YGFlexDirectionRow, direction, width, ownerWidth, ownerWidth), YGDimension.YGDimensionWidth)
    height = availableHeight
    if heightSizingMode in (SizingMode.MaxContent, SizingMode.FitContent):
        height = layout.padding(YGEdge.YGEdgeTop) + layout.padding(YGEdge.YGEdgeBottom) + layout.border(YGEdge.YGEdgeTop) + layout.border(YGEdge.YGEdgeBottom)
    node.setLayoutMeasuredDimension(boundAxis(node, YGFlexDirection.YGFlexDirectionColumn, direction, height, ownerHeight, ownerWidth), YGDimension.YGDimensionHeight)


def isFixedSize(dim: float, sizingMode: SizingMode) -> bool:
    return sizingMode == SizingMode.StretchFit or (dim == dim and sizingMode == SizingMode.FitContent and dim <= 0.0)


def measureNodeWithFixedSize(
    node: Node,
    direction: YGDirection,
    availableWidth: float,
    availableHeight: float,
    widthSizingMode: SizingMode,
    heightSizingMode: SizingMode,
    ownerWidth: float,
    ownerHeight: float,
) -> bool:
    if isFixedSize(availableWidth, widthSizingMode) and isFixedSize(availableHeight, heightSizingMode):
        node.setLayoutMeasuredDimension(boundAxis(node, YGFlexDirection.YGFlexDirectionRow, direction, 0.0 if isnan(availableWidth) or (widthSizingMode == SizingMode.FitContent and availableWidth < 0.0) else availableWidth, ownerWidth, ownerWidth), YGDimension.YGDimensionWidth)
        node.setLayoutMeasuredDimension(boundAxis(node, YGFlexDirection.YGFlexDirectionColumn, direction, 0.0 if isnan(availableHeight) or (heightSizingMode == SizingMode.FitContent and availableHeight < 0.0) else availableHeight, ownerHeight, ownerWidth), YGDimension.YGDimensionHeight)
        return True
    return False


def zeroOutLayoutRecursively(node: Node) -> None:
    node.setLayout(LayoutResults())
    node.setLayoutDimension(0, YGDimension.YGDimensionWidth)
    node.setLayoutDimension(0, YGDimension.YGDimensionHeight)
    node.setHasNewLayout(True)
    node.cloneChildrenIfNeeded()
    for child in node.getChildren():
        zeroOutLayoutRecursively(child)


def cleanupContentsNodesRecursively(node: Node) -> None:
    if node.hasContentsChildren():
        node.cloneContentsChildrenIfNeeded()
        for child in node.getChildren():
            if child.style().display().name.endswith("Contents"):
                child.setLayout(LayoutResults())
                child.setLayoutDimension(0, YGDimension.YGDimensionWidth)
                child.setLayoutDimension(0, YGDimension.YGDimensionHeight)
                child.setHasNewLayout(True)
                child.setDirty(False)
                child.cloneChildrenIfNeeded()
                cleanupContentsNodesRecursively(child)


def calculateAvailableInnerDimension(
    node: Node,
    direction: YGDirection,
    dimensionValue: YGDimension,
    availableDim: float,
    paddingAndBorder: float,
    ownerDim: float,
    ownerWidth: float,
) -> float:
    availableInnerDim = availableDim - paddingAndBorder
    if availableInnerDim == availableInnerDim:
        minDimensionOptional = node.style().resolvedMinDimension(direction, dimensionValue, ownerDim, ownerWidth)
        minInnerDim = 0.0 if minDimensionOptional.isUndefined() else minDimensionOptional.unwrap() - paddingAndBorder
        maxDimensionOptional = node.style().resolvedMaxDimension(direction, dimensionValue, ownerDim, ownerWidth)
        maxInnerDim = float("inf") if maxDimensionOptional.isUndefined() else maxDimensionOptional.unwrap() - paddingAndBorder
        availableInnerDim = maxOrDefined(min(availableInnerDim, maxInnerDim), minInnerDim)
    return availableInnerDim


def computeFlexBasisForChildren(
    node: Node,
    availableInnerWidth: float,
    availableInnerHeight: float,
    widthSizingMode: SizingMode,
    heightSizingMode: SizingMode,
    direction: YGDirection,
    mainAxis: YGFlexDirection,
    performLayout: bool,
    layoutMarkerData: LayoutData,
    depth: int,
    generationCount: int,
) -> float:
    totalOuterFlexBasis = float32(0.0)
    singleFlexChild = None
    children = list(node.getLayoutChildren())
    sizingModeMainDim = widthSizingMode if isRow(mainAxis) else heightSizingMode
    if sizingModeMainDim == SizingMode.StretchFit:
        for child in children:
            if child.isNodeFlexible():
                if singleFlexChild is not None or child.resolveFlexGrow() == 0.0 or child.resolveFlexShrink() == 0.0:
                    singleFlexChild = None
                    break
                singleFlexChild = child
    for child in children:
        child.processDimensions()
        if child.style().display().name.endswith("None"):
            zeroOutLayoutRecursively(child)
            child.setHasNewLayout(True)
            child.setDirty(False)
            continue
        if performLayout:
            childDirection = child.resolveDirection(direction)
            child.setPosition(childDirection, availableInnerWidth, availableInnerHeight)
        if child.style().positionType().name.endswith("Absolute"):
            continue
        if child == singleFlexChild:
            child.setLayoutComputedFlexBasisGeneration(generationCount)
            child.setLayoutComputedFlexBasis(FloatOptional(0.0))
        else:
            computeFlexBasisForChild(
                node,
                child,
                availableInnerWidth,
                widthSizingMode,
                availableInnerHeight,
                availableInnerWidth,
                availableInnerHeight,
                heightSizingMode,
                direction,
                layoutMarkerData,
                depth,
                generationCount,
            )
        totalOuterFlexBasis = float32(
            totalOuterFlexBasis
            + float32(
                child.getLayout().computedFlexBasis.unwrap()
                + child.style().computeMarginForAxis(mainAxis, availableInnerWidth)
            )
        )
    return totalOuterFlexBasis


def distributeFreeSpaceFirstPass(
    flexLine,
    direction: YGDirection,
    mainAxis: YGFlexDirection,
    ownerWidth: float,
    mainAxisOwnerSize: float,
    availableInnerMainDim: float,
    availableInnerWidth: float,
) -> None:
    deltaFreeSpace = float32(0.0)
    for currentLineChild in flexLine.itemsInFlow:
        childFlexBasis = float32(
            boundAxisWithinMinAndMax(
            currentLineChild,
            direction,
            mainAxis,
            currentLineChild.getLayout().computedFlexBasis,
            mainAxisOwnerSize,
            ownerWidth,
            ).unwrap()
        )
        if flexLine.layout.remainingFreeSpace < 0:
            flexShrinkScaledFactor = float32(
                -currentLineChild.resolveFlexShrink() * childFlexBasis
            )
            if flexShrinkScaledFactor == flexShrinkScaledFactor and flexShrinkScaledFactor != 0:
                shrinkRatio = float32(
                    floatDivision(
                        flexLine.layout.remainingFreeSpace,
                        flexLine.layout.totalFlexShrinkScaledFactors,
                    )
                )
                baseMainSize = float32(
                    childFlexBasis
                    + float32(shrinkRatio * flexShrinkScaledFactor)
                )
                boundMainSize = boundAxis(currentLineChild, mainAxis, direction, baseMainSize, availableInnerMainDim, availableInnerWidth)
                if baseMainSize == baseMainSize and boundMainSize == boundMainSize and baseMainSize != boundMainSize:
                    deltaFreeSpace = float32(
                        deltaFreeSpace + float32(boundMainSize - childFlexBasis)
                    )
                    flexLine.layout.totalFlexShrinkScaledFactors = float32(
                        flexLine.layout.totalFlexShrinkScaledFactors
                        - float32(
                            -currentLineChild.resolveFlexShrink()
                            * currentLineChild.getLayout().computedFlexBasis.unwrap()
                        )
                    )
        elif flexLine.layout.remainingFreeSpace == flexLine.layout.remainingFreeSpace and flexLine.layout.remainingFreeSpace > 0:
            flexGrowFactor = currentLineChild.resolveFlexGrow()
            if flexGrowFactor == flexGrowFactor and flexGrowFactor != 0:
                growRatio = float32(
                    floatDivision(
                        flexLine.layout.remainingFreeSpace,
                        flexLine.layout.totalFlexGrowFactors,
                    )
                )
                baseMainSize = float32(
                    childFlexBasis
                    + float32(growRatio * flexGrowFactor)
                )
                boundMainSize = boundAxis(currentLineChild, mainAxis, direction, baseMainSize, availableInnerMainDim, availableInnerWidth)
                if baseMainSize == baseMainSize and boundMainSize == boundMainSize and baseMainSize != boundMainSize:
                    deltaFreeSpace = float32(
                        deltaFreeSpace + float32(boundMainSize - childFlexBasis)
                    )
                    flexLine.layout.totalFlexGrowFactors = float32(
                        flexLine.layout.totalFlexGrowFactors - flexGrowFactor
                    )
    flexLine.layout.remainingFreeSpace = float32(
        flexLine.layout.remainingFreeSpace - deltaFreeSpace
    )


@cython.locals(
    deltaFreeSpace=cython.double,
    childFlexBasis=cython.double,
    updatedMainSize=cython.double,
    flexShrinkScaledFactor=cython.double,
    childSize=cython.double,
    flexGrowFactor=cython.double,
    growRatio=cython.double,
    marginMain=cython.double,
    marginCross=cython.double,
    childCrossSize=cython.double,
    childMainSize=cython.double,
    hasDefiniteCrossLength=cython.bint,
    crossStartMarginAuto=cython.bint,
    crossEndMarginAuto=cython.bint,
    requiresStretchLayout=cython.bint,
    isNodeFlexWrap=cython.bint,
)
def distributeFreeSpaceSecondPass(
    flexLine,
    node: Node,
    mainAxis: YGFlexDirection,
    crossAxis: YGFlexDirection,
    direction: YGDirection,
    ownerWidth: float,
    mainAxisOwnerSize: float,
    availableInnerMainDim: float,
    availableInnerCrossDim: float,
    availableInnerWidth: float,
    availableInnerHeight: float,
    mainAxisOverflows: bool,
    sizingModeCrossDim: SizingMode,
    performLayout: bool,
    layoutMarkerData: LayoutData,
    depth: int,
    generationCount: int,
) -> float:
    deltaFreeSpace = float32(0.0)
    isMainAxisRow = isRow(mainAxis)
    nodeStyle = node.style()
    nodeLayout = node.getLayout()
    isNodeFlexWrap = nodeStyle.flexWrap() != YGWrap.YGWrapNoWrap
    for currentLineChild in flexLine.itemsInFlow:
        childStyle = currentLineChild.style()
        childLayout = currentLineChild.getLayout()
        childFlexBasis = float32(
            boundAxisWithinMinAndMax(
            currentLineChild,
            direction,
            mainAxis,
            childLayout.computedFlexBasis,
            mainAxisOwnerSize,
            ownerWidth,
            ).unwrap()
        )
        updatedMainSize = childFlexBasis
        if flexLine.layout.remainingFreeSpace == flexLine.layout.remainingFreeSpace and flexLine.layout.remainingFreeSpace < 0:
            flexShrinkScaledFactor = float32(
                -currentLineChild.resolveFlexShrink() * childFlexBasis
            )
            if flexShrinkScaledFactor != 0:
                if flexLine.layout.totalFlexShrinkScaledFactors == 0:
                    childSize = float32(childFlexBasis + flexShrinkScaledFactor)
                else:
                    shrinkRatio = float32(
                        floatDivision(
                            flexLine.layout.remainingFreeSpace,
                            flexLine.layout.totalFlexShrinkScaledFactors,
                        )
                    )
                    childSize = float32(
                        childFlexBasis
                        + float32(shrinkRatio * flexShrinkScaledFactor)
                    )
                updatedMainSize = float32(
                    boundAxis(
                        currentLineChild,
                        mainAxis,
                        direction,
                        childSize,
                        availableInnerMainDim,
                        availableInnerWidth,
                    )
                )
        elif flexLine.layout.remainingFreeSpace == flexLine.layout.remainingFreeSpace and flexLine.layout.remainingFreeSpace > 0:
            flexGrowFactor = currentLineChild.resolveFlexGrow()
            if flexGrowFactor == flexGrowFactor and flexGrowFactor != 0:
                growRatio = float32(
                    floatDivision(
                        flexLine.layout.remainingFreeSpace,
                        flexLine.layout.totalFlexGrowFactors,
                    )
                )
                updatedMainSize = float32(
                    boundAxis(
                        currentLineChild,
                        mainAxis,
                        direction,
                        float32(
                            childFlexBasis
                            + float32(growRatio * flexGrowFactor)
                        ),
                        availableInnerMainDim,
                        availableInnerWidth,
                    )
                )
        deltaFreeSpace = float32(
            deltaFreeSpace + float32(updatedMainSize - childFlexBasis)
        )
        marginMain = childStyle.computeMarginForAxis(mainAxis, availableInnerWidth)
        marginCross = childStyle.computeMarginForAxis(crossAxis, availableInnerWidth)
        childCrossSize = float("nan")
        childMainSize = updatedMainSize + marginMain
        childMainSizingMode = SizingMode.StretchFit
        childAspectRatio = childStyle.aspectRatio()
        alignChild = resolveChildAlignment(node, currentLineChild)
        crossStartMarginAuto = childStyle.flexStartMarginIsAuto(crossAxis, direction)
        crossEndMarginAuto = childStyle.flexEndMarginIsAuto(crossAxis, direction)
        if childAspectRatio.isDefined():
            childCrossSize = (
                (childMainSize - marginMain) / childAspectRatio.unwrap()
                if isMainAxisRow
                else (childMainSize - marginMain) * childAspectRatio.unwrap()
            )
            childCrossSizingMode = SizingMode.StretchFit
            childCrossSize += marginCross
        elif (
            availableInnerCrossDim == availableInnerCrossDim
            and not currentLineChild.hasDefiniteLength(
                YGDimension.YGDimensionHeight if isMainAxisRow else YGDimension.YGDimensionWidth,
                availableInnerCrossDim,
            )
            and sizingModeCrossDim == SizingMode.StretchFit
            and not (isNodeFlexWrap and mainAxisOverflows)
            and alignChild == YGAlign.YGAlignStretch
            and not crossStartMarginAuto
            and not crossEndMarginAuto
        ):
            childCrossSize = availableInnerCrossDim
            childCrossSizingMode = SizingMode.StretchFit
        elif not currentLineChild.hasDefiniteLength(
            YGDimension.YGDimensionHeight if isMainAxisRow else YGDimension.YGDimensionWidth,
            availableInnerCrossDim,
        ):
            childCrossSize = availableInnerCrossDim
            childCrossSizingMode = SizingMode.MaxContent if isnan(childCrossSize) else SizingMode.FitContent
        else:
            childCrossSize = currentLineChild.getResolvedDimension(
                direction,
                YGDimension.YGDimensionHeight if isMainAxisRow else YGDimension.YGDimensionWidth,
                availableInnerCrossDim,
                availableInnerWidth,
            ).unwrap() + marginCross
            isLoosePercentageMeasurement = (
                currentLineChild.getProcessedDimension(
                    YGDimension.YGDimensionHeight if isMainAxisRow else YGDimension.YGDimensionWidth
                ).isPercent()
                and sizingModeCrossDim != SizingMode.StretchFit
            )
            childCrossSizingMode = (
                SizingMode.MaxContent
                if isnan(childCrossSize) or isLoosePercentageMeasurement
                else SizingMode.StretchFit
            )
        childMainSizingMode, childMainSize = constrainMaxSizeForMode(currentLineChild, direction, mainAxis, availableInnerMainDim, availableInnerWidth, childMainSizingMode, childMainSize)
        childCrossSizingMode, childCrossSize = constrainMaxSizeForMode(currentLineChild, direction, crossAxis, availableInnerCrossDim, availableInnerWidth, childCrossSizingMode, childCrossSize)
        requiresStretchLayout = (
            not currentLineChild.hasDefiniteLength(YGDimension.YGDimensionHeight if isMainAxisRow else YGDimension.YGDimensionWidth, availableInnerCrossDim)
            and alignChild == YGAlign.YGAlignStretch
            and not crossStartMarginAuto
            and not crossEndMarginAuto
        )
        childWidth = childMainSize if isMainAxisRow else childCrossSize
        childHeight = childMainSize if not isMainAxisRow else childCrossSize
        childWidthSizingMode = childMainSizingMode if isMainAxisRow else childCrossSizingMode
        childHeightSizingMode = childMainSizingMode if not isMainAxisRow else childCrossSizingMode
        isLayoutPass = performLayout and not requiresStretchLayout
        calculateLayoutInternal(
            currentLineChild,
            childWidth,
            childHeight,
            node.getLayout().direction(),
            childWidthSizingMode,
            childHeightSizingMode,
            availableInnerWidth,
            availableInnerHeight,
            isLayoutPass,
            LayoutPassReason.kFlexLayout if isLayoutPass else LayoutPassReason.kFlexMeasure,
            layoutMarkerData,
            depth,
            generationCount,
        )
        nodeLayout.setHadOverflow(nodeLayout.hadOverflow() or childLayout.hadOverflow())
    return deltaFreeSpace


def resolveFlexibleLength(
    node: Node,
    flexLine,
    mainAxis: YGFlexDirection,
    crossAxis: YGFlexDirection,
    direction: YGDirection,
    ownerWidth: float,
    mainAxisOwnerSize: float,
    availableInnerMainDim: float,
    availableInnerCrossDim: float,
    availableInnerWidth: float,
    availableInnerHeight: float,
    mainAxisOverflows: bool,
    sizingModeCrossDim: SizingMode,
    performLayout: bool,
    layoutMarkerData: LayoutData,
    depth: int,
    generationCount: int,
) -> None:
    originalFreeSpace = flexLine.layout.remainingFreeSpace
    distributeFreeSpaceFirstPass(
        flexLine,
        direction,
        mainAxis,
        ownerWidth,
        mainAxisOwnerSize,
        availableInnerMainDim,
        availableInnerWidth,
    )
    distributedFreeSpace = distributeFreeSpaceSecondPass(
        flexLine,
        node,
        mainAxis,
        crossAxis,
        direction,
        ownerWidth,
        mainAxisOwnerSize,
        availableInnerMainDim,
        availableInnerCrossDim,
        availableInnerWidth,
        availableInnerHeight,
        mainAxisOverflows,
        sizingModeCrossDim,
        performLayout,
        layoutMarkerData,
        depth,
        generationCount,
    )
    flexLine.layout.remainingFreeSpace = float32(
        originalFreeSpace - distributedFreeSpace
    )


@cython.locals(
    leadingPaddingAndBorderMain=cython.double,
    trailingPaddingAndBorderMain=cython.double,
    gap=cython.double,
    minAvailableMainDim=cython.double,
    occupiedSpaceByChildNodes=cython.double,
    leadingMainDim=cython.double,
    betweenMainDim=cython.double,
    maxAscentForCurrentLine=cython.double,
    maxDescentForCurrentLine=cython.double,
    lastChildIndex=cython.Py_ssize_t,
    canSkipFlex=cython.bint,
    ascent=cython.double,
    descent=cython.double,
    startMarginAuto=cython.bint,
    endMarginAuto=cython.bint,
)
def justifyMainAxis(
    node: Node,
    flexLine,
    mainAxis: YGFlexDirection,
    crossAxis: YGFlexDirection,
    direction: YGDirection,
    sizingModeMainDim: SizingMode,
    sizingModeCrossDim: SizingMode,
    mainAxisOwnerSize: float,
    ownerWidth: float,
    availableInnerMainDim: float,
    availableInnerCrossDim: float,
    availableInnerWidth: float,
    performLayout: bool,
) -> None:
    style = node.style()
    leadingPaddingAndBorderMain = style.computeFlexStartPaddingAndBorder(mainAxis, direction, ownerWidth)
    trailingPaddingAndBorderMain = style.computeFlexEndPaddingAndBorder(mainAxis, direction, ownerWidth)
    gap = style.computeGapForAxis(mainAxis, availableInnerMainDim)
    if sizingModeMainDim == SizingMode.FitContent and flexLine.layout.remainingFreeSpace > 0:
        if style.minDimension(dimension(mainAxis)).isDefined() and style.resolvedMinDimension(
            direction, dimension(mainAxis), mainAxisOwnerSize, ownerWidth
        ).isDefined():
            minAvailableMainDim = (
                style.resolvedMinDimension(direction, dimension(mainAxis), mainAxisOwnerSize, ownerWidth).unwrap()
                - leadingPaddingAndBorderMain
                - trailingPaddingAndBorderMain
            )
            occupiedSpaceByChildNodes = availableInnerMainDim - flexLine.layout.remainingFreeSpace
            flexLine.layout.remainingFreeSpace = maxOrDefined(0.0, minAvailableMainDim - occupiedSpaceByChildNodes)
        else:
            flexLine.layout.remainingFreeSpace = 0.0
    leadingMainDim = 0.0
    betweenMainDim = gap
    nodeJustifyContent = style.justifyContent()
    justifyContent = (
        nodeJustifyContent
        if flexLine.layout.remainingFreeSpace >= 0
        else fallbackAlignment(nodeJustifyContent)
    )
    if flexLine.numberOfAutoMargins == 0:
        if justifyContent == YGJustify.YGJustifyCenter:
            leadingMainDim = flexLine.layout.remainingFreeSpace / 2
        elif justifyContent == YGJustify.YGJustifyFlexEnd:
            leadingMainDim = flexLine.layout.remainingFreeSpace
        elif justifyContent == YGJustify.YGJustifySpaceBetween:
            if len(flexLine.itemsInFlow) > 1:
                betweenMainDim += flexLine.layout.remainingFreeSpace / float(len(flexLine.itemsInFlow) - 1)
        elif justifyContent == YGJustify.YGJustifySpaceEvenly:
            leadingMainDim = floatDivision(
                flexLine.layout.remainingFreeSpace,
                float(len(flexLine.itemsInFlow) + 1),
            )
            betweenMainDim += leadingMainDim
        elif justifyContent == YGJustify.YGJustifySpaceAround:
            leadingMainDim = 0.5 * floatDivision(
                flexLine.layout.remainingFreeSpace,
                float(len(flexLine.itemsInFlow)),
            )
            betweenMainDim += leadingMainDim * 2
    flexLine.layout.mainDim = leadingPaddingAndBorderMain + leadingMainDim
    flexLine.layout.crossDim = 0.0
    maxAscentForCurrentLine = 0.0
    maxDescentForCurrentLine = 0.0
    nodeBaselineLayout = isBaselineLayout(node)
    lastChildIndex = len(flexLine.itemsInFlow) - 1
    for child in flexLine.itemsInFlow:
        childLayout = child.getLayout()
        childStyle = child.style()
        startMarginAuto = childStyle.flexStartMarginIsAuto(mainAxis, direction)
        endMarginAuto = childStyle.flexEndMarginIsAuto(mainAxis, direction)
        if startMarginAuto and flexLine.layout.remainingFreeSpace > 0.0:
            flexLine.layout.mainDim += flexLine.layout.remainingFreeSpace / float(flexLine.numberOfAutoMargins)
        if performLayout:
            child.setLayoutPosition(
                childLayout.position(flexStartEdge(mainAxis)) + flexLine.layout.mainDim,
                flexStartEdge(mainAxis),
            )
        if lastChildIndex > 0 and child is not flexLine.itemsInFlow[lastChildIndex]:
            flexLine.layout.mainDim += betweenMainDim
        if endMarginAuto and flexLine.layout.remainingFreeSpace > 0.0:
            flexLine.layout.mainDim += flexLine.layout.remainingFreeSpace / float(flexLine.numberOfAutoMargins)
        canSkipFlex = (not performLayout) and sizingModeCrossDim == SizingMode.StretchFit
        if canSkipFlex:
            flexLine.layout.mainDim = float32(
                flexLine.layout.mainDim
                + childStyle.computeMarginForAxis(mainAxis, availableInnerWidth)
                + childLayout.computedFlexBasis.unwrap()
            )
            flexLine.layout.crossDim = availableInnerCrossDim
        else:
            flexLine.layout.mainDim += child.dimensionWithMargin(mainAxis, availableInnerWidth)
            if nodeBaselineLayout:
                ascent = calculateBaseline(child) + childStyle.computeFlexStartMargin(
                    YGFlexDirection.YGFlexDirectionColumn, direction, availableInnerWidth
                )
                descent = (
                    childLayout.measuredDimension(YGDimension.YGDimensionHeight)
                    + childStyle.computeMarginForAxis(YGFlexDirection.YGFlexDirectionColumn, availableInnerWidth)
                    - ascent
                )
                maxAscentForCurrentLine = maxOrDefined(maxAscentForCurrentLine, ascent)
                maxDescentForCurrentLine = maxOrDefined(maxDescentForCurrentLine, descent)
            else:
                flexLine.layout.crossDim = maxOrDefined(
                    flexLine.layout.crossDim, child.dimensionWithMargin(crossAxis, availableInnerWidth)
                )
    flexLine.layout.mainDim += trailingPaddingAndBorderMain
    if nodeBaselineLayout:
        flexLine.layout.crossDim = maxAscentForCurrentLine + maxDescentForCurrentLine


def calculateLayout(node: Node, ownerWidth: float, ownerHeight: float, ownerDirection: YGDirection) -> None:
    global gCurrentGenerationCount
    Event.publish(node, Event.LayoutPassStart, EventData())
    layoutMarkerData = LayoutData()
    gCurrentGenerationCount += 1
    node.processDimensions()
    direction = node.resolveDirection(ownerDirection)
    style = node.style()
    width = float("nan")
    widthSizingMode = SizingMode.MaxContent
    if node.hasDefiniteLength(YGDimension.YGDimensionWidth, ownerWidth):
        width = node.getResolvedDimension(direction, YGDimension.YGDimensionWidth, ownerWidth, ownerWidth).unwrap() + node.style().computeMarginForAxis(YGFlexDirection.YGFlexDirectionRow, ownerWidth)
        widthSizingMode = SizingMode.StretchFit
    elif style.resolvedMaxDimension(direction, YGDimension.YGDimensionWidth, ownerWidth, ownerWidth).isDefined():
        width = style.resolvedMaxDimension(direction, YGDimension.YGDimensionWidth, ownerWidth, ownerWidth).unwrap()
        widthSizingMode = SizingMode.FitContent
    else:
        width = ownerWidth
        widthSizingMode = SizingMode.MaxContent if isnan(width) else SizingMode.StretchFit
    height = float("nan")
    heightSizingMode = SizingMode.MaxContent
    if node.hasDefiniteLength(YGDimension.YGDimensionHeight, ownerHeight):
        height = node.getResolvedDimension(direction, YGDimension.YGDimensionHeight, ownerHeight, ownerWidth).unwrap() + node.style().computeMarginForAxis(YGFlexDirection.YGFlexDirectionColumn, ownerWidth)
        heightSizingMode = SizingMode.StretchFit
    elif style.resolvedMaxDimension(direction, YGDimension.YGDimensionHeight, ownerHeight, ownerWidth).isDefined():
        height = style.resolvedMaxDimension(direction, YGDimension.YGDimensionHeight, ownerHeight, ownerWidth).unwrap()
        heightSizingMode = SizingMode.FitContent
    else:
        height = ownerHeight
        heightSizingMode = SizingMode.MaxContent if isnan(height) else SizingMode.StretchFit
    if calculateLayoutInternal(
        node,
        width,
        height,
        ownerDirection,
        widthSizingMode,
        heightSizingMode,
        ownerWidth,
        ownerHeight,
        True,
        LayoutPassReason.kInitial,
        layoutMarkerData,
        0,
        gCurrentGenerationCount,
    ):
        node.setPosition(node.getLayout().direction(), ownerWidth, ownerHeight)
        roundLayoutResultsToPixelGrid(node, 0.0, 0.0)
    Event.publish(node, Event.LayoutPassEnd, LayoutPassEndData(layoutMarkerData))


def calculateLayoutImpl(
    node: Node,
    availableWidth: float,
    availableHeight: float,
    ownerDirection: YGDirection,
    widthSizingMode: SizingMode,
    heightSizingMode: SizingMode,
    ownerWidth: float,
    ownerHeight: float,
    performLayout: bool,
    reason: LayoutPassReason,
    layoutMarkerData: LayoutData,
    depth: int,
    generationCount: int,
) -> None:
    if isnan(availableWidth):
        assert widthSizingMode == SizingMode.MaxContent
    if isnan(availableHeight):
        assert heightSizingMode == SizingMode.MaxContent
    if performLayout:
        layoutMarkerData.layouts += 1
    else:
        layoutMarkerData.measures += 1
    style = node.style()
    direction = node.resolveDirection(ownerDirection)
    node.setLayoutDirection(direction)
    flexRowDirection = resolveDirection(YGFlexDirection.YGFlexDirectionRow, direction)
    flexColumnDirection = resolveDirection(YGFlexDirection.YGFlexDirectionColumn, direction)
    startEdge = YGEdge.YGEdgeLeft if direction == YGDirection.YGDirectionLTR else YGEdge.YGEdgeRight
    endEdge = YGEdge.YGEdgeRight if direction == YGDirection.YGDirectionLTR else YGEdge.YGEdgeLeft
    marginRowLeading = style.computeInlineStartMargin(flexRowDirection, direction, ownerWidth)
    node.setLayoutMargin(marginRowLeading, startEdge)
    marginRowTrailing = style.computeInlineEndMargin(flexRowDirection, direction, ownerWidth)
    node.setLayoutMargin(marginRowTrailing, endEdge)
    marginColumnLeading = style.computeInlineStartMargin(flexColumnDirection, direction, ownerWidth)
    node.setLayoutMargin(marginColumnLeading, YGEdge.YGEdgeTop)
    marginColumnTrailing = style.computeInlineEndMargin(flexColumnDirection, direction, ownerWidth)
    node.setLayoutMargin(marginColumnTrailing, YGEdge.YGEdgeBottom)
    marginAxisRow = marginRowLeading + marginRowTrailing
    marginAxisColumn = marginColumnLeading + marginColumnTrailing
    node.setLayoutBorder(style.computeInlineStartBorder(flexRowDirection, direction), startEdge)
    node.setLayoutBorder(style.computeInlineEndBorder(flexRowDirection, direction), endEdge)
    node.setLayoutBorder(style.computeInlineStartBorder(flexColumnDirection, direction), YGEdge.YGEdgeTop)
    node.setLayoutBorder(style.computeInlineEndBorder(flexColumnDirection, direction), YGEdge.YGEdgeBottom)
    node.setLayoutPadding(style.computeInlineStartPadding(flexRowDirection, direction, ownerWidth), startEdge)
    node.setLayoutPadding(style.computeInlineEndPadding(flexRowDirection, direction, ownerWidth), endEdge)
    node.setLayoutPadding(style.computeInlineStartPadding(flexColumnDirection, direction, ownerWidth), YGEdge.YGEdgeTop)
    node.setLayoutPadding(style.computeInlineEndPadding(flexColumnDirection, direction, ownerWidth), YGEdge.YGEdgeBottom)
    if node.hasMeasureFunc():
        measureNodeWithMeasureFunc(
            node,
            direction,
            availableWidth - marginAxisRow,
            availableHeight - marginAxisColumn,
            widthSizingMode,
            heightSizingMode,
            ownerWidth,
            ownerHeight,
            layoutMarkerData,
            reason,
        )
        cleanupContentsNodesRecursively(node)
        return
    childCount = node.getLayoutChildCount()
    if childCount == 0:
        measureNodeWithoutChildren(
            node,
            direction,
            availableWidth - marginAxisRow,
            availableHeight - marginAxisColumn,
            widthSizingMode,
            heightSizingMode,
            ownerWidth,
            ownerHeight,
        )
        cleanupContentsNodesRecursively(node)
        return
    if not performLayout and measureNodeWithFixedSize(
        node,
        direction,
        availableWidth - marginAxisRow,
        availableHeight - marginAxisColumn,
        widthSizingMode,
        heightSizingMode,
        ownerWidth,
        ownerHeight,
    ):
        cleanupContentsNodesRecursively(node)
        return
    node.cloneChildrenIfNeeded()
    node.setLayoutHadOverflow(False)
    cleanupContentsNodesRecursively(node)
    mainAxis = resolveDirection(node.style().flexDirection(), direction)
    crossAxis = resolveCrossDirection(mainAxis, direction)
    isMainAxisRow = isRow(mainAxis)
    isNodeFlexWrap = node.style().flexWrap() != YGWrap.YGWrapNoWrap
    mainAxisOwnerSize = ownerWidth if isMainAxisRow else ownerHeight
    crossAxisOwnerSize = ownerHeight if isMainAxisRow else ownerWidth
    paddingAndBorderAxisMain = paddingAndBorderForAxis(node, mainAxis, direction, ownerWidth)
    paddingAndBorderAxisCross = paddingAndBorderForAxis(node, crossAxis, direction, ownerWidth)
    leadingPaddingAndBorderCross = node.style().computeFlexStartPaddingAndBorder(crossAxis, direction, ownerWidth)
    sizingModeMainDim = widthSizingMode if isMainAxisRow else heightSizingMode
    sizingModeCrossDim = heightSizingMode if isMainAxisRow else widthSizingMode
    paddingAndBorderAxisRow = paddingAndBorderAxisMain if isMainAxisRow else paddingAndBorderAxisCross
    paddingAndBorderAxisColumn = paddingAndBorderAxisCross if isMainAxisRow else paddingAndBorderAxisMain
    availableInnerWidth = calculateAvailableInnerDimension(
        node,
        direction,
        YGDimension.YGDimensionWidth,
        availableWidth - marginAxisRow,
        paddingAndBorderAxisRow,
        ownerWidth,
        ownerWidth,
    )
    availableInnerHeight = calculateAvailableInnerDimension(
        node,
        direction,
        YGDimension.YGDimensionHeight,
        availableHeight - marginAxisColumn,
        paddingAndBorderAxisColumn,
        ownerHeight,
        ownerWidth,
    )
    availableInnerMainDim = availableInnerWidth if isMainAxisRow else availableInnerHeight
    availableInnerCrossDim = availableInnerHeight if isMainAxisRow else availableInnerWidth
    totalMainDim = computeFlexBasisForChildren(
        node,
        availableInnerWidth,
        availableInnerHeight,
        widthSizingMode,
        heightSizingMode,
        direction,
        mainAxis,
        performLayout,
        layoutMarkerData,
        depth,
        generationCount,
    )
    if childCount > 1:
        totalMainDim = float32(
            totalMainDim
            + float32(
                node.style().computeGapForAxis(mainAxis, availableInnerMainDim)
                * float(childCount - 1)
            )
        )
    mainAxisOverflows = sizingModeMainDim != SizingMode.MaxContent and availableInnerMainDim == availableInnerMainDim and totalMainDim > availableInnerMainDim
    if isNodeFlexWrap and mainAxisOverflows and sizingModeMainDim == SizingMode.FitContent:
        sizingModeMainDim = SizingMode.StretchFit
    layoutChildren = list(node.getLayoutChildren())
    lineCount = 0
    totalLineCrossDim = 0.0
    crossAxisGap = node.style().computeGapForAxis(crossAxis, availableInnerCrossDim)
    maxLineMainDim = 0.0
    startIndex = 0
    while startIndex < len(layoutChildren):
        flexLine = calculateFlexLine(
            node,
            ownerDirection,
            ownerWidth,
            mainAxisOwnerSize,
            availableInnerWidth,
            availableInnerMainDim,
            layoutChildren,
            startIndex,
            lineCount,
        )
        canSkipFlex = (not performLayout) and sizingModeCrossDim == SizingMode.StretchFit
        sizeBasedOnContent = False
        if sizingModeMainDim != SizingMode.StretchFit:
            style = node.style()
            minInnerWidth = style.resolvedMinDimension(direction, YGDimension.YGDimensionWidth, ownerWidth, ownerWidth).unwrap() - paddingAndBorderAxisRow
            maxInnerWidth = style.resolvedMaxDimension(direction, YGDimension.YGDimensionWidth, ownerWidth, ownerWidth).unwrap() - paddingAndBorderAxisRow
            minInnerHeight = style.resolvedMinDimension(direction, YGDimension.YGDimensionHeight, ownerHeight, ownerWidth).unwrap() - paddingAndBorderAxisColumn
            maxInnerHeight = style.resolvedMaxDimension(direction, YGDimension.YGDimensionHeight, ownerHeight, ownerWidth).unwrap() - paddingAndBorderAxisColumn
            minInnerMainDim = minInnerWidth if isMainAxisRow else minInnerHeight
            maxInnerMainDim = maxInnerWidth if isMainAxisRow else maxInnerHeight
            if minInnerMainDim == minInnerMainDim and flexLine.sizeConsumed < minInnerMainDim:
                availableInnerMainDim = minInnerMainDim
            elif maxInnerMainDim == maxInnerMainDim and flexLine.sizeConsumed > maxInnerMainDim:
                availableInnerMainDim = maxInnerMainDim
            else:
                useLegacyStretchBehaviour = node.hasErrata(YGErrata.YGErrataStretchFlexBasis)
                if (not useLegacyStretchBehaviour) and (
                    (flexLine.layout.totalFlexGrowFactors == flexLine.layout.totalFlexGrowFactors and flexLine.layout.totalFlexGrowFactors == 0)
                    or (node.resolveFlexGrow() == node.resolveFlexGrow() and node.resolveFlexGrow() == 0)
                ):
                    availableInnerMainDim = flexLine.sizeConsumed
                sizeBasedOnContent = not useLegacyStretchBehaviour
        if (not sizeBasedOnContent) and availableInnerMainDim == availableInnerMainDim:
            flexLine.layout.remainingFreeSpace = float32(
                availableInnerMainDim - flexLine.sizeConsumed
            )
        elif flexLine.sizeConsumed < 0:
            flexLine.layout.remainingFreeSpace = float32(-flexLine.sizeConsumed)
        if not canSkipFlex:
            resolveFlexibleLength(
                node,
                flexLine,
                mainAxis,
                crossAxis,
                direction,
                ownerWidth,
                mainAxisOwnerSize,
                availableInnerMainDim,
                availableInnerCrossDim,
                availableInnerWidth,
                availableInnerHeight,
                mainAxisOverflows,
                sizingModeCrossDim,
                performLayout,
                layoutMarkerData,
                depth,
                generationCount,
            )
        node.setLayoutHadOverflow(
            node.getLayout().hadOverflow() or (flexLine.layout.remainingFreeSpace < 0)
        )
        justifyMainAxis(
            node,
            flexLine,
            mainAxis,
            crossAxis,
            direction,
            sizingModeMainDim,
            sizingModeCrossDim,
            mainAxisOwnerSize,
            ownerWidth,
            availableInnerMainDim,
            availableInnerCrossDim,
            availableInnerWidth,
            performLayout,
        )
        containerCrossAxis = availableInnerCrossDim
        if sizingModeCrossDim in (SizingMode.MaxContent, SizingMode.FitContent):
            containerCrossAxis = (
                boundAxis(
                    node,
                    crossAxis,
                    direction,
                    flexLine.layout.crossDim + paddingAndBorderAxisCross,
                    crossAxisOwnerSize,
                    ownerWidth,
                )
                - paddingAndBorderAxisCross
            )
        if (not isNodeFlexWrap) and sizingModeCrossDim == SizingMode.StretchFit:
            flexLine.layout.crossDim = availableInnerCrossDim
        if not isNodeFlexWrap:
            flexLine.layout.crossDim = (
                boundAxis(
                    node,
                    crossAxis,
                    direction,
                    flexLine.layout.crossDim + paddingAndBorderAxisCross,
                    crossAxisOwnerSize,
                    ownerWidth,
                )
                - paddingAndBorderAxisCross
            )
        if performLayout:
            for child in flexLine.itemsInFlow:
                leadingCrossDim = leadingPaddingAndBorderCross
                alignItem = resolveChildAlignment(node, child)
                childStyle = child.style()
                childLayout = child.getLayout()
                startMarginAuto = childStyle.flexStartMarginIsAuto(crossAxis, direction)
                endMarginAuto = childStyle.flexEndMarginIsAuto(crossAxis, direction)
                if (
                    alignItem == YGAlign.YGAlignStretch
                    and not startMarginAuto
                    and not endMarginAuto
                ):
                    if not child.hasDefiniteLength(dimension(crossAxis), availableInnerCrossDim):
                        childMainSize = childLayout.measuredDimension(dimension(mainAxis))
                        childAspectRatio = childStyle.aspectRatio()
                        if childAspectRatio.isDefined():
                            childCrossSize = childStyle.computeMarginForAxis(crossAxis, availableInnerWidth) + (
                                childMainSize / childAspectRatio.unwrap()
                                if isMainAxisRow
                                else childMainSize * childAspectRatio.unwrap()
                            )
                        else:
                            childCrossSize = flexLine.layout.crossDim
                        childMainSize += childStyle.computeMarginForAxis(mainAxis, availableInnerWidth)
                        childMainSizingMode = SizingMode.StretchFit
                        childCrossSizingMode = SizingMode.StretchFit
                        childMainSizingMode, childMainSize = constrainMaxSizeForMode(
                            child, direction, mainAxis, availableInnerMainDim, availableInnerWidth, childMainSizingMode, childMainSize
                        )
                        childCrossSizingMode, childCrossSize = constrainMaxSizeForMode(
                            child, direction, crossAxis, availableInnerCrossDim, availableInnerWidth, childCrossSizingMode, childCrossSize
                        )
                        childWidth = childMainSize if isMainAxisRow else childCrossSize
                        childHeight = childMainSize if not isMainAxisRow else childCrossSize
                        alignContent = style.alignContent()
                        crossAxisDoesNotGrow = alignContent != YGAlign.YGAlignStretch and isNodeFlexWrap
                        childWidthSizingMode = (
                            SizingMode.MaxContent if isnan(childWidth) or ((not isMainAxisRow) and crossAxisDoesNotGrow) else SizingMode.StretchFit
                        )
                        childHeightSizingMode = (
                            SizingMode.MaxContent if isnan(childHeight) or (isMainAxisRow and crossAxisDoesNotGrow) else SizingMode.StretchFit
                        )
                        calculateLayoutInternal(
                            child,
                            childWidth,
                            childHeight,
                            direction,
                            childWidthSizingMode,
                            childHeightSizingMode,
                            availableInnerWidth,
                            availableInnerHeight,
                            True,
                            LayoutPassReason.kStretch,
                            layoutMarkerData,
                            depth,
                            generationCount,
                        )
                else:
                    remainingCrossDim = containerCrossAxis - child.dimensionWithMargin(crossAxis, availableInnerWidth)
                    if startMarginAuto and endMarginAuto:
                        leadingCrossDim += maxOrDefined(0.0, remainingCrossDim / 2)
                    elif endMarginAuto:
                        pass
                    elif startMarginAuto:
                        leadingCrossDim += maxOrDefined(0.0, remainingCrossDim)
                    elif alignItem == YGAlign.YGAlignCenter:
                        leadingCrossDim += remainingCrossDim / 2
                    elif alignItem not in (YGAlign.YGAlignFlexStart,):
                        leadingCrossDim += remainingCrossDim
                child.setLayoutPosition(
                    childLayout.position(flexStartEdge(crossAxis)) + totalLineCrossDim + leadingCrossDim,
                    flexStartEdge(crossAxis),
                )
        appliedCrossGap = crossAxisGap if lineCount != 0 else 0.0
        totalLineCrossDim += flexLine.layout.crossDim + appliedCrossGap
        maxLineMainDim = maxOrDefined(maxLineMainDim, flexLine.layout.mainDim)
        nextStartIndex = startIndex
        lineChildIndex = 0
        while nextStartIndex < len(layoutChildren):
            child = layoutChildren[nextStartIndex]
            if child.style().display() == YGDisplay.YGDisplayNone or child.style().positionType() == YGPositionType.YGPositionTypeAbsolute:
                nextStartIndex += 1
                continue

            if lineChildIndex < len(flexLine.itemsInFlow) and child == flexLine.itemsInFlow[lineChildIndex]:
                lineChildIndex += 1
                nextStartIndex += 1
                if lineChildIndex == len(flexLine.itemsInFlow):
                    break
                continue

            break

        while nextStartIndex < len(layoutChildren):
            child = layoutChildren[nextStartIndex]
            if child.style().display() == YGDisplay.YGDisplayNone or child.style().positionType() == YGPositionType.YGPositionTypeAbsolute:
                nextStartIndex += 1
                continue
            break

        startIndex = nextStartIndex
        lineCount += 1
    if performLayout and (isNodeFlexWrap or isBaselineLayout(node)):
        leadPerLine = 0.0
        currentLead = leadingPaddingAndBorderCross
        extraSpacePerLine = 0.0
        if sizingModeCrossDim == SizingMode.StretchFit:
            unclampedCrossDim = availableInnerCrossDim + paddingAndBorderAxisCross
        elif node.hasDefiniteLength(dimension(crossAxis), crossAxisOwnerSize):
            unclampedCrossDim = node.getResolvedDimension(
                direction,
                dimension(crossAxis),
                crossAxisOwnerSize,
                ownerWidth,
            ).unwrap()
        else:
            unclampedCrossDim = totalLineCrossDim + paddingAndBorderAxisCross
        innerCrossDim = (
            boundAxis(
                node,
                crossAxis,
                direction,
                unclampedCrossDim,
                crossAxisOwnerSize,
                ownerWidth,
            )
            - paddingAndBorderAxisCross
        )
        remainingAlignContentDim = innerCrossDim - totalLineCrossDim
        alignContent = style.alignContent()
        alignContentValue: YGAlign = (
            alignContent
            if remainingAlignContentDim >= 0
            else fallbackAlignment(alignContent)  # type: ignore[assignment]
        )
        if alignContentValue == YGAlign.YGAlignFlexEnd:
            currentLead += remainingAlignContentDim
        elif alignContentValue == YGAlign.YGAlignCenter:
            currentLead += remainingAlignContentDim / 2
        elif alignContentValue == YGAlign.YGAlignStretch:
            extraSpacePerLine = floatDivision(
                remainingAlignContentDim, float(lineCount)
            )
        elif alignContentValue == YGAlign.YGAlignSpaceAround:
            currentLead += floatDivision(
                remainingAlignContentDim, 2 * float(lineCount)
            )
            leadPerLine = floatDivision(
                remainingAlignContentDim, float(lineCount)
            )
        elif alignContentValue == YGAlign.YGAlignSpaceEvenly:
            currentLead += remainingAlignContentDim / float(lineCount + 1)
            leadPerLine = remainingAlignContentDim / float(lineCount + 1)
        elif alignContentValue == YGAlign.YGAlignSpaceBetween and lineCount > 1:
            leadPerLine = remainingAlignContentDim / float(lineCount - 1)
        endIndex = 0
        for i in range(lineCount):
            startLineIndex = endIndex
            lineHeight = 0.0
            maxAscentForCurrentLine = 0.0
            maxDescentForCurrentLine = 0.0
            while endIndex < len(layoutChildren):
                child = layoutChildren[endIndex]
                endIndex += 1
                childStyle = child.style()
                if childStyle.display() == YGDisplay.YGDisplayNone:
                    continue
                if childStyle.positionType() != YGPositionType.YGPositionTypeAbsolute:
                    childLayout = child.getLayout()
                    if child.getLineIndex() != i:
                        endIndex -= 1
                        break
                    if child.isLayoutDimensionDefined(crossAxis):
                        lineHeight = maxOrDefined(
                            lineHeight,
                            childLayout.measuredDimension(dimension(crossAxis))
                            + childStyle.computeMarginForAxis(crossAxis, availableInnerWidth),
                        )
                    childAlignment = resolveChildAlignment(node, child)
                    if childAlignment == YGAlign.YGAlignBaseline:
                        ascent = calculateBaseline(child) + childStyle.computeFlexStartMargin(
                            YGFlexDirection.YGFlexDirectionColumn, direction, availableInnerWidth
                        )
                        descent = (
                            childLayout.measuredDimension(YGDimension.YGDimensionHeight)
                            + childStyle.computeMarginForAxis(YGFlexDirection.YGFlexDirectionColumn, availableInnerWidth)
                            - ascent
                        )
                        maxAscentForCurrentLine = maxOrDefined(maxAscentForCurrentLine, ascent)
                        maxDescentForCurrentLine = maxOrDefined(maxDescentForCurrentLine, descent)
                        lineHeight = maxOrDefined(lineHeight, maxAscentForCurrentLine + maxDescentForCurrentLine)
            currentLead += crossAxisGap if i != 0 else 0.0
            lineHeight += extraSpacePerLine
            for child in layoutChildren[startLineIndex:endIndex]:
                childStyle = child.style()
                if childStyle.display() == YGDisplay.YGDisplayNone:
                    continue
                if childStyle.positionType() != YGPositionType.YGPositionTypeAbsolute:
                    childLayout = child.getLayout()
                    childAlignment = resolveChildAlignment(node, child)
                    if childAlignment == YGAlign.YGAlignFlexStart:
                        child.setLayoutPosition(
                            currentLead + childStyle.computeFlexStartPosition(crossAxis, direction, availableInnerWidth),
                            flexStartEdge(crossAxis),
                        )
                    elif childAlignment == YGAlign.YGAlignFlexEnd:
                        child.setLayoutPosition(
                            currentLead
                            + lineHeight
                            - childStyle.computeFlexEndMargin(crossAxis, direction, availableInnerWidth)
                            - childLayout.measuredDimension(dimension(crossAxis)),
                            flexStartEdge(crossAxis),
                        )
                    elif childAlignment == YGAlign.YGAlignCenter:
                        childHeight = childLayout.measuredDimension(dimension(crossAxis))
                        child.setLayoutPosition(
                            currentLead + (lineHeight - childHeight) / 2,
                            flexStartEdge(crossAxis),
                        )
                    elif childAlignment == YGAlign.YGAlignStretch:
                        child.setLayoutPosition(
                            currentLead + childStyle.computeFlexStartMargin(crossAxis, direction, availableInnerWidth),
                            flexStartEdge(crossAxis),
                        )
                        if not child.hasDefiniteLength(dimension(crossAxis), availableInnerCrossDim):
                            childWidth = (
                                childLayout.measuredDimension(YGDimension.YGDimensionWidth)
                                + childStyle.computeMarginForAxis(mainAxis, availableInnerWidth)
                                if isMainAxisRow
                                else leadPerLine + lineHeight
                            )
                            childHeight = (
                                childLayout.measuredDimension(YGDimension.YGDimensionHeight)
                                + childStyle.computeMarginForAxis(crossAxis, availableInnerWidth)
                                if not isMainAxisRow
                                else leadPerLine + lineHeight
                            )
                            if not (
                                inexactEquals(
                                    childWidth,
                                    child.getLayout().measuredDimension(YGDimension.YGDimensionWidth),
                                )
                                and inexactEquals(
                                    childHeight,
                                    child.getLayout().measuredDimension(YGDimension.YGDimensionHeight),
                                )
                            ):
                                calculateLayoutInternal(
                                    child,
                                    childWidth,
                                    childHeight,
                                    direction,
                                    SizingMode.StretchFit,
                                    SizingMode.StretchFit,
                                    availableInnerWidth,
                                    availableInnerHeight,
                                    True,
                                    LayoutPassReason.kMultilineStretch,
                                    layoutMarkerData,
                                    depth,
                                    generationCount,
                                )
                    elif childAlignment == YGAlign.YGAlignBaseline:
                        child.setLayoutPosition(
                            currentLead
                            + maxAscentForCurrentLine
                            - calculateBaseline(child)
                            + child.style().computeFlexStartPosition(
                                YGFlexDirection.YGFlexDirectionColumn,
                                direction,
                                availableInnerCrossDim,
                            ),
                            YGEdge.YGEdgeTop,
                        )
            currentLead = currentLead + leadPerLine + lineHeight
    node.setLayoutMeasuredDimension(
        boundAxis(node, YGFlexDirection.YGFlexDirectionRow, direction, availableWidth - marginAxisRow, ownerWidth, ownerWidth),
        YGDimension.YGDimensionWidth,
    )
    node.setLayoutMeasuredDimension(
        boundAxis(node, YGFlexDirection.YGFlexDirectionColumn, direction, availableHeight - marginAxisColumn, ownerHeight, ownerWidth),
        YGDimension.YGDimensionHeight,
    )
    if sizingModeMainDim == SizingMode.MaxContent or (
        node.style().overflow() != YGOverflow.YGOverflowScroll and sizingModeMainDim == SizingMode.FitContent
    ):
        node.setLayoutMeasuredDimension(
            boundAxis(node, mainAxis, direction, maxLineMainDim, mainAxisOwnerSize, ownerWidth),
            dimension(mainAxis),
        )
    elif sizingModeMainDim == SizingMode.FitContent and node.style().overflow() == YGOverflow.YGOverflowScroll:
        node.setLayoutMeasuredDimension(
            maxOrDefined(
                minOrDefined(
                    availableInnerMainDim + paddingAndBorderAxisMain,
                    boundAxisWithinMinAndMax(
                        node, direction, mainAxis, FloatOptional(maxLineMainDim), mainAxisOwnerSize, ownerWidth
                    ).unwrap(),
                ),
                paddingAndBorderAxisMain,
            ),
            dimension(mainAxis),
        )
    if sizingModeCrossDim == SizingMode.MaxContent or (
        node.style().overflow() != YGOverflow.YGOverflowScroll and sizingModeCrossDim == SizingMode.FitContent
    ):
        node.setLayoutMeasuredDimension(
            boundAxis(node, crossAxis, direction, totalLineCrossDim + paddingAndBorderAxisCross, crossAxisOwnerSize, ownerWidth),
            dimension(crossAxis),
        )
    elif sizingModeCrossDim == SizingMode.FitContent and node.style().overflow() == YGOverflow.YGOverflowScroll:
        node.setLayoutMeasuredDimension(
            maxOrDefined(
                minOrDefined(
                    availableInnerCrossDim + paddingAndBorderAxisCross,
                    boundAxisWithinMinAndMax(
                        node,
                        direction,
                        crossAxis,
                        FloatOptional(totalLineCrossDim + paddingAndBorderAxisCross),
                        crossAxisOwnerSize,
                        ownerWidth,
                    ).unwrap(),
                ),
                paddingAndBorderAxisCross,
            ),
            dimension(crossAxis),
        )
    if performLayout and node.style().flexWrap() == YGWrap.YGWrapWrapReverse:
        for child in node.getLayoutChildren():
            if child.style().positionType() != YGPositionType.YGPositionTypeAbsolute:
                child.setLayoutPosition(
                    node.getLayout().measuredDimension(dimension(crossAxis))
                    - child.getLayout().position(flexStartEdge(crossAxis))
                    - child.getLayout().measuredDimension(dimension(crossAxis)),
                    flexStartEdge(crossAxis),
                )
    if performLayout:
        needsMainTrailingPos = needsTrailingPosition(mainAxis)
        needsCrossTrailingPos = needsTrailingPosition(crossAxis)
        if needsMainTrailingPos or needsCrossTrailingPos:
            for child in node.getLayoutChildren():
                if child.style().display() == YGDisplay.YGDisplayNone or child.style().positionType() == YGPositionType.YGPositionTypeAbsolute:
                    continue
                if needsMainTrailingPos:
                    setChildTrailingPosition(node, child, mainAxis)
                if needsCrossTrailingPos:
                    setChildTrailingPosition(node, child, crossAxis)
        if node.style().positionType() != YGPositionType.YGPositionTypeStatic or node.alwaysFormsContainingBlock() or depth == 1:
            layoutAbsoluteDescendants(
                node,
                node,
                sizingModeMainDim if isMainAxisRow else sizingModeCrossDim,
                direction,
                layoutMarkerData,
                depth,
                generationCount,
                0.0,
                0.0,
                availableInnerWidth,
                availableInnerHeight,
            )


@cython.locals(
    marginAxisRow=cython.double,
    marginAxisColumn=cython.double,
    measuredWidth=cython.double,
    measuredHeight=cython.double,
)
def calculateLayoutInternal(
    node: Node,
    availableWidth: float,
    availableHeight: float,
    ownerDirection: YGDirection,
    widthSizingMode: SizingMode,
    heightSizingMode: SizingMode,
    ownerWidth: float,
    ownerHeight: float,
    performLayout: bool,
    reason: LayoutPassReason,
    layoutMarkerData: LayoutData,
    depth: int,
    generationCount: int,
) -> bool:
    layout = node.getLayout()
    depth += 1
    needToVisitNode = (
        (node.isDirty() and layout.generationCount != generationCount)
        or layout.configVersion != node.getConfig().getVersion()
        or layout.lastOwnerDirection != ownerDirection
    )
    if needToVisitNode:
        layout.nextCachedMeasurementsIndex = 0
        layout.cachedLayout.availableWidth = -1
        layout.cachedLayout.availableHeight = -1
        layout.cachedLayout.widthSizingMode = SizingMode.MaxContent
        layout.cachedLayout.heightSizingMode = SizingMode.MaxContent
        layout.cachedLayout.computedWidth = -1
        layout.cachedLayout.computedHeight = -1
    cachedResults = None
    if node.hasMeasureFunc():
        marginAxisRow = node.style().computeMarginForAxis(YGFlexDirection.YGFlexDirectionRow, ownerWidth)
        marginAxisColumn = node.style().computeMarginForAxis(YGFlexDirection.YGFlexDirectionColumn, ownerWidth)
        if canUseCachedMeasurement(
            widthSizingMode,
            availableWidth,
            heightSizingMode,
            availableHeight,
            layout.cachedLayout.widthSizingMode,
            layout.cachedLayout.availableWidth,
            layout.cachedLayout.heightSizingMode,
            layout.cachedLayout.availableHeight,
            layout.cachedLayout.computedWidth,
            layout.cachedLayout.computedHeight,
            marginAxisRow,
            marginAxisColumn,
            node.getConfig(),
        ):
            cachedResults = layout.cachedLayout
        else:
            for measurement in layout.cachedMeasurements[: layout.nextCachedMeasurementsIndex]:
                if canUseCachedMeasurement(
                    widthSizingMode,
                    availableWidth,
                    heightSizingMode,
                    availableHeight,
                    measurement.widthSizingMode,
                    measurement.availableWidth,
                    measurement.heightSizingMode,
                    measurement.availableHeight,
                    measurement.computedWidth,
                    measurement.computedHeight,
                    marginAxisRow,
                    marginAxisColumn,
                    node.getConfig(),
                ):
                    cachedResults = measurement
                    break
    elif performLayout:
        if (
            inexactEquals(availableWidth, layout.cachedLayout.availableWidth)
            and inexactEquals(availableHeight, layout.cachedLayout.availableHeight)
            and layout.cachedLayout.widthSizingMode == widthSizingMode
            and layout.cachedLayout.heightSizingMode == heightSizingMode
        ):
            cachedResults = layout.cachedLayout
    else:
        for measurement in layout.cachedMeasurements[: layout.nextCachedMeasurementsIndex]:
            if (
                inexactEquals(availableWidth, measurement.availableWidth)
                and inexactEquals(availableHeight, measurement.availableHeight)
                and measurement.widthSizingMode == widthSizingMode
                and measurement.heightSizingMode == heightSizingMode
            ):
                cachedResults = measurement
                break
    if (not needToVisitNode) and cachedResults is not None:
        layout.setMeasuredDimension(YGDimension.YGDimensionWidth, cachedResults.computedWidth)
        layout.setMeasuredDimension(YGDimension.YGDimensionHeight, cachedResults.computedHeight)
        if performLayout:
            layoutMarkerData.cachedLayouts += 1
        else:
            layoutMarkerData.cachedMeasures += 1
    else:
        calculateLayoutImpl(
            node,
            availableWidth,
            availableHeight,
            ownerDirection,
            widthSizingMode,
            heightSizingMode,
            ownerWidth,
            ownerHeight,
            performLayout,
            reason,
            layoutMarkerData,
            depth,
            generationCount,
        )
        layout.lastOwnerDirection = ownerDirection
        layout.configVersion = node.getConfig().getVersion()
        if cachedResults is None:
            layoutMarkerData.maxMeasureCache = max(layoutMarkerData.maxMeasureCache, layout.nextCachedMeasurementsIndex + 1)
            if layout.nextCachedMeasurementsIndex == LayoutResults.MaxCachedMeasurements:
                layout.nextCachedMeasurementsIndex = 0
            newCacheEntry = layout.cachedLayout if performLayout else layout.cachedMeasurements[layout.nextCachedMeasurementsIndex]
            if not performLayout:
                layout.nextCachedMeasurementsIndex += 1
            newCacheEntry.availableWidth = availableWidth
            newCacheEntry.availableHeight = availableHeight
            newCacheEntry.widthSizingMode = widthSizingMode
            newCacheEntry.heightSizingMode = heightSizingMode
            newCacheEntry.computedWidth = layout.measuredDimension(YGDimension.YGDimensionWidth)
            newCacheEntry.computedHeight = layout.measuredDimension(YGDimension.YGDimensionHeight)
    if performLayout:
        node.setLayoutDimension(layout.measuredDimension(YGDimension.YGDimensionWidth), YGDimension.YGDimensionWidth)
        node.setLayoutDimension(layout.measuredDimension(YGDimension.YGDimensionHeight), YGDimension.YGDimensionHeight)
        node.setHasNewLayout(True)
        node.setDirty(False)
    layout.generationCount = generationCount
    if performLayout:
        layoutType = LayoutType.kCachedLayout if ((not needToVisitNode) and cachedResults is layout.cachedLayout) else LayoutType.kLayout
    else:
        layoutType = LayoutType.kCachedMeasure if cachedResults is not None else LayoutType.kMeasure
    Event.publish(node, Event.NodeLayout, NodeLayoutData(layoutType))
    return needToVisitNode or cachedResults is None
