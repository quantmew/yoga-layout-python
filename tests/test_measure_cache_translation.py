import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import (  # noqa: E402  # noqa: E402  # noqa: E402
    YGAlign,
    YGConfigFree,
    YGConfigNew,
    YGConfigSetExperimentalFeatureEnabled,
    YGDirection,
    YGEdge,
    YGExperimentalFeature,
    YGFlexDirection,
    YGMeasureMode,
    YGNodeCalculateLayout,
    YGNodeFreeRecursive,
    YGNodeInsertChild,
    YGNodeNew,
    YGNodeNewWithConfig,
    YGNodeSetContext,
    YGNodeSetMeasureFunc,
    YGNodeStyleSetAlignItems,
    YGNodeStyleSetFlexBasisPercent,
    YGNodeStyleSetFlexDirection,
    YGNodeStyleSetFlexGrow,
    YGNodeStyleSetHeight,
    YGNodeStyleSetPadding,
    YGNodeStyleSetWidth,
    YGSize,
)


def _measure_max(node, width, widthMode, height, heightMode):
    measureCount = node.getContext()
    measureCount[0] += 1
    return YGSize(
        10 if widthMode == YGMeasureMode.YGMeasureModeUndefined else width,
        10 if heightMode == YGMeasureMode.YGMeasureModeUndefined else height,
    )


def _measure_min(node, width, widthMode, height, heightMode):
    measureCount = node.getContext()
    measureCount[0] += 1
    return YGSize(
        10
        if widthMode == YGMeasureMode.YGMeasureModeUndefined
        or (widthMode == YGMeasureMode.YGMeasureModeAtMost and width > 10)
        else width,
        10
        if heightMode == YGMeasureMode.YGMeasureModeUndefined
        or (heightMode == YGMeasureMode.YGMeasureModeAtMost and height > 10)
        else height,
    )


def _measure_84_49(node, _width, _widthMode, _height, _heightMode):
    measureCount = node.getContext()
    if measureCount is not None:
        measureCount[0] += 1
    return YGSize(84.0, 49.0)


def test_measure_once_single_flexible_child():
    root = YGNodeNew()
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    child = YGNodeNew()
    measureCount = [0]
    YGNodeSetContext(child, measureCount)
    YGNodeSetMeasureFunc(child, _measure_max)
    YGNodeStyleSetFlexGrow(child, 1)
    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert measureCount[0] == 1
    YGNodeFreeRecursive(root)


def test_remeasure_with_same_exact_width_larger_than_needed_height():
    root = YGNodeNew()
    child = YGNodeNew()
    measureCount = [0]
    YGNodeSetContext(child, measureCount)
    YGNodeSetMeasureFunc(child, _measure_min)
    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, 100, 100, YGDirection.YGDirectionLTR)
    YGNodeCalculateLayout(root, 100, 50, YGDirection.YGDirectionLTR)
    assert measureCount[0] == 1
    YGNodeFreeRecursive(root)


def test_remeasure_with_same_atmost_width_larger_than_needed_height():
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    child = YGNodeNew()
    measureCount = [0]
    YGNodeSetContext(child, measureCount)
    YGNodeSetMeasureFunc(child, _measure_min)
    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, 100, 100, YGDirection.YGDirectionLTR)
    YGNodeCalculateLayout(root, 100, 50, YGDirection.YGDirectionLTR)
    assert measureCount[0] == 1
    YGNodeFreeRecursive(root)


def test_dont_cache_computed_flex_basis_between_layouts():
    config = YGConfigNew()
    YGConfigSetExperimentalFeatureEnabled(
        config, YGExperimentalFeature.YGExperimentalFeatureWebFlexBasis, True
    )

    root = YGNodeNewWithConfig(config)
    from yoga import YGNodeStyleSetHeightPercent, YGNodeStyleSetWidthPercent
    YGNodeStyleSetHeightPercent(root, 100)
    YGNodeStyleSetWidthPercent(root, 100)

    child = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexBasisPercent(child, 100)
    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, 100, float("nan"), YGDirection.YGDirectionLTR)
    YGNodeCalculateLayout(root, 100, 100, YGDirection.YGDirectionLTR)

    from yoga import YGNodeLayoutGetHeight
    assert YGNodeLayoutGetHeight(child) == 100

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_remeasure_with_already_measured_value_smaller_but_still_float_equal():
    measureCount = [0]
    root = YGNodeNew()
    YGNodeStyleSetWidth(root, 288.0)
    YGNodeStyleSetHeight(root, 288.0)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    child = YGNodeNew()
    YGNodeStyleSetPadding(child, YGEdge.YGEdgeAll, 2.88)
    YGNodeStyleSetFlexDirection(child, YGFlexDirection.YGFlexDirectionRow)
    YGNodeInsertChild(root, child, 0)

    grandchild = YGNodeNew()
    YGNodeSetContext(grandchild, measureCount)
    YGNodeSetMeasureFunc(grandchild, _measure_84_49)
    YGNodeInsertChild(child, grandchild, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    YGNodeFreeRecursive(root)
    assert measureCount[0] == 1
