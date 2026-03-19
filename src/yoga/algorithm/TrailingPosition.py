"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from ..algorithm.FlexDirection import dimension, flexEndEdge, flexStartEdge
from ..node.Node import Node
from ..numeric.FloatMath import float32
from ..YGEnums import YGFlexDirection


def getPositionOfOppositeEdge(position: float, axis: YGFlexDirection, containingNode: Node, node: Node) -> float:
    return float32(
        float32(
            float32(containingNode.getLayout().measuredDimension(dimension(axis)))
            - float32(node.getLayout().measuredDimension(dimension(axis)))
        )
        - float32(position)
    )


def setChildTrailingPosition(node: Node, child: Node, axis: YGFlexDirection) -> None:
    child.setLayoutPosition(
        getPositionOfOppositeEdge(child.getLayout().position(flexStartEdge(axis)), axis, node, child),
        flexEndEdge(axis),
    )


def needsTrailingPosition(axis: YGFlexDirection) -> bool:
    return axis in (YGFlexDirection.YGFlexDirectionRowReverse, YGFlexDirection.YGFlexDirectionColumnReverse)
