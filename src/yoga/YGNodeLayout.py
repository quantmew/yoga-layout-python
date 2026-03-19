"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from .node.Node import Node
from .YGEnums import YGDimension, YGDirection, YGEdge


def _getResolvedLayoutProperty(node: Node, edge: YGEdge, member: str) -> float:
    if edge > YGEdge.YGEdgeEnd:
        raise ValueError("Cannot get layout properties of multi-edge shorthands")

    layout = node.getLayout()
    if edge == YGEdge.YGEdgeStart:
        if layout.direction() == YGDirection.YGDirectionRTL:
            result = getattr(layout, member)(YGEdge.YGEdgeRight)
            return result  # type: ignore[no-any-return]
        result = getattr(layout, member)(YGEdge.YGEdgeLeft)
        return result  # type: ignore[no-any-return]

    if edge == YGEdge.YGEdgeEnd:
        if layout.direction() == YGDirection.YGDirectionRTL:
            result = getattr(layout, member)(YGEdge.YGEdgeLeft)
            return result  # type: ignore[no-any-return]
        result = getattr(layout, member)(YGEdge.YGEdgeRight)
        return result  # type: ignore[no-any-return]

    result = getattr(layout, member)(edge)
    return result  # type: ignore[no-any-return]


def YGNodeLayoutGetLeft(node: Node) -> float:
    return node.getLayout().position(YGEdge.YGEdgeLeft)


def YGNodeLayoutGetTop(node: Node) -> float:
    return node.getLayout().position(YGEdge.YGEdgeTop)


def YGNodeLayoutGetRight(node: Node) -> float:
    return node.getLayout().position(YGEdge.YGEdgeRight)


def YGNodeLayoutGetBottom(node: Node) -> float:
    return node.getLayout().position(YGEdge.YGEdgeBottom)


def YGNodeLayoutGetWidth(node: Node) -> float:
    return node.getLayout().dimension(YGDimension.YGDimensionWidth)


def YGNodeLayoutGetHeight(node: Node) -> float:
    return node.getLayout().dimension(YGDimension.YGDimensionHeight)


def YGNodeLayoutGetDirection(node: Node) -> YGDirection:
    return node.getLayout().direction()


def YGNodeLayoutGetHadOverflow(node: Node) -> bool:
    return node.getLayout().hadOverflow()


def YGNodeLayoutGetMargin(node: Node, edge: YGEdge) -> float:
    return _getResolvedLayoutProperty(node, edge, "margin")


def YGNodeLayoutGetBorder(node: Node, edge: YGEdge) -> float:
    return _getResolvedLayoutProperty(node, edge, "border")


def YGNodeLayoutGetPadding(node: Node, edge: YGEdge) -> float:
    return _getResolvedLayoutProperty(node, edge, "padding")


def YGNodeLayoutGetRawHeight(node: Node) -> float:
    return node.getLayout().rawDimension(YGDimension.YGDimensionHeight)


def YGNodeLayoutGetRawWidth(node: Node) -> float:
    return node.getLayout().rawDimension(YGDimension.YGDimensionWidth)
