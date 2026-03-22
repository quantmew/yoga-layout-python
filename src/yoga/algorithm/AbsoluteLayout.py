# cython: infer_types=False
"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from ..algorithm.Align import resolveChildAlignment, resolveChildJustification
from ..algorithm.BoundAxis import boundAxis
from ..algorithm.FlexDirection import (
    dimension,
    flexEndEdge,
    flexStartEdge,
    inlineStartEdge,
    isRow,
    resolveCrossDirection,
    resolveDirection,
)
from ..algorithm.SizingMode import SizingMode
from ..algorithm.TrailingPosition import (
    getPositionOfOppositeEdge,
    needsTrailingPosition,
    setChildTrailingPosition,
)
from ..event.event import LayoutPassReason
from ..YGEnums import (
    YGAlign,
    YGDimension,
    YGDirection,
    YGDisplay,
    YGEdge,
    YGErrata,
    YGFlexDirection,
    YGJustify,
    YGPositionType,
)


def setFlexStartLayoutPosition(parent, child, direction, axis, containingBlockWidth):
    position = (
        child.style().computeFlexStartMargin(axis, direction, containingBlockWidth)
        + parent.getLayout().border(flexStartEdge(axis))
    )
    if (
        not child.hasErrata(YGErrata.YGErrataAbsolutePositionWithoutInsetsExcludesPadding)
        and parent.style().display() != YGDisplay.YGDisplayGrid
    ):
        position += parent.getLayout().padding(flexStartEdge(axis))
    child.setLayoutPosition(position, flexStartEdge(axis))


def setFlexEndLayoutPosition(parent, child, direction, axis, containingBlockWidth):
    flexEndPosition = (
        parent.getLayout().border(flexEndEdge(axis))
        + child.style().computeFlexEndMargin(axis, direction, containingBlockWidth)
    )
    if (
        not child.hasErrata(YGErrata.YGErrataAbsolutePositionWithoutInsetsExcludesPadding)
        and parent.style().display() != YGDisplay.YGDisplayGrid
    ):
        flexEndPosition += parent.getLayout().padding(flexEndEdge(axis))
    child.setLayoutPosition(getPositionOfOppositeEdge(flexEndPosition, axis, parent, child), flexStartEdge(axis))


def setCenterLayoutPosition(parent, child, direction, axis, containingBlockWidth):
    parentContentBoxSize = (
        parent.getLayout().measuredDimension(dimension(axis))
        - parent.getLayout().border(flexStartEdge(axis))
        - parent.getLayout().border(flexEndEdge(axis))
    )
    if (
        not child.hasErrata(YGErrata.YGErrataAbsolutePositionWithoutInsetsExcludesPadding)
        and parent.style().display() != YGDisplay.YGDisplayGrid
    ):
        parentContentBoxSize -= parent.getLayout().padding(flexStartEdge(axis))
        parentContentBoxSize -= parent.getLayout().padding(flexEndEdge(axis))
    childOuterSize = (
        child.getLayout().measuredDimension(dimension(axis))
        + child.style().computeMarginForAxis(axis, containingBlockWidth)
    )
    position = (
        (parentContentBoxSize - childOuterSize) / 2.0
        + parent.getLayout().border(flexStartEdge(axis))
        + child.style().computeFlexStartMargin(axis, direction, containingBlockWidth)
    )
    if (
        not child.hasErrata(YGErrata.YGErrataAbsolutePositionWithoutInsetsExcludesPadding)
        and parent.style().display() != YGDisplay.YGDisplayGrid
    ):
        position += parent.getLayout().padding(flexStartEdge(axis))
    child.setLayoutPosition(position, flexStartEdge(axis))


def justifyAbsoluteChild(parent, child, direction, mainAxis, containingBlockWidth):
    justify = resolveChildJustification(parent, child) if parent.style().display() == YGDisplay.YGDisplayGrid else parent.style().justifyContent()
    if justify in (YGJustify.YGJustifyStart, YGJustify.YGJustifyAuto, YGJustify.YGJustifyStretch, YGJustify.YGJustifyFlexStart, YGJustify.YGJustifySpaceBetween):
        setFlexStartLayoutPosition(parent, child, direction, mainAxis, containingBlockWidth)
    elif justify in (YGJustify.YGJustifyEnd, YGJustify.YGJustifyFlexEnd):
        setFlexEndLayoutPosition(parent, child, direction, mainAxis, containingBlockWidth)
    else:
        setCenterLayoutPosition(parent, child, direction, mainAxis, containingBlockWidth)


def alignAbsoluteChild(parent, child, direction, crossAxis, containingBlockWidth):
    itemAlign = resolveChildAlignment(parent, child)
    if parent.style().flexWrap().name.endswith("WrapReverse"):
        if itemAlign == YGAlign.YGAlignFlexEnd:
            itemAlign = YGAlign.YGAlignFlexStart
        elif itemAlign != YGAlign.YGAlignCenter:
            itemAlign = YGAlign.YGAlignFlexEnd
    if itemAlign in (
        YGAlign.YGAlignStart,
        YGAlign.YGAlignAuto,
        YGAlign.YGAlignFlexStart,
        YGAlign.YGAlignBaseline,
        YGAlign.YGAlignSpaceAround,
        YGAlign.YGAlignSpaceBetween,
        YGAlign.YGAlignStretch,
        YGAlign.YGAlignSpaceEvenly,
    ):
        setFlexStartLayoutPosition(parent, child, direction, crossAxis, containingBlockWidth)
    elif itemAlign in (YGAlign.YGAlignEnd, YGAlign.YGAlignFlexEnd):
        setFlexEndLayoutPosition(parent, child, direction, crossAxis, containingBlockWidth)
    else:
        setCenterLayoutPosition(parent, child, direction, crossAxis, containingBlockWidth)


def positionAbsoluteChild(
    containingNode,
    parent,
    child,
    direction: YGDirection,
    axis: YGFlexDirection,
    isMainAxis: bool,
    containingBlockWidth: float,
    containingBlockHeight: float,
):
    containingBlockSize = containingBlockWidth if isRow(axis) else containingBlockHeight

    if child.style().isInlineStartPositionDefined(axis, direction) and not child.style().isInlineStartPositionAuto(axis, direction):
        positionRelativeToInlineStart = (
            child.style().computeInlineStartPosition(axis, direction, containingBlockSize)
            + containingNode.style().computeInlineStartBorder(axis, direction)
            + child.style().computeInlineStartMargin(axis, direction, containingBlockSize)
        )
        positionRelativeToFlexStart = (
            getPositionOfOppositeEdge(positionRelativeToInlineStart, axis, containingNode, child)
            if inlineStartEdge(axis, direction) != flexStartEdge(axis)
            else positionRelativeToInlineStart
        )
        child.setLayoutPosition(positionRelativeToFlexStart, flexStartEdge(axis))
    elif child.style().isInlineEndPositionDefined(axis, direction) and not child.style().isInlineEndPositionAuto(axis, direction):
        positionRelativeToInlineStart = (
            containingNode.getLayout().measuredDimension(dimension(axis))
            - child.getLayout().measuredDimension(dimension(axis))
            - containingNode.style().computeInlineEndBorder(axis, direction)
            - child.style().computeInlineEndMargin(axis, direction, containingBlockSize)
            - child.style().computeInlineEndPosition(axis, direction, containingBlockSize)
        )
        positionRelativeToFlexStart = (
            getPositionOfOppositeEdge(positionRelativeToInlineStart, axis, containingNode, child)
            if inlineStartEdge(axis, direction) != flexStartEdge(axis)
            else positionRelativeToInlineStart
        )
        child.setLayoutPosition(positionRelativeToFlexStart, flexStartEdge(axis))
    else:
        if isMainAxis:
            justifyAbsoluteChild(parent, child, direction, axis, containingBlockWidth)
        else:
            alignAbsoluteChild(parent, child, direction, axis, containingBlockWidth)


def layoutAbsoluteChild(
    containingNode,
    node,
    child,
    containingBlockWidth: float,
    containingBlockHeight: float,
    widthMode: SizingMode,
    direction: YGDirection,
    layoutMarkerData,
    depth: int,
    generationCount: int,
):
    from ..algorithm.CalculateLayout import calculateLayoutInternal

    mainAxis = (
        resolveDirection(YGFlexDirection.YGFlexDirectionRow, direction)
        if node.style().display() == YGDisplay.YGDisplayGrid
        else resolveDirection(node.style().flexDirection(), direction)
    )
    crossAxis = (
        YGFlexDirection.YGFlexDirectionColumn
        if node.style().display() == YGDisplay.YGDisplayGrid
        else resolveCrossDirection(mainAxis, direction)
    )
    isMainAxisRow = isRow(mainAxis)

    childWidth = float("nan")
    childHeight = float("nan")
    childWidthSizingMode = SizingMode.MaxContent
    childHeightSizingMode = SizingMode.MaxContent

    marginRow = child.style().computeMarginForAxis(YGFlexDirection.YGFlexDirectionRow, containingBlockWidth)
    marginColumn = child.style().computeMarginForAxis(YGFlexDirection.YGFlexDirectionColumn, containingBlockWidth)

    if child.hasDefiniteLength(YGDimension.YGDimensionWidth, containingBlockWidth):
        childWidth = child.getResolvedDimension(
            direction, YGDimension.YGDimensionWidth, containingBlockWidth, containingBlockWidth
        ).unwrap() + marginRow
    elif (
        child.style().isFlexStartPositionDefined(YGFlexDirection.YGFlexDirectionRow, direction)
        and child.style().isFlexEndPositionDefined(YGFlexDirection.YGFlexDirectionRow, direction)
        and not child.style().isFlexStartPositionAuto(YGFlexDirection.YGFlexDirectionRow, direction)
        and not child.style().isFlexEndPositionAuto(YGFlexDirection.YGFlexDirectionRow, direction)
    ):
        childWidth = containingNode.getLayout().measuredDimension(YGDimension.YGDimensionWidth) - (
            containingNode.style().computeFlexStartBorder(YGFlexDirection.YGFlexDirectionRow, direction)
            + containingNode.style().computeFlexEndBorder(YGFlexDirection.YGFlexDirectionRow, direction)
        ) - (
            child.style().computeFlexStartPosition(YGFlexDirection.YGFlexDirectionRow, direction, containingBlockWidth)
            + child.style().computeFlexEndPosition(YGFlexDirection.YGFlexDirectionRow, direction, containingBlockWidth)
        )
        childWidth = boundAxis(
            child,
            YGFlexDirection.YGFlexDirectionRow,
            direction,
            childWidth,
            containingBlockWidth,
            containingBlockWidth,
        )

    if child.hasDefiniteLength(YGDimension.YGDimensionHeight, containingBlockHeight):
        childHeight = child.getResolvedDimension(
            direction, YGDimension.YGDimensionHeight, containingBlockHeight, containingBlockWidth
        ).unwrap() + marginColumn
    elif (
        child.style().isFlexStartPositionDefined(YGFlexDirection.YGFlexDirectionColumn, direction)
        and child.style().isFlexEndPositionDefined(YGFlexDirection.YGFlexDirectionColumn, direction)
        and not child.style().isFlexStartPositionAuto(YGFlexDirection.YGFlexDirectionColumn, direction)
        and not child.style().isFlexEndPositionAuto(YGFlexDirection.YGFlexDirectionColumn, direction)
    ):
        childHeight = containingNode.getLayout().measuredDimension(YGDimension.YGDimensionHeight) - (
            containingNode.style().computeFlexStartBorder(YGFlexDirection.YGFlexDirectionColumn, direction)
            + containingNode.style().computeFlexEndBorder(YGFlexDirection.YGFlexDirectionColumn, direction)
        ) - (
            child.style().computeFlexStartPosition(YGFlexDirection.YGFlexDirectionColumn, direction, containingBlockHeight)
            + child.style().computeFlexEndPosition(YGFlexDirection.YGFlexDirectionColumn, direction, containingBlockHeight)
        )
        childHeight = boundAxis(
            child,
            YGFlexDirection.YGFlexDirectionColumn,
            direction,
            childHeight,
            containingBlockHeight,
            containingBlockWidth,
        )

    childStyle = child.style()
    if (childWidth == childWidth) ^ (childHeight == childHeight):
        if childStyle.aspectRatio().isDefined():
            if childWidth != childWidth:
                childWidth = marginRow + (childHeight - marginColumn) * childStyle.aspectRatio().unwrap()
            else:
                childHeight = marginColumn + (childWidth - marginRow) / childStyle.aspectRatio().unwrap()

    if childWidth != childWidth or childHeight != childHeight:
        childWidthSizingMode = SizingMode.MaxContent if childWidth != childWidth else SizingMode.StretchFit
        childHeightSizingMode = SizingMode.MaxContent if childHeight != childHeight else SizingMode.StretchFit

        if (
            not isMainAxisRow
            and childWidth != childWidth
            and widthMode != SizingMode.MaxContent
            and containingBlockWidth == containingBlockWidth
            and containingBlockWidth > 0
        ):
            childWidth = containingBlockWidth
            childWidthSizingMode = SizingMode.FitContent

        calculateLayoutInternal(
            child,
            childWidth,
            childHeight,
            direction,
            childWidthSizingMode,
            childHeightSizingMode,
            containingBlockWidth,
            containingBlockHeight,
            False,
            LayoutPassReason.kAbsMeasureChild,
            layoutMarkerData,
            depth,
            generationCount,
        )
        childWidth = child.getLayout().measuredDimension(YGDimension.YGDimensionWidth) + child.style().computeMarginForAxis(
            YGFlexDirection.YGFlexDirectionRow, containingBlockWidth
        )
        childHeight = child.getLayout().measuredDimension(YGDimension.YGDimensionHeight) + child.style().computeMarginForAxis(
            YGFlexDirection.YGFlexDirectionColumn, containingBlockWidth
        )

    calculateLayoutInternal(
        child,
        childWidth,
        childHeight,
        direction,
        SizingMode.StretchFit,
        SizingMode.StretchFit,
        containingBlockWidth,
        containingBlockHeight,
        True,
        LayoutPassReason.kAbsLayout,
        layoutMarkerData,
        depth,
        generationCount,
    )

    positionAbsoluteChild(
        containingNode,
        node,
        child,
        direction,
        mainAxis,
        True,
        containingBlockWidth,
        containingBlockHeight,
    )
    positionAbsoluteChild(
        containingNode,
        node,
        child,
        direction,
        crossAxis,
        False,
        containingBlockWidth,
        containingBlockHeight,
    )


def layoutAbsoluteDescendants(
    containingNode,
    currentNode,
    widthSizingMode: SizingMode,
    currentNodeDirection: YGDirection,
    layoutMarkerData,
    currentDepth: int,
    generationCount: int,
    currentNodeLeftOffsetFromContainingBlock: float,
    currentNodeTopOffsetFromContainingBlock: float,
    containingNodeAvailableInnerWidth: float,
    containingNodeAvailableInnerHeight: float,
):
    hasNewLayout = False

    for child in currentNode.getLayoutChildren():
        if child.style().display() == YGDisplay.YGDisplayNone:
            continue
        if child.style().positionType() == YGPositionType.YGPositionTypeAbsolute:
            absoluteErrata = currentNode.hasErrata(YGErrata.YGErrataAbsolutePercentAgainstInnerSize)
            containingBlockWidth = (
                containingNodeAvailableInnerWidth
                if absoluteErrata
                else containingNode.getLayout().measuredDimension(YGDimension.YGDimensionWidth)
                - containingNode.style().computeBorderForAxis(YGFlexDirection.YGFlexDirectionRow)
            )
            containingBlockHeight = (
                containingNodeAvailableInnerHeight
                if absoluteErrata
                else containingNode.getLayout().measuredDimension(YGDimension.YGDimensionHeight)
                - containingNode.style().computeBorderForAxis(YGFlexDirection.YGFlexDirectionColumn)
            )

            layoutAbsoluteChild(
                containingNode,
                currentNode,
                child,
                containingBlockWidth,
                containingBlockHeight,
                widthSizingMode,
                currentNodeDirection,
                layoutMarkerData,
                currentDepth,
                generationCount,
            )
            hasNewLayout = hasNewLayout or child.getHasNewLayout()

            parentMainAxis = resolveDirection(currentNode.style().flexDirection(), currentNodeDirection)
            parentCrossAxis = resolveCrossDirection(parentMainAxis, currentNodeDirection)

            if needsTrailingPosition(parentMainAxis):
                mainInsetsDefined = child.style().horizontalInsetsDefined() if isRow(parentMainAxis) else child.style().verticalInsetsDefined()
                setChildTrailingPosition(containingNode if mainInsetsDefined else currentNode, child, parentMainAxis)
            if needsTrailingPosition(parentCrossAxis):
                crossInsetsDefined = child.style().horizontalInsetsDefined() if isRow(parentCrossAxis) else child.style().verticalInsetsDefined()
                setChildTrailingPosition(containingNode if crossInsetsDefined else currentNode, child, parentCrossAxis)

            childLeftPosition = child.getLayout().position(YGEdge.YGEdgeLeft)
            childTopPosition = child.getLayout().position(YGEdge.YGEdgeTop)

            childLeftOffsetFromParent = (
                childLeftPosition - currentNodeLeftOffsetFromContainingBlock
                if child.style().horizontalInsetsDefined()
                else childLeftPosition
            )
            childTopOffsetFromParent = (
                childTopPosition - currentNodeTopOffsetFromContainingBlock
                if child.style().verticalInsetsDefined()
                else childTopPosition
            )

            child.setLayoutPosition(childLeftOffsetFromParent, YGEdge.YGEdgeLeft)
            child.setLayoutPosition(childTopOffsetFromParent, YGEdge.YGEdgeTop)
        elif child.style().positionType() == YGPositionType.YGPositionTypeStatic and not child.alwaysFormsContainingBlock():
            child.cloneChildrenIfNeeded()
            childDirection = child.resolveDirection(currentNodeDirection)
            childLeftOffsetFromContainingBlock = currentNodeLeftOffsetFromContainingBlock + child.getLayout().position(YGEdge.YGEdgeLeft)
            childTopOffsetFromContainingBlock = currentNodeTopOffsetFromContainingBlock + child.getLayout().position(YGEdge.YGEdgeTop)

            hasNewLayout = (
                layoutAbsoluteDescendants(
                    containingNode,
                    child,
                    widthSizingMode,
                    childDirection,
                    layoutMarkerData,
                    currentDepth + 1,
                    generationCount,
                    childLeftOffsetFromContainingBlock,
                    childTopOffsetFromContainingBlock,
                    containingNodeAvailableInnerWidth,
                    containingNodeAvailableInnerHeight,
                )
                or hasNewLayout
            )
            if hasNewLayout:
                child.setHasNewLayout(hasNewLayout)

    return hasNewLayout
