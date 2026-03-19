import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from yoga import *  # noqa: E402,F403


def test_column_gap_flexible():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(root, 80)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetGap(root, YGGutter.YGGutterColumn, 10)
    YGNodeStyleSetGap(root, YGGutter.YGGutterRow, 20)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeStyleSetFlexShrink(root_child0, 1)
    YGNodeStyleSetFlexBasisPercent(root_child0, 0)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child1, 1)
    YGNodeStyleSetFlexShrink(root_child1, 1)
    YGNodeStyleSetFlexBasisPercent(root_child1, 0)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child2, 1)
    YGNodeStyleSetFlexShrink(root_child2, 1)
    YGNodeStyleSetFlexBasisPercent(root_child2, 0)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 80
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 30
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 60
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 80
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 30
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_column_gap_inflexible():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(root, 80)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetGap(root, YGGutter.YGGutterColumn, 10)

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
    assert YGNodeLayoutGetWidth(root) == 80
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 30
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 60
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 80
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 30
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_column_gap_mixed_flexible():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(root, 80)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetGap(root, YGGutter.YGGutterColumn, 10)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 20)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child1, 1)
    YGNodeStyleSetFlexShrink(root_child1, 1)
    YGNodeStyleSetFlexBasisPercent(root_child1, 0)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 20)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 80
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 30
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 60
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 80
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 30
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_column_gap_child_margins():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(root, 80)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetGap(root, YGGutter.YGGutterColumn, 10)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeStyleSetFlexShrink(root_child0, 1)
    YGNodeStyleSetFlexBasisPercent(root_child0, 0)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeHorizontal, 2)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child1, 1)
    YGNodeStyleSetFlexShrink(root_child1, 1)
    YGNodeStyleSetFlexBasisPercent(root_child1, 0)
    YGNodeStyleSetMargin(root_child1, YGEdge.YGEdgeHorizontal, 10)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child2, 1)
    YGNodeStyleSetFlexShrink(root_child2, 1)
    YGNodeStyleSetFlexBasisPercent(root_child2, 0)
    YGNodeStyleSetMargin(root_child2, YGEdge.YGEdgeHorizontal, 15)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 80
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 2
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 2
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 26
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 2
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 63
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 2
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 80
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 76
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 2
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 52
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 2
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 15
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 2
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_column_row_gap_wrapping():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetWidth(root, 80)
    YGNodeStyleSetGap(root, YGGutter.YGGutterColumn, 10)
    YGNodeStyleSetGap(root, YGGutter.YGGutterRow, 20)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 20)
    YGNodeStyleSetHeight(root_child0, 20)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 20)
    YGNodeStyleSetHeight(root_child1, 20)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 20)
    YGNodeStyleSetHeight(root_child2, 20)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 20)
    YGNodeStyleSetHeight(root_child3, 20)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 20)
    YGNodeStyleSetHeight(root_child4, 20)
    YGNodeInsertChild(root, root_child4, 4)

    root_child5 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child5, 20)
    YGNodeStyleSetHeight(root_child5, 20)
    YGNodeInsertChild(root, root_child5, 5)

    root_child6 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child6, 20)
    YGNodeStyleSetHeight(root_child6, 20)
    YGNodeInsertChild(root, root_child6, 6)

    root_child7 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child7, 20)
    YGNodeStyleSetHeight(root_child7, 20)
    YGNodeInsertChild(root, root_child7, 7)

    root_child8 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child8, 20)
    YGNodeStyleSetHeight(root_child8, 20)
    YGNodeInsertChild(root, root_child8, 8)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 80
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    assert YGNodeLayoutGetLeft(root_child1) == 30
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 60
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 20

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 40
    assert YGNodeLayoutGetWidth(root_child3) == 20
    assert YGNodeLayoutGetHeight(root_child3) == 20

    assert YGNodeLayoutGetLeft(root_child4) == 30
    assert YGNodeLayoutGetTop(root_child4) == 40
    assert YGNodeLayoutGetWidth(root_child4) == 20
    assert YGNodeLayoutGetHeight(root_child4) == 20

    assert YGNodeLayoutGetLeft(root_child5) == 60
    assert YGNodeLayoutGetTop(root_child5) == 40
    assert YGNodeLayoutGetWidth(root_child5) == 20
    assert YGNodeLayoutGetHeight(root_child5) == 20

    assert YGNodeLayoutGetLeft(root_child6) == 0
    assert YGNodeLayoutGetTop(root_child6) == 80
    assert YGNodeLayoutGetWidth(root_child6) == 20
    assert YGNodeLayoutGetHeight(root_child6) == 20

    assert YGNodeLayoutGetLeft(root_child7) == 30
    assert YGNodeLayoutGetTop(root_child7) == 80
    assert YGNodeLayoutGetWidth(root_child7) == 20
    assert YGNodeLayoutGetHeight(root_child7) == 20

    assert YGNodeLayoutGetLeft(root_child8) == 60
    assert YGNodeLayoutGetTop(root_child8) == 80
    assert YGNodeLayoutGetWidth(root_child8) == 20
    assert YGNodeLayoutGetHeight(root_child8) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 80
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    assert YGNodeLayoutGetLeft(root_child1) == 30
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 20

    assert YGNodeLayoutGetLeft(root_child3) == 60
    assert YGNodeLayoutGetTop(root_child3) == 40
    assert YGNodeLayoutGetWidth(root_child3) == 20
    assert YGNodeLayoutGetHeight(root_child3) == 20

    assert YGNodeLayoutGetLeft(root_child4) == 30
    assert YGNodeLayoutGetTop(root_child4) == 40
    assert YGNodeLayoutGetWidth(root_child4) == 20
    assert YGNodeLayoutGetHeight(root_child4) == 20

    assert YGNodeLayoutGetLeft(root_child5) == 0
    assert YGNodeLayoutGetTop(root_child5) == 40
    assert YGNodeLayoutGetWidth(root_child5) == 20
    assert YGNodeLayoutGetHeight(root_child5) == 20

    assert YGNodeLayoutGetLeft(root_child6) == 60
    assert YGNodeLayoutGetTop(root_child6) == 80
    assert YGNodeLayoutGetWidth(root_child6) == 20
    assert YGNodeLayoutGetHeight(root_child6) == 20

    assert YGNodeLayoutGetLeft(root_child7) == 30
    assert YGNodeLayoutGetTop(root_child7) == 80
    assert YGNodeLayoutGetWidth(root_child7) == 20
    assert YGNodeLayoutGetHeight(root_child7) == 20

    assert YGNodeLayoutGetLeft(root_child8) == 0
    assert YGNodeLayoutGetTop(root_child8) == 80
    assert YGNodeLayoutGetWidth(root_child8) == 20
    assert YGNodeLayoutGetHeight(root_child8) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_column_gap_start_index():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetWidth(root, 80)
    YGNodeStyleSetGap(root, YGGutter.YGGutterColumn, 10)
    YGNodeStyleSetGap(root, YGGutter.YGGutterRow, 20)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 20)
    YGNodeStyleSetHeight(root_child0, 20)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 20)
    YGNodeStyleSetHeight(root_child1, 20)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 20)
    YGNodeStyleSetHeight(root_child2, 20)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 20)
    YGNodeStyleSetHeight(root_child3, 20)
    YGNodeInsertChild(root, root_child3, 3)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 80
    assert YGNodeLayoutGetHeight(root) == 20

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 30
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 20

    assert YGNodeLayoutGetLeft(root_child3) == 60
    assert YGNodeLayoutGetTop(root_child3) == 0
    assert YGNodeLayoutGetWidth(root_child3) == 20
    assert YGNodeLayoutGetHeight(root_child3) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 80
    assert YGNodeLayoutGetHeight(root) == 20

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    assert YGNodeLayoutGetLeft(root_child1) == 60
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 30
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 20

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 0
    assert YGNodeLayoutGetWidth(root_child3) == 20
    assert YGNodeLayoutGetHeight(root_child3) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_column_gap_justify_flex_start():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetGap(root, YGGutter.YGGutterColumn, 10)

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

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 30
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 60
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 80
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 20
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_column_gap_justify_center():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyCenter)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetGap(root, YGGutter.YGGutterColumn, 10)

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

    assert YGNodeLayoutGetLeft(root_child0) == 10
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 70
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 70
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 10
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_column_gap_justify_flex_end():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyFlexEnd)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetGap(root, YGGutter.YGGutterColumn, 10)

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

    assert YGNodeLayoutGetLeft(root_child0) == 20
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 80
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 30
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_column_gap_justify_space_between():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifySpaceBetween)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetGap(root, YGGutter.YGGutterColumn, 10)

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

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 80
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 80
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_column_gap_justify_space_around():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifySpaceAround)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetGap(root, YGGutter.YGGutterColumn, 10)

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

    assert YGNodeLayoutGetLeft(root_child0) == 3
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 77
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 77
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 3
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_column_gap_justify_space_evenly():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifySpaceEvenly)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetGap(root, YGGutter.YGGutterColumn, 10)

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

    assert YGNodeLayoutGetLeft(root_child0) == 5
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 75
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 75
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 5
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_column_gap_wrap_align_flex_start():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetGap(root, YGGutter.YGGutterColumn, 10)
    YGNodeStyleSetGap(root, YGGutter.YGGutterRow, 20)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 20)
    YGNodeStyleSetHeight(root_child0, 20)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 20)
    YGNodeStyleSetHeight(root_child1, 20)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 20)
    YGNodeStyleSetHeight(root_child2, 20)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 20)
    YGNodeStyleSetHeight(root_child3, 20)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 20)
    YGNodeStyleSetHeight(root_child4, 20)
    YGNodeInsertChild(root, root_child4, 4)

    root_child5 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child5, 20)
    YGNodeStyleSetHeight(root_child5, 20)
    YGNodeInsertChild(root, root_child5, 5)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    assert YGNodeLayoutGetLeft(root_child1) == 30
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 60
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 20

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 40
    assert YGNodeLayoutGetWidth(root_child3) == 20
    assert YGNodeLayoutGetHeight(root_child3) == 20

    assert YGNodeLayoutGetLeft(root_child4) == 30
    assert YGNodeLayoutGetTop(root_child4) == 40
    assert YGNodeLayoutGetWidth(root_child4) == 20
    assert YGNodeLayoutGetHeight(root_child4) == 20

    assert YGNodeLayoutGetLeft(root_child5) == 60
    assert YGNodeLayoutGetTop(root_child5) == 40
    assert YGNodeLayoutGetWidth(root_child5) == 20
    assert YGNodeLayoutGetHeight(root_child5) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 80
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 20
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 20

    assert YGNodeLayoutGetLeft(root_child3) == 80
    assert YGNodeLayoutGetTop(root_child3) == 40
    assert YGNodeLayoutGetWidth(root_child3) == 20
    assert YGNodeLayoutGetHeight(root_child3) == 20

    assert YGNodeLayoutGetLeft(root_child4) == 50
    assert YGNodeLayoutGetTop(root_child4) == 40
    assert YGNodeLayoutGetWidth(root_child4) == 20
    assert YGNodeLayoutGetHeight(root_child4) == 20

    assert YGNodeLayoutGetLeft(root_child5) == 20
    assert YGNodeLayoutGetTop(root_child5) == 40
    assert YGNodeLayoutGetWidth(root_child5) == 20
    assert YGNodeLayoutGetHeight(root_child5) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_column_gap_wrap_align_center():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignCenter)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetGap(root, YGGutter.YGGutterColumn, 10)
    YGNodeStyleSetGap(root, YGGutter.YGGutterRow, 20)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 20)
    YGNodeStyleSetHeight(root_child0, 20)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 20)
    YGNodeStyleSetHeight(root_child1, 20)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 20)
    YGNodeStyleSetHeight(root_child2, 20)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 20)
    YGNodeStyleSetHeight(root_child3, 20)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 20)
    YGNodeStyleSetHeight(root_child4, 20)
    YGNodeInsertChild(root, root_child4, 4)

    root_child5 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child5, 20)
    YGNodeStyleSetHeight(root_child5, 20)
    YGNodeInsertChild(root, root_child5, 5)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 20
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    assert YGNodeLayoutGetLeft(root_child1) == 30
    assert YGNodeLayoutGetTop(root_child1) == 20
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 60
    assert YGNodeLayoutGetTop(root_child2) == 20
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 20

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 60
    assert YGNodeLayoutGetWidth(root_child3) == 20
    assert YGNodeLayoutGetHeight(root_child3) == 20

    assert YGNodeLayoutGetLeft(root_child4) == 30
    assert YGNodeLayoutGetTop(root_child4) == 60
    assert YGNodeLayoutGetWidth(root_child4) == 20
    assert YGNodeLayoutGetHeight(root_child4) == 20

    assert YGNodeLayoutGetLeft(root_child5) == 60
    assert YGNodeLayoutGetTop(root_child5) == 60
    assert YGNodeLayoutGetWidth(root_child5) == 20
    assert YGNodeLayoutGetHeight(root_child5) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 80
    assert YGNodeLayoutGetTop(root_child0) == 20
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 20
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 20
    assert YGNodeLayoutGetTop(root_child2) == 20
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 20

    assert YGNodeLayoutGetLeft(root_child3) == 80
    assert YGNodeLayoutGetTop(root_child3) == 60
    assert YGNodeLayoutGetWidth(root_child3) == 20
    assert YGNodeLayoutGetHeight(root_child3) == 20

    assert YGNodeLayoutGetLeft(root_child4) == 50
    assert YGNodeLayoutGetTop(root_child4) == 60
    assert YGNodeLayoutGetWidth(root_child4) == 20
    assert YGNodeLayoutGetHeight(root_child4) == 20

    assert YGNodeLayoutGetLeft(root_child5) == 20
    assert YGNodeLayoutGetTop(root_child5) == 60
    assert YGNodeLayoutGetWidth(root_child5) == 20
    assert YGNodeLayoutGetHeight(root_child5) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_column_gap_wrap_align_flex_end():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignFlexEnd)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetGap(root, YGGutter.YGGutterColumn, 10)
    YGNodeStyleSetGap(root, YGGutter.YGGutterRow, 20)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 20)
    YGNodeStyleSetHeight(root_child0, 20)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 20)
    YGNodeStyleSetHeight(root_child1, 20)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 20)
    YGNodeStyleSetHeight(root_child2, 20)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 20)
    YGNodeStyleSetHeight(root_child3, 20)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 20)
    YGNodeStyleSetHeight(root_child4, 20)
    YGNodeInsertChild(root, root_child4, 4)

    root_child5 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child5, 20)
    YGNodeStyleSetHeight(root_child5, 20)
    YGNodeInsertChild(root, root_child5, 5)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 40
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    assert YGNodeLayoutGetLeft(root_child1) == 30
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 60
    assert YGNodeLayoutGetTop(root_child2) == 40
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 20

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 80
    assert YGNodeLayoutGetWidth(root_child3) == 20
    assert YGNodeLayoutGetHeight(root_child3) == 20

    assert YGNodeLayoutGetLeft(root_child4) == 30
    assert YGNodeLayoutGetTop(root_child4) == 80
    assert YGNodeLayoutGetWidth(root_child4) == 20
    assert YGNodeLayoutGetHeight(root_child4) == 20

    assert YGNodeLayoutGetLeft(root_child5) == 60
    assert YGNodeLayoutGetTop(root_child5) == 80
    assert YGNodeLayoutGetWidth(root_child5) == 20
    assert YGNodeLayoutGetHeight(root_child5) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 80
    assert YGNodeLayoutGetTop(root_child0) == 40
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 20
    assert YGNodeLayoutGetTop(root_child2) == 40
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 20

    assert YGNodeLayoutGetLeft(root_child3) == 80
    assert YGNodeLayoutGetTop(root_child3) == 80
    assert YGNodeLayoutGetWidth(root_child3) == 20
    assert YGNodeLayoutGetHeight(root_child3) == 20

    assert YGNodeLayoutGetLeft(root_child4) == 50
    assert YGNodeLayoutGetTop(root_child4) == 80
    assert YGNodeLayoutGetWidth(root_child4) == 20
    assert YGNodeLayoutGetHeight(root_child4) == 20

    assert YGNodeLayoutGetLeft(root_child5) == 20
    assert YGNodeLayoutGetTop(root_child5) == 80
    assert YGNodeLayoutGetWidth(root_child5) == 20
    assert YGNodeLayoutGetHeight(root_child5) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_column_gap_wrap_align_space_between():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignSpaceBetween)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetGap(root, YGGutter.YGGutterColumn, 10)
    YGNodeStyleSetGap(root, YGGutter.YGGutterRow, 20)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 20)
    YGNodeStyleSetHeight(root_child0, 20)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 20)
    YGNodeStyleSetHeight(root_child1, 20)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 20)
    YGNodeStyleSetHeight(root_child2, 20)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 20)
    YGNodeStyleSetHeight(root_child3, 20)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 20)
    YGNodeStyleSetHeight(root_child4, 20)
    YGNodeInsertChild(root, root_child4, 4)

    root_child5 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child5, 20)
    YGNodeStyleSetHeight(root_child5, 20)
    YGNodeInsertChild(root, root_child5, 5)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    assert YGNodeLayoutGetLeft(root_child1) == 30
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 60
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 20

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 80
    assert YGNodeLayoutGetWidth(root_child3) == 20
    assert YGNodeLayoutGetHeight(root_child3) == 20

    assert YGNodeLayoutGetLeft(root_child4) == 30
    assert YGNodeLayoutGetTop(root_child4) == 80
    assert YGNodeLayoutGetWidth(root_child4) == 20
    assert YGNodeLayoutGetHeight(root_child4) == 20

    assert YGNodeLayoutGetLeft(root_child5) == 60
    assert YGNodeLayoutGetTop(root_child5) == 80
    assert YGNodeLayoutGetWidth(root_child5) == 20
    assert YGNodeLayoutGetHeight(root_child5) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 80
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 20
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 20

    assert YGNodeLayoutGetLeft(root_child3) == 80
    assert YGNodeLayoutGetTop(root_child3) == 80
    assert YGNodeLayoutGetWidth(root_child3) == 20
    assert YGNodeLayoutGetHeight(root_child3) == 20

    assert YGNodeLayoutGetLeft(root_child4) == 50
    assert YGNodeLayoutGetTop(root_child4) == 80
    assert YGNodeLayoutGetWidth(root_child4) == 20
    assert YGNodeLayoutGetHeight(root_child4) == 20

    assert YGNodeLayoutGetLeft(root_child5) == 20
    assert YGNodeLayoutGetTop(root_child5) == 80
    assert YGNodeLayoutGetWidth(root_child5) == 20
    assert YGNodeLayoutGetHeight(root_child5) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_column_gap_wrap_align_space_around():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignSpaceAround)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetGap(root, YGGutter.YGGutterColumn, 10)
    YGNodeStyleSetGap(root, YGGutter.YGGutterRow, 20)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 20)
    YGNodeStyleSetHeight(root_child0, 20)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 20)
    YGNodeStyleSetHeight(root_child1, 20)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 20)
    YGNodeStyleSetHeight(root_child2, 20)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 20)
    YGNodeStyleSetHeight(root_child3, 20)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 20)
    YGNodeStyleSetHeight(root_child4, 20)
    YGNodeInsertChild(root, root_child4, 4)

    root_child5 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child5, 20)
    YGNodeStyleSetHeight(root_child5, 20)
    YGNodeInsertChild(root, root_child5, 5)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    assert YGNodeLayoutGetLeft(root_child1) == 30
    assert YGNodeLayoutGetTop(root_child1) == 10
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 60
    assert YGNodeLayoutGetTop(root_child2) == 10
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 20

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 70
    assert YGNodeLayoutGetWidth(root_child3) == 20
    assert YGNodeLayoutGetHeight(root_child3) == 20

    assert YGNodeLayoutGetLeft(root_child4) == 30
    assert YGNodeLayoutGetTop(root_child4) == 70
    assert YGNodeLayoutGetWidth(root_child4) == 20
    assert YGNodeLayoutGetHeight(root_child4) == 20

    assert YGNodeLayoutGetLeft(root_child5) == 60
    assert YGNodeLayoutGetTop(root_child5) == 70
    assert YGNodeLayoutGetWidth(root_child5) == 20
    assert YGNodeLayoutGetHeight(root_child5) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 80
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 10
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 20
    assert YGNodeLayoutGetTop(root_child2) == 10
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 20

    assert YGNodeLayoutGetLeft(root_child3) == 80
    assert YGNodeLayoutGetTop(root_child3) == 70
    assert YGNodeLayoutGetWidth(root_child3) == 20
    assert YGNodeLayoutGetHeight(root_child3) == 20

    assert YGNodeLayoutGetLeft(root_child4) == 50
    assert YGNodeLayoutGetTop(root_child4) == 70
    assert YGNodeLayoutGetWidth(root_child4) == 20
    assert YGNodeLayoutGetHeight(root_child4) == 20

    assert YGNodeLayoutGetLeft(root_child5) == 20
    assert YGNodeLayoutGetTop(root_child5) == 70
    assert YGNodeLayoutGetWidth(root_child5) == 20
    assert YGNodeLayoutGetHeight(root_child5) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_column_gap_wrap_align_stretch():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetWidth(root, 300)
    YGNodeStyleSetHeight(root, 300)
    YGNodeStyleSetGap(root, YGGutter.YGGutterColumn, 5)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignStretch)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMinWidth(root_child0, 60)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMinWidth(root_child1, 60)
    YGNodeStyleSetFlexGrow(root_child1, 1)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMinWidth(root_child2, 60)
    YGNodeStyleSetFlexGrow(root_child2, 1)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMinWidth(root_child3, 60)
    YGNodeStyleSetFlexGrow(root_child3, 1)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMinWidth(root_child4, 60)
    YGNodeStyleSetFlexGrow(root_child4, 1)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 71
    assert YGNodeLayoutGetHeight(root_child0) == 150

    assert YGNodeLayoutGetLeft(root_child1) == 76
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 72
    assert YGNodeLayoutGetHeight(root_child1) == 150

    assert YGNodeLayoutGetLeft(root_child2) == 153
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 71
    assert YGNodeLayoutGetHeight(root_child2) == 150

    assert YGNodeLayoutGetLeft(root_child3) == 229
    assert YGNodeLayoutGetTop(root_child3) == 0
    assert YGNodeLayoutGetWidth(root_child3) == 71
    assert YGNodeLayoutGetHeight(root_child3) == 150

    assert YGNodeLayoutGetLeft(root_child4) == 0
    assert YGNodeLayoutGetTop(root_child4) == 150
    assert YGNodeLayoutGetWidth(root_child4) == 300
    assert YGNodeLayoutGetHeight(root_child4) == 150

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 229
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 71
    assert YGNodeLayoutGetHeight(root_child0) == 150

    assert YGNodeLayoutGetLeft(root_child1) == 153
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 71
    assert YGNodeLayoutGetHeight(root_child1) == 150

    assert YGNodeLayoutGetLeft(root_child2) == 76
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 72
    assert YGNodeLayoutGetHeight(root_child2) == 150

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 0
    assert YGNodeLayoutGetWidth(root_child3) == 71
    assert YGNodeLayoutGetHeight(root_child3) == 150

    assert YGNodeLayoutGetLeft(root_child4) == 0
    assert YGNodeLayoutGetTop(root_child4) == 150
    assert YGNodeLayoutGetWidth(root_child4) == 300
    assert YGNodeLayoutGetHeight(root_child4) == 150

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_column_gap_determines_parent_width():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetGap(root, YGGutter.YGGutterColumn, 10)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 20)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 30)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 80
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 20
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 50
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 30
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 80
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 70
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 30
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_row_gap_align_items_stretch():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 200)
    YGNodeStyleSetGap(root, YGGutter.YGGutterColumn, 10)
    YGNodeStyleSetGap(root, YGGutter.YGGutterRow, 20)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignStretch)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 20)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 20)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 20)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 20)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 20)
    YGNodeInsertChild(root, root_child4, 4)

    root_child5 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child5, 20)
    YGNodeInsertChild(root, root_child5, 5)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 90

    assert YGNodeLayoutGetLeft(root_child1) == 30
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 90

    assert YGNodeLayoutGetLeft(root_child2) == 60
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 90

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 110
    assert YGNodeLayoutGetWidth(root_child3) == 20
    assert YGNodeLayoutGetHeight(root_child3) == 90

    assert YGNodeLayoutGetLeft(root_child4) == 30
    assert YGNodeLayoutGetTop(root_child4) == 110
    assert YGNodeLayoutGetWidth(root_child4) == 20
    assert YGNodeLayoutGetHeight(root_child4) == 90

    assert YGNodeLayoutGetLeft(root_child5) == 60
    assert YGNodeLayoutGetTop(root_child5) == 110
    assert YGNodeLayoutGetWidth(root_child5) == 20
    assert YGNodeLayoutGetHeight(root_child5) == 90

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 80
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 90

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 90

    assert YGNodeLayoutGetLeft(root_child2) == 20
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 90

    assert YGNodeLayoutGetLeft(root_child3) == 80
    assert YGNodeLayoutGetTop(root_child3) == 110
    assert YGNodeLayoutGetWidth(root_child3) == 20
    assert YGNodeLayoutGetHeight(root_child3) == 90

    assert YGNodeLayoutGetLeft(root_child4) == 50
    assert YGNodeLayoutGetTop(root_child4) == 110
    assert YGNodeLayoutGetWidth(root_child4) == 20
    assert YGNodeLayoutGetHeight(root_child4) == 90

    assert YGNodeLayoutGetLeft(root_child5) == 20
    assert YGNodeLayoutGetTop(root_child5) == 110
    assert YGNodeLayoutGetWidth(root_child5) == 20
    assert YGNodeLayoutGetHeight(root_child5) == 90

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_row_gap_align_items_end():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 200)
    YGNodeStyleSetGap(root, YGGutter.YGGutterColumn, 10)
    YGNodeStyleSetGap(root, YGGutter.YGGutterRow, 20)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexEnd)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 20)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 20)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 20)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 20)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 20)
    YGNodeInsertChild(root, root_child4, 4)

    root_child5 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child5, 20)
    YGNodeInsertChild(root, root_child5, 5)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child1) == 30
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 0

    assert YGNodeLayoutGetLeft(root_child2) == 60
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 0

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 20
    assert YGNodeLayoutGetWidth(root_child3) == 20
    assert YGNodeLayoutGetHeight(root_child3) == 0

    assert YGNodeLayoutGetLeft(root_child4) == 30
    assert YGNodeLayoutGetTop(root_child4) == 20
    assert YGNodeLayoutGetWidth(root_child4) == 20
    assert YGNodeLayoutGetHeight(root_child4) == 0

    assert YGNodeLayoutGetLeft(root_child5) == 60
    assert YGNodeLayoutGetTop(root_child5) == 20
    assert YGNodeLayoutGetWidth(root_child5) == 20
    assert YGNodeLayoutGetHeight(root_child5) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 80
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 0

    assert YGNodeLayoutGetLeft(root_child2) == 20
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 20
    assert YGNodeLayoutGetHeight(root_child2) == 0

    assert YGNodeLayoutGetLeft(root_child3) == 80
    assert YGNodeLayoutGetTop(root_child3) == 20
    assert YGNodeLayoutGetWidth(root_child3) == 20
    assert YGNodeLayoutGetHeight(root_child3) == 0

    assert YGNodeLayoutGetLeft(root_child4) == 50
    assert YGNodeLayoutGetTop(root_child4) == 20
    assert YGNodeLayoutGetWidth(root_child4) == 20
    assert YGNodeLayoutGetHeight(root_child4) == 0

    assert YGNodeLayoutGetLeft(root_child5) == 20
    assert YGNodeLayoutGetTop(root_child5) == 20
    assert YGNodeLayoutGetWidth(root_child5) == 20
    assert YGNodeLayoutGetHeight(root_child5) == 0

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_row_gap_column_child_margins():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 200)
    YGNodeStyleSetGap(root, YGGutter.YGGutterRow, 10)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeStyleSetFlexShrink(root_child0, 1)
    YGNodeStyleSetFlexBasisPercent(root_child0, 0)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeVertical, 2)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child1, 1)
    YGNodeStyleSetFlexShrink(root_child1, 1)
    YGNodeStyleSetFlexBasisPercent(root_child1, 0)
    YGNodeStyleSetMargin(root_child1, YGEdge.YGEdgeVertical, 10)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child2, 1)
    YGNodeStyleSetFlexShrink(root_child2, 1)
    YGNodeStyleSetFlexBasisPercent(root_child2, 0)
    YGNodeStyleSetMargin(root_child2, YGEdge.YGEdgeVertical, 15)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 2
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 42

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 66
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 42

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 143
    assert YGNodeLayoutGetWidth(root_child2) == 100
    assert YGNodeLayoutGetHeight(root_child2) == 42

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 2
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 42

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 66
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 42

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 143
    assert YGNodeLayoutGetWidth(root_child2) == 100
    assert YGNodeLayoutGetHeight(root_child2) == 42

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_row_gap_row_wrap_child_margins():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 200)
    YGNodeStyleSetGap(root, YGGutter.YGGutterRow, 10)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 60)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeVertical, 2)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 60)
    YGNodeStyleSetMargin(root_child1, YGEdge.YGEdgeVertical, 10)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 60)
    YGNodeStyleSetMargin(root_child2, YGEdge.YGEdgeVertical, 15)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 2
    assert YGNodeLayoutGetWidth(root_child0) == 60
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 24
    assert YGNodeLayoutGetWidth(root_child1) == 60
    assert YGNodeLayoutGetHeight(root_child1) == 0

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 59
    assert YGNodeLayoutGetWidth(root_child2) == 60
    assert YGNodeLayoutGetHeight(root_child2) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 40
    assert YGNodeLayoutGetTop(root_child0) == 2
    assert YGNodeLayoutGetWidth(root_child0) == 60
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 24
    assert YGNodeLayoutGetWidth(root_child1) == 60
    assert YGNodeLayoutGetHeight(root_child1) == 0

    assert YGNodeLayoutGetLeft(root_child2) == 40
    assert YGNodeLayoutGetTop(root_child2) == 59
    assert YGNodeLayoutGetWidth(root_child2) == 60
    assert YGNodeLayoutGetHeight(root_child2) == 0

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_row_gap_determines_parent_height():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetGap(root, YGGutter.YGGutterRow, 10)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1, 20)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child2, 30)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 80

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 20
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 50
    assert YGNodeLayoutGetWidth(root_child2) == 100
    assert YGNodeLayoutGetHeight(root_child2) == 30

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 80

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 20
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 50
    assert YGNodeLayoutGetWidth(root_child2) == 100
    assert YGNodeLayoutGetHeight(root_child2) == 30

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_row_gap_percent_wrapping():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(root, 300)
    YGNodeStyleSetHeight(root, 700)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeAll, 10)
    YGNodeStyleSetGapPercent(root, YGGutter.YGGutterAll, 10)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 100)
    YGNodeStyleSetHeight(root_child1, 100)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 100)
    YGNodeStyleSetHeight(root_child2, 100)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 100)
    YGNodeStyleSetHeight(root_child3, 100)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 100)
    YGNodeStyleSetHeight(root_child4, 100)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 700

    assert YGNodeLayoutGetLeft(root_child0) == 10
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 138
    assert YGNodeLayoutGetTop(root_child1) == 10
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 10
    assert YGNodeLayoutGetTop(root_child2) == 178
    assert YGNodeLayoutGetWidth(root_child2) == 100
    assert YGNodeLayoutGetHeight(root_child2) == 100

    assert YGNodeLayoutGetLeft(root_child3) == 138
    assert YGNodeLayoutGetTop(root_child3) == 178
    assert YGNodeLayoutGetWidth(root_child3) == 100
    assert YGNodeLayoutGetHeight(root_child3) == 100

    assert YGNodeLayoutGetLeft(root_child4) == 10
    assert YGNodeLayoutGetTop(root_child4) == 346
    assert YGNodeLayoutGetWidth(root_child4) == 100
    assert YGNodeLayoutGetHeight(root_child4) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 700

    assert YGNodeLayoutGetLeft(root_child0) == 190
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 62
    assert YGNodeLayoutGetTop(root_child1) == 10
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 190
    assert YGNodeLayoutGetTop(root_child2) == 178
    assert YGNodeLayoutGetWidth(root_child2) == 100
    assert YGNodeLayoutGetHeight(root_child2) == 100

    assert YGNodeLayoutGetLeft(root_child3) == 62
    assert YGNodeLayoutGetTop(root_child3) == 178
    assert YGNodeLayoutGetWidth(root_child3) == 100
    assert YGNodeLayoutGetHeight(root_child3) == 100

    assert YGNodeLayoutGetLeft(root_child4) == 190
    assert YGNodeLayoutGetTop(root_child4) == 346
    assert YGNodeLayoutGetWidth(root_child4) == 100
    assert YGNodeLayoutGetHeight(root_child4) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_row_gap_percent_determines_parent_height():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(root, 300)
    YGNodeStyleSetGapPercent(root, YGGutter.YGGutterAll, 10)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 100)
    YGNodeStyleSetHeight(root_child1, 100)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 100)
    YGNodeStyleSetHeight(root_child2, 100)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 100)
    YGNodeStyleSetHeight(root_child3, 100)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 100)
    YGNodeStyleSetHeight(root_child4, 100)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 130
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 100
    assert YGNodeLayoutGetWidth(root_child2) == 100
    assert YGNodeLayoutGetHeight(root_child2) == 100

    assert YGNodeLayoutGetLeft(root_child3) == 130
    assert YGNodeLayoutGetTop(root_child3) == 100
    assert YGNodeLayoutGetWidth(root_child3) == 100
    assert YGNodeLayoutGetHeight(root_child3) == 100

    assert YGNodeLayoutGetLeft(root_child4) == 0
    assert YGNodeLayoutGetTop(root_child4) == 200
    assert YGNodeLayoutGetWidth(root_child4) == 100
    assert YGNodeLayoutGetHeight(root_child4) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 200
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 70
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 200
    assert YGNodeLayoutGetTop(root_child2) == 100
    assert YGNodeLayoutGetWidth(root_child2) == 100
    assert YGNodeLayoutGetHeight(root_child2) == 100

    assert YGNodeLayoutGetLeft(root_child3) == 70
    assert YGNodeLayoutGetTop(root_child3) == 100
    assert YGNodeLayoutGetWidth(root_child3) == 100
    assert YGNodeLayoutGetHeight(root_child3) == 100

    assert YGNodeLayoutGetLeft(root_child4) == 200
    assert YGNodeLayoutGetTop(root_child4) == 200
    assert YGNodeLayoutGetWidth(root_child4) == 100
    assert YGNodeLayoutGetHeight(root_child4) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_row_gap_percent_wrapping_with_both_content_padding_and_item_padding():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(root, 300)
    YGNodeStyleSetHeight(root, 700)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeAll, 10)
    YGNodeStyleSetGapPercent(root, YGGutter.YGGutterAll, 10)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeAll, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 100)
    YGNodeStyleSetHeight(root_child1, 100)
    YGNodeStyleSetPadding(root_child1, YGEdge.YGEdgeAll, 10)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 100)
    YGNodeStyleSetHeight(root_child2, 100)
    YGNodeStyleSetPadding(root_child2, YGEdge.YGEdgeAll, 10)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 100)
    YGNodeStyleSetHeight(root_child3, 100)
    YGNodeStyleSetPadding(root_child3, YGEdge.YGEdgeAll, 10)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 100)
    YGNodeStyleSetHeight(root_child4, 100)
    YGNodeStyleSetPadding(root_child4, YGEdge.YGEdgeAll, 10)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 700

    assert YGNodeLayoutGetLeft(root_child0) == 10
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 138
    assert YGNodeLayoutGetTop(root_child1) == 10
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 10
    assert YGNodeLayoutGetTop(root_child2) == 178
    assert YGNodeLayoutGetWidth(root_child2) == 100
    assert YGNodeLayoutGetHeight(root_child2) == 100

    assert YGNodeLayoutGetLeft(root_child3) == 138
    assert YGNodeLayoutGetTop(root_child3) == 178
    assert YGNodeLayoutGetWidth(root_child3) == 100
    assert YGNodeLayoutGetHeight(root_child3) == 100

    assert YGNodeLayoutGetLeft(root_child4) == 10
    assert YGNodeLayoutGetTop(root_child4) == 346
    assert YGNodeLayoutGetWidth(root_child4) == 100
    assert YGNodeLayoutGetHeight(root_child4) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 700

    assert YGNodeLayoutGetLeft(root_child0) == 190
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 62
    assert YGNodeLayoutGetTop(root_child1) == 10
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 190
    assert YGNodeLayoutGetTop(root_child2) == 178
    assert YGNodeLayoutGetWidth(root_child2) == 100
    assert YGNodeLayoutGetHeight(root_child2) == 100

    assert YGNodeLayoutGetLeft(root_child3) == 62
    assert YGNodeLayoutGetTop(root_child3) == 178
    assert YGNodeLayoutGetWidth(root_child3) == 100
    assert YGNodeLayoutGetHeight(root_child3) == 100

    assert YGNodeLayoutGetLeft(root_child4) == 190
    assert YGNodeLayoutGetTop(root_child4) == 346
    assert YGNodeLayoutGetWidth(root_child4) == 100
    assert YGNodeLayoutGetHeight(root_child4) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_row_gap_percent_wrapping_with_both_content_padding():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(root, 300)
    YGNodeStyleSetHeight(root, 700)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeAll, 10)
    YGNodeStyleSetGapPercent(root, YGGutter.YGGutterAll, 10)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 100)
    YGNodeStyleSetHeight(root_child1, 100)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 100)
    YGNodeStyleSetHeight(root_child2, 100)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 100)
    YGNodeStyleSetHeight(root_child3, 100)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 100)
    YGNodeStyleSetHeight(root_child4, 100)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 700

    assert YGNodeLayoutGetLeft(root_child0) == 10
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 138
    assert YGNodeLayoutGetTop(root_child1) == 10
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 10
    assert YGNodeLayoutGetTop(root_child2) == 178
    assert YGNodeLayoutGetWidth(root_child2) == 100
    assert YGNodeLayoutGetHeight(root_child2) == 100

    assert YGNodeLayoutGetLeft(root_child3) == 138
    assert YGNodeLayoutGetTop(root_child3) == 178
    assert YGNodeLayoutGetWidth(root_child3) == 100
    assert YGNodeLayoutGetHeight(root_child3) == 100

    assert YGNodeLayoutGetLeft(root_child4) == 10
    assert YGNodeLayoutGetTop(root_child4) == 346
    assert YGNodeLayoutGetWidth(root_child4) == 100
    assert YGNodeLayoutGetHeight(root_child4) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 700

    assert YGNodeLayoutGetLeft(root_child0) == 190
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 62
    assert YGNodeLayoutGetTop(root_child1) == 10
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 190
    assert YGNodeLayoutGetTop(root_child2) == 178
    assert YGNodeLayoutGetWidth(root_child2) == 100
    assert YGNodeLayoutGetHeight(root_child2) == 100

    assert YGNodeLayoutGetLeft(root_child3) == 62
    assert YGNodeLayoutGetTop(root_child3) == 178
    assert YGNodeLayoutGetWidth(root_child3) == 100
    assert YGNodeLayoutGetHeight(root_child3) == 100

    assert YGNodeLayoutGetLeft(root_child4) == 190
    assert YGNodeLayoutGetTop(root_child4) == 346
    assert YGNodeLayoutGetWidth(root_child4) == 100
    assert YGNodeLayoutGetHeight(root_child4) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_row_gap_percent_wrapping_with_content_margin():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(root, 300)
    YGNodeStyleSetHeight(root, 700)
    YGNodeStyleSetMargin(root, YGEdge.YGEdgeAll, 10)
    YGNodeStyleSetGapPercent(root, YGGutter.YGGutterAll, 10)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 100)
    YGNodeStyleSetHeight(root_child1, 100)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 100)
    YGNodeStyleSetHeight(root_child2, 100)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 100)
    YGNodeStyleSetHeight(root_child3, 100)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 100)
    YGNodeStyleSetHeight(root_child4, 100)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 10
    assert YGNodeLayoutGetTop(root) == 10
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 700

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 130
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 170
    assert YGNodeLayoutGetWidth(root_child2) == 100
    assert YGNodeLayoutGetHeight(root_child2) == 100

    assert YGNodeLayoutGetLeft(root_child3) == 130
    assert YGNodeLayoutGetTop(root_child3) == 170
    assert YGNodeLayoutGetWidth(root_child3) == 100
    assert YGNodeLayoutGetHeight(root_child3) == 100

    assert YGNodeLayoutGetLeft(root_child4) == 0
    assert YGNodeLayoutGetTop(root_child4) == 340
    assert YGNodeLayoutGetWidth(root_child4) == 100
    assert YGNodeLayoutGetHeight(root_child4) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 10
    assert YGNodeLayoutGetTop(root) == 10
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 700

    assert YGNodeLayoutGetLeft(root_child0) == 200
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 70
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 200
    assert YGNodeLayoutGetTop(root_child2) == 170
    assert YGNodeLayoutGetWidth(root_child2) == 100
    assert YGNodeLayoutGetHeight(root_child2) == 100

    assert YGNodeLayoutGetLeft(root_child3) == 70
    assert YGNodeLayoutGetTop(root_child3) == 170
    assert YGNodeLayoutGetWidth(root_child3) == 100
    assert YGNodeLayoutGetHeight(root_child3) == 100

    assert YGNodeLayoutGetLeft(root_child4) == 200
    assert YGNodeLayoutGetTop(root_child4) == 340
    assert YGNodeLayoutGetWidth(root_child4) == 100
    assert YGNodeLayoutGetHeight(root_child4) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_row_gap_percent_wrapping_with_content_margin_and_padding():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(root, 300)
    YGNodeStyleSetHeight(root, 700)
    YGNodeStyleSetMargin(root, YGEdge.YGEdgeAll, 10)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeAll, 10)
    YGNodeStyleSetGapPercent(root, YGGutter.YGGutterAll, 10)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 100)
    YGNodeStyleSetHeight(root_child1, 100)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 100)
    YGNodeStyleSetHeight(root_child2, 100)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 100)
    YGNodeStyleSetHeight(root_child3, 100)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 100)
    YGNodeStyleSetHeight(root_child4, 100)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 10
    assert YGNodeLayoutGetTop(root) == 10
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 700

    assert YGNodeLayoutGetLeft(root_child0) == 10
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 138
    assert YGNodeLayoutGetTop(root_child1) == 10
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 10
    assert YGNodeLayoutGetTop(root_child2) == 178
    assert YGNodeLayoutGetWidth(root_child2) == 100
    assert YGNodeLayoutGetHeight(root_child2) == 100

    assert YGNodeLayoutGetLeft(root_child3) == 138
    assert YGNodeLayoutGetTop(root_child3) == 178
    assert YGNodeLayoutGetWidth(root_child3) == 100
    assert YGNodeLayoutGetHeight(root_child3) == 100

    assert YGNodeLayoutGetLeft(root_child4) == 10
    assert YGNodeLayoutGetTop(root_child4) == 346
    assert YGNodeLayoutGetWidth(root_child4) == 100
    assert YGNodeLayoutGetHeight(root_child4) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 10
    assert YGNodeLayoutGetTop(root) == 10
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 700

    assert YGNodeLayoutGetLeft(root_child0) == 190
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 62
    assert YGNodeLayoutGetTop(root_child1) == 10
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 190
    assert YGNodeLayoutGetTop(root_child2) == 178
    assert YGNodeLayoutGetWidth(root_child2) == 100
    assert YGNodeLayoutGetHeight(root_child2) == 100

    assert YGNodeLayoutGetLeft(root_child3) == 62
    assert YGNodeLayoutGetTop(root_child3) == 178
    assert YGNodeLayoutGetWidth(root_child3) == 100
    assert YGNodeLayoutGetHeight(root_child3) == 100

    assert YGNodeLayoutGetLeft(root_child4) == 190
    assert YGNodeLayoutGetTop(root_child4) == 346
    assert YGNodeLayoutGetWidth(root_child4) == 100
    assert YGNodeLayoutGetHeight(root_child4) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_row_gap_percent_wrapping_with_flexible_content():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(root, 300)
    YGNodeStyleSetHeight(root, 300)
    YGNodeStyleSetGapPercent(root, YGGutter.YGGutterAll, 10)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeStyleSetFlexShrink(root_child0, 1)
    YGNodeStyleSetFlexBasisPercent(root_child0, 0)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child1, 1)
    YGNodeStyleSetFlexShrink(root_child1, 1)
    YGNodeStyleSetFlexBasisPercent(root_child1, 0)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child2, 1)
    YGNodeStyleSetFlexShrink(root_child2, 1)
    YGNodeStyleSetFlexBasisPercent(root_child2, 0)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 80
    assert YGNodeLayoutGetHeight(root_child0) == 300

    assert YGNodeLayoutGetLeft(root_child1) == 110
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 80
    assert YGNodeLayoutGetHeight(root_child1) == 300

    assert YGNodeLayoutGetLeft(root_child2) == 220
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 80
    assert YGNodeLayoutGetHeight(root_child2) == 300

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 220
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 80
    assert YGNodeLayoutGetHeight(root_child0) == 300

    assert YGNodeLayoutGetLeft(root_child1) == 110
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 80
    assert YGNodeLayoutGetHeight(root_child1) == 300

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 80
    assert YGNodeLayoutGetHeight(root_child2) == 300

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_row_gap_percent_wrapping_with_mixed_flexible_content():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(root, 300)
    YGNodeStyleSetHeight(root, 300)
    YGNodeStyleSetGapPercent(root, YGGutter.YGGutterAll, 10)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child1, 1)
    YGNodeStyleSetFlexShrink(root_child1, 1)
    YGNodeStyleSetFlexBasisPercent(root_child1, 0)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child2, 10)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 300

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 200
    assert YGNodeLayoutGetHeight(root_child1) == 300

    assert YGNodeLayoutGetLeft(root_child2) == 270
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 30
    assert YGNodeLayoutGetHeight(root_child2) == 300

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 290
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 300

    assert YGNodeLayoutGetLeft(root_child1) == 60
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 200
    assert YGNodeLayoutGetHeight(root_child1) == 300

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 30
    assert YGNodeLayoutGetHeight(root_child2) == 300

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_row_gap_percent_wrapping_with_min_width():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetMinWidth(root, 300)
    YGNodeStyleSetGapPercent(root, YGGutter.YGGutterAll, 10)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 100)
    YGNodeStyleSetHeight(root_child1, 100)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 100)
    YGNodeStyleSetHeight(root_child2, 100)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 100)
    YGNodeStyleSetHeight(root_child3, 100)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 100)
    YGNodeStyleSetHeight(root_child4, 100)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 130
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 100
    assert YGNodeLayoutGetWidth(root_child2) == 100
    assert YGNodeLayoutGetHeight(root_child2) == 100

    assert YGNodeLayoutGetLeft(root_child3) == 130
    assert YGNodeLayoutGetTop(root_child3) == 100
    assert YGNodeLayoutGetWidth(root_child3) == 100
    assert YGNodeLayoutGetHeight(root_child3) == 100

    assert YGNodeLayoutGetLeft(root_child4) == 0
    assert YGNodeLayoutGetTop(root_child4) == 200
    assert YGNodeLayoutGetWidth(root_child4) == 100
    assert YGNodeLayoutGetHeight(root_child4) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 200
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 70
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 200
    assert YGNodeLayoutGetTop(root_child2) == 100
    assert YGNodeLayoutGetWidth(root_child2) == 100
    assert YGNodeLayoutGetHeight(root_child2) == 100

    assert YGNodeLayoutGetLeft(root_child3) == 70
    assert YGNodeLayoutGetTop(root_child3) == 100
    assert YGNodeLayoutGetWidth(root_child3) == 100
    assert YGNodeLayoutGetHeight(root_child3) == 100

    assert YGNodeLayoutGetLeft(root_child4) == 200
    assert YGNodeLayoutGetTop(root_child4) == 200
    assert YGNodeLayoutGetWidth(root_child4) == 100
    assert YGNodeLayoutGetHeight(root_child4) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

