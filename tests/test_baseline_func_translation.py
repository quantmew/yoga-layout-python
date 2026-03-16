import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import (  # noqa: E402
    YGAlign,
    YGDirection,
    YGFlexDirection,
    YGNodeCalculateLayout,
    YGNodeInsertChild,
    YGNodeLayoutGetHeight,
    YGNodeLayoutGetLeft,
    YGNodeLayoutGetTop,
    YGNodeLayoutGetWidth,
    YGNodeNew,
    YGNodeSetBaselineFunc,
    YGNodeSetContext,
    YGNodeStyleSetAlignItems,
    YGNodeStyleSetFlexDirection,
    YGNodeStyleSetHeight,
    YGNodeStyleSetWidth,
)


def _baseline(node, _width, _height):
    return node.getContext()[0]


def test_align_baseline_customer_func():
    root = YGNodeNew()
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignBaseline)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNew()
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNew()
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 20)
    YGNodeInsertChild(root, root_child1, 1)

    baselineValue = [10.0]
    root_child1_child0 = YGNodeNew()
    YGNodeSetContext(root_child1_child0, baselineValue)
    YGNodeStyleSetWidth(root_child1_child0, 50)
    YGNodeSetBaselineFunc(root_child1_child0, _baseline)
    YGNodeStyleSetHeight(root_child1_child0, 20)
    YGNodeInsertChild(root_child1, root_child1_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child1_child0) == 0
    assert YGNodeLayoutGetTop(root_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child1_child0) == 50
    assert YGNodeLayoutGetHeight(root_child1_child0) == 20
