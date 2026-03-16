"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import (
    YGAlign,
    YGConfigNew,
    YGDirection,
    YGEdge,
    YGFlexDirection,
    YGJustify,
    YGNodeCalculateLayout,
    YGNodeInsertChild,
    YGNodeLayoutGetBottom,
    YGNodeLayoutGetHeight,
    YGNodeLayoutGetLeft,
    YGNodeLayoutGetRight,
    YGNodeLayoutGetTop,
    YGNodeLayoutGetWidth,
    YGNodeNew,
    YGNodeStyleSetAlignContent,
    YGNodeStyleSetAlignItems,
    YGNodeStyleSetAlignSelf,
    YGNodeStyleSetBorder,
    YGNodeStyleSetFlexDirection,
    YGNodeStyleSetFlexGrow,
    YGNodeStyleSetFlexWrap,
    YGNodeStyleSetHeight,
    YGNodeStyleSetJustifyContent,
    YGNodeStyleSetMargin,
    YGNodeStyleSetPadding,
    YGNodeStyleSetWidth,
    YGNodeStyleSetWidthPercent,
    YGNodeStyleSetHeightPercent,
    YGWrap,
)


def test_flex_direction_row():
    """Test flex direction row layout."""
    root = YGNodeNew()
    child0 = YGNodeNew()
    child1 = YGNodeNew()

    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 50)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(child0, 40)
    YGNodeStyleSetHeight(child0, 50)
    YGNodeStyleSetWidth(child1, 60)
    YGNodeStyleSetHeight(child1, 50)

    YGNodeInsertChild(root, child0, 0)
    YGNodeInsertChild(root, child1, 1)

    YGNodeCalculateLayout(root, 100, 50, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 50
    assert YGNodeLayoutGetLeft(child0) == 0
    assert YGNodeLayoutGetTop(child0) == 0
    assert YGNodeLayoutGetLeft(child1) == 40
    assert YGNodeLayoutGetTop(child1) == 0


def test_flex_direction_column():
    """Test flex direction column layout."""
    root = YGNodeNew()
    child0 = YGNodeNew()
    child1 = YGNodeNew()

    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionColumn)
    YGNodeStyleSetWidth(child0, 100)
    YGNodeStyleSetHeight(child0, 40)
    YGNodeStyleSetWidth(child1, 100)
    YGNodeStyleSetHeight(child1, 60)

    YGNodeInsertChild(root, child0, 0)
    YGNodeInsertChild(root, child1, 1)

    YGNodeCalculateLayout(root, 100, 100, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100
    assert YGNodeLayoutGetLeft(child0) == 0
    assert YGNodeLayoutGetTop(child0) == 0
    assert YGNodeLayoutGetLeft(child1) == 0
    assert YGNodeLayoutGetTop(child1) == 40


def test_justify_content_space_between():
    """Test justify-content: space-between."""
    root = YGNodeNew()
    child0 = YGNodeNew()
    child1 = YGNodeNew()
    child2 = YGNodeNew()

    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 50)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifySpaceBetween)
    YGNodeStyleSetWidth(child0, 20)
    YGNodeStyleSetHeight(child0, 50)
    YGNodeStyleSetWidth(child1, 20)
    YGNodeStyleSetHeight(child1, 50)
    YGNodeStyleSetWidth(child2, 20)
    YGNodeStyleSetHeight(child2, 50)

    YGNodeInsertChild(root, child0, 0)
    YGNodeInsertChild(root, child1, 1)
    YGNodeInsertChild(root, child2, 2)

    YGNodeCalculateLayout(root, 100, 50, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(child0) == 0
    assert YGNodeLayoutGetLeft(child2) == 80


def test_align_items_center():
    """Test align-items: center."""
    root = YGNodeNew()
    child0 = YGNodeNew()
    child1 = YGNodeNew()

    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)
    YGNodeStyleSetWidth(child0, 40)
    YGNodeStyleSetHeight(child0, 40)
    YGNodeStyleSetWidth(child1, 40)
    YGNodeStyleSetHeight(child1, 60)

    YGNodeInsertChild(root, child0, 0)
    YGNodeInsertChild(root, child1, 1)

    YGNodeCalculateLayout(root, 100, 100, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetTop(child0) == 30  # (100 - 40) / 2
    assert YGNodeLayoutGetTop(child1) == 20  # (100 - 60) / 2


def test_align_self_flex_end():
    """Test align-self: flex-end."""
    root = YGNodeNew()
    child0 = YGNodeNew()
    child1 = YGNodeNew()

    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetAlignSelf(child1, YGAlign.YGAlignFlexEnd)
    YGNodeStyleSetWidth(child0, 40)
    YGNodeStyleSetHeight(child0, 40)
    YGNodeStyleSetWidth(child1, 40)
    YGNodeStyleSetHeight(child1, 60)

    YGNodeInsertChild(root, child0, 0)
    YGNodeInsertChild(root, child1, 1)

    YGNodeCalculateLayout(root, 100, 100, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetTop(child0) == 0
    assert YGNodeLayoutGetTop(child1) == 40  # 100 - 60


def test_flex_grow():
    """Test flex-grow."""
    root = YGNodeNew()
    child0 = YGNodeNew()
    child1 = YGNodeNew()

    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 50)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexGrow(child0, 1)
    YGNodeStyleSetFlexGrow(child1, 2)
    YGNodeStyleSetHeight(child0, 50)
    YGNodeStyleSetHeight(child1, 50)

    YGNodeInsertChild(root, child0, 0)
    YGNodeInsertChild(root, child1, 1)

    YGNodeCalculateLayout(root, 100, 50, YGDirection.YGDirectionLTR)

    # child0 gets 1/3 of space, child1 gets 2/3
    # Note: due to pixel rounding, we allow some tolerance
    assert abs(YGNodeLayoutGetWidth(child0) - 33.333) < 1.0
    assert abs(YGNodeLayoutGetWidth(child1) - 66.666) < 1.0


def test_margin():
    """Test margin."""
    root = YGNodeNew()
    child = YGNodeNew()

    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetMargin(child, YGEdge.YGEdgeLeft, 10)
    YGNodeStyleSetMargin(child, YGEdge.YGEdgeTop, 20)
    YGNodeStyleSetWidth(child, 50)
    YGNodeStyleSetHeight(child, 50)

    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, 100, 100, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(child) == 10
    assert YGNodeLayoutGetTop(child) == 20


def test_padding():
    """Test padding."""
    root = YGNodeNew()
    child = YGNodeNew()

    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeLeft, 10)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeTop, 20)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeRight, 30)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeBottom, 40)
    YGNodeStyleSetWidth(child, 50)
    YGNodeStyleSetHeight(child, 50)

    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, 100, 100, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(child) == 10
    assert YGNodeLayoutGetTop(child) == 20


def test_border():
    """Test border."""
    root = YGNodeNew()
    child = YGNodeNew()

    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeLeft, 5)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetWidth(child, 50)
    YGNodeStyleSetHeight(child, 50)

    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, 100, 100, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(child) == 5
    assert YGNodeLayoutGetTop(child) == 10


def test_percent_width_height():
    """Test percentage width and height."""
    root = YGNodeNew()
    child = YGNodeNew()

    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidthPercent(child, 50)
    YGNodeStyleSetHeightPercent(child, 50)

    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, 200, 100, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetWidth(child) == 100
    assert YGNodeLayoutGetHeight(child) == 50


def test_align_content_stretch():
    """Test align-content: stretch with flex-wrap."""
    root = YGNodeNew()
    child0 = YGNodeNew()
    child1 = YGNodeNew()

    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignStretch)
    YGNodeStyleSetHeight(child0, 40)
    YGNodeStyleSetHeight(child1, 40)

    YGNodeInsertChild(root, child0, 0)
    YGNodeInsertChild(root, child1, 1)

    YGNodeCalculateLayout(root, 100, 100, YGDirection.YGDirectionLTR)

    # Children should stretch to fill the cross axis


def test_justify_content_center():
    """Test justify-content: center."""
    root = YGNodeNew()
    child = YGNodeNew()

    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 50)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyCenter)
    YGNodeStyleSetWidth(child, 40)
    YGNodeStyleSetHeight(child, 50)

    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, 100, 50, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(child) == 30  # (100 - 40) / 2


def test_justify_content_flex_end():
    """Test justify-content: flex-end."""
    root = YGNodeNew()
    child = YGNodeNew()

    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 50)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyFlexEnd)
    YGNodeStyleSetWidth(child, 40)
    YGNodeStyleSetHeight(child, 50)

    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, 100, 50, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(child) == 60  # 100 - 40
