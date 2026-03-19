import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from yoga import *  # noqa: E402,F403


def test_wrap_column():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 30)
    YGNodeStyleSetWidth(root_child0, 30)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1, 30)
    YGNodeStyleSetWidth(root_child1, 30)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child2, 30)
    YGNodeStyleSetWidth(root_child2, 30)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child3, 30)
    YGNodeStyleSetWidth(root_child3, 30)
    YGNodeInsertChild(root, root_child3, 3)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 30
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 30
    assert YGNodeLayoutGetHeight(root_child0) == 30

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 30
    assert YGNodeLayoutGetWidth(root_child1) == 30
    assert YGNodeLayoutGetHeight(root_child1) == 30

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 60
    assert YGNodeLayoutGetWidth(root_child2) == 30
    assert YGNodeLayoutGetHeight(root_child2) == 30

    assert YGNodeLayoutGetLeft(root_child3) == 30
    assert YGNodeLayoutGetTop(root_child3) == 0
    assert YGNodeLayoutGetWidth(root_child3) == 30
    assert YGNodeLayoutGetHeight(root_child3) == 30

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 30
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 30
    assert YGNodeLayoutGetHeight(root_child0) == 30

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 30
    assert YGNodeLayoutGetWidth(root_child1) == 30
    assert YGNodeLayoutGetHeight(root_child1) == 30

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 60
    assert YGNodeLayoutGetWidth(root_child2) == 30
    assert YGNodeLayoutGetHeight(root_child2) == 30

    assert YGNodeLayoutGetLeft(root_child3) == -30
    assert YGNodeLayoutGetTop(root_child3) == 0
    assert YGNodeLayoutGetWidth(root_child3) == 30
    assert YGNodeLayoutGetHeight(root_child3) == 30

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_wrap_row():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 30)
    YGNodeStyleSetWidth(root_child0, 30)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1, 30)
    YGNodeStyleSetWidth(root_child1, 30)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child2, 30)
    YGNodeStyleSetWidth(root_child2, 30)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child3, 30)
    YGNodeStyleSetWidth(root_child3, 30)
    YGNodeInsertChild(root, root_child3, 3)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 60

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 30
    assert YGNodeLayoutGetHeight(root_child0) == 30

    assert YGNodeLayoutGetLeft(root_child1) == 30
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 30
    assert YGNodeLayoutGetHeight(root_child1) == 30

    assert YGNodeLayoutGetLeft(root_child2) == 60
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 30
    assert YGNodeLayoutGetHeight(root_child2) == 30

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 30
    assert YGNodeLayoutGetWidth(root_child3) == 30
    assert YGNodeLayoutGetHeight(root_child3) == 30

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 60

    assert YGNodeLayoutGetLeft(root_child0) == 70
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 30
    assert YGNodeLayoutGetHeight(root_child0) == 30

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 30
    assert YGNodeLayoutGetHeight(root_child1) == 30

    assert YGNodeLayoutGetLeft(root_child2) == 10
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 30
    assert YGNodeLayoutGetHeight(root_child2) == 30

    assert YGNodeLayoutGetLeft(root_child3) == 70
    assert YGNodeLayoutGetTop(root_child3) == 30
    assert YGNodeLayoutGetWidth(root_child3) == 30
    assert YGNodeLayoutGetHeight(root_child3) == 30

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_wrap_row_align_items_flex_end():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexEnd)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeStyleSetWidth(root_child0, 30)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1, 20)
    YGNodeStyleSetWidth(root_child1, 30)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child2, 30)
    YGNodeStyleSetWidth(root_child2, 30)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child3, 30)
    YGNodeStyleSetWidth(root_child3, 30)
    YGNodeInsertChild(root, root_child3, 3)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 60

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 20
    assert YGNodeLayoutGetWidth(root_child0) == 30
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 30
    assert YGNodeLayoutGetTop(root_child1) == 10
    assert YGNodeLayoutGetWidth(root_child1) == 30
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 60
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 30
    assert YGNodeLayoutGetHeight(root_child2) == 30

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 30
    assert YGNodeLayoutGetWidth(root_child3) == 30
    assert YGNodeLayoutGetHeight(root_child3) == 30

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 60

    assert YGNodeLayoutGetLeft(root_child0) == 70
    assert YGNodeLayoutGetTop(root_child0) == 20
    assert YGNodeLayoutGetWidth(root_child0) == 30
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 10
    assert YGNodeLayoutGetWidth(root_child1) == 30
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 10
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 30
    assert YGNodeLayoutGetHeight(root_child2) == 30

    assert YGNodeLayoutGetLeft(root_child3) == 70
    assert YGNodeLayoutGetTop(root_child3) == 30
    assert YGNodeLayoutGetWidth(root_child3) == 30
    assert YGNodeLayoutGetHeight(root_child3) == 30

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_wrap_row_align_items_center():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeStyleSetWidth(root_child0, 30)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1, 20)
    YGNodeStyleSetWidth(root_child1, 30)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child2, 30)
    YGNodeStyleSetWidth(root_child2, 30)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child3, 30)
    YGNodeStyleSetWidth(root_child3, 30)
    YGNodeInsertChild(root, root_child3, 3)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 60

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 30
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 30
    assert YGNodeLayoutGetTop(root_child1) == 5
    assert YGNodeLayoutGetWidth(root_child1) == 30
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 60
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 30
    assert YGNodeLayoutGetHeight(root_child2) == 30

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 30
    assert YGNodeLayoutGetWidth(root_child3) == 30
    assert YGNodeLayoutGetHeight(root_child3) == 30

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 60

    assert YGNodeLayoutGetLeft(root_child0) == 70
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 30
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 5
    assert YGNodeLayoutGetWidth(root_child1) == 30
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 10
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 30
    assert YGNodeLayoutGetHeight(root_child2) == 30

    assert YGNodeLayoutGetLeft(root_child3) == 70
    assert YGNodeLayoutGetTop(root_child3) == 30
    assert YGNodeLayoutGetWidth(root_child3) == 30
    assert YGNodeLayoutGetHeight(root_child3) == 30

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_wrap_children_with_min_main_overriding_flex_basis():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexBasis(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeStyleSetMinWidth(root_child0, 55)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexBasis(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 50)
    YGNodeStyleSetMinWidth(root_child1, 55)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 55
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 50
    assert YGNodeLayoutGetWidth(root_child1) == 55
    assert YGNodeLayoutGetHeight(root_child1) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 45
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 55
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 45
    assert YGNodeLayoutGetTop(root_child1) == 50
    assert YGNodeLayoutGetWidth(root_child1) == 55
    assert YGNodeLayoutGetHeight(root_child1) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_wrap_wrap_to_child_height():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignItems(root_child0, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0_child0, 100)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 100)
    YGNodeStyleSetHeight(root_child1, 100)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 100
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 100
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_flex_wrap_align_stretch_fits_one_row():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 150)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 150
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 150
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 0

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_wrap_reverse_row_align_content_flex_start():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrapReverse)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeStyleSetWidth(root_child0, 30)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1, 20)
    YGNodeStyleSetWidth(root_child1, 30)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child2, 30)
    YGNodeStyleSetWidth(root_child2, 30)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child3, 40)
    YGNodeStyleSetWidth(root_child3, 30)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child4, 50)
    YGNodeStyleSetWidth(root_child4, 30)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 80

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 70
    assert YGNodeLayoutGetWidth(root_child0) == 30
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 30
    assert YGNodeLayoutGetTop(root_child1) == 60
    assert YGNodeLayoutGetWidth(root_child1) == 30
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 60
    assert YGNodeLayoutGetTop(root_child2) == 50
    assert YGNodeLayoutGetWidth(root_child2) == 30
    assert YGNodeLayoutGetHeight(root_child2) == 30

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 10
    assert YGNodeLayoutGetWidth(root_child3) == 30
    assert YGNodeLayoutGetHeight(root_child3) == 40

    assert YGNodeLayoutGetLeft(root_child4) == 30
    assert YGNodeLayoutGetTop(root_child4) == 0
    assert YGNodeLayoutGetWidth(root_child4) == 30
    assert YGNodeLayoutGetHeight(root_child4) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 80

    assert YGNodeLayoutGetLeft(root_child0) == 70
    assert YGNodeLayoutGetTop(root_child0) == 70
    assert YGNodeLayoutGetWidth(root_child0) == 30
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 60
    assert YGNodeLayoutGetWidth(root_child1) == 30
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 10
    assert YGNodeLayoutGetTop(root_child2) == 50
    assert YGNodeLayoutGetWidth(root_child2) == 30
    assert YGNodeLayoutGetHeight(root_child2) == 30

    assert YGNodeLayoutGetLeft(root_child3) == 70
    assert YGNodeLayoutGetTop(root_child3) == 10
    assert YGNodeLayoutGetWidth(root_child3) == 30
    assert YGNodeLayoutGetHeight(root_child3) == 40

    assert YGNodeLayoutGetLeft(root_child4) == 40
    assert YGNodeLayoutGetTop(root_child4) == 0
    assert YGNodeLayoutGetWidth(root_child4) == 30
    assert YGNodeLayoutGetHeight(root_child4) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_wrap_reverse_row_align_content_center():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrapReverse)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignCenter)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeStyleSetWidth(root_child0, 30)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1, 20)
    YGNodeStyleSetWidth(root_child1, 30)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child2, 30)
    YGNodeStyleSetWidth(root_child2, 30)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child3, 40)
    YGNodeStyleSetWidth(root_child3, 30)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child4, 50)
    YGNodeStyleSetWidth(root_child4, 30)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 80

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 70
    assert YGNodeLayoutGetWidth(root_child0) == 30
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 30
    assert YGNodeLayoutGetTop(root_child1) == 60
    assert YGNodeLayoutGetWidth(root_child1) == 30
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 60
    assert YGNodeLayoutGetTop(root_child2) == 50
    assert YGNodeLayoutGetWidth(root_child2) == 30
    assert YGNodeLayoutGetHeight(root_child2) == 30

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 10
    assert YGNodeLayoutGetWidth(root_child3) == 30
    assert YGNodeLayoutGetHeight(root_child3) == 40

    assert YGNodeLayoutGetLeft(root_child4) == 30
    assert YGNodeLayoutGetTop(root_child4) == 0
    assert YGNodeLayoutGetWidth(root_child4) == 30
    assert YGNodeLayoutGetHeight(root_child4) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 80

    assert YGNodeLayoutGetLeft(root_child0) == 70
    assert YGNodeLayoutGetTop(root_child0) == 70
    assert YGNodeLayoutGetWidth(root_child0) == 30
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 60
    assert YGNodeLayoutGetWidth(root_child1) == 30
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 10
    assert YGNodeLayoutGetTop(root_child2) == 50
    assert YGNodeLayoutGetWidth(root_child2) == 30
    assert YGNodeLayoutGetHeight(root_child2) == 30

    assert YGNodeLayoutGetLeft(root_child3) == 70
    assert YGNodeLayoutGetTop(root_child3) == 10
    assert YGNodeLayoutGetWidth(root_child3) == 30
    assert YGNodeLayoutGetHeight(root_child3) == 40

    assert YGNodeLayoutGetLeft(root_child4) == 40
    assert YGNodeLayoutGetTop(root_child4) == 0
    assert YGNodeLayoutGetWidth(root_child4) == 30
    assert YGNodeLayoutGetHeight(root_child4) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_wrap_reverse_row_single_line_different_size():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 300)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrapReverse)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeStyleSetWidth(root_child0, 30)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1, 20)
    YGNodeStyleSetWidth(root_child1, 30)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child2, 30)
    YGNodeStyleSetWidth(root_child2, 30)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child3, 40)
    YGNodeStyleSetWidth(root_child3, 30)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child4, 50)
    YGNodeStyleSetWidth(root_child4, 30)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 50

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 40
    assert YGNodeLayoutGetWidth(root_child0) == 30
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 30
    assert YGNodeLayoutGetTop(root_child1) == 30
    assert YGNodeLayoutGetWidth(root_child1) == 30
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 60
    assert YGNodeLayoutGetTop(root_child2) == 20
    assert YGNodeLayoutGetWidth(root_child2) == 30
    assert YGNodeLayoutGetHeight(root_child2) == 30

    assert YGNodeLayoutGetLeft(root_child3) == 90
    assert YGNodeLayoutGetTop(root_child3) == 10
    assert YGNodeLayoutGetWidth(root_child3) == 30
    assert YGNodeLayoutGetHeight(root_child3) == 40

    assert YGNodeLayoutGetLeft(root_child4) == 120
    assert YGNodeLayoutGetTop(root_child4) == 0
    assert YGNodeLayoutGetWidth(root_child4) == 30
    assert YGNodeLayoutGetHeight(root_child4) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 50

    assert YGNodeLayoutGetLeft(root_child0) == 270
    assert YGNodeLayoutGetTop(root_child0) == 40
    assert YGNodeLayoutGetWidth(root_child0) == 30
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 240
    assert YGNodeLayoutGetTop(root_child1) == 30
    assert YGNodeLayoutGetWidth(root_child1) == 30
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 210
    assert YGNodeLayoutGetTop(root_child2) == 20
    assert YGNodeLayoutGetWidth(root_child2) == 30
    assert YGNodeLayoutGetHeight(root_child2) == 30

    assert YGNodeLayoutGetLeft(root_child3) == 180
    assert YGNodeLayoutGetTop(root_child3) == 10
    assert YGNodeLayoutGetWidth(root_child3) == 30
    assert YGNodeLayoutGetHeight(root_child3) == 40

    assert YGNodeLayoutGetLeft(root_child4) == 150
    assert YGNodeLayoutGetTop(root_child4) == 0
    assert YGNodeLayoutGetWidth(root_child4) == 30
    assert YGNodeLayoutGetHeight(root_child4) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_wrap_reverse_row_align_content_stretch():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrapReverse)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignStretch)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeStyleSetWidth(root_child0, 30)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1, 20)
    YGNodeStyleSetWidth(root_child1, 30)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child2, 30)
    YGNodeStyleSetWidth(root_child2, 30)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child3, 40)
    YGNodeStyleSetWidth(root_child3, 30)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child4, 50)
    YGNodeStyleSetWidth(root_child4, 30)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 80

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 70
    assert YGNodeLayoutGetWidth(root_child0) == 30
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 30
    assert YGNodeLayoutGetTop(root_child1) == 60
    assert YGNodeLayoutGetWidth(root_child1) == 30
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 60
    assert YGNodeLayoutGetTop(root_child2) == 50
    assert YGNodeLayoutGetWidth(root_child2) == 30
    assert YGNodeLayoutGetHeight(root_child2) == 30

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 10
    assert YGNodeLayoutGetWidth(root_child3) == 30
    assert YGNodeLayoutGetHeight(root_child3) == 40

    assert YGNodeLayoutGetLeft(root_child4) == 30
    assert YGNodeLayoutGetTop(root_child4) == 0
    assert YGNodeLayoutGetWidth(root_child4) == 30
    assert YGNodeLayoutGetHeight(root_child4) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 80

    assert YGNodeLayoutGetLeft(root_child0) == 70
    assert YGNodeLayoutGetTop(root_child0) == 70
    assert YGNodeLayoutGetWidth(root_child0) == 30
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 60
    assert YGNodeLayoutGetWidth(root_child1) == 30
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 10
    assert YGNodeLayoutGetTop(root_child2) == 50
    assert YGNodeLayoutGetWidth(root_child2) == 30
    assert YGNodeLayoutGetHeight(root_child2) == 30

    assert YGNodeLayoutGetLeft(root_child3) == 70
    assert YGNodeLayoutGetTop(root_child3) == 10
    assert YGNodeLayoutGetWidth(root_child3) == 30
    assert YGNodeLayoutGetHeight(root_child3) == 40

    assert YGNodeLayoutGetLeft(root_child4) == 40
    assert YGNodeLayoutGetTop(root_child4) == 0
    assert YGNodeLayoutGetWidth(root_child4) == 30
    assert YGNodeLayoutGetHeight(root_child4) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_wrap_reverse_row_align_content_space_around():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrapReverse)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignSpaceAround)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeStyleSetWidth(root_child0, 30)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1, 20)
    YGNodeStyleSetWidth(root_child1, 30)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child2, 30)
    YGNodeStyleSetWidth(root_child2, 30)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child3, 40)
    YGNodeStyleSetWidth(root_child3, 30)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child4, 50)
    YGNodeStyleSetWidth(root_child4, 30)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 80

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 70
    assert YGNodeLayoutGetWidth(root_child0) == 30
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 30
    assert YGNodeLayoutGetTop(root_child1) == 60
    assert YGNodeLayoutGetWidth(root_child1) == 30
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 60
    assert YGNodeLayoutGetTop(root_child2) == 50
    assert YGNodeLayoutGetWidth(root_child2) == 30
    assert YGNodeLayoutGetHeight(root_child2) == 30

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 10
    assert YGNodeLayoutGetWidth(root_child3) == 30
    assert YGNodeLayoutGetHeight(root_child3) == 40

    assert YGNodeLayoutGetLeft(root_child4) == 30
    assert YGNodeLayoutGetTop(root_child4) == 0
    assert YGNodeLayoutGetWidth(root_child4) == 30
    assert YGNodeLayoutGetHeight(root_child4) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 80

    assert YGNodeLayoutGetLeft(root_child0) == 70
    assert YGNodeLayoutGetTop(root_child0) == 70
    assert YGNodeLayoutGetWidth(root_child0) == 30
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 60
    assert YGNodeLayoutGetWidth(root_child1) == 30
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 10
    assert YGNodeLayoutGetTop(root_child2) == 50
    assert YGNodeLayoutGetWidth(root_child2) == 30
    assert YGNodeLayoutGetHeight(root_child2) == 30

    assert YGNodeLayoutGetLeft(root_child3) == 70
    assert YGNodeLayoutGetTop(root_child3) == 10
    assert YGNodeLayoutGetWidth(root_child3) == 30
    assert YGNodeLayoutGetHeight(root_child3) == 40

    assert YGNodeLayoutGetLeft(root_child4) == 40
    assert YGNodeLayoutGetTop(root_child4) == 0
    assert YGNodeLayoutGetWidth(root_child4) == 30
    assert YGNodeLayoutGetHeight(root_child4) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_wrap_reverse_column_fixed_size():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrapReverse)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeStyleSetWidth(root_child0, 30)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1, 20)
    YGNodeStyleSetWidth(root_child1, 30)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child2, 30)
    YGNodeStyleSetWidth(root_child2, 30)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child3, 40)
    YGNodeStyleSetWidth(root_child3, 30)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child4, 50)
    YGNodeStyleSetWidth(root_child4, 30)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 170
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 30
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 170
    assert YGNodeLayoutGetTop(root_child1) == 10
    assert YGNodeLayoutGetWidth(root_child1) == 30
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 170
    assert YGNodeLayoutGetTop(root_child2) == 30
    assert YGNodeLayoutGetWidth(root_child2) == 30
    assert YGNodeLayoutGetHeight(root_child2) == 30

    assert YGNodeLayoutGetLeft(root_child3) == 170
    assert YGNodeLayoutGetTop(root_child3) == 60
    assert YGNodeLayoutGetWidth(root_child3) == 30
    assert YGNodeLayoutGetHeight(root_child3) == 40

    assert YGNodeLayoutGetLeft(root_child4) == 140
    assert YGNodeLayoutGetTop(root_child4) == 0
    assert YGNodeLayoutGetWidth(root_child4) == 30
    assert YGNodeLayoutGetHeight(root_child4) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 30
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 10
    assert YGNodeLayoutGetWidth(root_child1) == 30
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 30
    assert YGNodeLayoutGetWidth(root_child2) == 30
    assert YGNodeLayoutGetHeight(root_child2) == 30

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 60
    assert YGNodeLayoutGetWidth(root_child3) == 30
    assert YGNodeLayoutGetHeight(root_child3) == 40

    assert YGNodeLayoutGetLeft(root_child4) == 30
    assert YGNodeLayoutGetTop(root_child4) == 0
    assert YGNodeLayoutGetWidth(root_child4) == 30
    assert YGNodeLayoutGetHeight(root_child4) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_wrapped_row_within_align_items_center():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 200)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 150)
    YGNodeStyleSetHeight(root_child0_child0, 80)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 80)
    YGNodeStyleSetHeight(root_child0_child1, 80)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 160

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 150
    assert YGNodeLayoutGetHeight(root_child0_child0) == 80

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 80
    assert YGNodeLayoutGetWidth(root_child0_child1) == 80
    assert YGNodeLayoutGetHeight(root_child0_child1) == 80

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 160

    assert YGNodeLayoutGetLeft(root_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 150
    assert YGNodeLayoutGetHeight(root_child0_child0) == 80

    assert YGNodeLayoutGetLeft(root_child0_child1) == 120
    assert YGNodeLayoutGetTop(root_child0_child1) == 80
    assert YGNodeLayoutGetWidth(root_child0_child1) == 80
    assert YGNodeLayoutGetHeight(root_child0_child1) == 80

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_wrapped_row_within_align_items_flex_start():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 200)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 150)
    YGNodeStyleSetHeight(root_child0_child0, 80)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 80)
    YGNodeStyleSetHeight(root_child0_child1, 80)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 160

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 150
    assert YGNodeLayoutGetHeight(root_child0_child0) == 80

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 80
    assert YGNodeLayoutGetWidth(root_child0_child1) == 80
    assert YGNodeLayoutGetHeight(root_child0_child1) == 80

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 160

    assert YGNodeLayoutGetLeft(root_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 150
    assert YGNodeLayoutGetHeight(root_child0_child0) == 80

    assert YGNodeLayoutGetLeft(root_child0_child1) == 120
    assert YGNodeLayoutGetTop(root_child0_child1) == 80
    assert YGNodeLayoutGetWidth(root_child0_child1) == 80
    assert YGNodeLayoutGetHeight(root_child0_child1) == 80

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_wrapped_row_within_align_items_flex_end():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 200)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexEnd)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 150)
    YGNodeStyleSetHeight(root_child0_child0, 80)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 80)
    YGNodeStyleSetHeight(root_child0_child1, 80)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 160

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 150
    assert YGNodeLayoutGetHeight(root_child0_child0) == 80

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 80
    assert YGNodeLayoutGetWidth(root_child0_child1) == 80
    assert YGNodeLayoutGetHeight(root_child0_child1) == 80

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 160

    assert YGNodeLayoutGetLeft(root_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 150
    assert YGNodeLayoutGetHeight(root_child0_child0) == 80

    assert YGNodeLayoutGetLeft(root_child0_child1) == 120
    assert YGNodeLayoutGetTop(root_child0_child1) == 80
    assert YGNodeLayoutGetWidth(root_child0_child1) == 80
    assert YGNodeLayoutGetHeight(root_child0_child1) == 80

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_wrapped_column_max_height():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 500)
    YGNodeStyleSetWidth(root, 700)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyCenter)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignCenter)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetHeight(root_child0, 500)
    YGNodeStyleSetMaxHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 200)
    YGNodeStyleSetHeight(root_child1, 200)
    YGNodeStyleSetMargin(root_child1, YGEdge.YGEdgeAll, 20)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 100)
    YGNodeStyleSetHeight(root_child2, 100)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 700
    assert YGNodeLayoutGetHeight(root) == 500

    assert YGNodeLayoutGetLeft(root_child0) == 250
    assert YGNodeLayoutGetTop(root_child0) == 30
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child1) == 200
    assert YGNodeLayoutGetTop(root_child1) == 250
    assert YGNodeLayoutGetWidth(root_child1) == 200
    assert YGNodeLayoutGetHeight(root_child1) == 200

    assert YGNodeLayoutGetLeft(root_child2) == 420
    assert YGNodeLayoutGetTop(root_child2) == 200
    assert YGNodeLayoutGetWidth(root_child2) == 100
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 700
    assert YGNodeLayoutGetHeight(root) == 500

    assert YGNodeLayoutGetLeft(root_child0) == 350
    assert YGNodeLayoutGetTop(root_child0) == 30
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child1) == 300
    assert YGNodeLayoutGetTop(root_child1) == 250
    assert YGNodeLayoutGetWidth(root_child1) == 200
    assert YGNodeLayoutGetHeight(root_child1) == 200

    assert YGNodeLayoutGetLeft(root_child2) == 180
    assert YGNodeLayoutGetTop(root_child2) == 200
    assert YGNodeLayoutGetWidth(root_child2) == 100
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_wrapped_column_max_height_flex():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 500)
    YGNodeStyleSetWidth(root, 700)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyCenter)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignCenter)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetHeight(root_child0, 500)
    YGNodeStyleSetMaxHeight(root_child0, 200)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeStyleSetFlexShrink(root_child0, 1)
    YGNodeStyleSetFlexBasisPercent(root_child0, 0)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 200)
    YGNodeStyleSetHeight(root_child1, 200)
    YGNodeStyleSetMargin(root_child1, YGEdge.YGEdgeAll, 20)
    YGNodeStyleSetFlexGrow(root_child1, 1)
    YGNodeStyleSetFlexShrink(root_child1, 1)
    YGNodeStyleSetFlexBasisPercent(root_child1, 0)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 100)
    YGNodeStyleSetHeight(root_child2, 100)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 700
    assert YGNodeLayoutGetHeight(root) == 500

    assert YGNodeLayoutGetLeft(root_child0) == 300
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 180

    assert YGNodeLayoutGetLeft(root_child1) == 250
    assert YGNodeLayoutGetTop(root_child1) == 200
    assert YGNodeLayoutGetWidth(root_child1) == 200
    assert YGNodeLayoutGetHeight(root_child1) == 180

    assert YGNodeLayoutGetLeft(root_child2) == 300
    assert YGNodeLayoutGetTop(root_child2) == 400
    assert YGNodeLayoutGetWidth(root_child2) == 100
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 700
    assert YGNodeLayoutGetHeight(root) == 500

    assert YGNodeLayoutGetLeft(root_child0) == 300
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 180

    assert YGNodeLayoutGetLeft(root_child1) == 250
    assert YGNodeLayoutGetTop(root_child1) == 200
    assert YGNodeLayoutGetWidth(root_child1) == 200
    assert YGNodeLayoutGetHeight(root_child1) == 180

    assert YGNodeLayoutGetLeft(root_child2) == 300
    assert YGNodeLayoutGetTop(root_child2) == 400
    assert YGNodeLayoutGetWidth(root_child2) == 100
    assert YGNodeLayoutGetHeight(root_child2) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_wrap_nodes_with_content_sizing_overflowing_margin():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 500)
    YGNodeStyleSetHeight(root, 500)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeStyleSetWidth(root_child0, 85)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 40)
    YGNodeStyleSetWidth(root_child0_child0_child0, 40)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMargin(root_child0_child1, YGEdge.YGEdgeRight, 10)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child1_child0, 40)
    YGNodeStyleSetWidth(root_child0_child1_child0, 40)
    YGNodeInsertChild(root_child0_child1, root_child0_child1_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 500

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 85
    assert YGNodeLayoutGetHeight(root_child0) == 80

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0_child0) == 40

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 40

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 40
    assert YGNodeLayoutGetWidth(root_child0_child1) == 40
    assert YGNodeLayoutGetHeight(root_child0_child1) == 40

    assert YGNodeLayoutGetLeft(root_child0_child1_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0_child1_child0) == 40

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 500

    assert YGNodeLayoutGetLeft(root_child0) == 415
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 85
    assert YGNodeLayoutGetHeight(root_child0) == 80

    assert YGNodeLayoutGetLeft(root_child0_child0) == 45
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0_child0) == 40

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 40

    assert YGNodeLayoutGetLeft(root_child0_child1) == 35
    assert YGNodeLayoutGetTop(root_child0_child1) == 40
    assert YGNodeLayoutGetWidth(root_child0_child1) == 40
    assert YGNodeLayoutGetHeight(root_child0_child1) == 40

    assert YGNodeLayoutGetLeft(root_child0_child1_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0_child1_child0) == 40

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_wrap_nodes_with_content_sizing_margin_cross():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 500)
    YGNodeStyleSetHeight(root, 500)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeStyleSetWidth(root_child0, 70)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 40)
    YGNodeStyleSetWidth(root_child0_child0_child0, 40)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMargin(root_child0_child1, YGEdge.YGEdgeTop, 10)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child1_child0, 40)
    YGNodeStyleSetWidth(root_child0_child1_child0, 40)
    YGNodeInsertChild(root_child0_child1, root_child0_child1_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 500

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 70
    assert YGNodeLayoutGetHeight(root_child0) == 90

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0_child0) == 40

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 40

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 50
    assert YGNodeLayoutGetWidth(root_child0_child1) == 40
    assert YGNodeLayoutGetHeight(root_child0_child1) == 40

    assert YGNodeLayoutGetLeft(root_child0_child1_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0_child1_child0) == 40

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 500

    assert YGNodeLayoutGetLeft(root_child0) == 430
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 70
    assert YGNodeLayoutGetHeight(root_child0) == 90

    assert YGNodeLayoutGetLeft(root_child0_child0) == 30
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0_child0) == 40

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 40

    assert YGNodeLayoutGetLeft(root_child0_child1) == 30
    assert YGNodeLayoutGetTop(root_child0_child1) == 50
    assert YGNodeLayoutGetWidth(root_child0_child1) == 40
    assert YGNodeLayoutGetHeight(root_child0_child1) == 40

    assert YGNodeLayoutGetLeft(root_child0_child1_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0_child1_child0) == 40

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_wrap_with_min_cross_axis():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 500)
    YGNodeStyleSetMinHeight(root, 500)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 400)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 400)
    YGNodeStyleSetHeight(root_child1, 200)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 500

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 200
    assert YGNodeLayoutGetWidth(root_child1) == 400
    assert YGNodeLayoutGetHeight(root_child1) == 200

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 500

    assert YGNodeLayoutGetLeft(root_child0) == 100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child1) == 100
    assert YGNodeLayoutGetTop(root_child1) == 200
    assert YGNodeLayoutGetWidth(root_child1) == 400
    assert YGNodeLayoutGetHeight(root_child1) == 200

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_wrap_with_max_cross_axis():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 500)
    YGNodeStyleSetMaxHeight(root, 500)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 400)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 400)
    YGNodeStyleSetHeight(root_child1, 200)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 400

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 200
    assert YGNodeLayoutGetWidth(root_child1) == 400
    assert YGNodeLayoutGetHeight(root_child1) == 200

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 400

    assert YGNodeLayoutGetLeft(root_child0) == 100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child1) == 100
    assert YGNodeLayoutGetTop(root_child1) == 200
    assert YGNodeLayoutGetWidth(root_child1) == 400
    assert YGNodeLayoutGetHeight(root_child1) == 200

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_nowrap_expands_flexline_box_to_min_cross():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetMinHeight(root, 400)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeStyleSetFlexShrink(root_child0, 1)
    YGNodeStyleSetFlexBasisPercent(root_child0, 0)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 0
    assert YGNodeLayoutGetHeight(root) == 400

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0) == 400

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 0
    assert YGNodeLayoutGetHeight(root) == 400

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0) == 400

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_wrap_does_not_impose_min_cross_onto_single_flexline():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetMinHeight(root, 400)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeStyleSetFlexShrink(root_child0, 1)
    YGNodeStyleSetFlexBasisPercent(root_child0, 0)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 0
    assert YGNodeLayoutGetHeight(root) == 400

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 0
    assert YGNodeLayoutGetHeight(root) == 400

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0) == 0

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

