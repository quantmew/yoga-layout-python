"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import (
    YGConfigNew,
    YGDirection,
    YGEdge,
    YGFlexDirection,
    YGNodeCalculateLayout,
    YGNodeInsertChild,
    YGNodeLayoutGetHeight,
    YGNodeLayoutGetLeft,
    YGNodeLayoutGetTop,
    YGNodeLayoutGetWidth,
    YGNodeNewWithConfig,
    YGNodeStyleSetFlexDirection,
    YGNodeStyleSetHeight,
    YGNodeStyleSetMargin,
    YGNodeStyleSetWidth,
    YGNodeStyleSetPositionType,
    YGPositionType,
    YGUndefined,
)


def test_margin_top():
    """Test margin-top."""
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeTop, 10)
    YGNodeInsertChild(root, root_child0, 0)

    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 10

    # RTL test - margin-top is not affected by direction
    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 10


def test_margin_bottom():
    """Test margin-bottom."""
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeInsertChild(root, root_child0, 0)

    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    # Without justify-content, child is at the top
    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 10

    # RTL test - margin-bottom is not affected by direction
    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 10


def test_margin_left():
    """Test margin-left (physical edge, not affected by RTL)."""
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 10)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeLeft, 10)
    YGNodeInsertChild(root, root_child0, 0)

    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    # Physical left margin is always applied on the left
    assert YGNodeLayoutGetLeft(root_child0) == 10
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    # RTL test - physical left margin stays on left side
    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    # In RTL, the physical left margin is still on the left
    # But the flex direction is reversed, so the child is positioned from the right
    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100


def test_margin_right():
    """Test margin-right (physical edge, not affected by RTL)."""
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 10)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeRight, 10)
    YGNodeInsertChild(root, root_child0, 0)

    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    # Physical right margin doesn't affect left position in LTR
    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    # RTL test - physical right margin stays on right side
    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    # In RTL, the physical right margin is still on the right
    # But flex direction is reversed, so positioning is from the left edge
    assert YGNodeLayoutGetLeft(root_child0) == 80
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100
