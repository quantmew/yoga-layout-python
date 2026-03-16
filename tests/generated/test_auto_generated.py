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
    YGNodeStyleSetFlexBasisAuto,
    YGNodeStyleSetFlexDirection,
    YGNodeStyleSetHeight,
    YGNodeStyleSetHeightAuto,
    YGNodeStyleSetMarginAuto,
    YGNodeStyleSetPositionAuto,
    YGNodeStyleSetPositionType,
    YGNodeStyleSetWidth,
    YGNodeStyleSetWidthAuto,
    YGPositionType,
)


def test_auto_width():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidthAuto(root)
    YGNodeStyleSetHeight(root, 50)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    children = []
    for index in range(3):
        child = YGNodeNewWithConfig(config)
        YGNodeStyleSetWidth(child, 50)
        YGNodeStyleSetHeight(child, 50)
        YGNodeInsertChild(root, child, index)
        children.append(child)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetWidth(root) == 150
    assert YGNodeLayoutGetHeight(root) == 50
    assert [YGNodeLayoutGetLeft(child) for child in children] == [0, 50, 100]
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert [YGNodeLayoutGetLeft(child) for child in children] == [100, 50, 0]
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_auto_height():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 50)
    YGNodeStyleSetHeightAuto(root)
    children = []
    for index in range(3):
        child = YGNodeNewWithConfig(config)
        YGNodeStyleSetWidth(child, 50)
        YGNodeStyleSetHeight(child, 50)
        YGNodeInsertChild(root, child, index)
        children.append(child)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetWidth(root) == 50
    assert YGNodeLayoutGetHeight(root) == 150
    assert [YGNodeLayoutGetTop(child) for child in children] == [0, 50, 100]
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert [YGNodeLayoutGetTop(child) for child in children] == [0, 50, 100]
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_auto_flex_basis():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 50)
    YGNodeStyleSetFlexBasisAuto(root)
    children = []
    for index in range(3):
        child = YGNodeNewWithConfig(config)
        YGNodeStyleSetWidth(child, 50)
        YGNodeStyleSetHeight(child, 50)
        YGNodeInsertChild(root, child, index)
        children.append(child)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetWidth(root) == 50
    assert YGNodeLayoutGetHeight(root) == 150
    assert [YGNodeLayoutGetTop(child) for child in children] == [0, 50, 100]
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert [YGNodeLayoutGetTop(child) for child in children] == [0, 50, 100]
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_auto_position():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 50)
    YGNodeStyleSetHeight(root, 50)
    child = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child, 25)
    YGNodeStyleSetHeight(child, 25)
    YGNodeStyleSetPositionAuto(child, YGEdge.YGEdgeRight)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetLeft(child) == 0
    assert YGNodeLayoutGetTop(child) == 0
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetLeft(child) == 25
    assert YGNodeLayoutGetTop(child) == 0
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_auto_margin():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 50)
    YGNodeStyleSetHeight(root, 50)
    child = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child, 25)
    YGNodeStyleSetHeight(child, 25)
    YGNodeStyleSetMarginAuto(child, YGEdge.YGEdgeLeft)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetLeft(child) == 25
    assert YGNodeLayoutGetTop(child) == 0
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetLeft(child) == 25
    assert YGNodeLayoutGetTop(child) == 0
    YGNodeFreeRecursive(root)
    YGConfigFree(config)
