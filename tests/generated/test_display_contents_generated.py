import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from yoga import (  # noqa: E402
    YGConfigFree,
    YGConfigNew,
    YGDirection,
    YGDisplay,
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
    YGNodeStyleSetPositionType,
    YGNodeStyleSetWidth,
    YGPositionType,
)


def test_test1():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetDisplay(root_child0, YGDisplay.YGDisplayContents)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0_child0, 1)
    YGNodeStyleSetFlexShrink(root_child0_child0, 1)
    YGNodeStyleSetFlexBasisPercent(root_child0_child0, 0)
    YGNodeStyleSetHeight(root_child0_child0, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0_child1, 1)
    YGNodeStyleSetFlexShrink(root_child0_child1, 1)
    YGNodeStyleSetFlexBasisPercent(root_child0_child1, 0)
    YGNodeStyleSetHeight(root_child0_child1, 20)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 50
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 50
    assert YGNodeLayoutGetHeight(root_child0_child1) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 50
    assert YGNodeLayoutGetHeight(root_child0_child1) == 20

    YGNodeFreeRecursive(root)
    YGConfigFree(config)
