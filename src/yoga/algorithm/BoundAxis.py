# cython: infer_types=False
"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from .._cython_compat import cython
from ..algorithm.FlexDirection import isColumn, isRow
from ..node.Node import Node
from ..numeric.Comparison import maxOrDefined
from ..numeric.FloatOptional import FloatOptional
from ..YGEnums import YGDimension, YGDirection, YGFlexDirection


@cython.locals(result=cython.double)
def paddingAndBorderForAxis(
    node: Node,
    axis: YGFlexDirection,
    direction: YGDirection,
    widthSize: float,
) -> float:
    result = (
        node.style().computeInlineStartPaddingAndBorder(axis, direction, widthSize)
        + node.style().computeInlineEndPaddingAndBorder(axis, direction, widthSize)
    )
    return result


def boundAxisWithinMinAndMax(
    node: Node,
    direction: YGDirection,
    axis: YGFlexDirection,
    value: FloatOptional,
    axisSize: float,
    widthSize: float,
) -> FloatOptional:
    min_value = FloatOptional()
    max_value = FloatOptional()
    if isColumn(axis):
        min_value = node.style().resolvedMinDimension(
            direction, YGDimension.YGDimensionHeight, axisSize, widthSize
        )
        max_value = node.style().resolvedMaxDimension(
            direction, YGDimension.YGDimensionHeight, axisSize, widthSize
        )
    elif isRow(axis):
        min_value = node.style().resolvedMinDimension(
            direction, YGDimension.YGDimensionWidth, axisSize, widthSize
        )
        max_value = node.style().resolvedMaxDimension(
            direction, YGDimension.YGDimensionWidth, axisSize, widthSize
        )
    if max_value >= FloatOptional(0.0) and value > max_value:
        return max_value
    if min_value >= FloatOptional(0.0) and value < min_value:
        return min_value
    return value


def boundAxis(
    node: Node,
    axis: YGFlexDirection,
    direction: YGDirection,
    value: float,
    axisSize: float,
    widthSize: float,
) -> float:
    return maxOrDefined(
        boundAxisWithinMinAndMax(
            node, direction, axis, FloatOptional(value), axisSize, widthSize
        ).unwrap(),
        paddingAndBorderForAxis(node, axis, direction, widthSize),
    )
