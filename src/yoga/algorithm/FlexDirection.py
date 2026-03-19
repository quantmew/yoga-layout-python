"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from ..debug.AssertFatal import fatalWithMessage
from ..YGEnums import YGDimension, YGDirection, YGEdge, YGFlexDirection


def isRow(flexDirection: YGFlexDirection) -> bool:
    return flexDirection in (YGFlexDirection.YGFlexDirectionRow, YGFlexDirection.YGFlexDirectionRowReverse)


def isColumn(flexDirection: YGFlexDirection) -> bool:
    return flexDirection in (YGFlexDirection.YGFlexDirectionColumn, YGFlexDirection.YGFlexDirectionColumnReverse)


def resolveDirection(flexDirection: YGFlexDirection, direction: YGDirection) -> YGFlexDirection:
    if direction == YGDirection.YGDirectionRTL:
        if flexDirection == YGFlexDirection.YGFlexDirectionRow:
            return YGFlexDirection.YGFlexDirectionRowReverse
        if flexDirection == YGFlexDirection.YGFlexDirectionRowReverse:
            return YGFlexDirection.YGFlexDirectionRow
    return flexDirection


def resolveCrossDirection(flexDirection: YGFlexDirection, direction: YGDirection) -> YGFlexDirection:
    return resolveDirection(YGFlexDirection.YGFlexDirectionRow, direction) if isColumn(flexDirection) else YGFlexDirection.YGFlexDirectionColumn


def flexStartEdge(flexDirection: YGFlexDirection) -> YGEdge:
    if flexDirection == YGFlexDirection.YGFlexDirectionColumn:
        return YGEdge.YGEdgeTop
    if flexDirection == YGFlexDirection.YGFlexDirectionColumnReverse:
        return YGEdge.YGEdgeBottom
    if flexDirection == YGFlexDirection.YGFlexDirectionRow:
        return YGEdge.YGEdgeLeft
    if flexDirection == YGFlexDirection.YGFlexDirectionRowReverse:
        return YGEdge.YGEdgeRight
    fatalWithMessage("Invalid FlexDirection")


def flexEndEdge(flexDirection: YGFlexDirection) -> YGEdge:
    if flexDirection == YGFlexDirection.YGFlexDirectionColumn:
        return YGEdge.YGEdgeBottom
    if flexDirection == YGFlexDirection.YGFlexDirectionColumnReverse:
        return YGEdge.YGEdgeTop
    if flexDirection == YGFlexDirection.YGFlexDirectionRow:
        return YGEdge.YGEdgeRight
    if flexDirection == YGFlexDirection.YGFlexDirectionRowReverse:
        return YGEdge.YGEdgeLeft
    fatalWithMessage("Invalid FlexDirection")


def inlineStartEdge(flexDirection: YGFlexDirection, direction: YGDirection) -> YGEdge:
    if isRow(flexDirection):
        return YGEdge.YGEdgeRight if direction == YGDirection.YGDirectionRTL else YGEdge.YGEdgeLeft
    return YGEdge.YGEdgeTop


def inlineEndEdge(flexDirection: YGFlexDirection, direction: YGDirection) -> YGEdge:
    if isRow(flexDirection):
        return YGEdge.YGEdgeLeft if direction == YGDirection.YGDirectionRTL else YGEdge.YGEdgeRight
    return YGEdge.YGEdgeBottom


def dimension(flexDirection: YGFlexDirection) -> YGDimension:
    if flexDirection in (YGFlexDirection.YGFlexDirectionColumn, YGFlexDirection.YGFlexDirectionColumnReverse):
        return YGDimension.YGDimensionHeight
    if flexDirection in (YGFlexDirection.YGFlexDirectionRow, YGFlexDirection.YGFlexDirectionRowReverse):
        return YGDimension.YGDimensionWidth
    fatalWithMessage("Invalid FlexDirection")
    raise AssertionError("Unreachable")  # type: ignore[return-value]
