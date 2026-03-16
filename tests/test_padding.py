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
    YGJustify,
    YGNodeCalculateLayout,
    YGNodeInsertChild,
    YGNodeLayoutGetHeight,
    YGNodeLayoutGetLeft,
    YGNodeLayoutGetTop,
    YGNodeLayoutGetWidth,
    YGNodeNewWithConfig,
    YGNodeStyleSetAlignItems,
    YGNodeStyleSetFlexGrow,
    YGNodeStyleSetHeight,
    YGNodeStyleSetJustifyContent,
    YGNodeStyleSetPadding,
    YGNodeStyleSetPositionType,
    YGNodeStyleSetWidth,
    YGNodeStyleSetWidthPercent,
    YGPositionType,
    YGUndefined,
)


def test_padding_no_size():
    """Test padding with no size set on container."""
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeAll, 10)
    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 20
    assert YGNodeLayoutGetHeight(root) == 20

    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 20
    assert YGNodeLayoutGetHeight(root) == 20


def test_padding_container_match_child():
    """Test padding with container matching child size."""
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeAll, 10)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 10)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 30
    assert YGNodeLayoutGetHeight(root) == 30

    assert YGNodeLayoutGetLeft(root_child0) == 10
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 10

    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 30
    assert YGNodeLayoutGetHeight(root) == 30

    assert YGNodeLayoutGetLeft(root_child0) == 10
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 10


def test_padding_flex_child():
    """Test padding with flex-grow child."""
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeAll, 10)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 10)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 10
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 80

    # RTL test - same as LTR for column direction
    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    # In Yoga, column + RTL resolves the cross axis to RowReverse.
    assert YGNodeLayoutGetLeft(root_child0) == 80
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 80


def test_padding_stretch_child():
    """Test padding with stretched child."""
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeAll, 10)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 10
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 80
    assert YGNodeLayoutGetHeight(root_child0) == 10

    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 10
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 80
    assert YGNodeLayoutGetHeight(root_child0) == 10


def test_padding_center_child():
    """Test padding with centered child (using logical edges Start/End)."""
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeStart, 10)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeEnd, 20)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeBottom, 20)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyCenter)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeStyleSetWidth(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    # LTR: Start=Left=10, End=Right=20, so content width=70
    # Centered: (70-10)/2 = 30 from left edge of content = 10+30 = 40
    assert YGNodeLayoutGetLeft(root_child0) == 40
    # Top: Start=10 padding, Bottom=20 padding, so content height=70
    # Centered: (70-10)/2 = 30 from top edge of content = 10+25 = 35 (rounded)
    assert YGNodeLayoutGetTop(root_child0) == 35
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 10

    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    # RTL: Start=Right=10, End=Left=20, so content width=70
    # Child is centered in the content area, which starts at left=20
    # (70-10)/2 = 30 from left edge of content = 20+30 = 50
    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 35
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 10


def test_child_with_padding_align_end():
    """Test child with padding aligned to end."""
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 200)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyFlexEnd)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexEnd)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeAll, 20)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 100
    assert YGNodeLayoutGetTop(root_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    # In RTL, flex-end on row means left side
    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100


def test_physical_and_relative_edge_defined():
    """Test padding with both physical (Left) and logical (End) edges."""
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 200)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeLeft, 20)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeEnd, 50)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0, 100)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    # LTR: End=Right, so Left=20 + Right=50 = 70 total horizontal padding
    # Child width = 200 - 70 = 130
    assert YGNodeLayoutGetLeft(root_child0) == 20
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 130
    assert YGNodeLayoutGetHeight(root_child0) == 50

    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    # RTL: End=Left, so Left=20 + End(Left)=50 = 70 total on left
    # But physical Left=20 is separate from logical End=Left=50
    # The child starts at position 50 (the End padding which maps to Left in RTL)
    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 150
    assert YGNodeLayoutGetHeight(root_child0) == 50
