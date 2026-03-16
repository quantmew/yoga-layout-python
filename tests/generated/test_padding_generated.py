import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from yoga import (  # noqa: E402
    YGAlign,
    YGConfigFree,
    YGConfigNew,
    YGDirection,
    YGEdge,
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
    YGNodeStyleSetFlexGrow,
    YGNodeStyleSetHeight,
    YGNodeStyleSetJustifyContent,
    YGNodeStyleSetPadding,
    YGNodeStyleSetPositionType,
    YGNodeStyleSetWidth,
    YGNodeStyleSetWidthPercent,
    YGPositionType,
)


def test_padding_no_size():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeAll, 10)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetWidth(root) == 20
    assert YGNodeLayoutGetHeight(root) == 20
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetWidth(root) == 20
    assert YGNodeLayoutGetHeight(root) == 20
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_padding_container_match_child():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeAll, 10)
    child = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child, 10)
    YGNodeStyleSetHeight(child, 10)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetWidth(root) == 30
    assert YGNodeLayoutGetHeight(root) == 30
    assert YGNodeLayoutGetLeft(child) == 10
    assert YGNodeLayoutGetTop(child) == 10
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetLeft(child) == 10
    assert YGNodeLayoutGetTop(child) == 10
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_padding_flex_child():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeAll, 10)
    child = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child, 10)
    YGNodeStyleSetFlexGrow(child, 1)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetLeft(child) == 10
    assert YGNodeLayoutGetTop(child) == 10
    assert YGNodeLayoutGetWidth(child) == 10
    assert YGNodeLayoutGetHeight(child) == 80
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetLeft(child) == 80
    assert YGNodeLayoutGetTop(child) == 10
    assert YGNodeLayoutGetWidth(child) == 10
    assert YGNodeLayoutGetHeight(child) == 80
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_padding_stretch_child():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeAll, 10)
    child = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(child, 10)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetLeft(child) == 10
    assert YGNodeLayoutGetTop(child) == 10
    assert YGNodeLayoutGetWidth(child) == 80
    assert YGNodeLayoutGetHeight(child) == 10
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetLeft(child) == 10
    assert YGNodeLayoutGetTop(child) == 10
    assert YGNodeLayoutGetWidth(child) == 80
    assert YGNodeLayoutGetHeight(child) == 10
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_padding_center_child():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeStart, 10)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeEnd, 20)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeBottom, 20)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyCenter)
    child = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(child, 10)
    YGNodeStyleSetWidth(child, 10)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetLeft(child) == 40
    assert YGNodeLayoutGetTop(child) == 35
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetLeft(child) == 50
    assert YGNodeLayoutGetTop(child) == 35
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_child_with_padding_align_end():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 200)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyFlexEnd)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexEnd)
    child = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child, 100)
    YGNodeStyleSetHeight(child, 100)
    YGNodeStyleSetPadding(child, YGEdge.YGEdgeAll, 20)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetLeft(child) == 100
    assert YGNodeLayoutGetTop(child) == 100
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetLeft(child) == 0
    assert YGNodeLayoutGetTop(child) == 100
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_physical_and_relative_edge_defined():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 200)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeLeft, 20)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeEnd, 50)
    child = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(child, 100)
    YGNodeStyleSetHeight(child, 50)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetLeft(child) == 20
    assert YGNodeLayoutGetTop(child) == 0
    assert YGNodeLayoutGetWidth(child) == 130
    assert YGNodeLayoutGetHeight(child) == 50
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetLeft(child) == 50
    assert YGNodeLayoutGetTop(child) == 0
    assert YGNodeLayoutGetWidth(child) == 150
    assert YGNodeLayoutGetHeight(child) == 50
    YGNodeFreeRecursive(root)
    YGConfigFree(config)
