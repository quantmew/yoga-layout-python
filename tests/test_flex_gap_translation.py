import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import (  # noqa: E402
    YGConfigFree,
    YGConfigNew,
    YGDirection,
    YGFlexDirection,
    YGGutter,
    YGNodeCalculateLayout,
    YGNodeFreeRecursive,
    YGNodeInsertChild,
    YGNodeLayoutGetHeight,
    YGNodeLayoutGetLeft,
    YGNodeLayoutGetTop,
    YGNodeLayoutGetWidth,
    YGNodeNewWithConfig,
    YGNodeStyleSetFlexDirection,
    YGNodeStyleSetGap,
    YGNodeStyleSetHeight,
    YGNodeStyleSetWidth,
)


def test_gap_negative_value():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetGap(root, YGGutter.YGGutterAll, -20)
    YGNodeStyleSetHeight(root, 200)

    children = []
    for index in range(4):
        child = YGNodeNewWithConfig(config)
        YGNodeStyleSetWidth(child, 20)
        YGNodeInsertChild(root, child, index)
        children.append(child)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 80
    assert YGNodeLayoutGetHeight(root) == 200

    for index, child in enumerate(children):
        assert YGNodeLayoutGetLeft(child) == index * 20
        assert YGNodeLayoutGetTop(child) == 0
        assert YGNodeLayoutGetWidth(child) == 20
        assert YGNodeLayoutGetHeight(child) == 200

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 80
    assert YGNodeLayoutGetHeight(root) == 200

    for index, child in enumerate(children):
        assert YGNodeLayoutGetLeft(child) == (3 - index) * 20
        assert YGNodeLayoutGetTop(child) == 0
        assert YGNodeLayoutGetWidth(child) == 20
        assert YGNodeLayoutGetHeight(child) == 200

    YGNodeFreeRecursive(root)
    YGConfigFree(config)
