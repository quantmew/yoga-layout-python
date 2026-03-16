import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import (  # noqa: E402
    YGAlign,
    YGConfigFree,
    YGConfigNew,
    YGDirection,
    YGFlexDirection,
    YGNodeCalculateLayout,
    YGNodeFreeRecursive,
    YGNodeInsertChild,
    YGNodeLayoutGetHeight,
    YGNodeLayoutGetLeft,
    YGNodeLayoutGetTop,
    YGNodeLayoutGetWidth,
    YGNodeNewWithConfig,
    YGNodeStyleSetAlignItems,
    YGNodeStyleSetFlexDirection,
    YGNodeStyleSetHeight,
    YGNodeStyleSetPositionType,
    YGNodeStyleSetWidth,
    YGPositionType,
)


def test_align_items_stretch():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    child = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(child, 10)
    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetLeft(child) == 0
    assert YGNodeLayoutGetTop(child) == 0
    assert YGNodeLayoutGetWidth(child) == 100
    assert YGNodeLayoutGetHeight(child) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetLeft(child) == 0
    assert YGNodeLayoutGetTop(child) == 0
    assert YGNodeLayoutGetWidth(child) == 100
    assert YGNodeLayoutGetHeight(child) == 10

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_align_items_center():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)

    child = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(child, 10)
    YGNodeStyleSetWidth(child, 10)
    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetLeft(child) == 45
    assert YGNodeLayoutGetTop(child) == 0
    assert YGNodeLayoutGetWidth(child) == 10
    assert YGNodeLayoutGetHeight(child) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetLeft(child) == 45
    assert YGNodeLayoutGetTop(child) == 0
    assert YGNodeLayoutGetWidth(child) == 10
    assert YGNodeLayoutGetHeight(child) == 10

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_align_items_flex_start():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)

    child = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(child, 10)
    YGNodeStyleSetWidth(child, 10)
    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetLeft(child) == 0
    assert YGNodeLayoutGetTop(child) == 0
    assert YGNodeLayoutGetWidth(child) == 10
    assert YGNodeLayoutGetHeight(child) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetLeft(child) == 90
    assert YGNodeLayoutGetTop(child) == 0
    assert YGNodeLayoutGetWidth(child) == 10
    assert YGNodeLayoutGetHeight(child) == 10

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_align_items_flex_end():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexEnd)

    child = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(child, 10)
    YGNodeStyleSetWidth(child, 10)
    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetLeft(child) == 90
    assert YGNodeLayoutGetTop(child) == 0
    assert YGNodeLayoutGetWidth(child) == 10
    assert YGNodeLayoutGetHeight(child) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetLeft(child) == 0
    assert YGNodeLayoutGetTop(child) == 0
    assert YGNodeLayoutGetWidth(child) == 10
    assert YGNodeLayoutGetHeight(child) == 10

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

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child0, 50)
    YGNodeStyleSetHeight(child0, 50)
    YGNodeInsertChild(root, child0, 0)

    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child1, 50)
    YGNodeStyleSetHeight(child1, 20)
    YGNodeInsertChild(root, child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetLeft(child0) == 0
    assert YGNodeLayoutGetTop(child0) == 0
    assert YGNodeLayoutGetWidth(child0) == 50
    assert YGNodeLayoutGetHeight(child0) == 50
    assert YGNodeLayoutGetLeft(child1) == 50
    assert YGNodeLayoutGetTop(child1) == 30
    assert YGNodeLayoutGetWidth(child1) == 50
    assert YGNodeLayoutGetHeight(child1) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetLeft(child0) == 50
    assert YGNodeLayoutGetTop(child0) == 0
    assert YGNodeLayoutGetWidth(child0) == 50
    assert YGNodeLayoutGetHeight(child0) == 50
    assert YGNodeLayoutGetLeft(child1) == 0
    assert YGNodeLayoutGetTop(child1) == 30
    assert YGNodeLayoutGetWidth(child1) == 50
    assert YGNodeLayoutGetHeight(child1) == 20

    YGNodeFreeRecursive(root)
    YGConfigFree(config)
