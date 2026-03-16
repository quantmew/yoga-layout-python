import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import (  # noqa: E402
    YGAlign,
    YGConfigFree,
    YGConfigNew,
    YGConfigSetErrata,
    YGConfigSetPointScaleFactor,
    YGDirection,
    YGErrata,
    YGFlexDirection,
    YGNodeCalculateLayout,
    YGNodeFreeRecursive,
    YGNodeInsertChild,
    YGNodeLayoutGetHeight,
    YGNodeLayoutGetLeft,
    YGNodeNewWithConfig,
    YGNodeSetConfig,
    YGNodeSetMeasureFunc,
    YGNodeStyleSetAlignItems,
    YGNodeStyleSetFlexDirection,
    YGNodeStyleSetFlexGrow,
    YGNodeStyleSetFlexShrink,
    YGNodeStyleSetHeight,
    YGNodeStyleSetWidth,
    YGSize,
)


def test_scale_change_invalidates_layout():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGConfigSetPointScaleFactor(config, 1.0)

    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(root, 50)
    YGNodeStyleSetHeight(root, 50)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child0, 1)
    YGNodeInsertChild(root, child0, 0)

    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child1, 1)
    YGNodeInsertChild(root, child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetLeft(child0) == 0
    assert YGNodeLayoutGetLeft(child1) == 25

    YGConfigSetPointScaleFactor(config, 1.5)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetLeft(child0) == 0
    assert YGNodeLayoutGetLeft(child1) == pytest.approx(25.333334, abs=1e-5)

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_errata_config_change_relayout():
    config = YGConfigNew()
    YGConfigSetErrata(config, YGErrata.YGErrataStretchFlexBasis)
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root, 500)
    YGNodeStyleSetHeight(root, 500)

    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetAlignItems(child0, YGAlign.YGAlignFlexStart)
    YGNodeInsertChild(root, child0, 0)

    child00 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child00, 1)
    YGNodeStyleSetFlexShrink(child00, 1)
    YGNodeInsertChild(child0, child00, 0)

    child000 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child000, 1)
    YGNodeStyleSetFlexShrink(child000, 1)
    YGNodeInsertChild(child00, child000, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetHeight(child0) == 500
    assert YGNodeLayoutGetHeight(child00) == 500
    assert YGNodeLayoutGetHeight(child000) == 500

    YGConfigSetErrata(config, YGErrata.YGErrataNone)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetHeight(child0) == 0
    assert YGNodeLayoutGetHeight(child00) == 0
    assert YGNodeLayoutGetHeight(child000) == 0

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_setting_compatible_config_maintains_layout_cache():
    measure_call_count = [0]

    def measure_custom(_node, _width, _widthMode, _height, _heightMode):
        measure_call_count[0] += 1
        return YGSize(width=25.0, height=25.0)

    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGConfigSetPointScaleFactor(config, 1.0)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(root, 50)
    YGNodeStyleSetHeight(root, 50)

    child0 = YGNodeNewWithConfig(config)
    assert measure_call_count[0] == 0
    YGNodeSetMeasureFunc(child0, measure_custom)
    YGNodeInsertChild(root, child0, 0)

    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(child1, 1)
    YGNodeInsertChild(root, child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert measure_call_count[0] == 1
    assert YGNodeLayoutGetLeft(child0) == 0
    assert YGNodeLayoutGetLeft(child1) == 25

    config2 = YGConfigNew()
    YGConfigSetPointScaleFactor(config2, 1.0)
    YGConfigSetPointScaleFactor(config2, 1.5)
    YGConfigSetPointScaleFactor(config2, 1.0)

    YGNodeSetConfig(root, config2)
    YGNodeSetConfig(child0, config2)
    YGNodeSetConfig(child1, config2)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert measure_call_count[0] == 1
    assert YGNodeLayoutGetLeft(child0) == 0
    assert YGNodeLayoutGetLeft(child1) == 25

    YGNodeFreeRecursive(root)
    YGConfigFree(config)
    YGConfigFree(config2)
