import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from yoga import *  # noqa: E402,F403


def test_align_items_stretch():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_items_center():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeStyleSetWidth(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 45
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 45
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_items_flex_start():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeStyleSetWidth(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_items_flex_end():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexEnd)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeStyleSetWidth(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_baseline():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignBaseline)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 20)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 30
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 30
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_baseline_child():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignBaseline)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 20)
    YGNodeInsertChild(root, root_child1, 1)

    root_child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1_child0, 50)
    YGNodeStyleSetHeight(root_child1_child0, 10)
    YGNodeInsertChild(root_child1, root_child1_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child1_child0) == 0
    assert YGNodeLayoutGetTop(root_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child1_child0) == 50
    assert YGNodeLayoutGetHeight(root_child1_child0) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child1_child0) == 0
    assert YGNodeLayoutGetTop(root_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child1_child0) == 50
    assert YGNodeLayoutGetHeight(root_child1_child0) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_baseline_child_multiline():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignBaseline)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 60)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 25)
    YGNodeStyleSetFlexWrap(root_child1, YGWrap.YGWrapWrap)
    YGNodeStyleSetFlexDirection(root_child1, YGFlexDirection.YGFlexDirectionRow)
    YGNodeInsertChild(root, root_child1, 1)

    root_child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1_child0, 25)
    YGNodeStyleSetHeight(root_child1_child0, 20)
    YGNodeInsertChild(root_child1, root_child1_child0, 0)

    root_child1_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1_child1, 25)
    YGNodeStyleSetHeight(root_child1_child1, 10)
    YGNodeInsertChild(root_child1, root_child1_child1, 1)

    root_child1_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1_child2, 25)
    YGNodeStyleSetHeight(root_child1_child2, 20)
    YGNodeInsertChild(root_child1, root_child1_child2, 2)

    root_child1_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1_child3, 25)
    YGNodeStyleSetHeight(root_child1_child3, 10)
    YGNodeInsertChild(root_child1, root_child1_child3, 3)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 60

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 25

    assert YGNodeLayoutGetLeft(root_child1_child0) == 0
    assert YGNodeLayoutGetTop(root_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child1_child0) == 25
    assert YGNodeLayoutGetHeight(root_child1_child0) == 20

    assert YGNodeLayoutGetLeft(root_child1_child1) == 25
    assert YGNodeLayoutGetTop(root_child1_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1_child1) == 25
    assert YGNodeLayoutGetHeight(root_child1_child1) == 10

    assert YGNodeLayoutGetLeft(root_child1_child2) == 0
    assert YGNodeLayoutGetTop(root_child1_child2) == 20
    assert YGNodeLayoutGetWidth(root_child1_child2) == 25
    assert YGNodeLayoutGetHeight(root_child1_child2) == 20

    assert YGNodeLayoutGetLeft(root_child1_child3) == 25
    assert YGNodeLayoutGetTop(root_child1_child3) == 20
    assert YGNodeLayoutGetWidth(root_child1_child3) == 25
    assert YGNodeLayoutGetHeight(root_child1_child3) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 60

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 25

    assert YGNodeLayoutGetLeft(root_child1_child0) == 25
    assert YGNodeLayoutGetTop(root_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child1_child0) == 25
    assert YGNodeLayoutGetHeight(root_child1_child0) == 20

    assert YGNodeLayoutGetLeft(root_child1_child1) == 0
    assert YGNodeLayoutGetTop(root_child1_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1_child1) == 25
    assert YGNodeLayoutGetHeight(root_child1_child1) == 10

    assert YGNodeLayoutGetLeft(root_child1_child2) == 25
    assert YGNodeLayoutGetTop(root_child1_child2) == 20
    assert YGNodeLayoutGetWidth(root_child1_child2) == 25
    assert YGNodeLayoutGetHeight(root_child1_child2) == 20

    assert YGNodeLayoutGetLeft(root_child1_child3) == 0
    assert YGNodeLayoutGetTop(root_child1_child3) == 20
    assert YGNodeLayoutGetWidth(root_child1_child3) == 25
    assert YGNodeLayoutGetHeight(root_child1_child3) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_baseline_child_multiline_override():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignBaseline)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 60)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 25)
    YGNodeStyleSetFlexWrap(root_child1, YGWrap.YGWrapWrap)
    YGNodeStyleSetFlexDirection(root_child1, YGFlexDirection.YGFlexDirectionRow)
    YGNodeInsertChild(root, root_child1, 1)

    root_child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1_child0, 25)
    YGNodeStyleSetHeight(root_child1_child0, 20)
    YGNodeInsertChild(root_child1, root_child1_child0, 0)

    root_child1_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1_child1, 25)
    YGNodeStyleSetHeight(root_child1_child1, 10)
    YGNodeStyleSetAlignSelf(root_child1_child1, YGAlign.YGAlignBaseline)
    YGNodeInsertChild(root_child1, root_child1_child1, 1)

    root_child1_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1_child2, 25)
    YGNodeStyleSetHeight(root_child1_child2, 20)
    YGNodeInsertChild(root_child1, root_child1_child2, 2)

    root_child1_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1_child3, 25)
    YGNodeStyleSetHeight(root_child1_child3, 10)
    YGNodeStyleSetAlignSelf(root_child1_child3, YGAlign.YGAlignBaseline)
    YGNodeInsertChild(root_child1, root_child1_child3, 3)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 60

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 50
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 25

    assert YGNodeLayoutGetLeft(root_child1_child0) == 0
    assert YGNodeLayoutGetTop(root_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child1_child0) == 25
    assert YGNodeLayoutGetHeight(root_child1_child0) == 20

    assert YGNodeLayoutGetLeft(root_child1_child1) == 25
    assert YGNodeLayoutGetTop(root_child1_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1_child1) == 25
    assert YGNodeLayoutGetHeight(root_child1_child1) == 10

    assert YGNodeLayoutGetLeft(root_child1_child2) == 0
    assert YGNodeLayoutGetTop(root_child1_child2) == 20
    assert YGNodeLayoutGetWidth(root_child1_child2) == 25
    assert YGNodeLayoutGetHeight(root_child1_child2) == 20

    assert YGNodeLayoutGetLeft(root_child1_child3) == 25
    assert YGNodeLayoutGetTop(root_child1_child3) == 20
    assert YGNodeLayoutGetWidth(root_child1_child3) == 25
    assert YGNodeLayoutGetHeight(root_child1_child3) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 60

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 50
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 25

    assert YGNodeLayoutGetLeft(root_child1_child0) == 25
    assert YGNodeLayoutGetTop(root_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child1_child0) == 25
    assert YGNodeLayoutGetHeight(root_child1_child0) == 20

    assert YGNodeLayoutGetLeft(root_child1_child1) == 0
    assert YGNodeLayoutGetTop(root_child1_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1_child1) == 25
    assert YGNodeLayoutGetHeight(root_child1_child1) == 10

    assert YGNodeLayoutGetLeft(root_child1_child2) == 25
    assert YGNodeLayoutGetTop(root_child1_child2) == 20
    assert YGNodeLayoutGetWidth(root_child1_child2) == 25
    assert YGNodeLayoutGetHeight(root_child1_child2) == 20

    assert YGNodeLayoutGetLeft(root_child1_child3) == 0
    assert YGNodeLayoutGetTop(root_child1_child3) == 20
    assert YGNodeLayoutGetWidth(root_child1_child3) == 25
    assert YGNodeLayoutGetHeight(root_child1_child3) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_baseline_child_multiline_no_override_on_secondline():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignBaseline)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 60)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 25)
    YGNodeStyleSetFlexWrap(root_child1, YGWrap.YGWrapWrap)
    YGNodeStyleSetFlexDirection(root_child1, YGFlexDirection.YGFlexDirectionRow)
    YGNodeInsertChild(root, root_child1, 1)

    root_child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1_child0, 25)
    YGNodeStyleSetHeight(root_child1_child0, 20)
    YGNodeInsertChild(root_child1, root_child1_child0, 0)

    root_child1_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1_child1, 25)
    YGNodeStyleSetHeight(root_child1_child1, 10)
    YGNodeInsertChild(root_child1, root_child1_child1, 1)

    root_child1_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1_child2, 25)
    YGNodeStyleSetHeight(root_child1_child2, 20)
    YGNodeInsertChild(root_child1, root_child1_child2, 2)

    root_child1_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1_child3, 25)
    YGNodeStyleSetHeight(root_child1_child3, 10)
    YGNodeStyleSetAlignSelf(root_child1_child3, YGAlign.YGAlignBaseline)
    YGNodeInsertChild(root_child1, root_child1_child3, 3)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 60

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 25

    assert YGNodeLayoutGetLeft(root_child1_child0) == 0
    assert YGNodeLayoutGetTop(root_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child1_child0) == 25
    assert YGNodeLayoutGetHeight(root_child1_child0) == 20

    assert YGNodeLayoutGetLeft(root_child1_child1) == 25
    assert YGNodeLayoutGetTop(root_child1_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1_child1) == 25
    assert YGNodeLayoutGetHeight(root_child1_child1) == 10

    assert YGNodeLayoutGetLeft(root_child1_child2) == 0
    assert YGNodeLayoutGetTop(root_child1_child2) == 20
    assert YGNodeLayoutGetWidth(root_child1_child2) == 25
    assert YGNodeLayoutGetHeight(root_child1_child2) == 20

    assert YGNodeLayoutGetLeft(root_child1_child3) == 25
    assert YGNodeLayoutGetTop(root_child1_child3) == 20
    assert YGNodeLayoutGetWidth(root_child1_child3) == 25
    assert YGNodeLayoutGetHeight(root_child1_child3) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 60

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 25

    assert YGNodeLayoutGetLeft(root_child1_child0) == 25
    assert YGNodeLayoutGetTop(root_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child1_child0) == 25
    assert YGNodeLayoutGetHeight(root_child1_child0) == 20

    assert YGNodeLayoutGetLeft(root_child1_child1) == 0
    assert YGNodeLayoutGetTop(root_child1_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1_child1) == 25
    assert YGNodeLayoutGetHeight(root_child1_child1) == 10

    assert YGNodeLayoutGetLeft(root_child1_child2) == 25
    assert YGNodeLayoutGetTop(root_child1_child2) == 20
    assert YGNodeLayoutGetWidth(root_child1_child2) == 25
    assert YGNodeLayoutGetHeight(root_child1_child2) == 20

    assert YGNodeLayoutGetLeft(root_child1_child3) == 0
    assert YGNodeLayoutGetTop(root_child1_child3) == 20
    assert YGNodeLayoutGetWidth(root_child1_child3) == 25
    assert YGNodeLayoutGetHeight(root_child1_child3) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_baseline_child_top():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignBaseline)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeTop, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 20)
    YGNodeInsertChild(root, root_child1, 1)

    root_child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1_child0, 50)
    YGNodeStyleSetHeight(root_child1_child0, 10)
    YGNodeInsertChild(root_child1, root_child1_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child1_child0) == 0
    assert YGNodeLayoutGetTop(root_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child1_child0) == 50
    assert YGNodeLayoutGetHeight(root_child1_child0) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child1_child0) == 0
    assert YGNodeLayoutGetTop(root_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child1_child0) == 50
    assert YGNodeLayoutGetHeight(root_child1_child0) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_baseline_child_top2():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignBaseline)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 20)
    YGNodeStyleSetPosition(root_child1, YGEdge.YGEdgeTop, 5)
    YGNodeInsertChild(root, root_child1, 1)

    root_child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1_child0, 50)
    YGNodeStyleSetHeight(root_child1_child0, 10)
    YGNodeInsertChild(root_child1, root_child1_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 45
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child1_child0) == 0
    assert YGNodeLayoutGetTop(root_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child1_child0) == 50
    assert YGNodeLayoutGetHeight(root_child1_child0) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 45
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child1_child0) == 0
    assert YGNodeLayoutGetTop(root_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child1_child0) == 50
    assert YGNodeLayoutGetHeight(root_child1_child0) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_baseline_double_nested_child():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignBaseline)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 50)
    YGNodeStyleSetHeight(root_child0_child0, 20)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 20)
    YGNodeInsertChild(root, root_child1, 1)

    root_child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1_child0, 50)
    YGNodeStyleSetHeight(root_child1_child0, 15)
    YGNodeInsertChild(root_child1, root_child1_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 5
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child1_child0) == 0
    assert YGNodeLayoutGetTop(root_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child1_child0) == 50
    assert YGNodeLayoutGetHeight(root_child1_child0) == 15

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 5
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child1_child0) == 0
    assert YGNodeLayoutGetTop(root_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child1_child0) == 50
    assert YGNodeLayoutGetHeight(root_child1_child0) == 15

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_baseline_column():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignBaseline)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 20)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 50
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 50
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_baseline_child_margin():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignBaseline)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeAll, 5)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 20)
    YGNodeInsertChild(root, root_child1, 1)

    root_child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1_child0, 50)
    YGNodeStyleSetHeight(root_child1_child0, 10)
    YGNodeStyleSetMargin(root_child1_child0, YGEdge.YGEdgeAll, 1)
    YGNodeInsertChild(root_child1, root_child1_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 5
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 60
    assert YGNodeLayoutGetTop(root_child1) == 44
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child1_child0) == 1
    assert YGNodeLayoutGetTop(root_child1_child0) == 1
    assert YGNodeLayoutGetWidth(root_child1_child0) == 50
    assert YGNodeLayoutGetHeight(root_child1_child0) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 45
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == -10
    assert YGNodeLayoutGetTop(root_child1) == 44
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child1_child0) == -1
    assert YGNodeLayoutGetTop(root_child1_child0) == 1
    assert YGNodeLayoutGetWidth(root_child1_child0) == 50
    assert YGNodeLayoutGetHeight(root_child1_child0) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_baseline_child_padding():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeAll, 5)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignBaseline)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 20)
    YGNodeStyleSetPadding(root_child1, YGEdge.YGEdgeAll, 5)
    YGNodeInsertChild(root, root_child1, 1)

    root_child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1_child0, 50)
    YGNodeStyleSetHeight(root_child1_child0, 10)
    YGNodeInsertChild(root_child1, root_child1_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 5
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 55
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child1_child0) == 5
    assert YGNodeLayoutGetTop(root_child1_child0) == 5
    assert YGNodeLayoutGetWidth(root_child1_child0) == 50
    assert YGNodeLayoutGetHeight(root_child1_child0) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 45
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == -5
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child1_child0) == -5
    assert YGNodeLayoutGetTop(root_child1_child0) == 5
    assert YGNodeLayoutGetWidth(root_child1_child0) == 50
    assert YGNodeLayoutGetHeight(root_child1_child0) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_baseline_multiline():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignBaseline)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 20)
    YGNodeInsertChild(root, root_child1, 1)

    root_child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1_child0, 50)
    YGNodeStyleSetHeight(root_child1_child0, 10)
    YGNodeInsertChild(root_child1, root_child1_child0, 0)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 50)
    YGNodeStyleSetHeight(root_child2, 20)
    YGNodeInsertChild(root, root_child2, 2)

    root_child2_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2_child0, 50)
    YGNodeStyleSetHeight(root_child2_child0, 10)
    YGNodeInsertChild(root_child2, root_child2_child0, 0)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 50)
    YGNodeStyleSetHeight(root_child3, 50)
    YGNodeInsertChild(root, root_child3, 3)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child1_child0) == 0
    assert YGNodeLayoutGetTop(root_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child1_child0) == 50
    assert YGNodeLayoutGetHeight(root_child1_child0) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 100
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 20

    assert YGNodeLayoutGetLeft(root_child2_child0) == 0
    assert YGNodeLayoutGetTop(root_child2_child0) == 0
    assert YGNodeLayoutGetWidth(root_child2_child0) == 50
    assert YGNodeLayoutGetHeight(root_child2_child0) == 10

    assert YGNodeLayoutGetLeft(root_child3) == 50
    assert YGNodeLayoutGetTop(root_child3) == 60
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child1_child0) == 0
    assert YGNodeLayoutGetTop(root_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child1_child0) == 50
    assert YGNodeLayoutGetHeight(root_child1_child0) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 50
    assert YGNodeLayoutGetTop(root_child2) == 100
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 20

    assert YGNodeLayoutGetLeft(root_child2_child0) == 0
    assert YGNodeLayoutGetTop(root_child2_child0) == 0
    assert YGNodeLayoutGetWidth(root_child2_child0) == 50
    assert YGNodeLayoutGetHeight(root_child2_child0) == 10

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 60
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_baseline_multiline_column():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignBaseline)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 30)
    YGNodeStyleSetHeight(root_child1, 50)
    YGNodeInsertChild(root, root_child1, 1)

    root_child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1_child0, 20)
    YGNodeStyleSetHeight(root_child1_child0, 20)
    YGNodeInsertChild(root_child1, root_child1_child0, 0)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 40)
    YGNodeStyleSetHeight(root_child2, 70)
    YGNodeInsertChild(root, root_child2, 2)

    root_child2_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2_child0, 10)
    YGNodeStyleSetHeight(root_child2_child0, 10)
    YGNodeInsertChild(root_child2, root_child2_child0, 0)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 50)
    YGNodeStyleSetHeight(root_child3, 20)
    YGNodeInsertChild(root, root_child3, 3)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 50
    assert YGNodeLayoutGetWidth(root_child1) == 30
    assert YGNodeLayoutGetHeight(root_child1) == 50

    assert YGNodeLayoutGetLeft(root_child1_child0) == 0
    assert YGNodeLayoutGetTop(root_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child1_child0) == 20
    assert YGNodeLayoutGetHeight(root_child1_child0) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 50
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 40
    assert YGNodeLayoutGetHeight(root_child2) == 70

    assert YGNodeLayoutGetLeft(root_child2_child0) == 0
    assert YGNodeLayoutGetTop(root_child2_child0) == 0
    assert YGNodeLayoutGetWidth(root_child2_child0) == 10
    assert YGNodeLayoutGetHeight(root_child2_child0) == 10

    assert YGNodeLayoutGetLeft(root_child3) == 50
    assert YGNodeLayoutGetTop(root_child3) == 70
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 50
    assert YGNodeLayoutGetWidth(root_child1) == 30
    assert YGNodeLayoutGetHeight(root_child1) == 50

    assert YGNodeLayoutGetLeft(root_child1_child0) == 10
    assert YGNodeLayoutGetTop(root_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child1_child0) == 20
    assert YGNodeLayoutGetHeight(root_child1_child0) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 40
    assert YGNodeLayoutGetHeight(root_child2) == 70

    assert YGNodeLayoutGetLeft(root_child2_child0) == 30
    assert YGNodeLayoutGetTop(root_child2_child0) == 0
    assert YGNodeLayoutGetWidth(root_child2_child0) == 10
    assert YGNodeLayoutGetHeight(root_child2_child0) == 10

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 70
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_baseline_multiline_column2():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignBaseline)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 30)
    YGNodeStyleSetHeight(root_child1, 50)
    YGNodeInsertChild(root, root_child1, 1)

    root_child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1_child0, 20)
    YGNodeStyleSetHeight(root_child1_child0, 20)
    YGNodeInsertChild(root_child1, root_child1_child0, 0)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 40)
    YGNodeStyleSetHeight(root_child2, 70)
    YGNodeInsertChild(root, root_child2, 2)

    root_child2_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2_child0, 10)
    YGNodeStyleSetHeight(root_child2_child0, 10)
    YGNodeInsertChild(root_child2, root_child2_child0, 0)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 50)
    YGNodeStyleSetHeight(root_child3, 20)
    YGNodeInsertChild(root, root_child3, 3)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 50
    assert YGNodeLayoutGetWidth(root_child1) == 30
    assert YGNodeLayoutGetHeight(root_child1) == 50

    assert YGNodeLayoutGetLeft(root_child1_child0) == 0
    assert YGNodeLayoutGetTop(root_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child1_child0) == 20
    assert YGNodeLayoutGetHeight(root_child1_child0) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 50
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 40
    assert YGNodeLayoutGetHeight(root_child2) == 70

    assert YGNodeLayoutGetLeft(root_child2_child0) == 0
    assert YGNodeLayoutGetTop(root_child2_child0) == 0
    assert YGNodeLayoutGetWidth(root_child2_child0) == 10
    assert YGNodeLayoutGetHeight(root_child2_child0) == 10

    assert YGNodeLayoutGetLeft(root_child3) == 50
    assert YGNodeLayoutGetTop(root_child3) == 70
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 50
    assert YGNodeLayoutGetWidth(root_child1) == 30
    assert YGNodeLayoutGetHeight(root_child1) == 50

    assert YGNodeLayoutGetLeft(root_child1_child0) == 10
    assert YGNodeLayoutGetTop(root_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child1_child0) == 20
    assert YGNodeLayoutGetHeight(root_child1_child0) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 40
    assert YGNodeLayoutGetHeight(root_child2) == 70

    assert YGNodeLayoutGetLeft(root_child2_child0) == 30
    assert YGNodeLayoutGetTop(root_child2_child0) == 0
    assert YGNodeLayoutGetWidth(root_child2_child0) == 10
    assert YGNodeLayoutGetHeight(root_child2_child0) == 10

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 70
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_baseline_multiline_row_and_column():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignBaseline)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 50)
    YGNodeInsertChild(root, root_child1, 1)

    root_child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1_child0, 50)
    YGNodeStyleSetHeight(root_child1_child0, 10)
    YGNodeInsertChild(root_child1, root_child1_child0, 0)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 50)
    YGNodeStyleSetHeight(root_child2, 20)
    YGNodeInsertChild(root, root_child2, 2)

    root_child2_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2_child0, 50)
    YGNodeStyleSetHeight(root_child2_child0, 10)
    YGNodeInsertChild(root_child2, root_child2_child0, 0)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 50)
    YGNodeStyleSetHeight(root_child3, 20)
    YGNodeInsertChild(root, root_child3, 3)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 50

    assert YGNodeLayoutGetLeft(root_child1_child0) == 0
    assert YGNodeLayoutGetTop(root_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child1_child0) == 50
    assert YGNodeLayoutGetHeight(root_child1_child0) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 100
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 20

    assert YGNodeLayoutGetLeft(root_child2_child0) == 0
    assert YGNodeLayoutGetTop(root_child2_child0) == 0
    assert YGNodeLayoutGetWidth(root_child2_child0) == 50
    assert YGNodeLayoutGetHeight(root_child2_child0) == 10

    assert YGNodeLayoutGetLeft(root_child3) == 50
    assert YGNodeLayoutGetTop(root_child3) == 90
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 50

    assert YGNodeLayoutGetLeft(root_child1_child0) == 0
    assert YGNodeLayoutGetTop(root_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child1_child0) == 50
    assert YGNodeLayoutGetHeight(root_child1_child0) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 50
    assert YGNodeLayoutGetTop(root_child2) == 100
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 20

    assert YGNodeLayoutGetLeft(root_child2_child0) == 0
    assert YGNodeLayoutGetTop(root_child2_child0) == 0
    assert YGNodeLayoutGetWidth(root_child2_child0) == 50
    assert YGNodeLayoutGetHeight(root_child2_child0) == 10

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 90
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_items_center_child_with_margin_bigger_than_parent():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 52)
    YGNodeStyleSetWidth(root, 52)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyCenter)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetAlignItems(root_child0, YGAlign.YGAlignCenter)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 52)
    YGNodeStyleSetHeight(root_child0_child0, 52)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeLeft, 10)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeRight, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 52
    assert YGNodeLayoutGetHeight(root) == 52

    assert YGNodeLayoutGetLeft(root_child0) == -10
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 72
    assert YGNodeLayoutGetHeight(root_child0) == 52

    assert YGNodeLayoutGetLeft(root_child0_child0) == 10
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 52
    assert YGNodeLayoutGetHeight(root_child0_child0) == 52

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 52
    assert YGNodeLayoutGetHeight(root) == 52

    assert YGNodeLayoutGetLeft(root_child0) == -10
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 72
    assert YGNodeLayoutGetHeight(root_child0) == 52

    assert YGNodeLayoutGetLeft(root_child0_child0) == 10
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 52
    assert YGNodeLayoutGetHeight(root_child0_child0) == 52

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_items_flex_end_child_with_margin_bigger_than_parent():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 52)
    YGNodeStyleSetWidth(root, 52)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyCenter)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetAlignItems(root_child0, YGAlign.YGAlignFlexEnd)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 52)
    YGNodeStyleSetHeight(root_child0_child0, 52)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeLeft, 10)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeRight, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 52
    assert YGNodeLayoutGetHeight(root) == 52

    assert YGNodeLayoutGetLeft(root_child0) == -10
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 72
    assert YGNodeLayoutGetHeight(root_child0) == 52

    assert YGNodeLayoutGetLeft(root_child0_child0) == 10
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 52
    assert YGNodeLayoutGetHeight(root_child0_child0) == 52

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 52
    assert YGNodeLayoutGetHeight(root) == 52

    assert YGNodeLayoutGetLeft(root_child0) == -10
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 72
    assert YGNodeLayoutGetHeight(root_child0) == 52

    assert YGNodeLayoutGetLeft(root_child0_child0) == 10
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 52
    assert YGNodeLayoutGetHeight(root_child0_child0) == 52

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_items_center_child_without_margin_bigger_than_parent():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 52)
    YGNodeStyleSetWidth(root, 52)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyCenter)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetAlignItems(root_child0, YGAlign.YGAlignCenter)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 72)
    YGNodeStyleSetHeight(root_child0_child0, 72)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 52
    assert YGNodeLayoutGetHeight(root) == 52

    assert YGNodeLayoutGetLeft(root_child0) == -10
    assert YGNodeLayoutGetTop(root_child0) == -10
    assert YGNodeLayoutGetWidth(root_child0) == 72
    assert YGNodeLayoutGetHeight(root_child0) == 72

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 72
    assert YGNodeLayoutGetHeight(root_child0_child0) == 72

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 52
    assert YGNodeLayoutGetHeight(root) == 52

    assert YGNodeLayoutGetLeft(root_child0) == -10
    assert YGNodeLayoutGetTop(root_child0) == -10
    assert YGNodeLayoutGetWidth(root_child0) == 72
    assert YGNodeLayoutGetHeight(root_child0) == 72

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 72
    assert YGNodeLayoutGetHeight(root_child0_child0) == 72

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_items_flex_end_child_without_margin_bigger_than_parent():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 52)
    YGNodeStyleSetWidth(root, 52)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyCenter)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetAlignItems(root_child0, YGAlign.YGAlignFlexEnd)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 72)
    YGNodeStyleSetHeight(root_child0_child0, 72)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 52
    assert YGNodeLayoutGetHeight(root) == 52

    assert YGNodeLayoutGetLeft(root_child0) == -10
    assert YGNodeLayoutGetTop(root_child0) == -10
    assert YGNodeLayoutGetWidth(root_child0) == 72
    assert YGNodeLayoutGetHeight(root_child0) == 72

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 72
    assert YGNodeLayoutGetHeight(root_child0_child0) == 72

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 52
    assert YGNodeLayoutGetHeight(root) == 52

    assert YGNodeLayoutGetLeft(root_child0) == -10
    assert YGNodeLayoutGetTop(root_child0) == -10
    assert YGNodeLayoutGetWidth(root_child0) == 72
    assert YGNodeLayoutGetHeight(root_child0) == 72

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 72
    assert YGNodeLayoutGetHeight(root_child0_child0) == 72

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_center_should_size_based_on_content():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)
    YGNodeStyleSetMargin(root, YGEdge.YGEdgeTop, 20)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexShrink(root_child0, 1)
    YGNodeStyleSetJustifyContent(root_child0, YGJustify.YGJustifyCenter)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0_child0, 1)
    YGNodeStyleSetFlexShrink(root_child0_child0, 1)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0_child0, 20)
    YGNodeStyleSetHeight(root_child0_child0_child0, 20)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 20
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 40
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 20
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 40
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_stretch_should_size_based_on_parent():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetMargin(root, YGEdge.YGEdgeTop, 20)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexShrink(root_child0, 1)
    YGNodeStyleSetJustifyContent(root_child0, YGJustify.YGJustifyCenter)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0_child0, 1)
    YGNodeStyleSetFlexShrink(root_child0_child0, 1)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0_child0, 20)
    YGNodeStyleSetHeight(root_child0_child0_child0, 20)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 20
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 20
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 80
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_flex_start_with_shrinking_children():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 500)
    YGNodeStyleSetWidth(root, 500)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetAlignItems(root_child0, YGAlign.YGAlignFlexStart)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0_child0, 1)
    YGNodeStyleSetFlexShrink(root_child0_child0, 1)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0_child0_child0, 1)
    YGNodeStyleSetFlexShrink(root_child0_child0_child0, 1)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 500

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 500
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0_child0) == 0

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 500

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 500
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child0_child0) == 500
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0_child0) == 0

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 0

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_flex_start_with_stretching_children():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 500)
    YGNodeStyleSetWidth(root, 500)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0_child0, 1)
    YGNodeStyleSetFlexShrink(root_child0_child0, 1)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0_child0_child0, 1)
    YGNodeStyleSetFlexShrink(root_child0_child0_child0, 1)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 500

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 500
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 500
    assert YGNodeLayoutGetHeight(root_child0_child0) == 0

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 500
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 500

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 500
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 500
    assert YGNodeLayoutGetHeight(root_child0_child0) == 0

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 500
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 0

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_flex_start_with_shrinking_children_with_stretch():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 500)
    YGNodeStyleSetWidth(root, 500)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetAlignItems(root_child0, YGAlign.YGAlignFlexStart)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0_child0, 1)
    YGNodeStyleSetFlexShrink(root_child0_child0, 1)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0_child0_child0, 1)
    YGNodeStyleSetFlexShrink(root_child0_child0_child0, 1)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 500

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 500
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0_child0) == 0

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 500

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 500
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child0_child0) == 500
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0_child0) == 0

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 0

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_flex_end_with_row_reverse():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 75)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexEnd)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeLeft, 3)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 50)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 75

    assert YGNodeLayoutGetLeft(root_child0) == 3
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 58
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 75

    assert YGNodeLayoutGetLeft(root_child0) == 45
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == -8
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_stretch_with_row_reverse():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 75)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeLeft, 3)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 50)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 75

    assert YGNodeLayoutGetLeft(root_child0) == 3
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 58
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 75

    assert YGNodeLayoutGetLeft(root_child0) == 45
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == -8
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_items_non_stretch_s526008():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 400)
    YGNodeStyleSetHeight(root, 400)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetAlignItems(root_child0_child0, YGAlign.YGAlignFlexStart)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)

    root_child0_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0_child0_child0, 0)
    YGNodeStyleSetHeight(root_child0_child0_child0_child0, 10)
    YGNodeInsertChild(root_child0_child0_child0, root_child0_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 400
    assert YGNodeLayoutGetHeight(root) == 400

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0_child0_child0_child0) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 400
    assert YGNodeLayoutGetHeight(root) == 400

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 400
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0_child0_child0_child0) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

