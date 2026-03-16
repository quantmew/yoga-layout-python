import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from yoga import (  # noqa: E402
    YGConfigFree,
    YGConfigNew,
    YGDirection,
    YGNodeCalculateLayout,
    YGNodeFreeRecursive,
    YGNodeInsertChild,
    YGNodeLayoutGetHeight,
    YGNodeLayoutGetLeft,
    YGNodeLayoutGetTop,
    YGNodeLayoutGetWidth,
    YGNodeNewWithConfig,
    YGNodeStyleSetHeight,
    YGNodeStyleSetPositionType,
    YGNodeStyleSetWidth,
    YGPositionType,
)


def test_nested_overflowing_child():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    child = YGNodeNewWithConfig(config)
    YGNodeInsertChild(root, child, 0)

    grandchild = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(grandchild, 200)
    YGNodeStyleSetWidth(grandchild, 200)
    YGNodeInsertChild(child, grandchild, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100
    assert YGNodeLayoutGetLeft(child) == 0
    assert YGNodeLayoutGetTop(child) == 0
    assert YGNodeLayoutGetWidth(child) == 100
    assert YGNodeLayoutGetHeight(child) == 200
    assert YGNodeLayoutGetLeft(grandchild) == 0
    assert YGNodeLayoutGetTop(grandchild) == 0
    assert YGNodeLayoutGetWidth(grandchild) == 200
    assert YGNodeLayoutGetHeight(grandchild) == 200

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetLeft(child) == 0
    assert YGNodeLayoutGetTop(child) == 0
    assert YGNodeLayoutGetWidth(child) == 100
    assert YGNodeLayoutGetHeight(child) == 200
    assert YGNodeLayoutGetLeft(grandchild) == -100
    assert YGNodeLayoutGetTop(grandchild) == 0
    assert YGNodeLayoutGetWidth(grandchild) == 200
    assert YGNodeLayoutGetHeight(grandchild) == 200

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_nested_overflowing_child_in_constraint_parent():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    child = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(child, 100)
    YGNodeStyleSetWidth(child, 100)
    YGNodeInsertChild(root, child, 0)

    grandchild = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(grandchild, 200)
    YGNodeStyleSetWidth(grandchild, 200)
    YGNodeInsertChild(child, grandchild, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetWidth(child) == 100
    assert YGNodeLayoutGetHeight(child) == 100
    assert YGNodeLayoutGetLeft(grandchild) == 0
    assert YGNodeLayoutGetTop(grandchild) == 0
    assert YGNodeLayoutGetWidth(grandchild) == 200
    assert YGNodeLayoutGetHeight(grandchild) == 200

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetLeft(grandchild) == -100
    assert YGNodeLayoutGetTop(grandchild) == 0
    assert YGNodeLayoutGetWidth(grandchild) == 200
    assert YGNodeLayoutGetHeight(grandchild) == 200

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_parent_wrap_child_size_overflowing_parent():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    child = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child, 100)
    YGNodeInsertChild(root, child, 0)

    grandchild = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(grandchild, 100)
    YGNodeStyleSetHeight(grandchild, 200)
    YGNodeInsertChild(child, grandchild, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetWidth(child) == 100
    assert YGNodeLayoutGetHeight(child) == 200
    assert YGNodeLayoutGetLeft(grandchild) == 0
    assert YGNodeLayoutGetTop(grandchild) == 0
    assert YGNodeLayoutGetWidth(grandchild) == 100
    assert YGNodeLayoutGetHeight(grandchild) == 200

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetWidth(child) == 100
    assert YGNodeLayoutGetHeight(child) == 200
    assert YGNodeLayoutGetLeft(grandchild) == 0
    assert YGNodeLayoutGetTop(grandchild) == 0
    assert YGNodeLayoutGetWidth(grandchild) == 100
    assert YGNodeLayoutGetHeight(grandchild) == 200

    YGNodeFreeRecursive(root)
    YGConfigFree(config)
