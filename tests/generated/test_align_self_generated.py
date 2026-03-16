import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

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
    YGNodeStyleSetAlignSelf,
    YGNodeStyleSetFlexDirection,
    YGNodeStyleSetHeight,
    YGNodeStyleSetPositionType,
    YGNodeStyleSetWidth,
    YGPositionType,
)


def test_align_self_center():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(child, 10)
    YGNodeStyleSetWidth(child, 10)
    YGNodeStyleSetAlignSelf(child, YGAlign.YGAlignCenter)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetLeft(child) == 45
    assert YGNodeLayoutGetTop(child) == 0
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetLeft(child) == 45
    assert YGNodeLayoutGetTop(child) == 0
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_align_self_flex_end():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(child, 10)
    YGNodeStyleSetWidth(child, 10)
    YGNodeStyleSetAlignSelf(child, YGAlign.YGAlignFlexEnd)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetLeft(child) == 90
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetLeft(child) == 0
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_align_self_flex_start():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(child, 10)
    YGNodeStyleSetWidth(child, 10)
    YGNodeStyleSetAlignSelf(child, YGAlign.YGAlignFlexStart)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetLeft(child) == 0
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetLeft(child) == 90
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_align_self_flex_end_override_flex_start():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    child = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(child, 10)
    YGNodeStyleSetWidth(child, 10)
    YGNodeStyleSetAlignSelf(child, YGAlign.YGAlignFlexEnd)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetLeft(child) == 90
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetLeft(child) == 0
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_align_self_baseline():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child0, 50)
    YGNodeStyleSetHeight(child0, 50)
    YGNodeStyleSetAlignSelf(child0, YGAlign.YGAlignBaseline)
    YGNodeInsertChild(root, child0, 0)

    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child1, 50)
    YGNodeStyleSetHeight(child1, 20)
    YGNodeStyleSetAlignSelf(child1, YGAlign.YGAlignBaseline)
    YGNodeInsertChild(root, child1, 1)

    grandchild = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(grandchild, 50)
    YGNodeStyleSetHeight(grandchild, 10)
    YGNodeInsertChild(child1, grandchild, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetLeft(child0) == 0
    assert YGNodeLayoutGetTop(child0) == 0
    assert YGNodeLayoutGetLeft(child1) == 50
    assert YGNodeLayoutGetTop(child1) == 40
    assert YGNodeLayoutGetLeft(grandchild) == 0
    assert YGNodeLayoutGetTop(grandchild) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetLeft(child0) == 50
    assert YGNodeLayoutGetTop(child0) == 0
    assert YGNodeLayoutGetLeft(child1) == 0
    assert YGNodeLayoutGetTop(child1) == 40
    assert YGNodeLayoutGetLeft(grandchild) == 0
    assert YGNodeLayoutGetTop(grandchild) == 0

    YGNodeFreeRecursive(root)
    YGConfigFree(config)
