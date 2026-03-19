import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import (  # noqa: E402
    YGAlign,
    YGBoxSizing,
    YGConfigFree,
    YGConfigNew,
    YGConfigSetErrata,
    YGConfigSetUseWebDefaults,
    YGDirection,
    YGEdge,
    YGErrata,
    YGFlexDirection,
    YGFloatIsUndefined,
    YGJustify,
    YGNodeCalculateLayout,
    YGNodeFreeRecursive,
    YGNodeGetChild,
    YGNodeGetChildCount,
    YGNodeInsertChild,
    YGNodeLayoutGetBorder,
    YGNodeLayoutGetBottom,
    YGNodeLayoutGetDirection,
    YGNodeLayoutGetHeight,
    YGNodeLayoutGetLeft,
    YGNodeLayoutGetMargin,
    YGNodeLayoutGetPadding,
    YGNodeLayoutGetRight,
    YGNodeLayoutGetTop,
    YGNodeLayoutGetWidth,
    YGNodeNew,
    YGNodeNewWithConfig,
    YGNodeReset,
    YGNodeStyleGetAlignContent,
    YGNodeStyleGetAlignItems,
    YGNodeStyleGetAlignSelf,
    YGNodeStyleGetBorder,
    YGNodeStyleGetBoxSizing,
    YGNodeStyleGetDirection,
    YGNodeStyleGetFlexBasis,
    YGNodeStyleGetFlexDirection,
    YGNodeStyleGetFlexGrow,
    YGNodeStyleGetFlexShrink,
    YGNodeStyleGetFlexWrap,
    YGNodeStyleGetHeight,
    YGNodeStyleGetJustifyContent,
    YGNodeStyleGetMargin,
    YGNodeStyleGetMaxHeight,
    YGNodeStyleGetMaxWidth,
    YGNodeStyleGetMinHeight,
    YGNodeStyleGetMinWidth,
    YGNodeStyleGetOverflow,
    YGNodeStyleGetPadding,
    YGNodeStyleGetPosition,
    YGNodeStyleGetPositionType,
    YGNodeStyleGetWidth,
    YGNodeStyleSetAlignItems,
    YGNodeStyleSetFlexGrow,
    YGNodeStyleSetFlexShrink,
    YGNodeStyleSetHeight,
    YGNodeStyleSetWidth,
    YGOverflow,
    YGPositionType,
    YGUnit,
    YGWrap,
)


def test_assert_default_values():
    root = YGNodeNew()

    assert YGNodeGetChildCount(root) == 0
    assert YGNodeGetChild(root, 1) is None

    assert YGNodeStyleGetDirection(root) == YGDirection.YGDirectionInherit
    assert YGNodeStyleGetFlexDirection(root) == YGFlexDirection.YGFlexDirectionColumn
    assert YGNodeStyleGetJustifyContent(root) == YGJustify.YGJustifyFlexStart
    assert YGNodeStyleGetAlignContent(root) == YGAlign.YGAlignFlexStart
    assert YGNodeStyleGetAlignItems(root) == YGAlign.YGAlignStretch
    assert YGNodeStyleGetAlignSelf(root) == YGAlign.YGAlignAuto
    assert YGNodeStyleGetPositionType(root) == YGPositionType.YGPositionTypeRelative
    assert YGNodeStyleGetFlexWrap(root) == YGWrap.YGWrapNoWrap
    assert YGNodeStyleGetOverflow(root) == YGOverflow.YGOverflowVisible
    assert YGNodeStyleGetFlexGrow(root) == 0
    assert YGNodeStyleGetFlexShrink(root) == 0
    assert YGNodeStyleGetFlexBasis(root).unit == YGUnit.YGUnitAuto

    for edge in (
        YGEdge.YGEdgeLeft,
        YGEdge.YGEdgeTop,
        YGEdge.YGEdgeRight,
        YGEdge.YGEdgeBottom,
        YGEdge.YGEdgeStart,
        YGEdge.YGEdgeEnd,
    ):
        assert YGNodeStyleGetPosition(root, edge).unit == YGUnit.YGUnitUndefined
        assert YGNodeStyleGetMargin(root, edge).unit == YGUnit.YGUnitUndefined
        assert YGNodeStyleGetPadding(root, edge).unit == YGUnit.YGUnitUndefined
        assert YGFloatIsUndefined(YGNodeStyleGetBorder(root, edge))

    assert YGNodeStyleGetWidth(root).unit == YGUnit.YGUnitAuto
    assert YGNodeStyleGetHeight(root).unit == YGUnit.YGUnitAuto
    assert YGNodeStyleGetMinWidth(root).unit == YGUnit.YGUnitUndefined
    assert YGNodeStyleGetMinHeight(root).unit == YGUnit.YGUnitUndefined
    assert YGNodeStyleGetMaxWidth(root).unit == YGUnit.YGUnitUndefined
    assert YGNodeStyleGetMaxHeight(root).unit == YGUnit.YGUnitUndefined

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetRight(root) == 0
    assert YGNodeLayoutGetBottom(root) == 0

    for edge in (
        YGEdge.YGEdgeLeft,
        YGEdge.YGEdgeTop,
        YGEdge.YGEdgeRight,
        YGEdge.YGEdgeBottom,
    ):
        assert YGNodeLayoutGetMargin(root, edge) == 0
        assert YGNodeLayoutGetPadding(root, edge) == 0
        assert YGNodeLayoutGetBorder(root, edge) == 0

    assert YGFloatIsUndefined(YGNodeLayoutGetWidth(root))
    assert YGFloatIsUndefined(YGNodeLayoutGetHeight(root))
    assert YGNodeLayoutGetDirection(root) == YGDirection.YGDirectionInherit

    YGNodeFreeRecursive(root)


def test_assert_webdefault_values():
    config = YGConfigNew()
    YGConfigSetUseWebDefaults(config, True)
    root = YGNodeNewWithConfig(config)

    assert YGNodeStyleGetFlexDirection(root) == YGFlexDirection.YGFlexDirectionRow
    assert YGNodeStyleGetAlignContent(root) == YGAlign.YGAlignStretch
    assert YGNodeStyleGetFlexShrink(root) == 1.0

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_assert_webdefault_values_reset():
    config = YGConfigNew()
    YGConfigSetUseWebDefaults(config, True)
    root = YGNodeNewWithConfig(config)
    YGNodeReset(root)

    assert YGNodeStyleGetFlexDirection(root) == YGFlexDirection.YGFlexDirectionRow
    assert YGNodeStyleGetAlignContent(root) == YGAlign.YGAlignStretch
    assert YGNodeStyleGetFlexShrink(root) == 1.0

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_assert_legacy_stretch_behaviour():
    config = YGConfigNew()
    YGConfigSetErrata(config, YGErrata.YGErrataStretchFlexBasis)
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root, 500)
    YGNodeStyleSetHeight(root, 500)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetAlignItems(root_child0, YGAlign.YGAlignFlexStart)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0_child0, 1)
    YGNodeStyleSetFlexShrink(root_child0_child0, 1)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0_child0_child0, 1)
    YGNodeStyleSetFlexShrink(root_child0_child0_child0, 1)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 500

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 500
    assert YGNodeLayoutGetHeight(root_child0) == 500

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0_child0) == 500

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 500

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_assert_box_sizing_border_box():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)

    assert YGNodeStyleGetBoxSizing(root) == YGBoxSizing.YGBoxSizingBorderBox

    YGNodeFreeRecursive(root)
    YGConfigFree(config)
