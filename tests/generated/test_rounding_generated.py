import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from yoga import (  # noqa: E402
    YGConfigFree,
    YGConfigNew,
    YGDirection,
    YGEdge,
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
    YGNodeStyleSetFlexDirection,
    YGNodeStyleSetFlexGrow,
    YGNodeStyleSetFlexShrink,
    YGNodeStyleSetHeight,
    YGNodeStyleSetHeightPercent,
    YGNodeStyleSetPosition,
    YGNodeStyleSetPositionType,
    YGNodeStyleSetWidth,
    YGNodeStyleSetWidthPercent,
    YGPositionType,
)


def _assert_layout(node, left, top, width, height):
    assert YGNodeLayoutGetLeft(node) == left
    assert YGNodeLayoutGetTop(node) == top
    assert YGNodeLayoutGetWidth(node) == width
    assert YGNodeLayoutGetHeight(node) == height


def test_rounding_flex_basis_flex_grow_row_width_of_100():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    children = []
    for i in range(3):
        child = YGNodeNewWithConfig(config)
        YGNodeStyleSetFlexGrow(child, 1)
        YGNodeInsertChild(root, child, i)
        children.append(child)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(children[0], 0, 0, 33, 100)
    _assert_layout(children[1], 33, 0, 34, 100)
    _assert_layout(children[2], 67, 0, 33, 100)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(children[0], 67, 0, 33, 100)
    _assert_layout(children[1], 33, 0, 34, 100)
    _assert_layout(children[2], 0, 0, 33, 100)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_rounding_flex_basis_flex_grow_row_prime_number_width():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 113)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    children = []
    for i in range(5):
        child = YGNodeNewWithConfig(config)
        YGNodeStyleSetFlexGrow(child, 1)
        YGNodeInsertChild(root, child, i)
        children.append(child)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    expected = [(0, 0, 23, 100), (23, 0, 22, 100), (45, 0, 23, 100), (68, 0, 22, 100), (90, 0, 23, 100)]
    for child, values in zip(children, expected):
        _assert_layout(child, *values)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    expected = [(90, 0, 23, 100), (68, 0, 22, 100), (45, 0, 23, 100), (23, 0, 22, 100), (0, 0, 23, 100)]
    for child, values in zip(children, expected):
        _assert_layout(child, *values)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_rounding_flex_basis_flex_shrink_row():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 101)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexBasis(child0, 100)
    YGNodeStyleSetFlexShrink(child0, 1)
    YGNodeInsertChild(root, child0, 0)
    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexBasis(child1, 25)
    YGNodeInsertChild(root, child1, 1)
    child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexBasis(child2, 25)
    YGNodeInsertChild(root, child2, 2)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child0, 0, 0, 51, 100)
    _assert_layout(child1, 51, 0, 25, 100)
    _assert_layout(child2, 76, 0, 25, 100)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(child0, 50, 0, 51, 100)
    _assert_layout(child1, 25, 0, 25, 100)
    _assert_layout(child2, 0, 0, 25, 100)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_rounding_flex_basis_overrides_main_size():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 113)
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
    _assert_layout(child0, 0, 0, 100, 64)
    _assert_layout(child1, 0, 64, 100, 25)
    _assert_layout(child2, 0, 89, 100, 24)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(child0, 0, 0, 100, 64)
    _assert_layout(child1, 0, 64, 100, 25)
    _assert_layout(child2, 0, 89, 100, 24)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_rounding_total_fractial():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 113.4)
    YGNodeStyleSetWidth(root, 87.4)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(child0, 20.3)
    YGNodeStyleSetFlexGrow(child0, 0.7)
    YGNodeStyleSetFlexBasis(child0, 50.3)
    YGNodeInsertChild(root, child0, 0)
    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(child1, 10)
    YGNodeStyleSetFlexGrow(child1, 1.6)
    YGNodeInsertChild(root, child1, 1)
    child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(child2, 10.7)
    YGNodeStyleSetFlexGrow(child2, 1.1)
    YGNodeInsertChild(root, child2, 2)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 87, 113)
    _assert_layout(child0, 0, 0, 87, 59)
    _assert_layout(child1, 0, 59, 87, 30)
    _assert_layout(child2, 0, 89, 87, 24)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 87, 113)
    _assert_layout(child0, 0, 0, 87, 59)
    _assert_layout(child1, 0, 59, 87, 30)
    _assert_layout(child2, 0, 89, 87, 24)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_rounding_total_fractial_nested():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 113.4)
    YGNodeStyleSetWidth(root, 87.4)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(child0, 20.3)
    YGNodeStyleSetFlexGrow(child0, 0.7)
    YGNodeStyleSetFlexBasis(child0, 50.3)
    YGNodeInsertChild(root, child0, 0)

    child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPosition(child0_child0, YGEdge.YGEdgeBottom, 13.3)
    YGNodeStyleSetHeight(child0_child0, 9.9)
    YGNodeStyleSetFlexGrow(child0_child0, 1)
    YGNodeStyleSetFlexBasis(child0_child0, 0.3)
    YGNodeInsertChild(child0, child0_child0, 0)

    child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPosition(child0_child1, YGEdge.YGEdgeTop, 13.3)
    YGNodeStyleSetHeight(child0_child1, 1.1)
    YGNodeStyleSetFlexGrow(child0_child1, 4)
    YGNodeStyleSetFlexBasis(child0_child1, 0.3)
    YGNodeInsertChild(child0, child0_child1, 1)

    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(child1, 10)
    YGNodeStyleSetFlexGrow(child1, 1.6)
    YGNodeInsertChild(root, child1, 1)

    child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(child2, 10.7)
    YGNodeStyleSetFlexGrow(child2, 1.1)
    YGNodeInsertChild(root, child2, 2)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 87, 113)
    _assert_layout(child0, 0, 0, 87, 59)
    _assert_layout(child0_child0, 0, -13, 87, 12)
    _assert_layout(child0_child1, 0, 25, 87, 47)
    _assert_layout(child1, 0, 59, 87, 30)
    _assert_layout(child2, 0, 89, 87, 24)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 87, 113)
    _assert_layout(child0, 0, 0, 87, 59)
    _assert_layout(child0_child0, 0, -13, 87, 12)
    _assert_layout(child0_child1, 0, 25, 87, 47)
    _assert_layout(child1, 0, 59, 87, 30)
    _assert_layout(child2, 0, 89, 87, 24)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_rounding_fractial_input_1():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 113.4)
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
    _assert_layout(root, 0, 0, 100, 113)
    _assert_layout(child0, 0, 0, 100, 64)
    _assert_layout(child1, 0, 64, 100, 25)
    _assert_layout(child2, 0, 89, 100, 24)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 100, 113)
    _assert_layout(child0, 0, 0, 100, 64)
    _assert_layout(child1, 0, 64, 100, 25)
    _assert_layout(child2, 0, 89, 100, 24)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_rounding_fractial_input_2():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 113.6)
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
    _assert_layout(root, 0, 0, 100, 114)
    _assert_layout(child0, 0, 0, 100, 65)
    _assert_layout(child1, 0, 65, 100, 24)
    _assert_layout(child2, 0, 89, 100, 25)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 100, 114)
    _assert_layout(child0, 0, 0, 100, 65)
    _assert_layout(child1, 0, 65, 100, 24)
    _assert_layout(child2, 0, 89, 100, 25)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_rounding_fractial_input_3():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPosition(root, YGEdge.YGEdgeTop, 0.3)
    YGNodeStyleSetHeight(root, 113.4)
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
    _assert_layout(root, 0, 0, 100, 114)
    _assert_layout(child0, 0, 0, 100, 65)
    _assert_layout(child1, 0, 64, 100, 24)
    _assert_layout(child2, 0, 89, 100, 25)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 100, 114)
    _assert_layout(child0, 0, 0, 100, 65)
    _assert_layout(child1, 0, 64, 100, 24)
    _assert_layout(child2, 0, 89, 100, 25)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_rounding_fractial_input_4():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPosition(root, YGEdge.YGEdgeTop, 0.7)
    YGNodeStyleSetHeight(root, 113.4)
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
    _assert_layout(root, 0, 1, 100, 113)
    _assert_layout(child0, 0, 0, 100, 64)
    _assert_layout(child1, 0, 64, 100, 25)
    _assert_layout(child2, 0, 89, 100, 24)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 1, 100, 113)
    _assert_layout(child0, 0, 0, 100, 64)
    _assert_layout(child1, 0, 64, 100, 25)
    _assert_layout(child2, 0, 89, 100, 24)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_rounding_inner_node_controversy_horizontal():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 320)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(child0, 10)
    YGNodeStyleSetFlexGrow(child0, 1)
    YGNodeInsertChild(root, child0, 0)
    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(child1, 10)
    YGNodeStyleSetFlexGrow(child1, 1)
    YGNodeInsertChild(root, child1, 1)
    child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(child1_child0, 10)
    YGNodeStyleSetFlexGrow(child1_child0, 1)
    YGNodeInsertChild(child1, child1_child0, 0)
    child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(child2, 10)
    YGNodeStyleSetFlexGrow(child2, 1)
    YGNodeInsertChild(root, child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 320, 10)
    _assert_layout(child0, 0, 0, 107, 10)
    _assert_layout(child1, 107, 0, 106, 10)
    _assert_layout(child1_child0, 0, 0, 106, 10)
    _assert_layout(child2, 213, 0, 107, 10)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(child0, 213, 0, 107, 10)
    _assert_layout(child1, 107, 0, 106, 10)
    _assert_layout(child1_child0, 0, 0, 106, 10)
    _assert_layout(child2, 0, 0, 107, 10)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_rounding_inner_node_controversy_vertical():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 320)
    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child0, 10)
    YGNodeStyleSetFlexGrow(child0, 1)
    YGNodeInsertChild(root, child0, 0)
    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child1, 10)
    YGNodeStyleSetFlexGrow(child1, 1)
    YGNodeInsertChild(root, child1, 1)
    child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child1_child0, 10)
    YGNodeStyleSetFlexGrow(child1_child0, 1)
    YGNodeInsertChild(child1, child1_child0, 0)
    child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child2, 10)
    YGNodeStyleSetFlexGrow(child2, 1)
    YGNodeInsertChild(root, child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 10, 320)
    _assert_layout(child0, 0, 0, 10, 107)
    _assert_layout(child1, 0, 107, 10, 106)
    _assert_layout(child1_child0, 0, 0, 10, 106)
    _assert_layout(child2, 0, 213, 10, 107)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 10, 320)
    _assert_layout(child0, 0, 0, 10, 107)
    _assert_layout(child1, 0, 107, 10, 106)
    _assert_layout(child1_child0, 0, 0, 10, 106)
    _assert_layout(child2, 0, 213, 10, 107)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_rounding_inner_node_controversy_combined():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 640)
    YGNodeStyleSetHeight(root, 320)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeightPercent(child0, 100)
    YGNodeStyleSetFlexGrow(child0, 1)
    YGNodeInsertChild(root, child0, 0)

    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeightPercent(child1, 100)
    YGNodeStyleSetFlexGrow(child1, 1)
    YGNodeInsertChild(root, child1, 1)

    child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(child1_child0, 100)
    YGNodeStyleSetFlexGrow(child1_child0, 1)
    YGNodeInsertChild(child1, child1_child0, 0)

    child1_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(child1_child1, 100)
    YGNodeStyleSetFlexGrow(child1_child1, 1)
    YGNodeInsertChild(child1, child1_child1, 1)

    child1_child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child1_child1_child0, 1)
    YGNodeStyleSetWidthPercent(child1_child1_child0, 100)
    YGNodeInsertChild(child1_child1, child1_child1_child0, 0)

    child1_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(child1_child2, 100)
    YGNodeStyleSetFlexGrow(child1_child2, 1)
    YGNodeInsertChild(child1, child1_child2, 2)

    child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeightPercent(child2, 100)
    YGNodeStyleSetFlexGrow(child2, 1)
    YGNodeInsertChild(root, child2, 2)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 640, 320)
    _assert_layout(child0, 0, 0, 213, 320)
    _assert_layout(child1, 213, 0, 214, 320)
    _assert_layout(child1_child0, 0, 0, 214, 107)
    _assert_layout(child1_child1, 0, 107, 214, 106)
    _assert_layout(child1_child1_child0, 0, 0, 214, 106)
    _assert_layout(child1_child2, 0, 213, 214, 107)
    _assert_layout(child2, 427, 0, 213, 320)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(child0, 427, 0, 213, 320)
    _assert_layout(child1, 213, 0, 214, 320)
    _assert_layout(child1_child0, 0, 0, 214, 107)
    _assert_layout(child1_child1, 0, 107, 214, 106)
    _assert_layout(child1_child1_child0, 0, 0, 214, 106)
    _assert_layout(child1_child2, 0, 213, 214, 107)
    _assert_layout(child2, 0, 0, 213, 320)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)
