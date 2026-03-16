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
    YGNodeStyleSetBorder,
    YGNodeStyleSetFlexGrow,
    YGNodeStyleSetHeight,
    YGNodeStyleSetJustifyContent,
    YGNodeStyleSetPositionType,
    YGNodeStyleSetWidth,
    YGPositionType,
)


def test_border_no_size():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 10)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetWidth(root) == 20
    assert YGNodeLayoutGetHeight(root) == 20
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetWidth(root) == 20
    assert YGNodeLayoutGetHeight(root) == 20
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_border_container_match_child():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 10)
    child = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child, 10)
    YGNodeStyleSetHeight(child, 10)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetWidth(root) == 30
    assert YGNodeLayoutGetHeight(root) == 30
    assert YGNodeLayoutGetLeft(child) == 10
    assert YGNodeLayoutGetTop(child) == 10
    assert YGNodeLayoutGetWidth(child) == 10
    assert YGNodeLayoutGetHeight(child) == 10
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetLeft(child) == 10
    assert YGNodeLayoutGetTop(child) == 10
    assert YGNodeLayoutGetWidth(child) == 10
    assert YGNodeLayoutGetHeight(child) == 10
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_border_flex_child():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 10)
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


def test_border_stretch_child():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 10)
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


def test_border_center_child():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeStart, 10)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeEnd, 20)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeBottom, 20)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyCenter)
    child = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(child, 10)
    YGNodeStyleSetWidth(child, 10)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetLeft(child) == 40
    assert YGNodeLayoutGetTop(child) == 35
    assert YGNodeLayoutGetWidth(child) == 10
    assert YGNodeLayoutGetHeight(child) == 10
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetLeft(child) == 50
    assert YGNodeLayoutGetTop(child) == 35
    assert YGNodeLayoutGetWidth(child) == 10
    assert YGNodeLayoutGetHeight(child) == 10
    YGNodeFreeRecursive(root)
    YGConfigFree(config)
