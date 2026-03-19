import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import (  # noqa: E402
    YGAlign,
    YGBoxSizing,
    YGConfigFree,
    YGConfigNew,
    YGDirection,
    YGEdge,
    YGFlexDirection,
    YGJustify,
    YGMeasureMode,
    YGNodeCalculateLayout,
    YGNodeFree,
    YGNodeFreeRecursive,
    YGNodeHasMeasureFunc,
    YGNodeInsertChild,
    YGNodeLayoutGetHeight,
    YGNodeLayoutGetLeft,
    YGNodeLayoutGetTop,
    YGNodeLayoutGetWidth,
    YGNodeNew,
    YGNodeNewWithConfig,
    YGNodeSetContext,
    YGNodeSetMeasureFunc,
    YGNodeStyleSetAlignContent,
    YGNodeStyleSetAlignItems,
    YGNodeStyleSetAlignSelf,
    YGNodeStyleSetBorder,
    YGNodeStyleSetBoxSizing,
    YGNodeStyleSetFlexDirection,
    YGNodeStyleSetFlexGrow,
    YGNodeStyleSetFlexShrink,
    YGNodeStyleSetHeight,
    YGNodeStyleSetJustifyContent,
    YGNodeStyleSetMargin,
    YGNodeStyleSetMarginAuto,
    YGNodeStyleSetMarginPercent,
    YGNodeStyleSetMaxHeight,
    YGNodeStyleSetMaxHeightPercent,
    YGNodeStyleSetMaxWidth,
    YGNodeStyleSetMaxWidthPercent,
    YGNodeStyleSetMinHeight,
    YGNodeStyleSetMinHeightPercent,
    YGNodeStyleSetMinWidth,
    YGNodeStyleSetMinWidthPercent,
    YGNodeStyleSetPadding,
    YGNodeStyleSetPaddingPercent,
    YGNodeStyleSetPositionType,
    YGNodeStyleSetWidth,
    YGPositionType,
    YGSize,
)


def _measure(node, _width, _widthMode, _height, _heightMode):
    measureCount = node.getContext()
    if measureCount is not None:
        measureCount[0] += 1
    return YGSize(10, 10)


def _simulate_wrapping_text(_node, width, widthMode, _height, _heightMode):
    if widthMode == YGMeasureMode.YGMeasureModeUndefined or width >= 68:
        return YGSize(68, 16)
    return YGSize(50, 32)


def _measure_assert_negative(_node, width, _widthMode, height, _heightMode):
    assert width >= 0
    assert height >= 0
    return YGSize(0, 0)


def _measure_90_10(_node, _width, _widthMode, _height, _heightMode):
    return YGSize(90, 10)


def _measure_100_100(_node, _width, _widthMode, _height, _heightMode):
    return YGSize(100, 100)


def _measure_half_width_height(node, width, _widthMode, height, _heightMode):
    measureCount = node.getContext()
    if measureCount is not None:
        measureCount[0] += 1
    return YGSize(0.5 * width, 0.5 * height)


def test_dont_measure_single_grow_shrink_child():
    root = YGNodeNew()
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    measureCount = [0]
    root_child0 = YGNodeNew()
    YGNodeSetContext(root_child0, measureCount)
    YGNodeSetMeasureFunc(root_child0, _measure)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeStyleSetFlexShrink(root_child0, 1)
    YGNodeInsertChild(root, root_child0, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert measureCount[0] == 0
    YGNodeFreeRecursive(root)


def test_measure_absolute_child_with_no_constraints():
    root = YGNodeNew()
    root_child0 = YGNodeNew()
    YGNodeInsertChild(root, root_child0, 0)

    measureCount = [0]
    root_child0_child0 = YGNodeNew()
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeSetContext(root_child0_child0, measureCount)
    YGNodeSetMeasureFunc(root_child0_child0, _measure)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert measureCount[0] == 1
    YGNodeFreeRecursive(root)


@pytest.mark.parametrize(
    "min_width,max_width,min_height,max_height",
    [
        (10, 10, 10, 10),
        ("10%", "10%", "10%", "10%"),
        ("10%", "10%", 10, 10),
        (10, 10, "10%", "10%"),
    ],
)
def test_dont_measure_when_min_equals_max_variants(min_width, max_width, min_height, max_height):
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    measureCount = [0]
    child = YGNodeNew()
    YGNodeSetContext(child, measureCount)
    YGNodeSetMeasureFunc(child, _measure)

    if isinstance(min_width, str):
        YGNodeStyleSetMinWidthPercent(child, float(min_width[:-1]))
        YGNodeStyleSetMaxWidthPercent(child, float(max_width[:-1]))
    else:
        YGNodeStyleSetMinWidth(child, min_width)
        YGNodeStyleSetMaxWidth(child, max_width)

    if isinstance(min_height, str):
        YGNodeStyleSetMinHeightPercent(child, float(min_height[:-1]))
        YGNodeStyleSetMaxHeightPercent(child, float(max_height[:-1]))
    else:
        YGNodeStyleSetMinHeight(child, min_height)
        YGNodeStyleSetMaxHeight(child, max_height)

    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert measureCount[0] == 0
    assert YGNodeLayoutGetLeft(child) == 0
    assert YGNodeLayoutGetTop(child) == 0
    assert YGNodeLayoutGetWidth(child) == 10
    assert YGNodeLayoutGetHeight(child) == 10

    YGNodeFreeRecursive(root)


def test_measure_nodes_with_margin_auto_and_stretch():
    root = YGNodeNew()
    YGNodeStyleSetWidth(root, 500)
    YGNodeStyleSetHeight(root, 500)

    child = YGNodeNew()
    YGNodeSetMeasureFunc(child, _measure)
    YGNodeStyleSetMarginAuto(child, YGEdge.YGEdgeLeft)
    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(child) == 490
    assert YGNodeLayoutGetTop(child) == 0
    assert YGNodeLayoutGetWidth(child) == 10
    assert YGNodeLayoutGetHeight(child) == 10

    YGNodeFreeRecursive(root)


def test_measure_enough_size_should_be_in_single_line():
    root = YGNodeNew()
    YGNodeStyleSetWidth(root, 100)

    child = YGNodeNew()
    YGNodeStyleSetAlignSelf(child, YGAlign.YGAlignFlexStart)
    YGNodeSetMeasureFunc(child, _simulate_wrapping_text)
    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetWidth(child) == 68
    assert YGNodeLayoutGetHeight(child) == 16

    YGNodeFreeRecursive(root)


def test_measure_not_enough_size_should_wrap():
    root = YGNodeNew()
    YGNodeStyleSetWidth(root, 55)

    child = YGNodeNew()
    YGNodeStyleSetAlignSelf(child, YGAlign.YGAlignFlexStart)
    YGNodeSetMeasureFunc(child, _simulate_wrapping_text)
    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetWidth(child) == 50
    assert YGNodeLayoutGetHeight(child) == 32

    YGNodeFreeRecursive(root)


def test_measure_zero_space_should_grow():
    root = YGNodeNew()
    YGNodeStyleSetHeight(root, 200)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionColumn)
    YGNodeStyleSetFlexGrow(root, 0)

    measureCount = [0]
    child = YGNodeNew()
    YGNodeStyleSetFlexDirection(child, YGFlexDirection.YGFlexDirectionColumn)
    YGNodeStyleSetPadding(child, YGEdge.YGEdgeAll, 100)
    YGNodeSetContext(child, measureCount)
    YGNodeSetMeasureFunc(child, _measure)
    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, 282, float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetWidth(child) == 282
    assert YGNodeLayoutGetTop(child) == 0
    YGNodeFreeRecursive(root)


def test_cannot_add_child_to_node_with_measure_func():
    root = YGNodeNew()
    YGNodeSetMeasureFunc(root, _measure)
    child = YGNodeNew()
    with pytest.raises(AssertionError):
        YGNodeInsertChild(root, child, 0)
    YGNodeFree(child)
    YGNodeFreeRecursive(root)


def test_cannot_add_nonnull_measure_func_to_non_leaf_node():
    root = YGNodeNew()
    YGNodeInsertChild(root, YGNodeNew(), 0)
    with pytest.raises(AssertionError):
        YGNodeSetMeasureFunc(root, _measure)
    YGNodeFreeRecursive(root)


def test_can_nullify_measure_func_on_any_node():
    root = YGNodeNew()
    YGNodeInsertChild(root, YGNodeNew(), 0)
    YGNodeSetMeasureFunc(root, None)
    assert not YGNodeHasMeasureFunc(root)
    YGNodeFreeRecursive(root)


def test_cant_call_negative_measure():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionColumn)
    YGNodeStyleSetWidth(root, 50)
    YGNodeStyleSetHeight(root, 10)

    child = YGNodeNewWithConfig(config)
    YGNodeSetMeasureFunc(child, _measure_assert_negative)
    YGNodeStyleSetMargin(child, YGEdge.YGEdgeTop, 20)
    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_cant_call_negative_measure_horizontal():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(root, 10)
    YGNodeStyleSetHeight(root, 20)

    child = YGNodeNewWithConfig(config)
    YGNodeSetMeasureFunc(child, _measure_assert_negative)
    YGNodeStyleSetMargin(child, YGEdge.YGEdgeStart, 20)
    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_percent_with_text_node():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifySpaceBetween)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 80)

    child0 = YGNodeNewWithConfig(config)
    YGNodeInsertChild(root, child0, 0)

    child1 = YGNodeNewWithConfig(config)
    YGNodeSetMeasureFunc(child1, _measure_90_10)
    YGNodeStyleSetMaxWidthPercent(child1, 50)
    YGNodeStyleSetPaddingPercent(child1, YGEdge.YGEdgeTop, 50)
    YGNodeInsertChild(root, child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(child0) == 0
    assert YGNodeLayoutGetTop(child0) == 40
    assert YGNodeLayoutGetWidth(child0) == 0
    assert YGNodeLayoutGetHeight(child0) == 0

    assert YGNodeLayoutGetLeft(child1) == 50
    assert YGNodeLayoutGetTop(child1) == 10
    assert YGNodeLayoutGetWidth(child1) == 50
    assert YGNodeLayoutGetHeight(child1) == 60

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


@pytest.mark.parametrize(
    "setter_name,expected_tops,expected_heights",
    [
        ("margin", [0, 100, 50, 100], [100, 100, 100, 100]),
        ("padding", [0, 0, 0, 0], [100, 100, 150, 200]),
        ("padding_margin", [0, 0, 50, 100], [100, 100, 150, 200]),
    ],
)
def test_percent_margin_and_padding_with_measure_func_variants(setter_name, expected_tops, expected_heights):
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    if setter_name != "margin":
        YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
        YGNodeStyleSetAlignContent(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 500)
    YGNodeStyleSetHeight(root, 500)

    children = [YGNodeNewWithConfig(config) for _ in range(4)]

    YGNodeStyleSetWidth(children[0], 100)
    YGNodeStyleSetHeight(children[0], 100)
    if setter_name in ("margin", "padding_margin"):
        YGNodeStyleSetMargin(children[0], YGEdge.YGEdgeTop, 0)
    if setter_name in ("padding", "padding_margin"):
        YGNodeStyleSetPadding(children[0], YGEdge.YGEdgeTop, 0)
    YGNodeSetMeasureFunc(children[0], _measure_100_100)

    YGNodeStyleSetWidth(children[1], 100)
    YGNodeStyleSetHeight(children[1], 100)
    if setter_name == "margin":
        YGNodeStyleSetMargin(children[1], YGEdge.YGEdgeTop, 100)
    if setter_name in ("padding", "padding_margin"):
        YGNodeStyleSetPadding(children[1], YGEdge.YGEdgeTop, 100)
    YGNodeSetMeasureFunc(children[1], _measure_100_100)

    if setter_name == "margin":
        YGNodeStyleSetWidth(children[2], 100)
        YGNodeStyleSetHeight(children[2], 100)
        YGNodeStyleSetMarginPercent(children[2], YGEdge.YGEdgeTop, 10)
        YGNodeStyleSetWidth(children[3], 100)
        YGNodeStyleSetHeight(children[3], 100)
        YGNodeStyleSetMarginPercent(children[3], YGEdge.YGEdgeTop, 20)
    elif setter_name == "padding":
        YGNodeStyleSetPaddingPercent(children[2], YGEdge.YGEdgeTop, 10)
        YGNodeStyleSetPaddingPercent(children[3], YGEdge.YGEdgeTop, 20)
    else:
        YGNodeStyleSetPaddingPercent(children[2], YGEdge.YGEdgeTop, 10)
        YGNodeStyleSetMarginPercent(children[2], YGEdge.YGEdgeTop, 10)
        YGNodeStyleSetPaddingPercent(children[3], YGEdge.YGEdgeTop, 20)
        YGNodeStyleSetMarginPercent(children[3], YGEdge.YGEdgeTop, 20)
    YGNodeSetMeasureFunc(children[2], _measure_100_100)
    YGNodeSetMeasureFunc(children[3], _measure_100_100)

    for index, child in enumerate(children):
        YGNodeInsertChild(root, child, index)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    for index, child in enumerate(children):
        assert YGNodeLayoutGetLeft(child) == index * 100
        assert YGNodeLayoutGetTop(child) == expected_tops[index]
        assert YGNodeLayoutGetWidth(child) == 100
        assert YGNodeLayoutGetHeight(child) == expected_heights[index]

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_measure_content_box():
    root = YGNodeNew()
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 200)
    YGNodeStyleSetBoxSizing(root, YGBoxSizing.YGBoxSizingContentBox)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeAll, 5)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 10)

    measureCount = [0]
    child = YGNodeNew()
    YGNodeSetContext(child, measureCount)
    YGNodeSetMeasureFunc(child, _measure_half_width_height)
    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert measureCount[0] == 1
    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 130
    assert YGNodeLayoutGetHeight(root) == 230
    assert YGNodeLayoutGetLeft(child) == 15
    assert YGNodeLayoutGetTop(child) == 15
    assert YGNodeLayoutGetWidth(child) == 100
    assert YGNodeLayoutGetHeight(child) == 100

    YGNodeFreeRecursive(root)


def test_measure_border_box():
    root = YGNodeNew()
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 200)
    YGNodeStyleSetBoxSizing(root, YGBoxSizing.YGBoxSizingBorderBox)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeAll, 5)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 10)

    measureCount = [0]
    child = YGNodeNew()
    YGNodeSetContext(child, measureCount)
    YGNodeSetMeasureFunc(child, _measure_half_width_height)
    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert measureCount[0] == 1
    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 200
    assert YGNodeLayoutGetLeft(child) == 15
    assert YGNodeLayoutGetTop(child) == 15
    assert YGNodeLayoutGetWidth(child) == 70
    assert YGNodeLayoutGetHeight(child) == 85

    YGNodeFreeRecursive(root)
