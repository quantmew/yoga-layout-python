"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

import math
from typing import TYPE_CHECKING

from ..algorithm.Align import resolveChildAlignment
from ..algorithm.FlexDirection import isColumn
from ..YGEnums import YGAlign, YGDimension, YGEdge, YGPositionType

if TYPE_CHECKING:
    from ..node.Node import Node


def calculateBaseline(node: Node) -> float:
    if node.hasBaselineFunc():
        baseline = node.baseline(
            node.getLayout().measuredDimension(YGDimension.YGDimensionWidth),
            node.getLayout().measuredDimension(YGDimension.YGDimensionHeight),
        )
        if math.isnan(baseline):
            raise AssertionError("Expect custom baseline function to not return NaN")
        return baseline

    baselineChild = None
    for child in node.getLayoutChildren():
        if child.getLineIndex() > 0:
            break
        if child.style().positionType() == YGPositionType.YGPositionTypeAbsolute:
            continue
        if resolveChildAlignment(node, child) == YGAlign.YGAlignBaseline or child.isReferenceBaseline():
            baselineChild = child
            break
        if baselineChild is None:
            baselineChild = child

    if baselineChild is None:
        return node.getLayout().measuredDimension(YGDimension.YGDimensionHeight)

    baseline = calculateBaseline(baselineChild)
    return baseline + baselineChild.getLayout().position(YGEdge.YGEdgeTop)  # type: ignore[no-any-return]


def isBaselineLayout(node: Node) -> bool:
    if isColumn(node.style().flexDirection()):
        return False
    if node.style().alignItems() == YGAlign.YGAlignBaseline:
        return True
    for child in node.getLayoutChildren():
        if child.style().positionType() != YGPositionType.YGPositionTypeAbsolute and child.style().alignSelf() == YGAlign.YGAlignBaseline:
            return True
    return False
