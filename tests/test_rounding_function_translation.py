import math
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
    YGNodeLayoutGetRawHeight,
    YGNodeLayoutGetRawWidth,
    YGNodeLayoutGetWidth,
    YGNodeNewWithConfig,
    YGNodeSetMeasureFunc,
    YGNodeStyleSetHeight,
    YGNodeStyleSetMargin,
    YGNodeStyleSetWidth,
    YGRoundValueToPixelGrid,
    YGSize,
)


def test_rounding_value():
    assert YGRoundValueToPixelGrid(6.000001, 2.0, False, False) == 6.0
    assert YGRoundValueToPixelGrid(6.000001, 2.0, True, False) == 6.0
    assert YGRoundValueToPixelGrid(6.000001, 2.0, False, True) == 6.0
    assert YGRoundValueToPixelGrid(5.999999, 2.0, False, False) == 6.0
    assert YGRoundValueToPixelGrid(5.999999, 2.0, True, False) == 6.0
    assert YGRoundValueToPixelGrid(5.999999, 2.0, False, True) == 6.0
    assert YGRoundValueToPixelGrid(-6.000001, 2.0, False, False) == -6.0
    assert YGRoundValueToPixelGrid(-6.000001, 2.0, True, False) == -6.0
    assert YGRoundValueToPixelGrid(-6.000001, 2.0, False, True) == -6.0
    assert YGRoundValueToPixelGrid(-5.999999, 2.0, False, False) == -6.0
    assert YGRoundValueToPixelGrid(-5.999999, 2.0, True, False) == -6.0
    assert YGRoundValueToPixelGrid(-5.999999, 2.0, False, True) == -6.0

    assert YGRoundValueToPixelGrid(6.01, 2.0, False, False) == 6.0
    assert YGRoundValueToPixelGrid(6.01, 2.0, True, False) == 6.5
    assert YGRoundValueToPixelGrid(6.01, 2.0, False, True) == 6.0
    assert YGRoundValueToPixelGrid(5.99, 2.0, False, False) == 6.0
    assert YGRoundValueToPixelGrid(5.99, 2.0, True, False) == 6.0
    assert YGRoundValueToPixelGrid(5.99, 2.0, False, True) == 5.5
    assert YGRoundValueToPixelGrid(-6.01, 2.0, False, False) == -6.0
    assert YGRoundValueToPixelGrid(-6.01, 2.0, True, False) == -6.0
    assert YGRoundValueToPixelGrid(-6.01, 2.0, False, True) == -6.5
    assert YGRoundValueToPixelGrid(-5.99, 2.0, False, False) == -6.0
    assert YGRoundValueToPixelGrid(-5.99, 2.0, True, False) == -5.5
    assert YGRoundValueToPixelGrid(-5.99, 2.0, False, True) == -6.0

    assert YGRoundValueToPixelGrid(-3.5, 1.0, False, False) == -3
    assert YGRoundValueToPixelGrid(-3.4, 1.0, False, False) == -3
    assert YGRoundValueToPixelGrid(-3.6, 1.0, False, False) == -4
    assert YGRoundValueToPixelGrid(-3.499999, 1.0, False, False) == -3
    assert YGRoundValueToPixelGrid(-3.500001, 1.0, False, False) == -3
    assert YGRoundValueToPixelGrid(-3.5001, 1.0, False, False) == -4

    assert YGRoundValueToPixelGrid(-3.5, 1.0, True, False) == -3
    assert YGRoundValueToPixelGrid(-3.4, 1.0, True, False) == -3
    assert YGRoundValueToPixelGrid(-3.6, 1.0, True, False) == -3
    assert YGRoundValueToPixelGrid(-3.499999, 1.0, True, False) == -3
    assert YGRoundValueToPixelGrid(-3.500001, 1.0, True, False) == -3
    assert YGRoundValueToPixelGrid(-3.5001, 1.0, True, False) == -3
    assert YGRoundValueToPixelGrid(-3.00001, 1.0, True, False) == -3
    assert YGRoundValueToPixelGrid(-3, 1.0, True, False) == -3

    assert YGRoundValueToPixelGrid(-3.5, 1.0, False, True) == -4
    assert YGRoundValueToPixelGrid(-3.4, 1.0, False, True) == -4
    assert YGRoundValueToPixelGrid(-3.6, 1.0, False, True) == -4
    assert YGRoundValueToPixelGrid(-3.499999, 1.0, False, True) == -4
    assert YGRoundValueToPixelGrid(-3.500001, 1.0, False, True) == -4
    assert YGRoundValueToPixelGrid(-3.5001, 1.0, False, True) == -4
    assert YGRoundValueToPixelGrid(-3.00001, 1.0, False, True) == -3
    assert YGRoundValueToPixelGrid(-3, 1.0, False, True) == -3

    assert math.isnan(YGRoundValueToPixelGrid(float("nan"), 1.5, False, False))
    assert math.isnan(YGRoundValueToPixelGrid(1.5, float("nan"), False, False))
    assert math.isnan(
        YGRoundValueToPixelGrid(float("nan"), float("nan"), False, False)
    )


def _measure_text(_node, _width, _widthMode, _height, _heightMode):
    return YGSize(10, 10)


def test_consistent_rounding_during_repeated_layouts():
    config = YGConfigNew()
    YGConfigSetPointScaleFactor(config, 2)

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetMargin(root, YGEdge.YGEdgeTop, -1.49)
    YGNodeStyleSetWidth(root, 500)
    YGNodeStyleSetHeight(root, 500)

    node0 = YGNodeNewWithConfig(config)
    YGNodeInsertChild(root, node0, 0)

    node1 = YGNodeNewWithConfig(config)
    YGNodeSetMeasureFunc(node1, _measure_text)
    YGNodeInsertChild(node0, node1, 0)

    for i in range(5):
        YGNodeStyleSetMargin(root, YGEdge.YGEdgeLeft, float(i + 1))
        YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
        assert YGNodeLayoutGetHeight(node1) == 10

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_per_node_point_scale_factor():
    config1 = YGConfigNew()
    YGConfigSetPointScaleFactor(config1, 2)
    config2 = YGConfigNew()
    YGConfigSetPointScaleFactor(config2, 1)
    config3 = YGConfigNew()
    YGConfigSetPointScaleFactor(config3, 0.5)

    root = YGNodeNewWithConfig(config1)
    YGNodeStyleSetWidth(root, 11.5)
    YGNodeStyleSetHeight(root, 11.5)

    node0 = YGNodeNewWithConfig(config2)
    YGNodeStyleSetWidth(node0, 9.5)
    YGNodeStyleSetHeight(node0, 9.5)
    YGNodeInsertChild(root, node0, 0)

    node1 = YGNodeNewWithConfig(config3)
    YGNodeStyleSetWidth(node1, 7)
    YGNodeStyleSetHeight(node1, 7)
    YGNodeInsertChild(node0, node1, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetWidth(root) == 11.5
    assert YGNodeLayoutGetHeight(root) == 11.5
    assert YGNodeLayoutGetWidth(node0) == 10
    assert YGNodeLayoutGetHeight(node0) == 10
    assert YGNodeLayoutGetWidth(node1) == 8
    assert YGNodeLayoutGetHeight(node1) == 8

    YGNodeFreeRecursive(root)
    YGConfigFree(config1)
    YGConfigFree(config2)
    YGConfigFree(config3)


def test_raw_layout_dimensions():
    config = YGConfigNew()
    YGConfigSetPointScaleFactor(config, 0.5)

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root, 11.5)
    YGNodeStyleSetHeight(root, 9.5)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetWidth(root) == 12.0
    assert YGNodeLayoutGetHeight(root) == 10.0
    assert YGNodeLayoutGetRawWidth(root) == 11.5
    assert YGNodeLayoutGetRawHeight(root) == 9.5

    YGNodeFreeRecursive(root)
    YGConfigFree(config)
