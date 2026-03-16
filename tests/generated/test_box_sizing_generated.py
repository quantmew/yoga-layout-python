import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from yoga import *  # noqa: E402,F403

def test_box_sizing_content_box_simple():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeAll, 5)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 10)
    YGNodeStyleSetBoxSizing(root, YGBoxSizing.YGBoxSizingContentBox)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 130
    assert YGNodeLayoutGetHeight(root) == 130

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 130
    assert YGNodeLayoutGetHeight(root) == 130

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_border_box_simple():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeAll, 5)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 10)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_content_box_percent():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0, 50)
    YGNodeStyleSetHeightPercent(root_child0, 25)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeAll, 4)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeAll, 16)
    YGNodeStyleSetBoxSizing(root_child0, YGBoxSizing.YGBoxSizingContentBox)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 90
    assert YGNodeLayoutGetHeight(root_child0) == 65

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 10
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 90
    assert YGNodeLayoutGetHeight(root_child0) == 65

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_border_box_percent():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0, 50)
    YGNodeStyleSetHeightPercent(root_child0, 25)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeAll, 4)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeAll, 16)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 40

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 40

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_content_box_absolute():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeightPercent(root_child0, 25)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeAll, 12)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeAll, 8)
    YGNodeStyleSetBoxSizing(root_child0, YGBoxSizing.YGBoxSizingContentBox)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0) == 65

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0) == 65

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_border_box_absolute():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeightPercent(root_child0, 25)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeAll, 12)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeAll, 8)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0) == 40

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0) == 40

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_content_box_comtaining_block():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeAll, 12)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 8)
    YGNodeStyleSetBoxSizing(root, YGBoxSizing.YGBoxSizingContentBox)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 50)
    YGNodeStyleSetHeightPercent(root_child0_child0, 25)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 140

    assert YGNodeLayoutGetLeft(root_child0) == 20
    assert YGNodeLayoutGetTop(root_child0) == 20
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 31

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 140

    assert YGNodeLayoutGetLeft(root_child0) == 20
    assert YGNodeLayoutGetTop(root_child0) == 20
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 31

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_border_box_comtaining_block():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeAll, 12)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 8)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 50)
    YGNodeStyleSetHeightPercent(root_child0_child0, 25)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 20
    assert YGNodeLayoutGetTop(root_child0) == 20
    assert YGNodeLayoutGetWidth(root_child0) == 60
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 21

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 20
    assert YGNodeLayoutGetTop(root_child0) == 20
    assert YGNodeLayoutGetWidth(root_child0) == 60
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child0_child0) == 10
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 21

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_content_box_padding_only():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeAll, 5)
    YGNodeStyleSetBoxSizing(root, YGBoxSizing.YGBoxSizingContentBox)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 110
    assert YGNodeLayoutGetHeight(root) == 110

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 110
    assert YGNodeLayoutGetHeight(root) == 110

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_content_box_padding_only_percent():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 150)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 75)
    YGNodeStyleSetPaddingPercent(root_child0, YGEdge.YGEdgeAll, 10)
    YGNodeStyleSetBoxSizing(root_child0, YGBoxSizing.YGBoxSizingContentBox)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 150

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 70
    assert YGNodeLayoutGetHeight(root_child0) == 95

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 150

    assert YGNodeLayoutGetLeft(root_child0) == 30
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 70
    assert YGNodeLayoutGetHeight(root_child0) == 95

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_border_box_padding_only():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeAll, 5)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_border_box_padding_only_percent():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 150)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 75)
    YGNodeStyleSetPaddingPercent(root_child0, YGEdge.YGEdgeAll, 10)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 150

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 75

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 150

    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 75

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_content_box_border_only():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 10)
    YGNodeStyleSetBoxSizing(root, YGBoxSizing.YGBoxSizingContentBox)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 120
    assert YGNodeLayoutGetHeight(root) == 120

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 120
    assert YGNodeLayoutGetHeight(root) == 120

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_content_box_border_only_percent():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0, 50)
    YGNodeStyleSetBoxSizing(root_child0, YGBoxSizing.YGBoxSizingContentBox)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 0

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_border_box_border_only():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 10)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_border_box_border_only_percent():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 0

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_content_box_no_padding_no_border():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetBoxSizing(root, YGBoxSizing.YGBoxSizingContentBox)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_border_box_no_padding_no_border():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_content_box_children():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeAll, 5)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 10)
    YGNodeStyleSetBoxSizing(root, YGBoxSizing.YGBoxSizingContentBox)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 25)
    YGNodeStyleSetHeight(root_child0, 25)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 25)
    YGNodeStyleSetHeight(root_child1, 25)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 25)
    YGNodeStyleSetHeight(root_child2, 25)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 25)
    YGNodeStyleSetHeight(root_child3, 25)
    YGNodeInsertChild(root, root_child3, 3)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 130
    assert YGNodeLayoutGetHeight(root) == 130

    assert YGNodeLayoutGetLeft(root_child0) == 15
    assert YGNodeLayoutGetTop(root_child0) == 15
    assert YGNodeLayoutGetWidth(root_child0) == 25
    assert YGNodeLayoutGetHeight(root_child0) == 25

    assert YGNodeLayoutGetLeft(root_child1) == 15
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 25
    assert YGNodeLayoutGetHeight(root_child1) == 25

    assert YGNodeLayoutGetLeft(root_child2) == 15
    assert YGNodeLayoutGetTop(root_child2) == 65
    assert YGNodeLayoutGetWidth(root_child2) == 25
    assert YGNodeLayoutGetHeight(root_child2) == 25

    assert YGNodeLayoutGetLeft(root_child3) == 15
    assert YGNodeLayoutGetTop(root_child3) == 90
    assert YGNodeLayoutGetWidth(root_child3) == 25
    assert YGNodeLayoutGetHeight(root_child3) == 25

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 130
    assert YGNodeLayoutGetHeight(root) == 130

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 15
    assert YGNodeLayoutGetWidth(root_child0) == 25
    assert YGNodeLayoutGetHeight(root_child0) == 25

    assert YGNodeLayoutGetLeft(root_child1) == 90
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 25
    assert YGNodeLayoutGetHeight(root_child1) == 25

    assert YGNodeLayoutGetLeft(root_child2) == 90
    assert YGNodeLayoutGetTop(root_child2) == 65
    assert YGNodeLayoutGetWidth(root_child2) == 25
    assert YGNodeLayoutGetHeight(root_child2) == 25

    assert YGNodeLayoutGetLeft(root_child3) == 90
    assert YGNodeLayoutGetTop(root_child3) == 90
    assert YGNodeLayoutGetWidth(root_child3) == 25
    assert YGNodeLayoutGetHeight(root_child3) == 25

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_border_box_children():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeAll, 5)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 10)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 25)
    YGNodeStyleSetHeight(root_child0, 25)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 25)
    YGNodeStyleSetHeight(root_child1, 25)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 25)
    YGNodeStyleSetHeight(root_child2, 25)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 25)
    YGNodeStyleSetHeight(root_child3, 25)
    YGNodeInsertChild(root, root_child3, 3)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 15
    assert YGNodeLayoutGetTop(root_child0) == 15
    assert YGNodeLayoutGetWidth(root_child0) == 25
    assert YGNodeLayoutGetHeight(root_child0) == 25

    assert YGNodeLayoutGetLeft(root_child1) == 15
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 25
    assert YGNodeLayoutGetHeight(root_child1) == 25

    assert YGNodeLayoutGetLeft(root_child2) == 15
    assert YGNodeLayoutGetTop(root_child2) == 65
    assert YGNodeLayoutGetWidth(root_child2) == 25
    assert YGNodeLayoutGetHeight(root_child2) == 25

    assert YGNodeLayoutGetLeft(root_child3) == 15
    assert YGNodeLayoutGetTop(root_child3) == 90
    assert YGNodeLayoutGetWidth(root_child3) == 25
    assert YGNodeLayoutGetHeight(root_child3) == 25

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 15
    assert YGNodeLayoutGetWidth(root_child0) == 25
    assert YGNodeLayoutGetHeight(root_child0) == 25

    assert YGNodeLayoutGetLeft(root_child1) == 60
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 25
    assert YGNodeLayoutGetHeight(root_child1) == 25

    assert YGNodeLayoutGetLeft(root_child2) == 60
    assert YGNodeLayoutGetTop(root_child2) == 65
    assert YGNodeLayoutGetWidth(root_child2) == 25
    assert YGNodeLayoutGetHeight(root_child2) == 25

    assert YGNodeLayoutGetLeft(root_child3) == 60
    assert YGNodeLayoutGetTop(root_child3) == 90
    assert YGNodeLayoutGetWidth(root_child3) == 25
    assert YGNodeLayoutGetHeight(root_child3) == 25

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_content_box_siblings():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 25)
    YGNodeStyleSetHeight(root_child0, 25)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 25)
    YGNodeStyleSetHeight(root_child1, 25)
    YGNodeStyleSetBoxSizing(root_child1, YGBoxSizing.YGBoxSizingContentBox)
    YGNodeStyleSetPadding(root_child1, YGEdge.YGEdgeAll, 10)
    YGNodeStyleSetBorder(root_child1, YGEdge.YGEdgeAll, 10)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 25)
    YGNodeStyleSetHeight(root_child2, 25)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 25)
    YGNodeStyleSetHeight(root_child3, 25)
    YGNodeInsertChild(root, root_child3, 3)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 25
    assert YGNodeLayoutGetHeight(root_child0) == 25

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 25
    assert YGNodeLayoutGetWidth(root_child1) == 65
    assert YGNodeLayoutGetHeight(root_child1) == 65

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 90
    assert YGNodeLayoutGetWidth(root_child2) == 25
    assert YGNodeLayoutGetHeight(root_child2) == 25

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 115
    assert YGNodeLayoutGetWidth(root_child3) == 25
    assert YGNodeLayoutGetHeight(root_child3) == 25

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 75
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 25
    assert YGNodeLayoutGetHeight(root_child0) == 25

    assert YGNodeLayoutGetLeft(root_child1) == 35
    assert YGNodeLayoutGetTop(root_child1) == 25
    assert YGNodeLayoutGetWidth(root_child1) == 65
    assert YGNodeLayoutGetHeight(root_child1) == 65

    assert YGNodeLayoutGetLeft(root_child2) == 75
    assert YGNodeLayoutGetTop(root_child2) == 90
    assert YGNodeLayoutGetWidth(root_child2) == 25
    assert YGNodeLayoutGetHeight(root_child2) == 25

    assert YGNodeLayoutGetLeft(root_child3) == 75
    assert YGNodeLayoutGetTop(root_child3) == 115
    assert YGNodeLayoutGetWidth(root_child3) == 25
    assert YGNodeLayoutGetHeight(root_child3) == 25

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_border_box_siblings():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 25)
    YGNodeStyleSetHeight(root_child0, 25)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 25)
    YGNodeStyleSetHeight(root_child1, 25)
    YGNodeStyleSetPadding(root_child1, YGEdge.YGEdgeAll, 10)
    YGNodeStyleSetBorder(root_child1, YGEdge.YGEdgeAll, 10)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 25)
    YGNodeStyleSetHeight(root_child2, 25)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 25)
    YGNodeStyleSetHeight(root_child3, 25)
    YGNodeInsertChild(root, root_child3, 3)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 25
    assert YGNodeLayoutGetHeight(root_child0) == 25

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 25
    assert YGNodeLayoutGetWidth(root_child1) == 40
    assert YGNodeLayoutGetHeight(root_child1) == 40

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 65
    assert YGNodeLayoutGetWidth(root_child2) == 25
    assert YGNodeLayoutGetHeight(root_child2) == 25

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 90
    assert YGNodeLayoutGetWidth(root_child3) == 25
    assert YGNodeLayoutGetHeight(root_child3) == 25

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 75
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 25
    assert YGNodeLayoutGetHeight(root_child0) == 25

    assert YGNodeLayoutGetLeft(root_child1) == 60
    assert YGNodeLayoutGetTop(root_child1) == 25
    assert YGNodeLayoutGetWidth(root_child1) == 40
    assert YGNodeLayoutGetHeight(root_child1) == 40

    assert YGNodeLayoutGetLeft(root_child2) == 75
    assert YGNodeLayoutGetTop(root_child2) == 65
    assert YGNodeLayoutGetWidth(root_child2) == 25
    assert YGNodeLayoutGetHeight(root_child2) == 25

    assert YGNodeLayoutGetLeft(root_child3) == 75
    assert YGNodeLayoutGetTop(root_child3) == 90
    assert YGNodeLayoutGetWidth(root_child3) == 25
    assert YGNodeLayoutGetHeight(root_child3) == 25

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_content_box_max_width():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMaxWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 25)
    YGNodeStyleSetBoxSizing(root_child0, YGBoxSizing.YGBoxSizingContentBox)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeAll, 5)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeAll, 15)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 25)
    YGNodeStyleSetHeight(root_child1, 25)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 90
    assert YGNodeLayoutGetHeight(root_child0) == 65

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 65
    assert YGNodeLayoutGetWidth(root_child1) == 25
    assert YGNodeLayoutGetHeight(root_child1) == 25

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 10
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 90
    assert YGNodeLayoutGetHeight(root_child0) == 65

    assert YGNodeLayoutGetLeft(root_child1) == 75
    assert YGNodeLayoutGetTop(root_child1) == 65
    assert YGNodeLayoutGetWidth(root_child1) == 25
    assert YGNodeLayoutGetHeight(root_child1) == 25

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_border_box_max_width():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMaxWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 25)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeAll, 5)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeAll, 15)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 25)
    YGNodeStyleSetHeight(root_child1, 25)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 40

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 25
    assert YGNodeLayoutGetHeight(root_child1) == 25

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 40

    assert YGNodeLayoutGetLeft(root_child1) == 75
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 25
    assert YGNodeLayoutGetHeight(root_child1) == 25

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_content_box_max_height():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetMaxHeight(root_child0, 50)
    YGNodeStyleSetBoxSizing(root_child0, YGBoxSizing.YGBoxSizingContentBox)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeAll, 5)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeAll, 15)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 25)
    YGNodeStyleSetHeight(root_child1, 25)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 90
    assert YGNodeLayoutGetHeight(root_child0) == 40

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 25
    assert YGNodeLayoutGetHeight(root_child1) == 25

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 10
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 90
    assert YGNodeLayoutGetHeight(root_child0) == 40

    assert YGNodeLayoutGetLeft(root_child1) == 75
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 25
    assert YGNodeLayoutGetHeight(root_child1) == 25

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_border_box_max_height():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetMaxHeight(root_child0, 50)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeAll, 5)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeAll, 15)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 25)
    YGNodeStyleSetHeight(root_child1, 25)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 40

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 25
    assert YGNodeLayoutGetHeight(root_child1) == 25

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 40

    assert YGNodeLayoutGetLeft(root_child1) == 75
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 25
    assert YGNodeLayoutGetHeight(root_child1) == 25

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_content_box_min_width():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMinWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 25)
    YGNodeStyleSetBoxSizing(root_child0, YGBoxSizing.YGBoxSizingContentBox)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeAll, 5)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeAll, 15)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 25)
    YGNodeStyleSetHeight(root_child1, 25)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 65

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 65
    assert YGNodeLayoutGetWidth(root_child1) == 25
    assert YGNodeLayoutGetHeight(root_child1) == 25

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 65

    assert YGNodeLayoutGetLeft(root_child1) == 75
    assert YGNodeLayoutGetTop(root_child1) == 65
    assert YGNodeLayoutGetWidth(root_child1) == 25
    assert YGNodeLayoutGetHeight(root_child1) == 25

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_border_box_min_width():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMinWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 25)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeAll, 5)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeAll, 15)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 25)
    YGNodeStyleSetHeight(root_child1, 25)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 40

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 25
    assert YGNodeLayoutGetHeight(root_child1) == 25

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 40

    assert YGNodeLayoutGetLeft(root_child1) == 75
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 25
    assert YGNodeLayoutGetHeight(root_child1) == 25

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_content_box_min_height():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetMinHeight(root_child0, 50)
    YGNodeStyleSetBoxSizing(root_child0, YGBoxSizing.YGBoxSizingContentBox)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeAll, 5)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeAll, 15)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 25)
    YGNodeStyleSetHeight(root_child1, 25)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 90
    assert YGNodeLayoutGetHeight(root_child0) == 90

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 90
    assert YGNodeLayoutGetWidth(root_child1) == 25
    assert YGNodeLayoutGetHeight(root_child1) == 25

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 10
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 90
    assert YGNodeLayoutGetHeight(root_child0) == 90

    assert YGNodeLayoutGetLeft(root_child1) == 75
    assert YGNodeLayoutGetTop(root_child1) == 90
    assert YGNodeLayoutGetWidth(root_child1) == 25
    assert YGNodeLayoutGetHeight(root_child1) == 25

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_border_box_min_height():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetMinHeight(root_child0, 50)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeAll, 5)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeAll, 15)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 25)
    YGNodeStyleSetHeight(root_child1, 25)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 50
    assert YGNodeLayoutGetWidth(root_child1) == 25
    assert YGNodeLayoutGetHeight(root_child1) == 25

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 75
    assert YGNodeLayoutGetTop(root_child1) == 50
    assert YGNodeLayoutGetWidth(root_child1) == 25
    assert YGNodeLayoutGetHeight(root_child1) == 25

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_content_box_no_height_no_width():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetBoxSizing(root_child0, YGBoxSizing.YGBoxSizingContentBox)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeAll, 2)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeAll, 7)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 18

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 18

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_border_box_no_height_no_width():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeAll, 2)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeAll, 7)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 18

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 18

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_content_box_nested():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetBoxSizing(root, YGBoxSizing.YGBoxSizingContentBox)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeAll, 15)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 3)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 20)
    YGNodeStyleSetHeight(root_child0, 20)
    YGNodeStyleSetBoxSizing(root_child0, YGBoxSizing.YGBoxSizingContentBox)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeAll, 2)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeAll, 7)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeStyleSetHeight(root_child0_child0, 5)
    YGNodeStyleSetBoxSizing(root_child0_child0, YGBoxSizing.YGBoxSizingContentBox)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeAll, 1)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeAll, 2)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 136
    assert YGNodeLayoutGetHeight(root) == 136

    assert YGNodeLayoutGetLeft(root_child0) == 18
    assert YGNodeLayoutGetTop(root_child0) == 18
    assert YGNodeLayoutGetWidth(root_child0) == 38
    assert YGNodeLayoutGetHeight(root_child0) == 38

    assert YGNodeLayoutGetLeft(root_child0_child0) == 9
    assert YGNodeLayoutGetTop(root_child0_child0) == 9
    assert YGNodeLayoutGetWidth(root_child0_child0) == 16
    assert YGNodeLayoutGetHeight(root_child0_child0) == 11

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 136
    assert YGNodeLayoutGetHeight(root) == 136

    assert YGNodeLayoutGetLeft(root_child0) == 80
    assert YGNodeLayoutGetTop(root_child0) == 18
    assert YGNodeLayoutGetWidth(root_child0) == 38
    assert YGNodeLayoutGetHeight(root_child0) == 38

    assert YGNodeLayoutGetLeft(root_child0_child0) == 13
    assert YGNodeLayoutGetTop(root_child0_child0) == 9
    assert YGNodeLayoutGetWidth(root_child0_child0) == 16
    assert YGNodeLayoutGetHeight(root_child0_child0) == 11

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_border_box_nested():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeAll, 15)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 3)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 20)
    YGNodeStyleSetHeight(root_child0, 20)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeAll, 2)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeAll, 7)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeStyleSetHeight(root_child0_child0, 5)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeAll, 1)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeAll, 2)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 18
    assert YGNodeLayoutGetTop(root_child0) == 18
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child0) == 9
    assert YGNodeLayoutGetTop(root_child0_child0) == 9
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 6

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 62
    assert YGNodeLayoutGetTop(root_child0) == 18
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child0) == 1
    assert YGNodeLayoutGetTop(root_child0_child0) == 9
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 6

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_content_box_nested_alternating():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetBoxSizing(root, YGBoxSizing.YGBoxSizingContentBox)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeAll, 3)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 2)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 40)
    YGNodeStyleSetHeight(root_child0, 40)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeAll, 8)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeAll, 2)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 20)
    YGNodeStyleSetHeight(root_child0_child0, 25)
    YGNodeStyleSetBoxSizing(root_child0_child0, YGBoxSizing.YGBoxSizingContentBox)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeAll, 3)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeAll, 6)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0_child0, 10)
    YGNodeStyleSetHeight(root_child0_child0_child0, 5)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeAll, 1)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeAll, 1)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 110
    assert YGNodeLayoutGetHeight(root) == 110

    assert YGNodeLayoutGetLeft(root_child0) == 5
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0) == 40

    assert YGNodeLayoutGetLeft(root_child0_child0) == 10
    assert YGNodeLayoutGetTop(root_child0_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0_child0) == 38
    assert YGNodeLayoutGetHeight(root_child0_child0) == 43

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 9
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 9
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 5

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 110
    assert YGNodeLayoutGetHeight(root) == 110

    assert YGNodeLayoutGetLeft(root_child0) == 65
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0) == 40

    assert YGNodeLayoutGetLeft(root_child0_child0) == -8
    assert YGNodeLayoutGetTop(root_child0_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0_child0) == 38
    assert YGNodeLayoutGetHeight(root_child0_child0) == 43

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 19
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 9
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 5

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_border_box_nested_alternating():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeAll, 3)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 2)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 40)
    YGNodeStyleSetHeight(root_child0, 40)
    YGNodeStyleSetBoxSizing(root_child0, YGBoxSizing.YGBoxSizingContentBox)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeAll, 8)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeAll, 2)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 20)
    YGNodeStyleSetHeight(root_child0_child0, 25)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeAll, 3)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeAll, 6)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0_child0, 10)
    YGNodeStyleSetHeight(root_child0_child0_child0, 5)
    YGNodeStyleSetBoxSizing(root_child0_child0_child0, YGBoxSizing.YGBoxSizingContentBox)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeAll, 1)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeAll, 1)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 5
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 60
    assert YGNodeLayoutGetHeight(root_child0) == 60

    assert YGNodeLayoutGetLeft(root_child0_child0) == 10
    assert YGNodeLayoutGetTop(root_child0_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0) == 25

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 9
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 9
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 14
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 9

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 35
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 60
    assert YGNodeLayoutGetHeight(root_child0) == 60

    assert YGNodeLayoutGetLeft(root_child0_child0) == 30
    assert YGNodeLayoutGetTop(root_child0_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0) == 25

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == -3
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 9
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 14
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 9

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_content_box_flex_basis_row():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexBasis(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 25)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeAll, 5)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeAll, 10)
    YGNodeStyleSetBoxSizing(root_child0, YGBoxSizing.YGBoxSizingContentBox)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 80
    assert YGNodeLayoutGetHeight(root_child0) == 55

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 20
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 80
    assert YGNodeLayoutGetHeight(root_child0) == 55

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_border_box_flex_basis_row():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexBasis(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 25)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeAll, 5)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeAll, 10)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 30

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 30

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_content_box_flex_basis_column():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexBasis(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 25)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeAll, 5)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeAll, 10)
    YGNodeStyleSetBoxSizing(root_child0, YGBoxSizing.YGBoxSizingContentBox)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 80

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 80

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_border_box_flex_basis_column():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexBasis(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 25)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeAll, 5)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeAll, 10)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_content_box_padding_start():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeStart, 5)
    YGNodeStyleSetBoxSizing(root, YGBoxSizing.YGBoxSizingContentBox)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 105
    assert YGNodeLayoutGetHeight(root) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 105
    assert YGNodeLayoutGetHeight(root) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_border_box_padding_start():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeStart, 5)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_content_box_padding_end():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeEnd, 5)
    YGNodeStyleSetBoxSizing(root, YGBoxSizing.YGBoxSizingContentBox)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 105
    assert YGNodeLayoutGetHeight(root) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 105
    assert YGNodeLayoutGetHeight(root) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_border_box_padding_end():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeEnd, 5)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_content_box_border_start():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeStart, 5)
    YGNodeStyleSetBoxSizing(root, YGBoxSizing.YGBoxSizingContentBox)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 105
    assert YGNodeLayoutGetHeight(root) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 105
    assert YGNodeLayoutGetHeight(root) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_border_box_border_start():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeStart, 5)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_content_box_border_end():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeEnd, 5)
    YGNodeStyleSetBoxSizing(root, YGBoxSizing.YGBoxSizingContentBox)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 105
    assert YGNodeLayoutGetHeight(root) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 105
    assert YGNodeLayoutGetHeight(root) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_box_sizing_border_box_border_end():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeEnd, 5)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

