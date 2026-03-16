import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from yoga import *  # noqa: E402,F403

def test_flex_direction_column_no_height():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)

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
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 30

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 10
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 20
    assert YGNodeLayoutGetWidth(root_child2) == 100
    assert YGNodeLayoutGetHeight(root_child2) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 30

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 10
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 20
    assert YGNodeLayoutGetWidth(root_child2) == 100
    assert YGNodeLayoutGetHeight(root_child2) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_no_width():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
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
    assert YGNodeLayoutGetWidth(root) == 30
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 10
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 20
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 30
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 20
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 10
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_column():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

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
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 10
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 20
    assert YGNodeLayoutGetWidth(root_child2) == 100
    assert YGNodeLayoutGetHeight(root_child2) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 10
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 20
    assert YGNodeLayoutGetWidth(root_child2) == 100
    assert YGNodeLayoutGetHeight(root_child2) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)
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
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 10
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 20
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 80
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 70
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_column_reverse():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionColumnReverse)

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
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 90
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 80
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 70
    assert YGNodeLayoutGetWidth(root_child2) == 100
    assert YGNodeLayoutGetHeight(root_child2) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 90
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 80
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 70
    assert YGNodeLayoutGetWidth(root_child2) == 100
    assert YGNodeLayoutGetHeight(root_child2) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRowReverse)

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
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 80
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 70
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 10
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 20
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse_margin_left():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeStyleSetMargin(root, YGEdge.YGEdgeLeft, 100)

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

    assert YGNodeLayoutGetLeft(root) == 100
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 80
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 70
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 100
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 10
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 20
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse_margin_start():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeStyleSetMargin(root, YGEdge.YGEdgeStart, 100)

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

    assert YGNodeLayoutGetLeft(root) == 100
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 80
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 70
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 10
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 20
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse_margin_right():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeStyleSetMargin(root, YGEdge.YGEdgeRight, 100)

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
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 80
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 70
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 10
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 20
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse_margin_end():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeStyleSetMargin(root, YGEdge.YGEdgeEnd, 100)

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
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 80
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 70
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 100
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 10
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 20
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_column_reverse_margin_top():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionColumnReverse)
    YGNodeStyleSetMargin(root, YGEdge.YGEdgeTop, 100)

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
    assert YGNodeLayoutGetTop(root) == 100
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 100
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 0

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 100
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 100
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child1) == 90
    assert YGNodeLayoutGetTop(root_child1) == 100
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 0

    assert YGNodeLayoutGetLeft(root_child2) == 90
    assert YGNodeLayoutGetTop(root_child2) == 100
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 0

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_column_reverse_margin_bottom():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionColumnReverse)
    YGNodeStyleSetMargin(root, YGEdge.YGEdgeBottom, 100)

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
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 100
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 0

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 100
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child1) == 90
    assert YGNodeLayoutGetTop(root_child1) == 100
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 0

    assert YGNodeLayoutGetLeft(root_child2) == 90
    assert YGNodeLayoutGetTop(root_child2) == 100
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 0

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse_padding_left():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeLeft, 100)

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
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 80
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 70
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 110
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 120
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse_padding_start():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeStart, 100)

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
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 80
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 70
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 10
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 20
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse_padding_right():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeRight, 100)

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
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == -10
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == -20
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == -30
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 10
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 20
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse_padding_end():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeEnd, 100)

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
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == -10
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == -20
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == -30
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 110
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 120
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_column_reverse_padding_top():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionColumnReverse)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeTop, 100)

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
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 100
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 0

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 100
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child1) == 90
    assert YGNodeLayoutGetTop(root_child1) == 100
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 0

    assert YGNodeLayoutGetLeft(root_child2) == 90
    assert YGNodeLayoutGetTop(root_child2) == 100
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 0

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_column_reverse_padding_bottom():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionColumnReverse)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeBottom, 100)

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
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 0

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child1) == 90
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 0

    assert YGNodeLayoutGetLeft(root_child2) == 90
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 0

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse_border_left():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeLeft, 100)

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
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 80
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 70
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 110
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 120
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse_border_start():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeStart, 100)

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
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 80
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 70
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 10
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 20
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse_border_right():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeRight, 100)

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
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == -10
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == -20
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == -30
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 10
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 20
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse_border_end():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeEnd, 100)

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
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == -10
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == -20
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == -30
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 110
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 120
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_column_reverse_border_top():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionColumnReverse)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeTop, 100)

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
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 100
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 0

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 100
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child1) == 90
    assert YGNodeLayoutGetTop(root_child1) == 100
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 0

    assert YGNodeLayoutGetLeft(root_child2) == 90
    assert YGNodeLayoutGetTop(root_child2) == 100
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 0

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_column_reverse_border_bottom():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionColumnReverse)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeBottom, 100)

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
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 0

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child1) == 90
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 0

    assert YGNodeLayoutGetLeft(root_child2) == 90
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 0

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse_pos_left():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeLeft, 100)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 10)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 10)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 90
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child1) == 80
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 70
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child1) == 10
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 20
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse_pos_start():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeStart, 100)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 10)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 10)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 90
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child1) == 80
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 70
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == -100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child1) == 10
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 20
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse_pos_right():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeRight, 100)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 10)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 10)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == -100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 90
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child1) == 80
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 70
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == -100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child1) == 10
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 20
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse_pos_end():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeEnd, 100)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 10)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 10)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == -100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 90
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child1) == 80
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 70
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child1) == 10
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 20
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_column_reverse_pos_top():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionColumnReverse)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeTop, 100)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 10)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 10)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 0

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 100
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 0

    assert YGNodeLayoutGetLeft(root_child0_child2) == 0
    assert YGNodeLayoutGetTop(root_child0_child2) == 100
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 90
    assert YGNodeLayoutGetTop(root_child0_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 0

    assert YGNodeLayoutGetLeft(root_child0_child1) == 90
    assert YGNodeLayoutGetTop(root_child0_child1) == 100
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 0

    assert YGNodeLayoutGetLeft(root_child0_child2) == 90
    assert YGNodeLayoutGetTop(root_child0_child2) == 100
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 0

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_column_reverse_pos_bottom():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionColumnReverse)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeBottom, 100)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 10)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 10)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == -100
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 0

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 100
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 0

    assert YGNodeLayoutGetLeft(root_child0_child2) == 0
    assert YGNodeLayoutGetTop(root_child0_child2) == 100
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == -100
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 90
    assert YGNodeLayoutGetTop(root_child0_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 0

    assert YGNodeLayoutGetLeft(root_child0_child1) == 90
    assert YGNodeLayoutGetTop(root_child0_child1) == 100
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 0

    assert YGNodeLayoutGetLeft(root_child0_child2) == 90
    assert YGNodeLayoutGetTop(root_child0_child2) == 100
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 0

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse_inner_pos_left():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeStyleSetHeight(root_child0_child0, 10)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPosition(root_child0_child0, YGEdge.YGEdgeLeft, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 10)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 10)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 10
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 90
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 80
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 10
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 10
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse_inner_pos_right():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeStyleSetHeight(root_child0_child0, 10)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPosition(root_child0_child0, YGEdge.YGEdgeRight, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 10)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 10)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 80
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 90
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 80
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 80
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 10
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_col_reverse_inner_pos_top():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionColumnReverse)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeStyleSetHeight(root_child0_child0, 10)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPosition(root_child0_child0, YGEdge.YGEdgeTop, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 10)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 10)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 100
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 0

    assert YGNodeLayoutGetLeft(root_child0_child2) == 0
    assert YGNodeLayoutGetTop(root_child0_child2) == 100
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 90
    assert YGNodeLayoutGetTop(root_child0_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 90
    assert YGNodeLayoutGetTop(root_child0_child1) == 100
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 0

    assert YGNodeLayoutGetLeft(root_child0_child2) == 90
    assert YGNodeLayoutGetTop(root_child0_child2) == 100
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 0

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_col_reverse_inner_pos_bottom():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionColumnReverse)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeStyleSetHeight(root_child0_child0, 10)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPosition(root_child0_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 10)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 10)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 80
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 100
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 0

    assert YGNodeLayoutGetLeft(root_child0_child2) == 0
    assert YGNodeLayoutGetTop(root_child0_child2) == 100
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 90
    assert YGNodeLayoutGetTop(root_child0_child0) == 80
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 90
    assert YGNodeLayoutGetTop(root_child0_child1) == 100
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 0

    assert YGNodeLayoutGetLeft(root_child0_child2) == 90
    assert YGNodeLayoutGetTop(root_child0_child2) == 100
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 0

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse_inner_pos_start():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeStyleSetHeight(root_child0_child0, 10)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPosition(root_child0_child0, YGEdge.YGEdgeStart, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 10)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 10)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 10
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 90
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 80
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 80
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 10
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse_inner_pos_end():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeStyleSetHeight(root_child0_child0, 10)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPosition(root_child0_child0, YGEdge.YGEdgeEnd, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 10)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 10)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 80
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 90
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 80
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 10
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 10
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse_inner_margin_left():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeStyleSetHeight(root_child0_child0, 10)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeLeft, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 10)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 10)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 90
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 90
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 80
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 10
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 10
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse_inner_margin_right():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeStyleSetHeight(root_child0_child0, 10)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeRight, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 10)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 10)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 80
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 90
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 80
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 10
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_col_reverse_inner_margin_top():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionColumnReverse)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeStyleSetHeight(root_child0_child0, 10)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeTop, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 10)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 10)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 90
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 100
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 0

    assert YGNodeLayoutGetLeft(root_child0_child2) == 0
    assert YGNodeLayoutGetTop(root_child0_child2) == 100
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 90
    assert YGNodeLayoutGetTop(root_child0_child0) == 90
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 90
    assert YGNodeLayoutGetTop(root_child0_child1) == 100
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 0

    assert YGNodeLayoutGetLeft(root_child0_child2) == 90
    assert YGNodeLayoutGetTop(root_child0_child2) == 100
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 0

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_col_reverse_inner_margin_bottom():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionColumnReverse)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeStyleSetHeight(root_child0_child0, 10)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 10)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 10)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 80
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 100
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 0

    assert YGNodeLayoutGetLeft(root_child0_child2) == 0
    assert YGNodeLayoutGetTop(root_child0_child2) == 100
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 90
    assert YGNodeLayoutGetTop(root_child0_child0) == 80
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 90
    assert YGNodeLayoutGetTop(root_child0_child1) == 100
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 0

    assert YGNodeLayoutGetLeft(root_child0_child2) == 90
    assert YGNodeLayoutGetTop(root_child0_child2) == 100
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 0

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse_inner_marign_start():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeStyleSetHeight(root_child0_child0, 10)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeStart, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 10)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 10)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 90
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 90
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 80
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 10
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse_inner_margin_end():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeStyleSetHeight(root_child0_child0, 10)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeEnd, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 10)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 10)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 80
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 90
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 80
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 10
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 10
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse_inner_border_left():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeStyleSetHeight(root_child0_child0, 10)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeLeft, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 10)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 10)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 90
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 90
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 80
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 10
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse_inner_border_right():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeStyleSetHeight(root_child0_child0, 10)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeRight, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 10)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 10)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 90
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 90
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 80
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 10
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_col_reverse_inner_border_top():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionColumnReverse)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeStyleSetHeight(root_child0_child0, 10)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeTop, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 10)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 10)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 90
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 100
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 0

    assert YGNodeLayoutGetLeft(root_child0_child2) == 0
    assert YGNodeLayoutGetTop(root_child0_child2) == 100
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 90
    assert YGNodeLayoutGetTop(root_child0_child0) == 90
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 90
    assert YGNodeLayoutGetTop(root_child0_child1) == 100
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 0

    assert YGNodeLayoutGetLeft(root_child0_child2) == 90
    assert YGNodeLayoutGetTop(root_child0_child2) == 100
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 0

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_col_reverse_inner_border_bottom():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionColumnReverse)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeStyleSetHeight(root_child0_child0, 10)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 10)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 10)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 90
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 100
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 0

    assert YGNodeLayoutGetLeft(root_child0_child2) == 0
    assert YGNodeLayoutGetTop(root_child0_child2) == 100
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 90
    assert YGNodeLayoutGetTop(root_child0_child0) == 90
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 90
    assert YGNodeLayoutGetTop(root_child0_child1) == 100
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 0

    assert YGNodeLayoutGetLeft(root_child0_child2) == 90
    assert YGNodeLayoutGetTop(root_child0_child2) == 100
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 0

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse_inner_border_start():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeStyleSetHeight(root_child0_child0, 10)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeStart, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 10)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 10)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 90
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 90
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 80
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 10
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse_inner_border_end():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeStyleSetHeight(root_child0_child0, 10)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeEnd, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 10)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 10)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 90
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 90
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 80
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 10
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse_inner_padding_left():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeStyleSetHeight(root_child0_child0, 10)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeLeft, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 10)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 10)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 90
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 90
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 80
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 10
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse_inner_padding_right():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeStyleSetHeight(root_child0_child0, 10)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeRight, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 10)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 10)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 90
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 90
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 80
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 10
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_col_reverse_inner_padding_top():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionColumnReverse)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeStyleSetHeight(root_child0_child0, 10)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeTop, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 10)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 10)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 90
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 100
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 0

    assert YGNodeLayoutGetLeft(root_child0_child2) == 0
    assert YGNodeLayoutGetTop(root_child0_child2) == 100
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 90
    assert YGNodeLayoutGetTop(root_child0_child0) == 90
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 90
    assert YGNodeLayoutGetTop(root_child0_child1) == 100
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 0

    assert YGNodeLayoutGetLeft(root_child0_child2) == 90
    assert YGNodeLayoutGetTop(root_child0_child2) == 100
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 0

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_col_reverse_inner_padding_bottom():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionColumnReverse)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeStyleSetHeight(root_child0_child0, 10)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 10)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 10)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 90
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 100
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 0

    assert YGNodeLayoutGetLeft(root_child0_child2) == 0
    assert YGNodeLayoutGetTop(root_child0_child2) == 100
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 90
    assert YGNodeLayoutGetTop(root_child0_child0) == 90
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 90
    assert YGNodeLayoutGetTop(root_child0_child1) == 100
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 0

    assert YGNodeLayoutGetLeft(root_child0_child2) == 90
    assert YGNodeLayoutGetTop(root_child0_child2) == 100
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 0

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse_inner_padding_start():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeStyleSetHeight(root_child0_child0, 10)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeStart, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 10)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 10)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 90
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 90
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 80
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 10
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_row_reverse_inner_padding_end():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeStyleSetHeight(root_child0_child0, 10)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeEnd, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 10)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 10)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 90
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 90
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 80
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 10
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 10
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 10
    assert YGNodeLayoutGetHeight(root_child0_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_direction_alternating_with_percent():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 300)
    YGNodeStyleSetWidth(root, 200)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeightPercent(root_child0, 50)
    YGNodeStyleSetWidthPercent(root_child0, 50)
    YGNodeStyleSetPositionPercent(root_child0, YGEdge.YGEdgeLeft, 10)
    YGNodeStyleSetPositionPercent(root_child0, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 20
    assert YGNodeLayoutGetTop(root_child0) == 30
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 150

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 120
    assert YGNodeLayoutGetTop(root_child0) == 30
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 150

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

