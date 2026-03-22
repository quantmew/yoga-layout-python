"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from .._cython_compat import cython
from ..algorithm.BoundAxis import boundAxisWithinMinAndMax
from ..algorithm.FlexDirection import resolveDirection
from ..numeric.FloatMath import float32
from ..YGEnums import YGDirection, YGDisplay, YGPositionType, YGWrap


class FlexLineRunningLayout:
    __slots__ = (
        "totalFlexGrowFactors",
        "totalFlexShrinkScaledFactors",
        "remainingFreeSpace",
        "mainDim",
        "crossDim",
    )

    def __init__(
        self,
        totalFlexGrowFactors: float = 0.0,
        totalFlexShrinkScaledFactors: float = 0.0,
        remainingFreeSpace: float = 0.0,
        mainDim: float = 0.0,
        crossDim: float = 0.0,
    ) -> None:
        self.totalFlexGrowFactors = totalFlexGrowFactors
        self.totalFlexShrinkScaledFactors = totalFlexShrinkScaledFactors
        self.remainingFreeSpace = remainingFreeSpace
        self.mainDim = mainDim
        self.crossDim = crossDim


class FlexLine:
    __slots__ = ("itemsInFlow", "sizeConsumed", "numberOfAutoMargins", "layout")

    def __init__(
        self,
        itemsInFlow: list | None = None,
        sizeConsumed: float = 0.0,
        numberOfAutoMargins: int = 0,
        layout: FlexLineRunningLayout | None = None,
    ) -> None:
        self.itemsInFlow = [] if itemsInFlow is None else itemsInFlow
        self.sizeConsumed = sizeConsumed
        self.numberOfAutoMargins = numberOfAutoMargins
        self.layout = FlexLineRunningLayout() if layout is None else layout


@cython.locals(
    sizeConsumed=cython.double,
    totalFlexGrowFactors=cython.double,
    totalFlexShrinkScaledFactors=cython.double,
    numberOfAutoMargins=cython.int,
    sizeConsumedIncludingMinConstraint=cython.double,
    gap=cython.double,
    childMarginMainAxis=cython.double,
    childLeadingGapMainAxis=cython.double,
    flexBasisWithMinAndMaxConstraints=cython.double,
    isNodeFlexWrap=cython.bint,
)
def calculateFlexLine(
    node,
    ownerDirection: YGDirection,
    ownerWidth: float,
    mainAxisOwnerSize: float,
    availableInnerWidth: float,
    availableInnerMainDim: float,
    children,
    startIndex: int,
    lineCount: int,
) -> FlexLine:
    itemsInFlow: list = []
    sizeConsumed = float32(0.0)
    totalFlexGrowFactors = 0.0
    totalFlexShrinkScaledFactors = 0.0
    numberOfAutoMargins = 0
    firstElementInLine = None
    sizeConsumedIncludingMinConstraint = float32(0.0)
    direction = node.resolveDirection(ownerDirection)
    nodeStyle = node.style()
    mainAxis = resolveDirection(nodeStyle.flexDirection(), direction)
    isNodeFlexWrap = nodeStyle.flexWrap() != YGWrap.YGWrapNoWrap
    gap = nodeStyle.computeGapForAxis(mainAxis, availableInnerMainDim)

    for child in children[startIndex:]:
        childStyle = child.style()
        if childStyle.display() == YGDisplay.YGDisplayNone or childStyle.positionType() == YGPositionType.YGPositionTypeAbsolute:
            continue
        if firstElementInLine is None:
            firstElementInLine = child
        if childStyle.flexStartMarginIsAuto(mainAxis, ownerDirection):
            numberOfAutoMargins += 1
        if childStyle.flexEndMarginIsAuto(mainAxis, ownerDirection):
            numberOfAutoMargins += 1
        child.setLineIndex(lineCount)
        childMarginMainAxis = childStyle.computeMarginForAxis(mainAxis, availableInnerWidth)
        childLeadingGapMainAxis = 0.0 if child == firstElementInLine else gap
        childLayout = child.getLayout()
        flexBasisWithMinAndMaxConstraints = boundAxisWithinMinAndMax(
            child,
            direction,
            mainAxis,
            childLayout.computedFlexBasis,
            mainAxisOwnerSize,
            ownerWidth,
        ).unwrap()
        if (
            sizeConsumedIncludingMinConstraint
            + flexBasisWithMinAndMaxConstraints
            + childMarginMainAxis
            + childLeadingGapMainAxis
            > availableInnerMainDim
            and isNodeFlexWrap
            and itemsInFlow
        ):
            break
        sizeConsumedIncludingMinConstraint = float32(
            sizeConsumedIncludingMinConstraint
            + float32(
                flexBasisWithMinAndMaxConstraints
                + childMarginMainAxis
                + childLeadingGapMainAxis
            )
        )
        sizeConsumed = float32(
            sizeConsumed
            + float32(
                flexBasisWithMinAndMaxConstraints
                + childMarginMainAxis
                + childLeadingGapMainAxis
            )
        )
        if child.isNodeFlexible():
            totalFlexGrowFactors = float32(
                totalFlexGrowFactors + child.resolveFlexGrow()
            )
            totalFlexShrinkScaledFactors = float32(
                totalFlexShrinkScaledFactors
                + float32(
                    -child.resolveFlexShrink()
                    * childLayout.computedFlexBasis.unwrap()
                )
            )
        itemsInFlow.append(child)

    if 0 < totalFlexGrowFactors < 1:
        totalFlexGrowFactors = 1
    if 0 < totalFlexShrinkScaledFactors < 1:
        totalFlexShrinkScaledFactors = 1

    return FlexLine(
        itemsInFlow=itemsInFlow,
        sizeConsumed=sizeConsumed,
        numberOfAutoMargins=numberOfAutoMargins,
        layout=FlexLineRunningLayout(
            totalFlexGrowFactors=totalFlexGrowFactors,
            totalFlexShrinkScaledFactors=totalFlexShrinkScaledFactors,
        ),
    )
