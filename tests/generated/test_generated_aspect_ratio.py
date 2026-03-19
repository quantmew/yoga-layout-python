import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from yoga import (  # noqa: E402
    YGConfigFree,
    YGConfigNew,
    YGDirection,
    YGNodeCalculateLayout,
    YGNodeFreeRecursive,
    YGNodeInsertChild,
    YGNodeLayoutGetHeight,
    YGNodeLayoutGetLeft,
    YGNodeLayoutGetTop,
    YGNodeLayoutGetWidth,
    YGNodeNewWithConfig,
    YGNodeStyleSetAspectRatio,
    YGNodeStyleSetHeight,
    YGNodeStyleSetPositionType,
    YGNodeStyleSetWidth,
    YGPositionType,
)


@pytest.mark.skip(reason="Upstream test is GTEST_SKIP()")
def test_aspect_ratio_does_not_stretch_cross_axis_dim():
    pytest.skip("Upstream test is GTEST_SKIP()")


def test_zero_aspect_ratio_behaves_like_auto():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 300)
    YGNodeStyleSetHeight(root, 300)

    child = YGNodeNewWithConfig(config)
    YGNodeStyleSetAspectRatio(child, 0)
    YGNodeStyleSetWidth(child, 50)
    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetLeft(child) == 0
    assert YGNodeLayoutGetTop(child) == 0
    assert YGNodeLayoutGetWidth(child) == 50
    assert YGNodeLayoutGetHeight(child) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetLeft(child) == 250
    assert YGNodeLayoutGetTop(child) == 0
    assert YGNodeLayoutGetWidth(child) == 50
    assert YGNodeLayoutGetHeight(child) == 0

    YGNodeFreeRecursive(root)
    YGConfigFree(config)
