"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from ..algorithm.BoundAxis import boundAxisWithinMinAndMax
from ..algorithm.FlexDirection import resolveDirection
from ..YGEnums import YGDirection, YGDisplay, YGPositionType, YGWrap


@dataclass
class FlexLineRunningLayout:
    totalFlexGrowFactors: float = 0.0
    totalFlexShrinkScaledFactors: float = 0.0
    remainingFreeSpace: float = 0.0
    mainDim: float = 0.0
    crossDim: float = 0.0


@dataclass
class FlexLine:
    itemsInFlow: list = field(default_factory=list)
    sizeConsumed: float = 0.0
    numberOfAutoMargins: int = 0
    layout: FlexLineRunningLayout = field(default_factory=FlexLineRunningLayout)


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
    itemsInFlow = []
    sizeConsumed = 0.0
    totalFlexGrowFactors = 0.0
    totalFlexShrinkScaledFactors = 0.0
    numberOfAutoMargins = 0
    firstElementInLine = None
    sizeConsumedIncludingMinConstraint = 0.0
    direction = node.resolveDirection(ownerDirection)
    mainAxis = resolveDirection(node.style().flexDirection(), direction)
    isNodeFlexWrap = node.style().flexWrap() != YGWrap.YGWrapNoWrap
    gap = node.style().computeGapForAxis(mainAxis, availableInnerMainDim)

    for child in children[startIndex:]:
        if child.style().display() == YGDisplay.YGDisplayNone or child.style().positionType() == YGPositionType.YGPositionTypeAbsolute:
            continue
        if firstElementInLine is None:
            firstElementInLine = child
        if child.style().flexStartMarginIsAuto(mainAxis, ownerDirection):
            numberOfAutoMargins += 1
        if child.style().flexEndMarginIsAuto(mainAxis, ownerDirection):
            numberOfAutoMargins += 1
        child.setLineIndex(lineCount)
        childMarginMainAxis = child.style().computeMarginForAxis(mainAxis, availableInnerWidth)
        childLeadingGapMainAxis = 0.0 if child == firstElementInLine else gap
        flexBasisWithMinAndMaxConstraints = boundAxisWithinMinAndMax(
            child,
            direction,
            mainAxis,
            child.getLayout().computedFlexBasis,
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
        sizeConsumedIncludingMinConstraint += (
            flexBasisWithMinAndMaxConstraints + childMarginMainAxis + childLeadingGapMainAxis
        )
        sizeConsumed += flexBasisWithMinAndMaxConstraints + childMarginMainAxis + childLeadingGapMainAxis
        if child.isNodeFlexible():
            totalFlexGrowFactors += child.resolveFlexGrow()
            totalFlexShrinkScaledFactors += -child.resolveFlexShrink() * child.getLayout().computedFlexBasis.unwrap()
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
