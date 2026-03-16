import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import (  # noqa: E402
    YGConfigFree,
    YGConfigNew,
    YGConfigSetPointScaleFactor,
    YGDirection,
    YGEdge,
    YGNodeCalculateLayout,
    YGNodeFreeRecursive,
    YGNodeInsertChild,
    YGNodeLayoutGetHeight,
    YGNodeLayoutGetLeft,
    YGNodeLayoutGetWidth,
    YGNodeNewWithConfig,
    YGNodeSetMeasureFunc,
    YGNodeStyleSetPosition,
    YGNodeStyleSetPositionType,
    YGPositionType,
    YGSize,
)


def _measure_floor(_node, width, _widthMode, height, _heightMode):
    return YGSize(width=10.2, height=10.2)


def _measure_ceil(_node, width, _widthMode, height, _heightMode):
    return YGSize(width=10.5, height=10.5)


def _measure_fractial(_node, width, _widthMode, height, _heightMode):
    return YGSize(width=0.5, height=0.5)


def test_rounding_feature_with_custom_measure_func_floor():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)

    child = YGNodeNewWithConfig(config)
    YGNodeSetMeasureFunc(child, _measure_floor)
    YGNodeInsertChild(root, child, 0)

    YGConfigSetPointScaleFactor(config, 0.0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetWidth(child) == 10.2
    assert YGNodeLayoutGetHeight(child) == 10.2

    YGConfigSetPointScaleFactor(config, 1.0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetWidth(child) == 11
    assert YGNodeLayoutGetHeight(child) == 11

    YGConfigSetPointScaleFactor(config, 2.0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetWidth(child) == 10.5
    assert YGNodeLayoutGetHeight(child) == 10.5

    YGConfigSetPointScaleFactor(config, 4.0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetWidth(child) == 10.25
    assert YGNodeLayoutGetHeight(child) == 10.25

    YGConfigSetPointScaleFactor(config, 1.0 / 3.0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetWidth(child) == 12.0
    assert YGNodeLayoutGetHeight(child) == 12.0

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_rounding_feature_with_custom_measure_func_ceil():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)

    child = YGNodeNewWithConfig(config)
    YGNodeSetMeasureFunc(child, _measure_ceil)
    YGNodeInsertChild(root, child, 0)

    YGConfigSetPointScaleFactor(config, 1.0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetWidth(child) == 11
    assert YGNodeLayoutGetHeight(child) == 11

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_rounding_feature_with_custom_measure_and_fractial_matching_scale():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    child = YGNodeNewWithConfig(config)
    YGNodeStyleSetPosition(child, YGEdge.YGEdgeLeft, 73.625)
    YGNodeStyleSetPositionType(child, YGPositionType.YGPositionTypeRelative)
    YGNodeSetMeasureFunc(child, _measure_fractial)
    YGNodeInsertChild(root, child, 0)

    YGConfigSetPointScaleFactor(config, 2.0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetWidth(child) == 0.5
    assert YGNodeLayoutGetHeight(child) == 0.5
    assert YGNodeLayoutGetLeft(child) == 73.5

    YGNodeFreeRecursive(root)
    YGConfigFree(config)
