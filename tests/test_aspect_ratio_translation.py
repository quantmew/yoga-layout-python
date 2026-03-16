import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import (  # noqa: E402
    YGAlign,
    YGConfigFree,
    YGConfigNew,
    YGConfigSetUseWebDefaults,
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
    YGNodeNew,
    YGNodeNewWithConfig,
    YGNodeSetMeasureFunc,
    YGNodeStyleSetAlignItems,
    YGNodeStyleSetAspectRatio,
    YGNodeStyleSetFlexBasis,
    YGNodeStyleSetFlexDirection,
    YGNodeStyleSetFlexGrow,
    YGNodeStyleSetFlexShrink,
    YGNodeStyleSetHeight,
    YGNodeStyleSetHeightPercent,
    YGNodeStyleSetJustifyContent,
    YGNodeStyleSetMargin,
    YGNodeStyleSetMaxHeight,
    YGNodeStyleSetMaxWidth,
    YGNodeStyleSetMinHeight,
    YGNodeStyleSetMinWidth,
    YGNodeStyleSetPosition,
    YGNodeStyleSetPositionType,
    YGNodeStyleSetWidth,
    YGPositionType,
    YGSize,
)


def _measure(_node, width, width_mode, height, height_mode):
    return YGSize(
        width if width_mode == 1 else 50,
        height if height_mode == 1 else 50,
    )


def _assert_layout(node, left, top, width, height):
    assert YGNodeLayoutGetLeft(node) == left
    assert YGNodeLayoutGetTop(node) == top
    assert YGNodeLayoutGetWidth(node) == width
    assert YGNodeLayoutGetHeight(node) == height


def test_aspect_ratio_cross_defined():
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeStyleSetWidth(child, 50)
    YGNodeStyleSetAspectRatio(child, 1)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child, 0, 0, 50, 50)
    YGNodeFreeRecursive(root)


def test_aspect_ratio_main_defined():
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeStyleSetHeight(child, 50)
    YGNodeStyleSetAspectRatio(child, 1)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child, 0, 0, 50, 50)
    YGNodeFreeRecursive(root)


def test_aspect_ratio_both_dimensions_defined_row():
    root = YGNodeNew()
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeStyleSetWidth(child, 100)
    YGNodeStyleSetHeight(child, 50)
    YGNodeStyleSetAspectRatio(child, 1)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child, 0, 0, 100, 100)
    YGNodeFreeRecursive(root)


def test_aspect_ratio_both_dimensions_defined_column():
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeStyleSetWidth(child, 100)
    YGNodeStyleSetHeight(child, 50)
    YGNodeStyleSetAspectRatio(child, 1)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child, 0, 0, 50, 50)
    YGNodeFreeRecursive(root)


def test_aspect_ratio_align_stretch():
    root = YGNodeNew()
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeStyleSetAspectRatio(child, 1)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child, 0, 0, 100, 100)
    YGNodeFreeRecursive(root)


def test_aspect_ratio_flex_grow():
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeStyleSetHeight(child, 50)
    YGNodeStyleSetFlexGrow(child, 1)
    YGNodeStyleSetAspectRatio(child, 1)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child, 0, 0, 100, 100)
    YGNodeFreeRecursive(root)


def test_aspect_ratio_flex_shrink():
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeStyleSetHeight(child, 150)
    YGNodeStyleSetFlexShrink(child, 1)
    YGNodeStyleSetAspectRatio(child, 1)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child, 0, 0, 100, 100)
    YGNodeFreeRecursive(root)


def test_aspect_ratio_flex_shrink_2():
    root = YGNodeNew()
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child0 = YGNodeNew()
    YGNodeStyleSetHeightPercent(child0, 100)
    YGNodeStyleSetFlexShrink(child0, 1)
    YGNodeStyleSetAspectRatio(child0, 1)
    YGNodeInsertChild(root, child0, 0)
    child1 = YGNodeNew()
    YGNodeStyleSetHeightPercent(child1, 100)
    YGNodeStyleSetFlexShrink(child1, 1)
    YGNodeStyleSetAspectRatio(child1, 1)
    YGNodeInsertChild(root, child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child0, 0, 0, 50, 50)
    _assert_layout(child1, 0, 50, 50, 50)
    YGNodeFreeRecursive(root)


def test_aspect_ratio_basis():
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeStyleSetFlexBasis(child, 50)
    YGNodeStyleSetAspectRatio(child, 1)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child, 0, 0, 50, 50)
    YGNodeFreeRecursive(root)


def test_aspect_ratio_absolute_layout_width_defined():
    root = YGNodeNew()
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeStyleSetPositionType(child, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPosition(child, YGEdge.YGEdgeLeft, 0)
    YGNodeStyleSetPosition(child, YGEdge.YGEdgeTop, 0)
    YGNodeStyleSetWidth(child, 50)
    YGNodeStyleSetAspectRatio(child, 1)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child, 0, 0, 50, 50)
    YGNodeFreeRecursive(root)


def test_aspect_ratio_absolute_layout_height_defined():
    root = YGNodeNew()
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeStyleSetPositionType(child, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPosition(child, YGEdge.YGEdgeLeft, 0)
    YGNodeStyleSetPosition(child, YGEdge.YGEdgeTop, 0)
    YGNodeStyleSetHeight(child, 50)
    YGNodeStyleSetAspectRatio(child, 1)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child, 0, 0, 50, 50)
    YGNodeFreeRecursive(root)


def test_aspect_ratio_with_max_cross_defined():
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeStyleSetHeight(child, 50)
    YGNodeStyleSetMaxWidth(child, 40)
    YGNodeStyleSetAspectRatio(child, 1)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child, 0, 0, 40, 50)
    YGNodeFreeRecursive(root)


def test_aspect_ratio_with_max_main_defined():
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeStyleSetWidth(child, 50)
    YGNodeStyleSetMaxHeight(child, 40)
    YGNodeStyleSetAspectRatio(child, 1)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child, 0, 0, 40, 40)
    YGNodeFreeRecursive(root)


def test_aspect_ratio_with_min_cross_defined():
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeStyleSetHeight(child, 30)
    YGNodeStyleSetMinWidth(child, 40)
    YGNodeStyleSetAspectRatio(child, 1)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child, 0, 0, 40, 30)
    YGNodeFreeRecursive(root)


def test_aspect_ratio_with_min_main_defined():
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeStyleSetWidth(child, 30)
    YGNodeStyleSetMinHeight(child, 40)
    YGNodeStyleSetAspectRatio(child, 1)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child, 0, 0, 40, 40)
    YGNodeFreeRecursive(root)


def test_aspect_ratio_double_cross():
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeStyleSetHeight(child, 50)
    YGNodeStyleSetAspectRatio(child, 2)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child, 0, 0, 100, 50)
    YGNodeFreeRecursive(root)


def test_aspect_ratio_half_cross():
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeStyleSetHeight(child, 100)
    YGNodeStyleSetAspectRatio(child, 0.5)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child, 0, 0, 50, 100)
    YGNodeFreeRecursive(root)


def test_aspect_ratio_double_main():
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeStyleSetWidth(child, 50)
    YGNodeStyleSetAspectRatio(child, 0.5)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child, 0, 0, 50, 100)
    YGNodeFreeRecursive(root)


def test_aspect_ratio_half_main():
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeStyleSetWidth(child, 100)
    YGNodeStyleSetAspectRatio(child, 2)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child, 0, 0, 100, 50)
    YGNodeFreeRecursive(root)


def test_aspect_ratio_with_measure_func():
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeSetMeasureFunc(child, _measure)
    YGNodeStyleSetAspectRatio(child, 1)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child, 0, 0, 50, 50)
    YGNodeFreeRecursive(root)


def test_aspect_ratio_width_height_flex_grow_row():
    root = YGNodeNew()
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 200)
    child = YGNodeNew()
    YGNodeStyleSetWidth(child, 50)
    YGNodeStyleSetHeight(child, 50)
    YGNodeStyleSetFlexGrow(child, 1)
    YGNodeStyleSetAspectRatio(child, 1)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child, 0, 0, 100, 100)
    YGNodeFreeRecursive(root)


def test_aspect_ratio_width_height_flex_grow_column():
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeStyleSetWidth(child, 50)
    YGNodeStyleSetHeight(child, 50)
    YGNodeStyleSetFlexGrow(child, 1)
    YGNodeStyleSetAspectRatio(child, 1)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child, 0, 0, 100, 100)
    YGNodeFreeRecursive(root)


def test_aspect_ratio_height_as_flex_basis():
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 200)
    child0 = YGNodeNew()
    YGNodeStyleSetHeight(child0, 50)
    YGNodeStyleSetFlexGrow(child0, 1)
    YGNodeStyleSetAspectRatio(child0, 1)
    YGNodeInsertChild(root, child0, 0)
    child1 = YGNodeNew()
    YGNodeStyleSetHeight(child1, 100)
    YGNodeStyleSetFlexGrow(child1, 1)
    YGNodeStyleSetAspectRatio(child1, 1)
    YGNodeInsertChild(root, child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child0, 0, 0, 75, 75)
    _assert_layout(child1, 75, 0, 125, 125)
    YGNodeFreeRecursive(root)


def test_aspect_ratio_width_as_flex_basis():
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 200)
    child0 = YGNodeNew()
    YGNodeStyleSetWidth(child0, 50)
    YGNodeStyleSetFlexGrow(child0, 1)
    YGNodeStyleSetAspectRatio(child0, 1)
    YGNodeInsertChild(root, child0, 0)
    child1 = YGNodeNew()
    YGNodeStyleSetWidth(child1, 100)
    YGNodeStyleSetFlexGrow(child1, 1)
    YGNodeStyleSetAspectRatio(child1, 1)
    YGNodeInsertChild(root, child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child0, 0, 0, 75, 75)
    _assert_layout(child1, 0, 75, 125, 125)
    YGNodeFreeRecursive(root)


def test_aspect_ratio_overrides_flex_grow_row():
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeStyleSetWidth(child, 50)
    YGNodeStyleSetFlexGrow(child, 1)
    YGNodeStyleSetAspectRatio(child, 0.5)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child, 0, 0, 100, 200)
    YGNodeFreeRecursive(root)


def test_aspect_ratio_overrides_flex_grow_column():
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeStyleSetHeight(child, 50)
    YGNodeStyleSetFlexGrow(child, 1)
    YGNodeStyleSetAspectRatio(child, 2)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child, 0, 0, 200, 100)
    YGNodeFreeRecursive(root)


def test_aspect_ratio_left_right_absolute():
    root = YGNodeNew()
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeStyleSetPositionType(child, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPosition(child, YGEdge.YGEdgeLeft, 10)
    YGNodeStyleSetPosition(child, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetPosition(child, YGEdge.YGEdgeRight, 10)
    YGNodeStyleSetAspectRatio(child, 1)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child, 10, 10, 80, 80)
    YGNodeFreeRecursive(root)


def test_aspect_ratio_top_bottom_absolute():
    root = YGNodeNew()
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeStyleSetPositionType(child, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPosition(child, YGEdge.YGEdgeLeft, 10)
    YGNodeStyleSetPosition(child, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetPosition(child, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetAspectRatio(child, 1)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child, 10, 10, 80, 80)
    YGNodeFreeRecursive(root)


def test_aspect_ratio_width_overrides_align_stretch_row():
    root = YGNodeNew()
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeStyleSetWidth(child, 50)
    YGNodeStyleSetAspectRatio(child, 1)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child, 0, 0, 50, 50)
    YGNodeFreeRecursive(root)


def test_aspect_ratio_height_overrides_align_stretch_column():
    root = YGNodeNew()
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeStyleSetHeight(child, 50)
    YGNodeStyleSetAspectRatio(child, 1)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child, 0, 0, 50, 50)
    YGNodeFreeRecursive(root)


def test_aspect_ratio_allow_child_overflow_parent_size():
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 100)
    child = YGNodeNew()
    YGNodeStyleSetHeight(child, 50)
    YGNodeStyleSetAspectRatio(child, 4)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 50
    assert YGNodeLayoutGetWidth(child) == 200
    assert YGNodeLayoutGetHeight(child) == 50
    YGNodeFreeRecursive(root)


def test_aspect_ratio_defined_main_with_margin():
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyCenter)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeStyleSetHeight(child, 50)
    YGNodeStyleSetAspectRatio(child, 1)
    YGNodeStyleSetMargin(child, YGEdge.YGEdgeLeft, 10)
    YGNodeStyleSetMargin(child, YGEdge.YGEdgeRight, 10)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetWidth(child) == 50
    assert YGNodeLayoutGetHeight(child) == 50
    YGNodeFreeRecursive(root)


def test_aspect_ratio_defined_cross_with_margin():
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyCenter)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeStyleSetWidth(child, 50)
    YGNodeStyleSetAspectRatio(child, 1)
    YGNodeStyleSetMargin(child, YGEdge.YGEdgeLeft, 10)
    YGNodeStyleSetMargin(child, YGEdge.YGEdgeRight, 10)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetWidth(child) == 50
    assert YGNodeLayoutGetHeight(child) == 50
    YGNodeFreeRecursive(root)


def test_aspect_ratio_defined_cross_with_main_margin():
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyCenter)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeStyleSetWidth(child, 50)
    YGNodeStyleSetAspectRatio(child, 1)
    YGNodeStyleSetMargin(child, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetMargin(child, YGEdge.YGEdgeBottom, 10)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetWidth(child) == 50
    assert YGNodeLayoutGetHeight(child) == 50
    YGNodeFreeRecursive(root)


def test_aspect_ratio_should_prefer_explicit_height():
    config = YGConfigNew()
    YGConfigSetUseWebDefaults(config, True)
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionColumn)
    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(child0, YGFlexDirection.YGFlexDirectionColumn)
    YGNodeInsertChild(root, child0, 0)
    child00 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(child00, YGFlexDirection.YGFlexDirectionColumn)
    YGNodeStyleSetHeight(child00, 100)
    YGNodeStyleSetAspectRatio(child00, 2)
    YGNodeInsertChild(child0, child00, 0)
    YGNodeCalculateLayout(root, 100, 200, YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 100, 200)
    _assert_layout(child0, 0, 0, 100, 100)
    _assert_layout(child00, 0, 0, 200, 100)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_aspect_ratio_should_prefer_explicit_width():
    config = YGConfigNew()
    YGConfigSetUseWebDefaults(config, True)
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeInsertChild(root, child0, 0)
    child00 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(child00, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(child00, 100)
    YGNodeStyleSetAspectRatio(child00, 0.5)
    YGNodeInsertChild(child0, child00, 0)
    YGNodeCalculateLayout(root, 200, 100, YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 200, 100)
    _assert_layout(child0, 0, 0, 100, 100)
    _assert_layout(child00, 0, 0, 100, 200)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_aspect_ratio_should_prefer_flexed_dimension():
    config = YGConfigNew()
    YGConfigSetUseWebDefaults(config, True)
    root = YGNodeNewWithConfig(config)
    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(child0, YGFlexDirection.YGFlexDirectionColumn)
    YGNodeStyleSetAspectRatio(child0, 2)
    YGNodeStyleSetFlexGrow(child0, 1)
    YGNodeInsertChild(root, child0, 0)
    child00 = YGNodeNewWithConfig(config)
    YGNodeStyleSetAspectRatio(child00, 4)
    YGNodeStyleSetFlexGrow(child00, 1)
    YGNodeInsertChild(child0, child00, 0)
    YGNodeCalculateLayout(root, 100, 100, YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 100, 100)
    _assert_layout(child0, 0, 0, 100, 50)
    _assert_layout(child00, 0, 0, 200, 50)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)
