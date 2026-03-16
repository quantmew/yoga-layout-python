import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from yoga import (  # noqa: E402
    YGAlign,
    YGConfigFree,
    YGConfigNew,
    YGDirection,
    YGFlexDirection,
    YGJustify,
    YGNodeCalculateLayout,
    YGNodeFreeRecursive,
    YGNodeInsertChild,
    YGNodeLayoutGetHeight,
    YGNodeLayoutGetLeft,
    YGNodeLayoutGetTop,
    YGNodeLayoutGetWidth,
    YGNodeNewWithConfig,
    YGNodeStyleSetAlignItems,
    YGNodeStyleSetFlexBasis,
    YGNodeStyleSetFlexBasisPercent,
    YGNodeStyleSetFlexDirection,
    YGNodeStyleSetFlexGrow,
    YGNodeStyleSetFlexShrink,
    YGNodeStyleSetHeight,
    YGNodeStyleSetJustifyContent,
    YGNodeStyleSetMaxHeight,
    YGNodeStyleSetMaxHeightPercent,
    YGNodeStyleSetMaxWidth,
    YGNodeStyleSetMaxWidthPercent,
    YGNodeStyleSetMinHeight,
    YGNodeStyleSetMinHeightPercent,
    YGNodeStyleSetMinWidth,
    YGNodeStyleSetMinWidthPercent,
    YGNodeStyleSetPositionType,
    YGNodeStyleSetWidth,
    YGPositionType,
)


def test_max_width():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeStyleSetMaxWidth(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_max_height():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 10)
    YGNodeStyleSetMaxHeight(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 50

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_min_height():
    pytest.skip("Upstream GTEST_SKIP()")


def test_min_width():
    pytest.skip("Upstream GTEST_SKIP()")


def test_justify_content_min_max():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetMaxHeight(root, 200)
    YGNodeStyleSetMinHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyCenter)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 60)
    YGNodeStyleSetHeight(root_child0, 60)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 20
    assert YGNodeLayoutGetWidth(root_child0) == 60
    assert YGNodeLayoutGetHeight(root_child0) == 60

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 40
    assert YGNodeLayoutGetTop(root_child0) == 20
    assert YGNodeLayoutGetWidth(root_child0) == 60
    assert YGNodeLayoutGetHeight(root_child0) == 60

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_align_items_min_max():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetMaxWidth(root, 200)
    YGNodeStyleSetMinWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 60)
    YGNodeStyleSetHeight(root_child0, 60)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 20
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 60
    assert YGNodeLayoutGetHeight(root_child0) == 60

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 20
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 60
    assert YGNodeLayoutGetHeight(root_child0) == 60

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_justify_content_overflow_min_max():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetMinHeight(root, 100)
    YGNodeStyleSetMaxHeight(root, 110)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyCenter)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 50)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 50)
    YGNodeStyleSetHeight(root_child2, 50)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 50
    assert YGNodeLayoutGetHeight(root) == 110

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == -20
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 30
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 50

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 80
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 50
    assert YGNodeLayoutGetHeight(root) == 110

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == -20
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 30
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 50

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 80
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 50

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_flex_grow_to_min():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetMinHeight(root, 100)
    YGNodeStyleSetMaxHeight(root, 500)
    YGNodeStyleSetWidth(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeStyleSetFlexShrink(root_child0, 1)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1, 50)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 50
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 50
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 50

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_flex_grow_in_at_most_container():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0_child0, 1)
    YGNodeStyleSetFlexBasis(root_child0_child0, 0)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)
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
    assert YGNodeLayoutGetWidth(root_child0_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0_child0) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0_child0) == 0

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_flex_grow_child():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeStyleSetFlexBasis(root_child0, 0)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 0
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 0
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0) == 100

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_flex_grow_within_constrained_min_max_column():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetMinHeight(root, 100)
    YGNodeStyleSetMaxHeight(root, 200)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1, 50)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 0
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 50
    assert YGNodeLayoutGetWidth(root_child1) == 0
    assert YGNodeLayoutGetHeight(root_child1) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 0
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 50
    assert YGNodeLayoutGetWidth(root_child1) == 0
    assert YGNodeLayoutGetHeight(root_child1) == 50

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_flex_grow_within_max_width():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetMaxWidth(root_child0, 100)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 20)
    YGNodeStyleSetFlexGrow(root_child0_child0, 1)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_flex_grow_within_constrained_max_width():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetMaxWidth(root_child0, 300)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 20)
    YGNodeStyleSetFlexGrow(root_child0_child0, 1)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_flex_root_ignored():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetMinHeight(root, 100)
    YGNodeStyleSetMaxHeight(root, 500)
    YGNodeStyleSetFlexGrow(root, 1)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexBasis(root_child0, 200)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1, 100)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 200
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 200
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 100

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_flex_grow_root_minimized():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetMinHeight(root, 100)
    YGNodeStyleSetMaxHeight(root, 500)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMinHeight(root_child0, 100)
    YGNodeStyleSetMaxHeight(root_child0, 500)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexBasis(root_child0_child0, 200)
    YGNodeStyleSetFlexGrow(root_child0_child0, 1)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child1, 100)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 300

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 200
    assert YGNodeLayoutGetWidth(root_child0_child1) == 100
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 300

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 200
    assert YGNodeLayoutGetWidth(root_child0_child1) == 100
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_flex_grow_height_maximized():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 500)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMinHeight(root_child0, 100)
    YGNodeStyleSetMaxHeight(root_child0, 500)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexBasis(root_child0_child0, 200)
    YGNodeStyleSetFlexGrow(root_child0_child0, 1)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child1, 100)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 500

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 500

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 400

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 400
    assert YGNodeLayoutGetWidth(root_child0_child1) == 100
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 500

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 500

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 400

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 400
    assert YGNodeLayoutGetWidth(root_child0_child1) == 100
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_flex_grow_within_constrained_min_row():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetMinWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 100

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_flex_grow_within_constrained_min_column():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetMinHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1, 50)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 0
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 50
    assert YGNodeLayoutGetWidth(root_child1) == 0
    assert YGNodeLayoutGetHeight(root_child1) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 0
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 0
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 50
    assert YGNodeLayoutGetWidth(root_child1) == 0
    assert YGNodeLayoutGetHeight(root_child1) == 50

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_flex_grow_within_constrained_max_row():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetMaxWidth(root_child0, 100)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexShrink(root_child0_child0, 1)
    YGNodeStyleSetFlexBasis(root_child0_child0, 100)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 50)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child1) == 50
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 50
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 50
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_flex_grow_within_constrained_max_column():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetMaxHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexShrink(root_child0, 1)
    YGNodeStyleSetFlexBasis(root_child0, 100)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1, 50)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 50
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 50
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 50

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_child_min_max_width_flexing():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 120)
    YGNodeStyleSetHeight(root, 50)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMinWidth(root_child0, 60)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeStyleSetFlexBasis(root_child0, 0)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMaxWidth(root_child1, 20)
    YGNodeStyleSetFlexGrow(root_child1, 1)
    YGNodeStyleSetFlexBasisPercent(root_child1, 50)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 120
    assert YGNodeLayoutGetHeight(root) == 50

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 100
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 120
    assert YGNodeLayoutGetHeight(root) == 50

    assert YGNodeLayoutGetLeft(root_child0) == 20
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 20
    assert YGNodeLayoutGetHeight(root_child1) == 50

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_min_width_overrides_width():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetMinWidth(root, 100)
    YGNodeStyleSetWidth(root, 50)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 0

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_max_width_overrides_width():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetMaxWidth(root, 100)
    YGNodeStyleSetWidth(root, 200)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 0

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_min_height_overrides_height():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetMinHeight(root, 100)
    YGNodeStyleSetHeight(root, 50)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 0
    assert YGNodeLayoutGetHeight(root) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 0
    assert YGNodeLayoutGetHeight(root) == 100

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_max_height_overrides_height():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetMaxHeight(root, 100)
    YGNodeStyleSetHeight(root, 200)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 0
    assert YGNodeLayoutGetHeight(root) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 0
    assert YGNodeLayoutGetHeight(root) == 100

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_min_max_percent_no_width_height():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMinWidthPercent(root_child0, 10)
    YGNodeStyleSetMaxWidthPercent(root_child0, 10)
    YGNodeStyleSetMinHeightPercent(root_child0, 10)
    YGNodeStyleSetMaxHeightPercent(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 10

    YGNodeFreeRecursive(root)
    YGConfigFree(config)
