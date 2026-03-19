import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from yoga import (  # noqa: E402
    YGAlign,
    YGConfigFree,
    YGConfigNew,
    YGDirection,
    YGEdge,
    YGFlexDirection,
    YGJustify,
    YGNodeCalculateLayout,
    YGNodeFreeRecursive,
    YGNodeInsertChild,
    YGNodeLayoutGetHeight,
    YGNodeLayoutGetLeft,
    YGNodeLayoutGetTop,
    YGNodeLayoutGetWidth,
    YGNodeNewWithConfig,
    YGNodeStyleSetAlignItems,
    YGNodeStyleSetFlexBasisPercent,
    YGNodeStyleSetFlexDirection,
    YGNodeStyleSetFlexGrow,
    YGNodeStyleSetHeight,
    YGNodeStyleSetHeightPercent,
    YGNodeStyleSetJustifyContent,
    YGNodeStyleSetMargin,
    YGNodeStyleSetMarginPercent,
    YGNodeStyleSetMaxHeightPercent,
    YGNodeStyleSetMaxWidth,
    YGNodeStyleSetMaxWidthPercent,
    YGNodeStyleSetMinWidth,
    YGNodeStyleSetMinWidthPercent,
    YGNodeStyleSetPadding,
    YGNodeStyleSetPaddingPercent,
    YGNodeStyleSetPositionPercent,
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


def test_percentage_width_height():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 200)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0, 30)
    YGNodeStyleSetHeightPercent(root_child0, 30)
    YGNodeInsertChild(root, root_child0, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 200, 200)
    _assert_layout(root_child0, 0, 0, 60, 60)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 200, 200)
    _assert_layout(root_child0, 140, 0, 60, 60)

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_percentage_position_left_top():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 400)
    YGNodeStyleSetHeight(root, 400)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0, 45)
    YGNodeStyleSetHeightPercent(root_child0, 55)
    YGNodeStyleSetPositionPercent(root_child0, YGEdge.YGEdgeLeft, 10)
    YGNodeStyleSetPositionPercent(root_child0, YGEdge.YGEdgeTop, 20)
    YGNodeInsertChild(root, root_child0, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 400, 400)
    _assert_layout(root_child0, 40, 80, 180, 220)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 400, 400)
    _assert_layout(root_child0, 260, 80, 180, 220)

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_percentage_position_bottom_right():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 500)
    YGNodeStyleSetHeight(root, 500)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0, 55)
    YGNodeStyleSetHeightPercent(root_child0, 15)
    YGNodeStyleSetPositionPercent(root_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPositionPercent(root_child0, YGEdge.YGEdgeRight, 20)
    YGNodeInsertChild(root, root_child0, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 500, 500)
    _assert_layout(root_child0, -100, -50, 275, 75)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 500, 500)
    _assert_layout(root_child0, 125, -50, 275, 75)

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_percentage_flex_basis():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 200)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeStyleSetFlexBasisPercent(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child1, 1)
    YGNodeStyleSetFlexBasisPercent(root_child1, 25)
    YGNodeInsertChild(root, root_child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 200, 200)
    _assert_layout(root_child0, 0, 0, 125, 200)
    _assert_layout(root_child1, 125, 0, 75, 200)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 200, 200)
    _assert_layout(root_child0, 75, 0, 125, 200)
    _assert_layout(root_child1, 0, 0, 75, 200)

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_percentage_flex_basis_cross():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 200)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeStyleSetFlexBasisPercent(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child1, 1)
    YGNodeStyleSetFlexBasisPercent(root_child1, 25)
    YGNodeInsertChild(root, root_child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 200, 200)
    _assert_layout(root_child0, 0, 0, 200, 125)
    _assert_layout(root_child1, 0, 125, 200, 75)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 200, 200)
    _assert_layout(root_child0, 0, 0, 200, 125)
    _assert_layout(root_child1, 0, 125, 200, 75)

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_percentage_flex_basis_cross_min_height():
    pytest.skip("Upstream GTEST_SKIP()")


def test_percentage_flex_basis_main_max_height():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 200)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeStyleSetFlexBasisPercent(root_child0, 10)
    YGNodeStyleSetMaxHeightPercent(root_child0, 60)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child1, 4)
    YGNodeStyleSetFlexBasisPercent(root_child1, 10)
    YGNodeStyleSetMaxHeightPercent(root_child1, 20)
    YGNodeInsertChild(root, root_child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 200, 200)
    _assert_layout(root_child0, 0, 0, 52, 120)
    _assert_layout(root_child1, 52, 0, 148, 40)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 200, 200)
    _assert_layout(root_child0, 148, 0, 52, 120)
    _assert_layout(root_child1, 0, 0, 148, 40)

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_percentage_flex_basis_cross_max_height():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 200)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeStyleSetFlexBasisPercent(root_child0, 10)
    YGNodeStyleSetMaxHeightPercent(root_child0, 60)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child1, 4)
    YGNodeStyleSetFlexBasisPercent(root_child1, 10)
    YGNodeStyleSetMaxHeightPercent(root_child1, 20)
    YGNodeInsertChild(root, root_child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 200, 200)
    _assert_layout(root_child0, 0, 0, 200, 120)
    _assert_layout(root_child1, 0, 120, 200, 40)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 200, 200)
    _assert_layout(root_child0, 0, 0, 200, 120)
    _assert_layout(root_child1, 0, 120, 200, 40)

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_percentage_flex_basis_main_max_width():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 200)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeStyleSetFlexBasisPercent(root_child0, 15)
    YGNodeStyleSetMaxWidthPercent(root_child0, 60)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child1, 4)
    YGNodeStyleSetFlexBasisPercent(root_child1, 10)
    YGNodeStyleSetMaxWidthPercent(root_child1, 20)
    YGNodeInsertChild(root, root_child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 200, 200)
    _assert_layout(root_child0, 0, 0, 120, 200)
    _assert_layout(root_child1, 120, 0, 40, 200)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 200, 200)
    _assert_layout(root_child0, 80, 0, 120, 200)
    _assert_layout(root_child1, 40, 0, 40, 200)

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_percentage_flex_basis_cross_max_width():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 200)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeStyleSetFlexBasisPercent(root_child0, 10)
    YGNodeStyleSetMaxWidthPercent(root_child0, 60)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child1, 4)
    YGNodeStyleSetFlexBasisPercent(root_child1, 15)
    YGNodeStyleSetMaxWidthPercent(root_child1, 20)
    YGNodeInsertChild(root, root_child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 200, 200)
    _assert_layout(root_child0, 0, 0, 120, 50)
    _assert_layout(root_child1, 0, 50, 40, 150)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 200, 200)
    _assert_layout(root_child0, 80, 0, 120, 50)
    _assert_layout(root_child1, 160, 50, 40, 150)

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_percentage_flex_basis_main_min_width():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 200)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeStyleSetFlexBasisPercent(root_child0, 15)
    YGNodeStyleSetMinWidthPercent(root_child0, 60)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child1, 4)
    YGNodeStyleSetFlexBasisPercent(root_child1, 10)
    YGNodeStyleSetMinWidthPercent(root_child1, 20)
    YGNodeInsertChild(root, root_child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 200, 200)
    _assert_layout(root_child0, 0, 0, 120, 200)
    _assert_layout(root_child1, 120, 0, 80, 200)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 200, 200)
    _assert_layout(root_child0, 80, 0, 120, 200)
    _assert_layout(root_child1, 0, 0, 80, 200)

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_percentage_flex_basis_cross_min_width():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 200)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeStyleSetFlexBasisPercent(root_child0, 10)
    YGNodeStyleSetMinWidthPercent(root_child0, 60)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child1, 4)
    YGNodeStyleSetFlexBasisPercent(root_child1, 15)
    YGNodeStyleSetMinWidthPercent(root_child1, 20)
    YGNodeInsertChild(root, root_child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 200, 200)
    _assert_layout(root_child0, 0, 0, 200, 50)
    _assert_layout(root_child1, 0, 50, 200, 150)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 200, 200)
    _assert_layout(root_child0, 0, 0, 200, 50)
    _assert_layout(root_child1, 0, 50, 200, 150)

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_percentage_multiple_nested_with_padding_margin_and_percentage_values():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 200)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeStyleSetFlexBasisPercent(root_child0, 10)
    YGNodeStyleSetMinWidthPercent(root_child0, 60)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeAll, 5)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeAll, 3)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child0, 50)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeAll, 5)
    YGNodeStyleSetPaddingPercent(root_child0_child0, YGEdge.YGEdgeAll, 3)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child0_child0, 45)
    YGNodeStyleSetMarginPercent(root_child0_child0_child0, YGEdge.YGEdgeAll, 5)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeAll, 3)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child1, 4)
    YGNodeStyleSetFlexBasisPercent(root_child1, 15)
    YGNodeStyleSetMinWidthPercent(root_child1, 20)
    YGNodeInsertChild(root, root_child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 200, 200)
    _assert_layout(root_child0, 5, 5, 190, 48)
    _assert_layout(root_child0_child0, 8, 8, 92, 25)
    _assert_layout(root_child0_child0_child0, 10, 10, 36, 6)
    _assert_layout(root_child1, 0, 58, 200, 142)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 200, 200)
    _assert_layout(root_child0, 5, 5, 190, 48)
    _assert_layout(root_child0_child0, 90, 8, 92, 25)
    _assert_layout(root_child0_child0_child0, 46, 10, 36, 6)
    _assert_layout(root_child1, 0, 58, 200, 142)

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_percentage_margin_should_calculate_based_only_on_width():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeStyleSetMarginPercent(root_child0, YGEdge.YGEdgeAll, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeStyleSetHeight(root_child0_child0, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 200, 100)
    _assert_layout(root_child0, 20, 20, 160, 60)
    _assert_layout(root_child0_child0, 0, 0, 10, 10)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 200, 100)
    _assert_layout(root_child0, 20, 20, 160, 60)
    _assert_layout(root_child0_child0, 150, 0, 10, 10)

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_percentage_padding_should_calculate_based_only_on_width():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeStyleSetPaddingPercent(root_child0, YGEdge.YGEdgeAll, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeStyleSetHeight(root_child0_child0, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 200, 100)
    _assert_layout(root_child0, 0, 0, 200, 100)
    _assert_layout(root_child0_child0, 20, 20, 10, 10)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 200, 100)
    _assert_layout(root_child0, 0, 0, 200, 100)
    _assert_layout(root_child0_child0, 170, 20, 10, 10)

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_percentage_absolute_position():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPositionPercent(root_child0, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetPositionPercent(root_child0, YGEdge.YGEdgeLeft, 30)
    YGNodeStyleSetWidth(root_child0, 10)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 200, 100)
    _assert_layout(root_child0, 60, 10, 10, 10)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 200, 100)
    _assert_layout(root_child0, 60, 10, 10, 10)

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_percentage_width_height_undefined_parent_size():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0, 50)
    YGNodeStyleSetHeightPercent(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 0, 0)
    _assert_layout(root_child0, 0, 0, 0, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 0, 0)
    _assert_layout(root_child0, 0, 0, 0, 0)

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_percent_within_flex_grow():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(root, 350)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child1, 1)
    YGNodeInsertChild(root, root_child1, 1)

    root_child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child1_child0, 100)
    YGNodeInsertChild(root_child1, root_child1_child0, 0)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 100)
    YGNodeInsertChild(root, root_child2, 2)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 350, 100)
    _assert_layout(root_child0, 0, 0, 100, 100)
    _assert_layout(root_child1, 100, 0, 150, 100)
    _assert_layout(root_child1_child0, 0, 0, 150, 0)
    _assert_layout(root_child2, 250, 0, 100, 100)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 350, 100)
    _assert_layout(root_child0, 250, 0, 100, 100)
    _assert_layout(root_child1, 100, 0, 150, 100)
    _assert_layout(root_child1_child0, 0, 0, 150, 0)
    _assert_layout(root_child2, 0, 0, 100, 100)

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_percentage_container_in_wrapping_container():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 200)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyCenter)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetJustifyContent(root_child0_child0, YGJustify.YGJustifyCenter)
    YGNodeStyleSetWidthPercent(root_child0_child0, 100)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)

    root_child0_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0_child1, 50)
    YGNodeStyleSetHeight(root_child0_child0_child1, 50)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 200, 200)
    _assert_layout(root_child0, 50, 75, 100, 50)
    _assert_layout(root_child0_child0, 0, 0, 100, 50)
    _assert_layout(root_child0_child0_child0, 0, 0, 50, 50)
    _assert_layout(root_child0_child0_child1, 50, 0, 50, 50)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 200, 200)
    _assert_layout(root_child0, 50, 75, 100, 50)
    _assert_layout(root_child0_child0, 0, 0, 100, 50)
    _assert_layout(root_child0_child0_child0, 50, 0, 50, 50)
    _assert_layout(root_child0_child0_child1, 0, 0, 50, 50)

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_percent_absolute_position():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 60)
    YGNodeStyleSetHeight(root, 50)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeStyleSetWidthPercent(root_child0, 100)
    YGNodeStyleSetPositionPercent(root_child0, YGEdge.YGEdgeLeft, 50)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child0, 100)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child1, 100)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 60, 50)
    _assert_layout(root_child0, 30, 0, 60, 50)
    _assert_layout(root_child0_child0, 0, 0, 60, 50)
    _assert_layout(root_child0_child1, 60, 0, 60, 50)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 60, 50)
    _assert_layout(root_child0, 30, 0, 60, 50)
    _assert_layout(root_child0_child0, 0, 0, 60, 50)
    _assert_layout(root_child0_child1, -60, 0, 60, 50)

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_percent_of_minmax_main():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetMinWidth(root, 60)
    YGNodeStyleSetMaxWidth(root, 60)
    YGNodeStyleSetHeight(root, 50)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 20)
    YGNodeInsertChild(root, root_child0, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 60, 50)
    _assert_layout(root_child0, 0, 0, 30, 20)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 60, 50)
    _assert_layout(root_child0, 30, 0, 30, 20)

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_percent_of_min_main():
    pytest.skip("Upstream GTEST_SKIP()")


def test_percent_of_min_main_multiple():
    pytest.skip("Upstream GTEST_SKIP()")


def test_percent_of_max_main():
    pytest.skip("Upstream GTEST_SKIP()")


def test_percent_of_minmax_cross_stretched():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetMinWidth(root, 60)
    YGNodeStyleSetMaxWidth(root, 60)
    YGNodeStyleSetHeight(root, 50)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 20)
    YGNodeInsertChild(root, root_child0, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 60, 50)
    _assert_layout(root_child0, 0, 0, 30, 20)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 60, 50)
    _assert_layout(root_child0, 30, 0, 30, 20)

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_percent_absolute_of_minmax_cross_stretched():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetMinWidth(root, 60)
    YGNodeStyleSetMaxWidth(root, 60)
    YGNodeStyleSetHeight(root, 50)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 20)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeInsertChild(root, root_child0, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 60, 50)
    _assert_layout(root_child0, 0, 0, 30, 20)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 60, 50)
    _assert_layout(root_child0, 30, 0, 30, 20)

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_percent_of_minmax_cross_unstretched():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetMinWidth(root, 60)
    YGNodeStyleSetMaxWidth(root, 60)
    YGNodeStyleSetHeight(root, 50)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 20)
    YGNodeInsertChild(root, root_child0, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 60, 50)
    _assert_layout(root_child0, 0, 0, 30, 20)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 60, 50)
    _assert_layout(root_child0, 30, 0, 30, 20)

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_percent_of_min_cross_unstretched():
    pytest.skip("Upstream GTEST_SKIP()")


def test_percent_of_max_cross_unstretched():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetMaxWidth(root, 60)
    YGNodeStyleSetHeight(root, 50)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 20)
    YGNodeInsertChild(root, root_child0, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 0, 50)
    _assert_layout(root_child0, 0, 0, 0, 20)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 0, 50)
    _assert_layout(root_child0, 0, 0, 0, 20)

    YGNodeFreeRecursive(root)
    YGConfigFree(config)
