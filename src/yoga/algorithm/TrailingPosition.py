"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from ..algorithm.FlexDirection import dimension, flexEndEdge, flexStartEdge
from ..YGEnums import YGFlexDirection
from ..node.Node import Node


def getPositionOfOppositeEdge(position: float, axis: YGFlexDirection, containingNode: Node, node: Node) -> float:
    return containingNode.getLayout().measuredDimension(dimension(axis)) - node.getLayout().measuredDimension(dimension(axis)) - position


def setChildTrailingPosition(node: Node, child: Node, axis: YGFlexDirection) -> None:
    child.setLayoutPosition(
        getPositionOfOppositeEdge(child.getLayout().position(flexStartEdge(axis)), axis, node, child),
        flexEndEdge(axis),
    )


def needsTrailingPosition(axis: YGFlexDirection) -> bool:
    return axis in (YGFlexDirection.YGFlexDirectionRowReverse, YGFlexDirection.YGFlexDirectionColumnReverse)
