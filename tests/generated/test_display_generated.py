import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from yoga import (  # noqa: E402
    YGConfigFree,
    YGConfigNew,
    YGDirection,
    YGDisplay,
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
    YGNodeStyleSetDisplay,
    YGNodeStyleSetFlexBasisPercent,
    YGNodeStyleSetFlexDirection,
    YGNodeStyleSetFlexGrow,
    YGNodeStyleSetFlexShrink,
    YGNodeStyleSetHeight,
    YGNodeStyleSetMargin,
    YGNodeStyleSetPadding,
    YGNodeStyleSetPosition,
    YGNodeStyleSetPositionType,
    YGNodeStyleSetWidth,
    YGPositionType,
)


def _assert_layout(node, left, top, width, height):
    assert YGNodeLayoutGetLeft(node) == left
    assert YGNodeLayoutGetTop(node) == top
    assert YGNodeLayoutGetWidth(node) == width
    assert YGNodeLayoutGetHeight(node) == height


def test_display_none():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child0, 1)
    YGNodeInsertChild(root, child0, 0)

    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child1, 1)
    YGNodeStyleSetDisplay(child1, YGDisplay.YGDisplayNone)
    YGNodeInsertChild(root, child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 100, 100)
    _assert_layout(child0, 0, 0, 100, 100)
    _assert_layout(child1, 0, 0, 0, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(child0, 0, 0, 100, 100)
    _assert_layout(child1, 0, 0, 0, 0)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_display_none_fixed_size():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child0, 1)
    YGNodeInsertChild(root, child0, 0)

    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child1, 20)
    YGNodeStyleSetHeight(child1, 20)
    YGNodeStyleSetDisplay(child1, YGDisplay.YGDisplayNone)
    YGNodeInsertChild(root, child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child0, 0, 0, 100, 100)
    _assert_layout(child1, 0, 0, 0, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(child0, 0, 0, 100, 100)
    _assert_layout(child1, 0, 0, 0, 0)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_display_none_with_margin():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child0, 20)
    YGNodeStyleSetHeight(child0, 20)
    YGNodeStyleSetDisplay(child0, YGDisplay.YGDisplayNone)
    YGNodeStyleSetMargin(child0, YGEdge.YGEdgeAll, 10)
    YGNodeInsertChild(root, child0, 0)

    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child1, 1)
    YGNodeInsertChild(root, child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child0, 0, 0, 0, 0)
    _assert_layout(child1, 0, 0, 100, 100)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(child0, 0, 0, 0, 0)
    _assert_layout(child1, 0, 0, 100, 100)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_display_none_with_child():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child0, 1)
    YGNodeStyleSetFlexShrink(child0, 1)
    YGNodeStyleSetFlexBasisPercent(child0, 0)
    YGNodeInsertChild(root, child0, 0)

    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child1, 1)
    YGNodeStyleSetFlexShrink(child1, 1)
    YGNodeStyleSetFlexBasisPercent(child1, 0)
    YGNodeStyleSetDisplay(child1, YGDisplay.YGDisplayNone)
    YGNodeInsertChild(root, child1, 1)

    child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child1_child0, 1)
    YGNodeStyleSetFlexShrink(child1_child0, 1)
    YGNodeStyleSetFlexBasisPercent(child1_child0, 0)
    YGNodeStyleSetWidth(child1_child0, 20)
    YGNodeInsertChild(child1, child1_child0, 0)

    child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child2, 1)
    YGNodeStyleSetFlexShrink(child2, 1)
    YGNodeStyleSetFlexBasisPercent(child2, 0)
    YGNodeInsertChild(root, child2, 2)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child0, 0, 0, 50, 100)
    _assert_layout(child1, 0, 0, 0, 0)
    _assert_layout(child1_child0, 0, 0, 0, 0)
    _assert_layout(child2, 50, 0, 50, 100)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(child0, 50, 0, 50, 100)
    _assert_layout(child1, 0, 0, 0, 0)
    _assert_layout(child1_child0, 0, 0, 0, 0)
    _assert_layout(child2, 0, 0, 50, 100)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_display_none_with_position():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child0, 1)
    YGNodeInsertChild(root, child0, 0)

    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child1, 1)
    YGNodeStyleSetDisplay(child1, YGDisplay.YGDisplayNone)
    YGNodeStyleSetPosition(child1, YGEdge.YGEdgeTop, 10)
    YGNodeInsertChild(root, child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child0, 0, 0, 100, 100)
    _assert_layout(child1, 0, 0, 0, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(child0, 0, 0, 100, 100)
    _assert_layout(child1, 0, 0, 0, 0)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_display_none_with_position_absolute():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetDisplay(child0, YGDisplay.YGDisplayNone)
    YGNodeStyleSetPositionType(child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(child0, 100)
    YGNodeStyleSetHeight(child0, 100)
    YGNodeInsertChild(root, child0, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child0, 0, 0, 0, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(child0, 0, 0, 0, 0)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_display_contents():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetDisplay(child0, YGDisplay.YGDisplayContents)
    YGNodeInsertChild(root, child0, 0)

    child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child0_child0, 1)
    YGNodeStyleSetFlexShrink(child0_child0, 1)
    YGNodeStyleSetFlexBasisPercent(child0_child0, 0)
    YGNodeStyleSetHeight(child0_child0, 10)
    YGNodeInsertChild(child0, child0_child0, 0)

    child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child0_child1, 1)
    YGNodeStyleSetFlexShrink(child0_child1, 1)
    YGNodeStyleSetFlexBasisPercent(child0_child1, 0)
    YGNodeStyleSetHeight(child0_child1, 20)
    YGNodeInsertChild(child0, child0_child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child0, 0, 0, 0, 0)
    _assert_layout(child0_child0, 0, 0, 50, 10)
    _assert_layout(child0_child1, 50, 0, 50, 20)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(child0, 0, 0, 0, 0)
    _assert_layout(child0_child0, 50, 0, 50, 10)
    _assert_layout(child0_child1, 0, 0, 50, 20)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_display_contents_fixed_size():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetDisplay(child0, YGDisplay.YGDisplayContents)
    YGNodeStyleSetWidth(child0, 50)
    YGNodeStyleSetHeight(child0, 50)
    YGNodeInsertChild(root, child0, 0)

    child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child0_child0, 1)
    YGNodeStyleSetFlexShrink(child0_child0, 1)
    YGNodeStyleSetFlexBasisPercent(child0_child0, 0)
    YGNodeStyleSetHeight(child0_child0, 10)
    YGNodeInsertChild(child0, child0_child0, 0)

    child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child0_child1, 1)
    YGNodeStyleSetFlexShrink(child0_child1, 1)
    YGNodeStyleSetFlexBasisPercent(child0_child1, 0)
    YGNodeStyleSetHeight(child0_child1, 20)
    YGNodeInsertChild(child0, child0_child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child0, 0, 0, 0, 0)
    _assert_layout(child0_child0, 0, 0, 50, 10)
    _assert_layout(child0_child1, 50, 0, 50, 20)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(child0, 0, 0, 0, 0)
    _assert_layout(child0_child0, 50, 0, 50, 10)
    _assert_layout(child0_child1, 0, 0, 50, 20)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_display_contents_with_margin():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child0, 20)
    YGNodeStyleSetHeight(child0, 20)
    YGNodeStyleSetDisplay(child0, YGDisplay.YGDisplayContents)
    YGNodeStyleSetMargin(child0, YGEdge.YGEdgeAll, 10)
    YGNodeInsertChild(root, child0, 0)

    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child1, 1)
    YGNodeInsertChild(root, child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child0, 0, 0, 0, 0)
    _assert_layout(child1, 0, 0, 100, 100)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(child0, 0, 0, 0, 0)
    _assert_layout(child1, 0, 0, 100, 100)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_display_contents_with_padding():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetDisplay(child0, YGDisplay.YGDisplayContents)
    YGNodeStyleSetPadding(child0, YGEdge.YGEdgeAll, 10)
    YGNodeInsertChild(root, child0, 0)

    child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child0_child0, 1)
    YGNodeStyleSetFlexShrink(child0_child0, 1)
    YGNodeStyleSetFlexBasisPercent(child0_child0, 0)
    YGNodeStyleSetHeight(child0_child0, 10)
    YGNodeInsertChild(child0, child0_child0, 0)

    child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child0_child1, 1)
    YGNodeStyleSetFlexShrink(child0_child1, 1)
    YGNodeStyleSetFlexBasisPercent(child0_child1, 0)
    YGNodeStyleSetHeight(child0_child1, 20)
    YGNodeInsertChild(child0, child0_child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child0, 0, 0, 0, 0)
    _assert_layout(child0_child0, 0, 0, 50, 10)
    _assert_layout(child0_child1, 50, 0, 50, 20)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(child0, 0, 0, 0, 0)
    _assert_layout(child0_child0, 50, 0, 50, 10)
    _assert_layout(child0_child1, 0, 0, 50, 20)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_display_contents_with_position():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetDisplay(child0, YGDisplay.YGDisplayContents)
    YGNodeStyleSetPosition(child0, YGEdge.YGEdgeTop, 10)
    YGNodeInsertChild(root, child0, 0)

    child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child0_child0, 1)
    YGNodeStyleSetFlexShrink(child0_child0, 1)
    YGNodeStyleSetFlexBasisPercent(child0_child0, 0)
    YGNodeStyleSetHeight(child0_child0, 10)
    YGNodeInsertChild(child0, child0_child0, 0)

    child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child0_child1, 1)
    YGNodeStyleSetFlexShrink(child0_child1, 1)
    YGNodeStyleSetFlexBasisPercent(child0_child1, 0)
    YGNodeStyleSetHeight(child0_child1, 20)
    YGNodeInsertChild(child0, child0_child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child0, 0, 0, 0, 0)
    _assert_layout(child0_child0, 0, 0, 50, 10)
    _assert_layout(child0_child1, 50, 0, 50, 20)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(child0, 0, 0, 0, 0)
    _assert_layout(child0_child0, 50, 0, 50, 10)
    _assert_layout(child0_child1, 0, 0, 50, 20)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_display_contents_with_position_absolute():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetDisplay(child0, YGDisplay.YGDisplayContents)
    YGNodeStyleSetPositionType(child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(child0, 50)
    YGNodeStyleSetHeight(child0, 50)
    YGNodeInsertChild(root, child0, 0)

    child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child0_child0, 1)
    YGNodeStyleSetFlexShrink(child0_child0, 1)
    YGNodeStyleSetFlexBasisPercent(child0_child0, 0)
    YGNodeStyleSetHeight(child0_child0, 10)
    YGNodeInsertChild(child0, child0_child0, 0)

    child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child0_child1, 1)
    YGNodeStyleSetFlexShrink(child0_child1, 1)
    YGNodeStyleSetFlexBasisPercent(child0_child1, 0)
    YGNodeStyleSetHeight(child0_child1, 20)
    YGNodeInsertChild(child0, child0_child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child0, 0, 0, 0, 0)
    _assert_layout(child0_child0, 0, 0, 50, 10)
    _assert_layout(child0_child1, 50, 0, 50, 20)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(child0, 0, 0, 0, 0)
    _assert_layout(child0_child0, 50, 0, 50, 10)
    _assert_layout(child0_child1, 0, 0, 50, 20)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_display_contents_nested():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetDisplay(child0, YGDisplay.YGDisplayContents)
    YGNodeInsertChild(root, child0, 0)

    child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetDisplay(child0_child0, YGDisplay.YGDisplayContents)
    YGNodeInsertChild(child0, child0_child0, 0)

    gc0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(gc0, 1)
    YGNodeStyleSetFlexShrink(gc0, 1)
    YGNodeStyleSetFlexBasisPercent(gc0, 0)
    YGNodeStyleSetHeight(gc0, 10)
    YGNodeInsertChild(child0_child0, gc0, 0)

    gc1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(gc1, 1)
    YGNodeStyleSetFlexShrink(gc1, 1)
    YGNodeStyleSetFlexBasisPercent(gc1, 0)
    YGNodeStyleSetHeight(gc1, 20)
    YGNodeInsertChild(child0_child0, gc1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child0, 0, 0, 0, 0)
    _assert_layout(child0_child0, 0, 0, 0, 0)
    _assert_layout(gc0, 0, 0, 50, 10)
    _assert_layout(gc1, 50, 0, 50, 20)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(child0, 0, 0, 0, 0)
    _assert_layout(child0_child0, 0, 0, 0, 0)
    _assert_layout(gc0, 50, 0, 50, 10)
    _assert_layout(gc1, 0, 0, 50, 20)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_display_contents_with_siblings():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child0, 1)
    YGNodeStyleSetFlexShrink(child0, 1)
    YGNodeStyleSetFlexBasisPercent(child0, 0)
    YGNodeStyleSetHeight(child0, 30)
    YGNodeInsertChild(root, child0, 0)

    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetDisplay(child1, YGDisplay.YGDisplayContents)
    YGNodeInsertChild(root, child1, 1)

    child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child1_child0, 1)
    YGNodeStyleSetFlexShrink(child1_child0, 1)
    YGNodeStyleSetFlexBasisPercent(child1_child0, 0)
    YGNodeStyleSetHeight(child1_child0, 10)
    YGNodeInsertChild(child1, child1_child0, 0)

    child1_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child1_child1, 1)
    YGNodeStyleSetFlexShrink(child1_child1, 1)
    YGNodeStyleSetFlexBasisPercent(child1_child1, 0)
    YGNodeStyleSetHeight(child1_child1, 20)
    YGNodeInsertChild(child1, child1_child1, 1)

    child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child2, 1)
    YGNodeStyleSetFlexShrink(child2, 1)
    YGNodeStyleSetFlexBasisPercent(child2, 0)
    YGNodeStyleSetHeight(child2, 30)
    YGNodeInsertChild(root, child2, 2)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(child0, 0, 0, 25, 30)
    _assert_layout(child1, 0, 0, 0, 0)
    _assert_layout(child1_child0, 25, 0, 25, 10)
    _assert_layout(child1_child1, 50, 0, 25, 20)
    _assert_layout(child2, 75, 0, 25, 30)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(child0, 75, 0, 25, 30)
    _assert_layout(child1, 0, 0, 0, 0)
    _assert_layout(child1_child0, 50, 0, 25, 10)
    _assert_layout(child1_child1, 25, 0, 25, 20)
    _assert_layout(child2, 0, 0, 25, 30)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)
