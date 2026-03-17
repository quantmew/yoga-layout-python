import sys
from pathlib import Path

import pytest

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


def assert_float_eq(expected, actual):
    assert actual == pytest.approx(expected, rel=1e-6, abs=1e-6)


def test_rounding_feature_with_custom_measure_func_floor():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)

    child = YGNodeNewWithConfig(config)
    YGNodeSetMeasureFunc(child, _measure_floor)
    YGNodeInsertChild(root, child, 0)

    YGConfigSetPointScaleFactor(config, 0.0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert_float_eq(10.2, YGNodeLayoutGetWidth(child))
    assert_float_eq(10.2, YGNodeLayoutGetHeight(child))

    YGConfigSetPointScaleFactor(config, 1.0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert_float_eq(11, YGNodeLayoutGetWidth(child))
    assert_float_eq(11, YGNodeLayoutGetHeight(child))

    YGConfigSetPointScaleFactor(config, 2.0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert_float_eq(10.5, YGNodeLayoutGetWidth(child))
    assert_float_eq(10.5, YGNodeLayoutGetHeight(child))

    YGConfigSetPointScaleFactor(config, 4.0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert_float_eq(10.25, YGNodeLayoutGetWidth(child))
    assert_float_eq(10.25, YGNodeLayoutGetHeight(child))

    YGConfigSetPointScaleFactor(config, 1.0 / 3.0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert_float_eq(12.0, YGNodeLayoutGetWidth(child))
    assert_float_eq(12.0, YGNodeLayoutGetHeight(child))

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
    assert_float_eq(11, YGNodeLayoutGetWidth(child))
    assert_float_eq(11, YGNodeLayoutGetHeight(child))

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

    assert_float_eq(0.5, YGNodeLayoutGetWidth(child))
    assert_float_eq(0.5, YGNodeLayoutGetHeight(child))
    assert_float_eq(73.5, YGNodeLayoutGetLeft(child))

    YGNodeFreeRecursive(root)
    YGConfigFree(config)
