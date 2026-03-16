import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import *  # noqa: E402,F403


def test_dont_cache_computed_flex_basis_between_layouts_recalculate_resolved_dimension_onchange():
    root = YGNodeNew()
    child = YGNodeNew()
    YGNodeStyleSetMinHeight(child, 10)
    YGNodeStyleSetMaxHeight(child, 10)
    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetHeight(child) == 10

    YGNodeStyleSetMinHeight(child, float("nan"))
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetHeight(child) == 0

    YGNodeFreeRecursive(root)


def test_relayout_containing_block_size_changes():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(child0, YGPositionType.YGPositionTypeRelative)
    YGNodeStyleSetMargin(child0, YGEdge.YGEdgeLeft, 4)
    YGNodeStyleSetMargin(child0, YGEdge.YGEdgeTop, 5)
    YGNodeStyleSetMargin(child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetMargin(child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetPadding(child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(child0, YGEdge.YGEdgeTop, 9)
    YGNodeStyleSetPadding(child0, YGEdge.YGEdgeRight, 11)
    YGNodeStyleSetPadding(child0, YGEdge.YGEdgeBottom, 13)
    YGNodeStyleSetBorder(child0, YGEdge.YGEdgeLeft, 5)
    YGNodeStyleSetBorder(child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetBorder(child0, YGEdge.YGEdgeRight, 7)
    YGNodeStyleSetBorder(child0, YGEdge.YGEdgeBottom, 8)
    YGNodeStyleSetWidth(child0, 500)
    YGNodeStyleSetHeight(child0, 500)
    YGNodeInsertChild(root, child0, 0)

    child00 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(child00, YGPositionType.YGPositionTypeStatic)
    YGNodeStyleSetMargin(child00, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetMargin(child00, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetMargin(child00, YGEdge.YGEdgeRight, 3)
    YGNodeStyleSetMargin(child00, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetPadding(child00, YGEdge.YGEdgeLeft, 1)
    YGNodeStyleSetPadding(child00, YGEdge.YGEdgeTop, 7)
    YGNodeStyleSetPadding(child00, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetPadding(child00, YGEdge.YGEdgeBottom, 4)
    YGNodeStyleSetBorder(child00, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetBorder(child00, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetBorder(child00, YGEdge.YGEdgeRight, 2)
    YGNodeStyleSetBorder(child00, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetWidth(child00, 200)
    YGNodeStyleSetHeight(child00, 200)
    YGNodeInsertChild(child0, child00, 0)

    child000 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(child000, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPosition(child000, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPosition(child000, YGEdge.YGEdgeRight, 12)
    YGNodeStyleSetMargin(child000, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetMargin(child000, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(child000, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(child000, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetPadding(child000, YGEdge.YGEdgeLeft, 5)
    YGNodeStyleSetPadding(child000, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(child000, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(child000, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetBorder(child000, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetBorder(child000, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(child000, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(child000, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetWidthPercent(child000, 41)
    YGNodeStyleSetHeightPercent(child000, 63)
    YGNodeInsertChild(child00, child000, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetWidth(root) == 513
    assert YGNodeLayoutGetHeight(root) == 506
    assert YGNodeLayoutGetLeft(child0) == 4
    assert YGNodeLayoutGetTop(child0) == 5
    assert YGNodeLayoutGetWidth(child0) == 500
    assert YGNodeLayoutGetHeight(child0) == 500
    assert YGNodeLayoutGetLeft(child00) == 15
    assert YGNodeLayoutGetTop(child00) == 21
    assert YGNodeLayoutGetWidth(child00) == 200
    assert YGNodeLayoutGetHeight(child00) == 200
    assert YGNodeLayoutGetLeft(child000) == 1
    assert YGNodeLayoutGetTop(child000) == 29
    assert YGNodeLayoutGetWidth(child000) == 200
    assert YGNodeLayoutGetHeight(child000) == 306

    YGNodeStyleSetWidth(child0, 456)
    YGNodeStyleSetHeight(child0, 432)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetWidth(root) == 469
    assert YGNodeLayoutGetHeight(root) == 438
    assert YGNodeLayoutGetWidth(child0) == 456
    assert YGNodeLayoutGetHeight(child0) == 432
    assert YGNodeLayoutGetLeft(child000) == 1
    assert YGNodeLayoutGetTop(child000) == 29
    assert YGNodeLayoutGetWidth(child000) == 182
    assert YGNodeLayoutGetHeight(child000) == 263

    YGNodeFreeRecursive(root)
    YGConfigFree(config)
