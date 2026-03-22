# cython: infer_types=False
"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

import math

from ..numeric.Comparison import inexactEquals, isUndefined
from ..YGEnums import YGDimension, YGEdge, YGNodeType
from ..YGPixelGrid import YGRoundValueToPixelGrid as roundValueToPixelGrid


def roundLayoutResultsToPixelGrid(node, absoluteLeft: float, absoluteTop: float) -> None:
    pointScaleFactor = float(node.getConfig().getPointScaleFactor())
    nodeLeft = node.getLayout().position(YGEdge.YGEdgeLeft)
    nodeTop = node.getLayout().position(YGEdge.YGEdgeTop)
    nodeWidth = node.getLayout().dimension(YGDimension.YGDimensionWidth)
    nodeHeight = node.getLayout().dimension(YGDimension.YGDimensionHeight)
    absoluteNodeLeft = absoluteLeft + nodeLeft
    absoluteNodeTop = absoluteTop + nodeTop
    absoluteNodeRight = absoluteNodeLeft + nodeWidth
    absoluteNodeBottom = absoluteNodeTop + nodeHeight
    if pointScaleFactor != 0.0:
        textRounding = node.getNodeType() == YGNodeType.YGNodeTypeText
        node.setLayoutPosition(roundValueToPixelGrid(nodeLeft, pointScaleFactor, False, textRounding), YGEdge.YGEdgeLeft)
        node.setLayoutPosition(roundValueToPixelGrid(nodeTop, pointScaleFactor, False, textRounding), YGEdge.YGEdgeTop)
        if not isUndefined(nodeWidth):
            scaledNodeWidth = nodeWidth * pointScaleFactor
            hasFractionalWidth = (
                not inexactEquals(round(scaledNodeWidth), scaledNodeWidth)
                if math.isfinite(scaledNodeWidth)
                else False
            )
            node.getLayout().setDimension(
                YGDimension.YGDimensionWidth,
                roundValueToPixelGrid(absoluteNodeRight, pointScaleFactor, textRounding and hasFractionalWidth, textRounding and not hasFractionalWidth)
                - roundValueToPixelGrid(absoluteNodeLeft, pointScaleFactor, False, textRounding),
            )
        if not isUndefined(nodeHeight):
            scaledNodeHeight = nodeHeight * pointScaleFactor
            hasFractionalHeight = (
                not inexactEquals(round(scaledNodeHeight), scaledNodeHeight)
                if math.isfinite(scaledNodeHeight)
                else False
            )
            node.getLayout().setDimension(
                YGDimension.YGDimensionHeight,
                roundValueToPixelGrid(absoluteNodeBottom, pointScaleFactor, textRounding and hasFractionalHeight, textRounding and not hasFractionalHeight)
                - roundValueToPixelGrid(absoluteNodeTop, pointScaleFactor, False, textRounding),
            )
    for child in node.getChildren():
        roundLayoutResultsToPixelGrid(child, absoluteNodeLeft, absoluteNodeTop)
