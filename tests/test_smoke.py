import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import (  # noqa: E402
    YGAlign,
    YGConfigNew,
    YGConfigSetErrata,
    YGDirection,
    YGDisplay,
    YGEdge,
    YGErrata,
    YGFlexDirection,
    YGJustify,
    YGNodeCalculateLayout,
    YGNodeInsertChild,
    YGNodeLayoutGetHeight,
    YGNodeLayoutGetLeft,
    YGNodeLayoutGetTop,
    YGNodeLayoutGetWidth,
    YGNodeNew,
    YGNodeSetConfig,
    YGNodeStyleSetAlignSelf,
    YGNodeStyleSetBorder,
    YGNodeStyleSetDisplay,
    YGNodeStyleSetFlexDirection,
    YGNodeStyleSetHeight,
    YGNodeStyleSetJustifySelf,
    YGNodeStyleSetPadding,
    YGNodeStyleSetPositionType,
    YGNodeStyleSetWidth,
    YGNodeStyleSetWidthPercent,
    YGPositionType,
)


def test_basic_row_layout():
    root = YGNodeNew()
    child = YGNodeNew()

    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(child, 50)
    YGNodeStyleSetHeight(child, 20)
    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, 200, 100, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 100
    assert YGNodeLayoutGetLeft(child) == 0
    assert YGNodeLayoutGetTop(child) == 0


def test_absolute_percent_errata_uses_inner_size():
    root = YGNodeNew()
    child = YGNodeNew()
    config = YGConfigNew()

    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeLeft, 10)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeRight, 10)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeLeft, 5)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetPositionType(child, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidthPercent(child, 50)
    YGNodeStyleSetHeight(child, 10)
    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, 100, 100, YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetWidth(child) == 45

    YGConfigSetErrata(config, YGErrata.YGErrataAbsolutePercentAgainstInnerSize)
    YGNodeSetConfig(root, config)
    YGNodeSetConfig(child, config)
    YGNodeCalculateLayout(root, 100, 100, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetWidth(child) == 35


def test_absolute_grid_item_uses_grid_alignment_axes():
    root = YGNodeNew()
    child = YGNodeNew()

    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 80)
    YGNodeStyleSetDisplay(root, YGDisplay.YGDisplayGrid)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeLeft, 10)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeTop, 10)

    YGNodeStyleSetPositionType(child, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(child, 20)
    YGNodeStyleSetHeight(child, 10)
    YGNodeStyleSetJustifySelf(child, YGJustify.YGJustifyFlexStart)
    YGNodeStyleSetAlignSelf(child, YGAlign.YGAlignFlexStart)
    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, 100, 80, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(child) == 0
    assert YGNodeLayoutGetTop(child) == 0
