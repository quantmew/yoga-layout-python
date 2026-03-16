import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from yoga import (  # noqa: E402
    YGAlign,
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
    YGNodeStyleSetAlignContent,
    YGNodeStyleSetAlignItems,
    YGNodeStyleSetFlexDirection,
    YGNodeStyleSetFlexShrink,
    YGNodeStyleSetHeight,
    YGNodeStyleSetMargin,
    YGNodeStyleSetPadding,
    YGNodeStyleSetPositionType,
    YGNodeStyleSetWidth,
    YGPositionType,
)


def _assert_layout(node, left, top, width, height):
    assert YGNodeLayoutGetLeft(node) == left
    assert YGNodeLayoutGetTop(node) == top
    assert YGNodeLayoutGetWidth(node) == width
    assert YGNodeLayoutGetHeight(node) == height


def test_android_news_feed():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignStretch)
    YGNodeStyleSetWidth(root, 1080)

    c0 = YGNodeNewWithConfig(config)
    YGNodeInsertChild(root, c0, 0)

    c0_0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetAlignContent(c0_0, YGAlign.YGAlignStretch)
    YGNodeInsertChild(c0, c0_0, 0)

    c0_0_0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetAlignContent(c0_0_0, YGAlign.YGAlignStretch)
    YGNodeInsertChild(c0_0, c0_0_0, 0)

    c0_0_0_0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(c0_0_0_0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignItems(c0_0_0_0, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetAlignContent(c0_0_0_0, YGAlign.YGAlignStretch)
    YGNodeStyleSetMargin(c0_0_0_0, YGEdge.YGEdgeTop, 24)
    YGNodeStyleSetMargin(c0_0_0_0, YGEdge.YGEdgeStart, 36)
    YGNodeInsertChild(c0_0_0, c0_0_0_0, 0)

    c0_0_0_0_0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(c0_0_0_0_0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(c0_0_0_0_0, YGAlign.YGAlignStretch)
    YGNodeInsertChild(c0_0_0_0, c0_0_0_0_0, 0)

    c0_0_0_0_0_0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetAlignContent(c0_0_0_0_0_0, YGAlign.YGAlignStretch)
    YGNodeStyleSetWidth(c0_0_0_0_0_0, 120)
    YGNodeStyleSetHeight(c0_0_0_0_0_0, 120)
    YGNodeInsertChild(c0_0_0_0_0, c0_0_0_0_0_0, 0)

    c0_0_0_0_1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetAlignContent(c0_0_0_0_1, YGAlign.YGAlignStretch)
    YGNodeStyleSetFlexShrink(c0_0_0_0_1, 1)
    YGNodeStyleSetMargin(c0_0_0_0_1, YGEdge.YGEdgeRight, 36)
    YGNodeStyleSetPadding(c0_0_0_0_1, YGEdge.YGEdgeLeft, 36)
    YGNodeStyleSetPadding(c0_0_0_0_1, YGEdge.YGEdgeTop, 21)
    YGNodeStyleSetPadding(c0_0_0_0_1, YGEdge.YGEdgeRight, 36)
    YGNodeStyleSetPadding(c0_0_0_0_1, YGEdge.YGEdgeBottom, 18)
    YGNodeInsertChild(c0_0_0_0, c0_0_0_0_1, 1)

    c0_0_0_0_1_0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(c0_0_0_0_1_0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(c0_0_0_0_1_0, YGAlign.YGAlignStretch)
    YGNodeStyleSetFlexShrink(c0_0_0_0_1_0, 1)
    YGNodeInsertChild(c0_0_0_0_1, c0_0_0_0_1_0, 0)

    c0_0_0_0_1_1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetAlignContent(c0_0_0_0_1_1, YGAlign.YGAlignStretch)
    YGNodeStyleSetFlexShrink(c0_0_0_0_1_1, 1)
    YGNodeInsertChild(c0_0_0_0_1, c0_0_0_0_1_1, 1)

    c0_0_1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetAlignContent(c0_0_1, YGAlign.YGAlignStretch)
    YGNodeInsertChild(c0_0, c0_0_1, 1)

    c0_0_1_0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(c0_0_1_0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignItems(c0_0_1_0, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetAlignContent(c0_0_1_0, YGAlign.YGAlignStretch)
    YGNodeStyleSetMargin(c0_0_1_0, YGEdge.YGEdgeTop, 24)
    YGNodeStyleSetMargin(c0_0_1_0, YGEdge.YGEdgeStart, 174)
    YGNodeInsertChild(c0_0_1, c0_0_1_0, 0)

    c0_0_1_0_0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(c0_0_1_0_0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(c0_0_1_0_0, YGAlign.YGAlignStretch)
    YGNodeInsertChild(c0_0_1_0, c0_0_1_0_0, 0)

    c0_0_1_0_0_0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetAlignContent(c0_0_1_0_0_0, YGAlign.YGAlignStretch)
    YGNodeStyleSetWidth(c0_0_1_0_0_0, 72)
    YGNodeStyleSetHeight(c0_0_1_0_0_0, 72)
    YGNodeInsertChild(c0_0_1_0_0, c0_0_1_0_0_0, 0)

    c0_0_1_0_1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetAlignContent(c0_0_1_0_1, YGAlign.YGAlignStretch)
    YGNodeStyleSetFlexShrink(c0_0_1_0_1, 1)
    YGNodeStyleSetMargin(c0_0_1_0_1, YGEdge.YGEdgeRight, 36)
    YGNodeStyleSetPadding(c0_0_1_0_1, YGEdge.YGEdgeLeft, 36)
    YGNodeStyleSetPadding(c0_0_1_0_1, YGEdge.YGEdgeTop, 21)
    YGNodeStyleSetPadding(c0_0_1_0_1, YGEdge.YGEdgeRight, 36)
    YGNodeStyleSetPadding(c0_0_1_0_1, YGEdge.YGEdgeBottom, 18)
    YGNodeInsertChild(c0_0_1_0, c0_0_1_0_1, 1)

    c0_0_1_0_1_0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(c0_0_1_0_1_0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(c0_0_1_0_1_0, YGAlign.YGAlignStretch)
    YGNodeStyleSetFlexShrink(c0_0_1_0_1_0, 1)
    YGNodeInsertChild(c0_0_1_0_1, c0_0_1_0_1_0, 0)

    c0_0_1_0_1_1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetAlignContent(c0_0_1_0_1_1, YGAlign.YGAlignStretch)
    YGNodeStyleSetFlexShrink(c0_0_1_0_1_1, 1)
    YGNodeInsertChild(c0_0_1_0_1, c0_0_1_0_1_1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    _assert_layout(root, 0, 0, 1080, 240)
    _assert_layout(c0, 0, 0, 1080, 240)
    _assert_layout(c0_0, 0, 0, 1080, 240)
    _assert_layout(c0_0_0, 0, 0, 1080, 144)
    _assert_layout(c0_0_0_0, 36, 24, 1044, 120)
    _assert_layout(c0_0_0_0_0, 0, 0, 120, 120)
    _assert_layout(c0_0_0_0_0_0, 0, 0, 120, 120)
    _assert_layout(c0_0_0_0_1, 120, 0, 72, 39)
    _assert_layout(c0_0_0_0_1_0, 36, 21, 0, 0)
    _assert_layout(c0_0_0_0_1_1, 36, 21, 0, 0)
    _assert_layout(c0_0_1, 0, 144, 1080, 96)
    _assert_layout(c0_0_1_0, 174, 24, 906, 72)
    _assert_layout(c0_0_1_0_0, 0, 0, 72, 72)
    _assert_layout(c0_0_1_0_0_0, 0, 0, 72, 72)
    _assert_layout(c0_0_1_0_1, 72, 0, 72, 39)
    _assert_layout(c0_0_1_0_1_0, 36, 21, 0, 0)
    _assert_layout(c0_0_1_0_1_1, 36, 21, 0, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    _assert_layout(root, 0, 0, 1080, 240)
    _assert_layout(c0, 0, 0, 1080, 240)
    _assert_layout(c0_0, 0, 0, 1080, 240)
    _assert_layout(c0_0_0, 0, 0, 1080, 144)
    _assert_layout(c0_0_0_0, 0, 24, 1044, 120)
    _assert_layout(c0_0_0_0_0, 924, 0, 120, 120)
    _assert_layout(c0_0_0_0_0_0, 0, 0, 120, 120)
    _assert_layout(c0_0_0_0_1, 816, 0, 72, 39)
    _assert_layout(c0_0_0_0_1_0, 36, 21, 0, 0)
    _assert_layout(c0_0_0_0_1_1, 36, 21, 0, 0)
    _assert_layout(c0_0_1, 0, 144, 1080, 96)
    _assert_layout(c0_0_1_0, 0, 24, 906, 72)
    _assert_layout(c0_0_1_0_0, 834, 0, 72, 72)
    _assert_layout(c0_0_1_0_0_0, 0, 0, 72, 72)
    _assert_layout(c0_0_1_0_1, 726, 0, 72, 39)
    _assert_layout(c0_0_1_0_1_0, 36, 21, 0, 0)
    _assert_layout(c0_0_1_0_1_1, 36, 21, 0, 0)

    YGNodeFreeRecursive(root)
    YGConfigFree(config)
