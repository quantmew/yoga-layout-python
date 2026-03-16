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
    YGNodeSetBaselineFunc,
    YGNodeSetIsReferenceBaseline,
    YGNodeSetMeasureFunc,
    YGNodeStyleSetAlignContent,
    YGNodeStyleSetAlignItems,
    YGNodeStyleSetFlexDirection,
    YGNodeStyleSetFlexGrow,
    YGNodeStyleSetFlexShrink,
    YGNodeStyleSetHeight,
    YGNodeStyleSetMargin,
    YGNodeStyleSetMaxHeight,
    YGNodeStyleSetMinHeight,
    YGNodeStyleSetPadding,
    YGNodeStyleSetWidth,
)
from yoga import YGEdge, YGSize  # noqa: E402


def _baseline_func(_node, _width, height):
    return height / 2


def _measure1(_node, _width, _width_mode, _height, _height_mode):
    return YGSize(42, 50)


def _measure2(_node, _width, _width_mode, _height, _height_mode):
    return YGSize(279, 126)


def _create_yg_node(config, direction, width, height, align_baseline):
    node = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(node, direction)
    if align_baseline:
        YGNodeStyleSetAlignItems(node, YGAlign.YGAlignBaseline)
    YGNodeStyleSetWidth(node, float(width))
    YGNodeStyleSetHeight(node, float(height))
    return node


def _assert_layout(node, left=None, top=None, width=None, height=None):
    if left is not None:
        assert YGNodeLayoutGetLeft(node) == left
    if top is not None:
        assert YGNodeLayoutGetTop(node) == top
    if width is not None:
        assert YGNodeLayoutGetWidth(node) == width
    if height is not None:
        assert YGNodeLayoutGetHeight(node) == height


def test_align_baseline_parent_ht_not_specified():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignStretch)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignBaseline)
    YGNodeStyleSetWidth(root, 340)
    YGNodeStyleSetMaxHeight(root, 170)
    YGNodeStyleSetMinHeight(root, 0)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child0, 0)
    YGNodeStyleSetFlexShrink(child0, 1)
    YGNodeSetMeasureFunc(child0, _measure1)
    YGNodeInsertChild(root, child0, 0)

    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child1, 0)
    YGNodeStyleSetFlexShrink(child1, 1)
    YGNodeSetMeasureFunc(child1, _measure2)
    YGNodeInsertChild(root, child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 340, 126)
    _assert_layout(child0, 0, 76, 42, 50)
    _assert_layout(child1, 42, 0, 279, 126)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_align_baseline_with_no_parent_ht():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignBaseline)
    YGNodeStyleSetWidth(root, 150)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child0, 50)
    YGNodeStyleSetHeight(child0, 50)
    YGNodeInsertChild(root, child0, 0)

    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child1, 50)
    YGNodeStyleSetHeight(child1, 40)
    YGNodeSetBaselineFunc(child1, _baseline_func)
    YGNodeInsertChild(root, child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 150, 70)
    _assert_layout(child0, 0, 0, 50, 50)
    _assert_layout(child1, 50, 30, 50, 40)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_align_baseline_with_no_baseline_func_and_no_parent_ht():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignBaseline)
    YGNodeStyleSetWidth(root, 150)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child0, 50)
    YGNodeStyleSetHeight(child0, 80)
    YGNodeInsertChild(root, child0, 0)

    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child1, 50)
    YGNodeStyleSetHeight(child1, 50)
    YGNodeInsertChild(root, child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 150, 80)
    _assert_layout(child0, 0, 0, 50, 80)
    _assert_layout(child1, 50, 30, 50, 50)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_align_baseline_parent_using_child_in_column_as_reference():
    config = YGConfigNew()
    root = _create_yg_node(config, YGFlexDirection.YGFlexDirectionRow, 1000, 1000, True)
    child0 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 600, False)
    YGNodeInsertChild(root, child0, 0)
    child1 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 800, False)
    YGNodeInsertChild(root, child1, 1)
    child10 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 300, False)
    YGNodeInsertChild(child1, child10, 0)
    child11 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 400, False)
    YGNodeSetBaselineFunc(child11, _baseline_func)
    YGNodeSetIsReferenceBaseline(child11, True)
    YGNodeInsertChild(child1, child11, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child0, 0, 0)
    _assert_layout(child1, 500, 100)
    _assert_layout(child10, 0, 0)
    _assert_layout(child11, 0, 300)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_align_baseline_parent_using_child_with_padding_in_column_as_reference():
    config = YGConfigNew()
    root = _create_yg_node(config, YGFlexDirection.YGFlexDirectionRow, 1000, 1000, True)
    child0 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 600, False)
    YGNodeInsertChild(root, child0, 0)
    child1 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 800, False)
    YGNodeInsertChild(root, child1, 1)
    child10 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 300, False)
    YGNodeInsertChild(child1, child10, 0)
    child11 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 400, False)
    YGNodeSetBaselineFunc(child11, _baseline_func)
    YGNodeSetIsReferenceBaseline(child11, True)
    for edge in (YGEdge.YGEdgeLeft, YGEdge.YGEdgeRight, YGEdge.YGEdgeTop, YGEdge.YGEdgeBottom):
        YGNodeStyleSetPadding(child11, edge, 100)
    YGNodeInsertChild(child1, child11, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child0, 0, 0)
    _assert_layout(child1, 500, 100)
    _assert_layout(child10, 0, 0)
    _assert_layout(child11, 0, 300)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_align_baseline_parent_with_padding_using_child_in_column_as_reference():
    config = YGConfigNew()
    root = _create_yg_node(config, YGFlexDirection.YGFlexDirectionRow, 1000, 1000, True)
    child0 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 600, False)
    YGNodeInsertChild(root, child0, 0)
    child1 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 800, False)
    for edge in (YGEdge.YGEdgeLeft, YGEdge.YGEdgeRight, YGEdge.YGEdgeTop, YGEdge.YGEdgeBottom):
        YGNodeStyleSetPadding(child1, edge, 100)
    YGNodeInsertChild(root, child1, 1)
    child10 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 300, False)
    YGNodeInsertChild(child1, child10, 0)
    child11 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 400, False)
    YGNodeSetBaselineFunc(child11, _baseline_func)
    YGNodeSetIsReferenceBaseline(child11, True)
    YGNodeInsertChild(child1, child11, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child0, 0, 0)
    _assert_layout(child1, 500, 0)
    _assert_layout(child10, 100, 100)
    _assert_layout(child11, 100, 400)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_align_baseline_parent_with_margin_using_child_in_column_as_reference():
    config = YGConfigNew()
    root = _create_yg_node(config, YGFlexDirection.YGFlexDirectionRow, 1000, 1000, True)
    child0 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 600, False)
    YGNodeInsertChild(root, child0, 0)
    child1 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 800, False)
    for edge in (YGEdge.YGEdgeLeft, YGEdge.YGEdgeRight, YGEdge.YGEdgeTop, YGEdge.YGEdgeBottom):
        YGNodeStyleSetMargin(child1, edge, 100)
    YGNodeInsertChild(root, child1, 1)
    child10 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 300, False)
    YGNodeInsertChild(child1, child10, 0)
    child11 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 400, False)
    YGNodeSetBaselineFunc(child11, _baseline_func)
    YGNodeSetIsReferenceBaseline(child11, True)
    YGNodeInsertChild(child1, child11, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child0, 0, 0)
    _assert_layout(child1, 600, 100)
    _assert_layout(child10, 0, 0)
    _assert_layout(child11, 0, 300)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_align_baseline_parent_using_child_with_margin_in_column_as_reference():
    config = YGConfigNew()
    root = _create_yg_node(config, YGFlexDirection.YGFlexDirectionRow, 1000, 1000, True)
    child0 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 600, False)
    YGNodeInsertChild(root, child0, 0)
    child1 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 800, False)
    YGNodeInsertChild(root, child1, 1)
    child10 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 300, False)
    YGNodeInsertChild(child1, child10, 0)
    child11 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 400, False)
    YGNodeSetBaselineFunc(child11, _baseline_func)
    YGNodeSetIsReferenceBaseline(child11, True)
    for edge in (YGEdge.YGEdgeLeft, YGEdge.YGEdgeRight, YGEdge.YGEdgeTop, YGEdge.YGEdgeBottom):
        YGNodeStyleSetMargin(child11, edge, 100)
    YGNodeInsertChild(child1, child11, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child0, 0, 0)
    _assert_layout(child1, 500, 0)
    _assert_layout(child10, 0, 0)
    _assert_layout(child11, 100, 400)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_align_baseline_parent_using_child_in_row_as_reference():
    config = YGConfigNew()
    root = _create_yg_node(config, YGFlexDirection.YGFlexDirectionRow, 1000, 1000, True)
    child0 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 600, False)
    YGNodeInsertChild(root, child0, 0)
    child1 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionRow, 500, 800, True)
    YGNodeInsertChild(root, child1, 1)
    child10 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 500, False)
    YGNodeInsertChild(child1, child10, 0)
    child11 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 400, False)
    YGNodeSetBaselineFunc(child11, _baseline_func)
    YGNodeSetIsReferenceBaseline(child11, True)
    YGNodeInsertChild(child1, child11, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child0, 0, 0)
    _assert_layout(child1, 500, 100)
    _assert_layout(child10, 0, 0)
    _assert_layout(child11, 500, 300)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_align_baseline_parent_using_child_with_padding_in_row_as_reference():
    config = YGConfigNew()
    root = _create_yg_node(config, YGFlexDirection.YGFlexDirectionRow, 1000, 1000, True)
    child0 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 600, False)
    YGNodeInsertChild(root, child0, 0)
    child1 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionRow, 500, 800, True)
    YGNodeInsertChild(root, child1, 1)
    child10 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 500, False)
    YGNodeInsertChild(child1, child10, 0)
    child11 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 400, False)
    YGNodeSetBaselineFunc(child11, _baseline_func)
    YGNodeSetIsReferenceBaseline(child11, True)
    for edge in (YGEdge.YGEdgeLeft, YGEdge.YGEdgeRight, YGEdge.YGEdgeTop, YGEdge.YGEdgeBottom):
        YGNodeStyleSetPadding(child11, edge, 100)
    YGNodeInsertChild(child1, child11, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child0, 0, 0)
    _assert_layout(child1, 500, 100)
    _assert_layout(child10, 0, 0)
    _assert_layout(child11, 500, 300)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_align_baseline_parent_using_child_with_margin_in_row_as_reference():
    config = YGConfigNew()
    root = _create_yg_node(config, YGFlexDirection.YGFlexDirectionRow, 1000, 1000, True)
    child0 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 600, False)
    YGNodeInsertChild(root, child0, 0)
    child1 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionRow, 500, 800, True)
    YGNodeInsertChild(root, child1, 1)
    child10 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 500, False)
    YGNodeInsertChild(child1, child10, 0)
    child11 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 400, False)
    YGNodeSetBaselineFunc(child11, _baseline_func)
    YGNodeSetIsReferenceBaseline(child11, True)
    for edge in (YGEdge.YGEdgeLeft, YGEdge.YGEdgeRight, YGEdge.YGEdgeTop, YGEdge.YGEdgeBottom):
        YGNodeStyleSetMargin(child11, edge, 100)
    YGNodeInsertChild(child1, child11, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child0, 0, 0)
    _assert_layout(child1, 500, 100)
    _assert_layout(child10, 0, 0)
    _assert_layout(child11, 600, 300)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_align_baseline_parent_using_child_in_column_as_reference_with_no_baseline_func():
    config = YGConfigNew()
    root = _create_yg_node(config, YGFlexDirection.YGFlexDirectionRow, 1000, 1000, True)
    child0 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 600, False)
    YGNodeInsertChild(root, child0, 0)
    child1 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 800, False)
    YGNodeInsertChild(root, child1, 1)
    child10 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 300, False)
    YGNodeInsertChild(child1, child10, 0)
    child11 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 400, False)
    YGNodeSetIsReferenceBaseline(child11, True)
    YGNodeInsertChild(child1, child11, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child0, 0, 100)
    _assert_layout(child1, 500, 0)
    _assert_layout(child10, 0, 0)
    _assert_layout(child11, 0, 300)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_align_baseline_parent_using_child_in_row_as_reference_with_no_baseline_func():
    config = YGConfigNew()
    root = _create_yg_node(config, YGFlexDirection.YGFlexDirectionRow, 1000, 1000, True)
    child0 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 600, False)
    YGNodeInsertChild(root, child0, 0)
    child1 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionRow, 500, 800, True)
    YGNodeInsertChild(root, child1, 1)
    child10 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 500, False)
    YGNodeInsertChild(child1, child10, 0)
    child11 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 400, False)
    YGNodeSetIsReferenceBaseline(child11, True)
    YGNodeInsertChild(child1, child11, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child0, 0, 0)
    _assert_layout(child1, 500, 100)
    _assert_layout(child10, 0, 0)
    _assert_layout(child11, 500, 100)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_align_baseline_parent_using_child_in_column_as_reference_with_height_not_specified():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignBaseline)
    YGNodeStyleSetWidth(root, 1000)
    child0 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 600, False)
    YGNodeInsertChild(root, child0, 0)
    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(child1, YGFlexDirection.YGFlexDirectionColumn)
    YGNodeStyleSetWidth(child1, 500)
    YGNodeInsertChild(root, child1, 1)
    child10 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 300, False)
    YGNodeInsertChild(child1, child10, 0)
    child11 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 400, False)
    YGNodeSetBaselineFunc(child11, _baseline_func)
    YGNodeSetIsReferenceBaseline(child11, True)
    YGNodeInsertChild(child1, child11, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetHeight(root) == 800
    _assert_layout(child0, 0, 0)
    _assert_layout(child1, 500, 100, height=700)
    _assert_layout(child10, 0, 0)
    _assert_layout(child11, 0, 300)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_align_baseline_parent_using_child_in_row_as_reference_with_height_not_specified():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignBaseline)
    YGNodeStyleSetWidth(root, 1000)
    child0 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 600, False)
    YGNodeInsertChild(root, child0, 0)
    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(child1, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(child1, 500)
    YGNodeInsertChild(root, child1, 1)
    child10 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 500, False)
    YGNodeInsertChild(child1, child10, 0)
    child11 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 400, False)
    YGNodeSetBaselineFunc(child11, _baseline_func)
    YGNodeSetIsReferenceBaseline(child11, True)
    YGNodeInsertChild(child1, child11, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetHeight(root) == 900
    _assert_layout(child0, 0, 0)
    _assert_layout(child1, 500, 400, height=500)
    _assert_layout(child10, 0, 0)
    _assert_layout(child11, 500, 0)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_align_baseline_parent_using_child_in_column_as_reference_with_no_baseline_func_and_height_not_specified():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignBaseline)
    YGNodeStyleSetWidth(root, 1000)
    child0 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 600, False)
    YGNodeInsertChild(root, child0, 0)
    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(child1, YGFlexDirection.YGFlexDirectionColumn)
    YGNodeStyleSetWidth(child1, 500)
    YGNodeInsertChild(root, child1, 1)
    child10 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 300, False)
    YGNodeInsertChild(child1, child10, 0)
    child11 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 400, False)
    YGNodeSetIsReferenceBaseline(child11, True)
    YGNodeInsertChild(child1, child11, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetHeight(root) == 700
    _assert_layout(child0, 0, 100)
    _assert_layout(child1, 500, 0, height=700)
    _assert_layout(child10, 0, 0)
    _assert_layout(child11, 0, 300)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_align_baseline_parent_using_child_in_row_as_reference_with_no_baseline_func_and_height_not_specified():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignBaseline)
    YGNodeStyleSetWidth(root, 1000)
    child0 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 600, False)
    YGNodeInsertChild(root, child0, 0)
    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(child1, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(child1, 500)
    YGNodeInsertChild(root, child1, 1)
    child10 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 500, False)
    YGNodeInsertChild(child1, child10, 0)
    child11 = _create_yg_node(config, YGFlexDirection.YGFlexDirectionColumn, 500, 400, False)
    YGNodeSetIsReferenceBaseline(child11, True)
    YGNodeInsertChild(child1, child11, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetHeight(root) == 700
    _assert_layout(child0, 0, 0)
    _assert_layout(child1, 500, 200, height=500)
    _assert_layout(child10, 0, 0)
    _assert_layout(child11, 500, 0)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)
