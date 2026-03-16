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


def test_wrap_child():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    child = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child, 100)
    YGNodeStyleSetHeight(child, 100)
    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100
    assert YGNodeLayoutGetLeft(child) == 0
    assert YGNodeLayoutGetTop(child) == 0
    assert YGNodeLayoutGetWidth(child) == 100
    assert YGNodeLayoutGetHeight(child) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100
    assert YGNodeLayoutGetLeft(child) == 0
    assert YGNodeLayoutGetTop(child) == 0
    assert YGNodeLayoutGetWidth(child) == 100
    assert YGNodeLayoutGetHeight(child) == 100

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_wrap_grandchild():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    child = YGNodeNewWithConfig(config)
    YGNodeInsertChild(root, child, 0)

    grandchild = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(grandchild, 100)
    YGNodeStyleSetHeight(grandchild, 100)
    YGNodeInsertChild(child, grandchild, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100
    assert YGNodeLayoutGetLeft(child) == 0
    assert YGNodeLayoutGetTop(child) == 0
    assert YGNodeLayoutGetWidth(child) == 100
    assert YGNodeLayoutGetHeight(child) == 100
    assert YGNodeLayoutGetLeft(grandchild) == 0
    assert YGNodeLayoutGetTop(grandchild) == 0
    assert YGNodeLayoutGetWidth(grandchild) == 100
    assert YGNodeLayoutGetHeight(grandchild) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100
    assert YGNodeLayoutGetLeft(child) == 0
    assert YGNodeLayoutGetTop(child) == 0
    assert YGNodeLayoutGetWidth(child) == 100
    assert YGNodeLayoutGetHeight(child) == 100
    assert YGNodeLayoutGetLeft(grandchild) == 0
    assert YGNodeLayoutGetTop(grandchild) == 0
    assert YGNodeLayoutGetWidth(grandchild) == 100
    assert YGNodeLayoutGetHeight(grandchild) == 100

    YGNodeFreeRecursive(root)
    YGConfigFree(config)
