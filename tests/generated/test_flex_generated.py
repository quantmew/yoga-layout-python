import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from yoga import (  # noqa: E402
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
    YGNodeStyleSetFlexBasis,
    YGNodeStyleSetFlexGrow,
    YGNodeStyleSetFlexShrink,
    YGNodeStyleSetFlexDirection,
    YGNodeStyleSetHeight,
    YGNodeStyleSetPositionType,
    YGNodeStyleSetWidth,
    YGPositionType,
)


def _assert_layout(node, left, top, width, height):
    assert YGNodeLayoutGetLeft(node) == left
    assert YGNodeLayoutGetTop(node) == top
    assert YGNodeLayoutGetWidth(node) == width
    assert YGNodeLayoutGetHeight(node) == height


def test_flex_basis_flex_grow_column():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexBasis(child0, 50)
    YGNodeStyleSetFlexGrow(child0, 1)
    YGNodeInsertChild(root, child0, 0)

    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child1, 1)
    YGNodeInsertChild(root, child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 100, 100)
    _assert_layout(child0, 0, 0, 100, 75)
    _assert_layout(child1, 0, 75, 100, 25)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 100, 100)
    _assert_layout(child0, 0, 0, 100, 75)
    _assert_layout(child1, 0, 75, 100, 25)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_flex_shrink_flex_grow_row():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 500)
    YGNodeStyleSetHeight(root, 500)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child0, 500)
    YGNodeStyleSetHeight(child0, 100)
    YGNodeStyleSetFlexShrink(child0, 1)
    YGNodeInsertChild(root, child0, 0)

    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child1, 500)
    YGNodeStyleSetHeight(child1, 100)
    YGNodeStyleSetFlexShrink(child1, 1)
    YGNodeInsertChild(root, child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 500, 500)
    _assert_layout(child0, 0, 0, 250, 100)
    _assert_layout(child1, 250, 0, 250, 100)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 500, 500)
    _assert_layout(child0, 250, 0, 250, 100)
    _assert_layout(child1, 0, 0, 250, 100)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_flex_shrink_flex_grow_child_flex_shrink_other_child():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 500)
    YGNodeStyleSetHeight(root, 500)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child0, 500)
    YGNodeStyleSetHeight(child0, 100)
    YGNodeStyleSetFlexShrink(child0, 1)
    YGNodeInsertChild(root, child0, 0)

    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child1, 500)
    YGNodeStyleSetHeight(child1, 100)
    YGNodeStyleSetFlexGrow(child1, 1)
    YGNodeStyleSetFlexShrink(child1, 1)
    YGNodeInsertChild(root, child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 500, 500)
    _assert_layout(child0, 0, 0, 250, 100)
    _assert_layout(child1, 250, 0, 250, 100)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 500, 500)
    _assert_layout(child0, 250, 0, 250, 100)
    _assert_layout(child1, 0, 0, 250, 100)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_flex_basis_flex_grow_row():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexBasis(child0, 50)
    YGNodeStyleSetFlexGrow(child0, 1)
    YGNodeInsertChild(root, child0, 0)

    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child1, 1)
    YGNodeInsertChild(root, child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 100, 100)
    _assert_layout(child0, 0, 0, 75, 100)
    _assert_layout(child1, 75, 0, 25, 100)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 100, 100)
    _assert_layout(child0, 25, 0, 75, 100)
    _assert_layout(child1, 0, 0, 25, 100)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_flex_basis_flex_shrink_column():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexBasis(child0, 100)
    YGNodeStyleSetFlexShrink(child0, 1)
    YGNodeInsertChild(root, child0, 0)

    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexBasis(child1, 50)
    YGNodeInsertChild(root, child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 100, 100)
    _assert_layout(child0, 0, 0, 100, 50)
    _assert_layout(child1, 0, 50, 100, 50)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 100, 100)
    _assert_layout(child0, 0, 0, 100, 50)
    _assert_layout(child1, 0, 50, 100, 50)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_flex_basis_flex_shrink_row():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexBasis(child0, 100)
    YGNodeStyleSetFlexShrink(child0, 1)
    YGNodeInsertChild(root, child0, 0)

    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexBasis(child1, 50)
    YGNodeInsertChild(root, child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 100, 100)
    _assert_layout(child0, 0, 0, 50, 100)
    _assert_layout(child1, 50, 0, 50, 100)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 100, 100)
    _assert_layout(child0, 50, 0, 50, 100)
    _assert_layout(child1, 0, 0, 50, 100)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_flex_shrink_to_zero():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 75)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child0, 50)
    YGNodeStyleSetHeight(child0, 50)
    YGNodeInsertChild(root, child0, 0)

    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child1, 50)
    YGNodeStyleSetHeight(child1, 50)
    YGNodeStyleSetFlexShrink(child1, 1)
    YGNodeInsertChild(root, child1, 1)

    child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child2, 50)
    YGNodeStyleSetHeight(child2, 50)
    YGNodeInsertChild(root, child2, 2)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 50, 75)
    _assert_layout(child0, 0, 0, 50, 50)
    _assert_layout(child1, 0, 50, 50, 0)
    _assert_layout(child2, 0, 50, 50, 50)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 50, 75)
    _assert_layout(child0, 0, 0, 50, 50)
    _assert_layout(child1, 0, 50, 50, 0)
    _assert_layout(child2, 0, 50, 50, 50)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_flex_basis_overrides_main_size():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(child0, 20)
    YGNodeStyleSetFlexGrow(child0, 1)
    YGNodeStyleSetFlexBasis(child0, 50)
    YGNodeInsertChild(root, child0, 0)

    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(child1, 10)
    YGNodeStyleSetFlexGrow(child1, 1)
    YGNodeInsertChild(root, child1, 1)

    child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(child2, 10)
    YGNodeStyleSetFlexGrow(child2, 1)
    YGNodeInsertChild(root, child2, 2)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 100, 100)
    _assert_layout(child0, 0, 0, 100, 60)
    _assert_layout(child1, 0, 60, 100, 20)
    _assert_layout(child2, 0, 80, 100, 20)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 100, 100)
    _assert_layout(child0, 0, 0, 100, 60)
    _assert_layout(child1, 0, 60, 100, 20)
    _assert_layout(child2, 0, 80, 100, 20)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_flex_grow_shrink_at_most():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    child0 = YGNodeNewWithConfig(config)
    YGNodeInsertChild(root, child0, 0)

    grandchild0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(grandchild0, 1)
    YGNodeStyleSetFlexShrink(grandchild0, 1)
    YGNodeInsertChild(child0, grandchild0, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 100, 100)
    _assert_layout(child0, 0, 0, 100, 0)
    _assert_layout(grandchild0, 0, 0, 100, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 100, 100)
    _assert_layout(child0, 0, 0, 100, 0)
    _assert_layout(grandchild0, 0, 0, 100, 0)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_flex_grow_less_than_factor_one():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 500)
    YGNodeStyleSetWidth(root, 200)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child0, 0.2)
    YGNodeStyleSetFlexBasis(child0, 40)
    YGNodeInsertChild(root, child0, 0)

    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child1, 0.2)
    YGNodeInsertChild(root, child1, 1)

    child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child2, 0.4)
    YGNodeInsertChild(root, child2, 2)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 200, 500)
    _assert_layout(child0, 0, 0, 200, 132)
    _assert_layout(child1, 0, 132, 200, 92)
    _assert_layout(child2, 0, 224, 200, 184)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 200, 500)
    _assert_layout(child0, 0, 0, 200, 132)
    _assert_layout(child1, 0, 132, 200, 92)
    _assert_layout(child2, 0, 224, 200, 184)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)
