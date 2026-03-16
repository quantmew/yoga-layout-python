import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from yoga import *  # noqa: E402,F403

def test_justify_content_row_flex_start():
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
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

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

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

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

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_justify_content_row_flex_end():
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
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

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

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

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

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_justify_content_row_center():
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
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

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

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

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

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_justify_content_row_space_between():
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
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

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

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 92
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 102

    assert YGNodeLayoutGetLeft(root_child1) == 46
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 102

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 102

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_justify_content_row_space_around():
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
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

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

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 80
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 102

    assert YGNodeLayoutGetLeft(root_child1) == 46
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 102

    assert YGNodeLayoutGetLeft(root_child2) == 12
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 102

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_justify_content_column_flex_start():
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
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

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

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

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

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_justify_content_column_flex_end():
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
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

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

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

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

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_justify_content_column_center():
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
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

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

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

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

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_justify_content_column_space_between():
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
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

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

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

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

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_justify_content_column_space_around():
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
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

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

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

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

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_justify_content_row_min_width_and_margin():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetMinWidth(root, 50)
    YGNodeStyleSetMargin(root, YGEdge.YGEdgeLeft, 100)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyCenter)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 20)
    YGNodeStyleSetWidth(root_child0, 20)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 100
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 50
    assert YGNodeLayoutGetHeight(root) == 20

    assert YGNodeLayoutGetLeft(root_child0) == 15
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 100
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 50
    assert YGNodeLayoutGetHeight(root) == 20

    assert YGNodeLayoutGetLeft(root_child0) == 15
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_justify_content_row_max_width_and_margin():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetMaxWidth(root, 80)
    YGNodeStyleSetMargin(root, YGEdge.YGEdgeLeft, 100)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyCenter)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 20)
    YGNodeStyleSetWidth(root_child0, 20)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 100
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 80
    assert YGNodeLayoutGetHeight(root) == 20

    assert YGNodeLayoutGetLeft(root_child0) == 30
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 100
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 80
    assert YGNodeLayoutGetHeight(root) == 20

    assert YGNodeLayoutGetLeft(root_child0) == 30
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_justify_content_column_min_height_and_margin():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetMinHeight(root, 50)
    YGNodeStyleSetMargin(root, YGEdge.YGEdgeTop, 100)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyCenter)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 20)
    YGNodeStyleSetWidth(root_child0, 20)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 100
    assert YGNodeLayoutGetWidth(root) == 20
    assert YGNodeLayoutGetHeight(root) == 50

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 15
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 100
    assert YGNodeLayoutGetWidth(root) == 20
    assert YGNodeLayoutGetHeight(root) == 50

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 15
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_justify_content_column_max_height_and_margin():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetMaxHeight(root, 80)
    YGNodeStyleSetMargin(root, YGEdge.YGEdgeTop, 100)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyCenter)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 20)
    YGNodeStyleSetWidth(root_child0, 20)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 100
    assert YGNodeLayoutGetWidth(root) == 20
    assert YGNodeLayoutGetHeight(root) == 80

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 30
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 100
    assert YGNodeLayoutGetWidth(root) == 20
    assert YGNodeLayoutGetHeight(root) == 80

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 30
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_justify_content_column_space_evenly():
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
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

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

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

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

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_justify_content_row_space_evenly():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 102)
    YGNodeStyleSetHeight(root, 102)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifySpaceEvenly)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child2, 10)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 26
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 51
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 0
    assert YGNodeLayoutGetHeight(root_child1) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 77
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 0
    assert YGNodeLayoutGetHeight(root_child2) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 77
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 51
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 0
    assert YGNodeLayoutGetHeight(root_child1) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 26
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 0
    assert YGNodeLayoutGetHeight(root_child2) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_justify_content_min_width_with_padding_child_width_greater_than_parent():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 1000)
    YGNodeStyleSetHeight(root, 1584)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignStretch)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(root_child0, YGAlign.YGAlignStretch)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetJustifyContent(root_child0_child0, YGJustify.YGJustifyCenter)
    YGNodeStyleSetAlignContent(root_child0_child0, YGAlign.YGAlignStretch)
    YGNodeStyleSetMinWidth(root_child0_child0, 400)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeLeft, 100)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeRight, 100)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0_child0, 300)
    YGNodeStyleSetAlignContent(root_child0_child0_child0, YGAlign.YGAlignStretch)
    YGNodeStyleSetFlexDirection(root_child0_child0_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 1000
    assert YGNodeLayoutGetHeight(root) == 1584

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 1000
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 500
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 300
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 1000
    assert YGNodeLayoutGetHeight(root) == 1584

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 1000
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 500
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 500
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 300
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_justify_content_min_width_with_padding_child_width_lower_than_parent():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 1080)
    YGNodeStyleSetHeight(root, 1584)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignStretch)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(root_child0, YGAlign.YGAlignStretch)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetJustifyContent(root_child0_child0, YGJustify.YGJustifyCenter)
    YGNodeStyleSetAlignContent(root_child0_child0, YGAlign.YGAlignStretch)
    YGNodeStyleSetMinWidth(root_child0_child0, 400)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeLeft, 100)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeRight, 100)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0_child0, 199)
    YGNodeStyleSetAlignContent(root_child0_child0_child0, YGAlign.YGAlignStretch)
    YGNodeStyleSetFlexDirection(root_child0_child0_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 1080
    assert YGNodeLayoutGetHeight(root) == 1584

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 1080
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 101
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 199
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 1080
    assert YGNodeLayoutGetHeight(root) == 1584

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 1080
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 680
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 101
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 199
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_justify_content_space_between_indefinite_container_dim_with_free_space():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 300)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetMinWidth(root_child0, 200)
    YGNodeStyleSetJustifyContent(root_child0, YGJustify.YGJustifySpaceBetween)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 50)
    YGNodeStyleSetHeight(root_child0_child0, 50)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 50)
    YGNodeStyleSetHeight(root_child0_child1, 50)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 50

    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 150
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 50
    assert YGNodeLayoutGetHeight(root_child0_child1) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 50

    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0) == 150
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 50
    assert YGNodeLayoutGetHeight(root_child0_child1) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_justify_content_flex_start_row_reverse():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRowReverse)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 20)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 20)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 20)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 80
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 60
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 40
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 20
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 40
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_justify_content_flex_end_row_reverse():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRowReverse)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 20)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 20)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 20)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 80
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 60
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 40
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 20
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 40
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_justify_content_overflow_row_flex_start():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 102)
    YGNodeStyleSetHeight(root, 102)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 40)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 40)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 40)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0) == 102

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 40
    assert YGNodeLayoutGetHeight(root_child1) == 102

    assert YGNodeLayoutGetLeft(root_child2) == 80
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 40
    assert YGNodeLayoutGetHeight(root_child2) == 102

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 62
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0) == 102

    assert YGNodeLayoutGetLeft(root_child1) == 22
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 40
    assert YGNodeLayoutGetHeight(root_child1) == 102

    assert YGNodeLayoutGetLeft(root_child2) == -18
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 40
    assert YGNodeLayoutGetHeight(root_child2) == 102

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_justify_content_overflow_row_flex_end():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 102)
    YGNodeStyleSetHeight(root, 102)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyFlexEnd)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 40)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 40)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 40)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == -18
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0) == 102

    assert YGNodeLayoutGetLeft(root_child1) == 22
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 40
    assert YGNodeLayoutGetHeight(root_child1) == 102

    assert YGNodeLayoutGetLeft(root_child2) == 62
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 40
    assert YGNodeLayoutGetHeight(root_child2) == 102

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 80
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0) == 102

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 40
    assert YGNodeLayoutGetHeight(root_child1) == 102

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 40
    assert YGNodeLayoutGetHeight(root_child2) == 102

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_justify_content_overflow_row_center():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 102)
    YGNodeStyleSetHeight(root, 102)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyCenter)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 40)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 40)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 40)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == -9
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0) == 102

    assert YGNodeLayoutGetLeft(root_child1) == 31
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 40
    assert YGNodeLayoutGetHeight(root_child1) == 102

    assert YGNodeLayoutGetLeft(root_child2) == 71
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 40
    assert YGNodeLayoutGetHeight(root_child2) == 102

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 71
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0) == 102

    assert YGNodeLayoutGetLeft(root_child1) == 31
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 40
    assert YGNodeLayoutGetHeight(root_child1) == 102

    assert YGNodeLayoutGetLeft(root_child2) == -9
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 40
    assert YGNodeLayoutGetHeight(root_child2) == 102

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_justify_content_overflow_row_space_between():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 102)
    YGNodeStyleSetHeight(root, 102)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifySpaceBetween)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 40)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 40)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 40)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0) == 102

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 40
    assert YGNodeLayoutGetHeight(root_child1) == 102

    assert YGNodeLayoutGetLeft(root_child2) == 80
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 40
    assert YGNodeLayoutGetHeight(root_child2) == 102

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 62
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0) == 102

    assert YGNodeLayoutGetLeft(root_child1) == 22
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 40
    assert YGNodeLayoutGetHeight(root_child1) == 102

    assert YGNodeLayoutGetLeft(root_child2) == -18
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 40
    assert YGNodeLayoutGetHeight(root_child2) == 102

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_justify_content_overflow_row_space_around():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 102)
    YGNodeStyleSetHeight(root, 102)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifySpaceAround)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 40)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 40)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 40)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0) == 102

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 40
    assert YGNodeLayoutGetHeight(root_child1) == 102

    assert YGNodeLayoutGetLeft(root_child2) == 80
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 40
    assert YGNodeLayoutGetHeight(root_child2) == 102

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 62
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0) == 102

    assert YGNodeLayoutGetLeft(root_child1) == 22
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 40
    assert YGNodeLayoutGetHeight(root_child1) == 102

    assert YGNodeLayoutGetLeft(root_child2) == -18
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 40
    assert YGNodeLayoutGetHeight(root_child2) == 102

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_justify_content_overflow_row_space_evenly():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 102)
    YGNodeStyleSetHeight(root, 102)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifySpaceEvenly)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 40)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 40)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 40)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0) == 102

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 40
    assert YGNodeLayoutGetHeight(root_child1) == 102

    assert YGNodeLayoutGetLeft(root_child2) == 80
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 40
    assert YGNodeLayoutGetHeight(root_child2) == 102

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 62
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0) == 102

    assert YGNodeLayoutGetLeft(root_child1) == 22
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 40
    assert YGNodeLayoutGetHeight(root_child1) == 102

    assert YGNodeLayoutGetLeft(root_child2) == -18
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 40
    assert YGNodeLayoutGetHeight(root_child2) == 102

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_justify_content_overflow_row_reverse_space_around():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 102)
    YGNodeStyleSetHeight(root, 102)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifySpaceAround)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 40)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 40)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 40)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 80
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0) == 102

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 40
    assert YGNodeLayoutGetHeight(root_child1) == 102

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 40
    assert YGNodeLayoutGetHeight(root_child2) == 102

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == -18
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0) == 102

    assert YGNodeLayoutGetLeft(root_child1) == 22
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 40
    assert YGNodeLayoutGetHeight(root_child1) == 102

    assert YGNodeLayoutGetLeft(root_child2) == 62
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 40
    assert YGNodeLayoutGetHeight(root_child2) == 102

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_justify_content_overflow_row_reverse_space_evenly():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 102)
    YGNodeStyleSetHeight(root, 102)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifySpaceEvenly)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 40)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 40)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 40)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 80
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0) == 102

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 40
    assert YGNodeLayoutGetHeight(root_child1) == 102

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 40
    assert YGNodeLayoutGetHeight(root_child2) == 102

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == -18
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0) == 102

    assert YGNodeLayoutGetLeft(root_child1) == 22
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 40
    assert YGNodeLayoutGetHeight(root_child1) == 102

    assert YGNodeLayoutGetLeft(root_child2) == 62
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 40
    assert YGNodeLayoutGetHeight(root_child2) == 102

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_justify_content_overflow_row_space_evenly_auto_margin():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 102)
    YGNodeStyleSetHeight(root, 102)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifySpaceEvenly)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 40)
    YGNodeStyleSetMarginAuto(root_child0, YGEdge.YGEdgeRight)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 40)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 40)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0) == 102

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 40
    assert YGNodeLayoutGetHeight(root_child1) == 102

    assert YGNodeLayoutGetLeft(root_child2) == 80
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 40
    assert YGNodeLayoutGetHeight(root_child2) == 102

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 102
    assert YGNodeLayoutGetHeight(root) == 102

    assert YGNodeLayoutGetLeft(root_child0) == 62
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0) == 102

    assert YGNodeLayoutGetLeft(root_child1) == 22
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 40
    assert YGNodeLayoutGetHeight(root_child1) == 102

    assert YGNodeLayoutGetLeft(root_child2) == -18
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 40
    assert YGNodeLayoutGetHeight(root_child2) == 102

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

