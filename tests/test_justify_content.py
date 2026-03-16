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
    YGNodeNewWithConfig,
    YGNodeStyleSetAlignContent,
    YGNodeStyleSetAlignItems,
    YGNodeStyleSetAlignSelf,
    YGNodeStyleSetBorder,
    YGNodeStyleSetDisplay,
    YGNodeStyleSetFlexDirection,
    YGNodeStyleSetFlexGrow,
    YGNodeStyleSetFlexShrink,
    YGNodeStyleSetFlexWrap,
    YGNodeStyleSetHeight,
    YGNodeStyleSetJustifyContent,
    YGNodeStyleSetMargin,
    YGNodeStyleSetMaxHeight,
    YGNodeStyleSetMaxWidth,
    YGNodeStyleSetMinHeight,
    YGNodeStyleSetMinWidth,
    YGNodeStyleSetOverflow,
    YGNodeStyleSetPadding,
    YGNodeStyleSetPosition,
    YGNodeStyleSetPositionType,
    YGNodeStyleSetWidth,
    YGNodeStyleSetHeightPercent,
    YGNodeStyleSetWidthPercent,
    YGPositionType,
    YGWrap,
    YGUndefined,
)


def test_justify_content_row_flex_start():
    """Test justify-content: flex-start on row."""
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 102)
    YGNodeStyleSetHeight(root, 102)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 10)
    YGNodeInsertChild(root, root_child2, 2)

    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 102

    assert YGNodeLayoutGetLeft(root_child1) == 10
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 102

    assert YGNodeLayoutGetLeft(root_child2) == 20
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 102

    # RTL test
    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 92
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 102

    assert YGNodeLayoutGetLeft(root_child1) == 82
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 102

    assert YGNodeLayoutGetLeft(root_child2) == 72
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 102


def test_justify_content_row_flex_end():
    """Test justify-content: flex-end on row."""
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 102)
    YGNodeStyleSetHeight(root, 102)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyFlexEnd)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 10)
    YGNodeInsertChild(root, root_child2, 2)

    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 72
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 102

    assert YGNodeLayoutGetLeft(root_child1) == 82
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 102

    assert YGNodeLayoutGetLeft(root_child2) == 92
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 102

    # RTL test
    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 20
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 102

    assert YGNodeLayoutGetLeft(root_child1) == 10
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 102

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 102


def test_justify_content_row_center():
    """Test justify-content: center on row."""
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 102)
    YGNodeStyleSetHeight(root, 102)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyCenter)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 10)
    YGNodeInsertChild(root, root_child2, 2)

    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 36
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 102

    assert YGNodeLayoutGetLeft(root_child1) == 46
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 102

    assert YGNodeLayoutGetLeft(root_child2) == 56
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 102

    # RTL test
    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 56
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 102

    assert YGNodeLayoutGetLeft(root_child1) == 46
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 102

    assert YGNodeLayoutGetLeft(root_child2) == 36
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 102


def test_justify_content_row_space_between():
    """Test justify-content: space-between on row."""
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 102)
    YGNodeStyleSetHeight(root, 102)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifySpaceBetween)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 10)
    YGNodeInsertChild(root, root_child2, 2)

    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 102

    assert YGNodeLayoutGetLeft(root_child1) == 46
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 102

    assert YGNodeLayoutGetLeft(root_child2) == 92
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 102


def test_justify_content_row_space_around():
    """Test justify-content: space-around on row."""
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 102)
    YGNodeStyleSetHeight(root, 102)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifySpaceAround)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 10)
    YGNodeInsertChild(root, root_child2, 2)

    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 12
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 102

    assert YGNodeLayoutGetLeft(root_child1) == 46
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 102

    assert YGNodeLayoutGetLeft(root_child2) == 80
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 102


def test_justify_content_row_space_evenly():
    """Test justify-content: space-evenly on row."""
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 102)
    YGNodeStyleSetHeight(root, 102)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifySpaceEvenly)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 10)
    YGNodeInsertChild(root, root_child2, 2)

    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 18
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 102

    assert YGNodeLayoutGetLeft(root_child1) == 46
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 102

    assert YGNodeLayoutGetLeft(root_child2) == 74
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 102


def test_justify_content_column_flex_start():
    """Test justify-content: flex-start on column."""
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 102)
    YGNodeStyleSetHeight(root, 102)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child2, 10)
    YGNodeInsertChild(root, root_child2, 2)

    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 102
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 10
    assert YGNodeLayoutGetWidth(root_child1) == 102
    assert YGNodeLayoutGetHeight(root_child1) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 20
    assert YGNodeLayoutGetWidth(root_child2) == 102
    assert YGNodeLayoutGetHeight(root_child2) == 10


def test_justify_content_column_flex_end():
    """Test justify-content: flex-end on column."""
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 102)
    YGNodeStyleSetHeight(root, 102)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyFlexEnd)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child2, 10)
    YGNodeInsertChild(root, root_child2, 2)

    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 72
    assert YGNodeLayoutGetWidth(root_child0) == 102
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 82
    assert YGNodeLayoutGetWidth(root_child1) == 102
    assert YGNodeLayoutGetHeight(root_child1) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 92
    assert YGNodeLayoutGetWidth(root_child2) == 102
    assert YGNodeLayoutGetHeight(root_child2) == 10


def test_justify_content_column_center():
    """Test justify-content: center on column."""
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 102)
    YGNodeStyleSetHeight(root, 102)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyCenter)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child2, 10)
    YGNodeInsertChild(root, root_child2, 2)

    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 36
    assert YGNodeLayoutGetWidth(root_child0) == 102
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 46
    assert YGNodeLayoutGetWidth(root_child1) == 102
    assert YGNodeLayoutGetHeight(root_child1) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 56
    assert YGNodeLayoutGetWidth(root_child2) == 102
    assert YGNodeLayoutGetHeight(root_child2) == 10


def test_justify_content_column_space_between():
    """Test justify-content: space-between on column."""
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 102)
    YGNodeStyleSetHeight(root, 102)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifySpaceBetween)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child2, 10)
    YGNodeInsertChild(root, root_child2, 2)

    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 102
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 46
    assert YGNodeLayoutGetWidth(root_child1) == 102
    assert YGNodeLayoutGetHeight(root_child1) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 92
    assert YGNodeLayoutGetWidth(root_child2) == 102
    assert YGNodeLayoutGetHeight(root_child2) == 10


def test_justify_content_column_space_around():
    """Test justify-content: space-around on column."""
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 102)
    YGNodeStyleSetHeight(root, 102)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifySpaceAround)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child2, 10)
    YGNodeInsertChild(root, root_child2, 2)

    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 12
    assert YGNodeLayoutGetWidth(root_child0) == 102
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 46
    assert YGNodeLayoutGetWidth(root_child1) == 102
    assert YGNodeLayoutGetHeight(root_child1) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 80
    assert YGNodeLayoutGetWidth(root_child2) == 102
    assert YGNodeLayoutGetHeight(root_child2) == 10


def test_justify_content_column_space_evenly():
    """Test justify-content: space-evenly on column."""
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 102)
    YGNodeStyleSetHeight(root, 102)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifySpaceEvenly)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child2, 10)
    YGNodeInsertChild(root, root_child2, 2)

    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 18
    assert YGNodeLayoutGetWidth(root_child0) == 102
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 46
    assert YGNodeLayoutGetWidth(root_child1) == 102
    assert YGNodeLayoutGetHeight(root_child1) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 74
    assert YGNodeLayoutGetWidth(root_child2) == 102
    assert YGNodeLayoutGetHeight(root_child2) == 10
