import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import (  # noqa: E402
    YGAlign,
    YGDirection,
    YGFlexDirection,
    YGMeasureMode,
    YGNodeCalculateLayout,
    YGNodeFreeRecursive,
    YGNodeInsertChild,
    YGNodeNew,
    YGNodeSetContext,
    YGNodeSetMeasureFunc,
    YGNodeStyleSetAlignItems,
    YGNodeStyleSetFlexBasis,
    YGNodeStyleSetFlexDirection,
    YGNodeStyleSetFlexGrow,
    YGNodeStyleSetHeight,
    YGNodeStyleSetWidth,
)


def _measure(node, width, widthMode, height, heightMode):
    constraintList = node.getContext()
    constraintList.append(
        {
            "width": width,
            "widthMode": widthMode,
            "height": height,
            "heightMode": heightMode,
        }
    )
    return (
        width if widthMode != YGMeasureMode.YGMeasureModeUndefined else 10,
        width if heightMode != YGMeasureMode.YGMeasureModeUndefined else 10,
    )


def _measure_size(node, width, widthMode, height, heightMode):
    s = _measure(node, width, widthMode, height, heightMode)
    from yoga import YGSize
    return YGSize(*s)


def test_exactly_measure_stretched_child_column():
    constraints = []
    root = YGNodeNew()
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeSetContext(child, constraints)
    YGNodeSetMeasureFunc(child, _measure_size)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert len(constraints) == 1
    assert constraints[0]["width"] == 100
    assert constraints[0]["widthMode"] == YGMeasureMode.YGMeasureModeExactly
    YGNodeFreeRecursive(root)


def test_exactly_measure_stretched_child_row():
    constraints = []
    root = YGNodeNew()
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeSetContext(child, constraints)
    YGNodeSetMeasureFunc(child, _measure_size)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert len(constraints) == 1
    assert constraints[0]["height"] == 100
    assert constraints[0]["heightMode"] == YGMeasureMode.YGMeasureModeExactly
    YGNodeFreeRecursive(root)


def test_at_most_main_axis_column():
    constraints = []
    root = YGNodeNew()
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeSetContext(child, constraints)
    YGNodeSetMeasureFunc(child, _measure_size)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert len(constraints) == 1
    assert constraints[0]["height"] == 100
    assert constraints[0]["heightMode"] == YGMeasureMode.YGMeasureModeAtMost
    YGNodeFreeRecursive(root)


def test_at_most_cross_axis_column():
    constraints = []
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeSetContext(child, constraints)
    YGNodeSetMeasureFunc(child, _measure_size)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert len(constraints) == 1
    assert constraints[0]["width"] == 100
    assert constraints[0]["widthMode"] == YGMeasureMode.YGMeasureModeAtMost
    YGNodeFreeRecursive(root)


def test_at_most_main_axis_row():
    constraints = []
    root = YGNodeNew()
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeSetContext(child, constraints)
    YGNodeSetMeasureFunc(child, _measure_size)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert len(constraints) == 1
    assert constraints[0]["width"] == 100
    assert constraints[0]["widthMode"] == YGMeasureMode.YGMeasureModeAtMost
    YGNodeFreeRecursive(root)


def test_at_most_cross_axis_row():
    constraints = []
    root = YGNodeNew()
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeSetContext(child, constraints)
    YGNodeSetMeasureFunc(child, _measure_size)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert len(constraints) == 1
    assert constraints[0]["height"] == 100
    assert constraints[0]["heightMode"] == YGMeasureMode.YGMeasureModeAtMost
    YGNodeFreeRecursive(root)


def test_flex_child():
    constraints = []
    root = YGNodeNew()
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeStyleSetFlexGrow(child, 1)
    YGNodeSetContext(child, constraints)
    YGNodeSetMeasureFunc(child, _measure_size)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert len(constraints) == 2
    assert constraints[0]["height"] == 100
    assert constraints[0]["heightMode"] == YGMeasureMode.YGMeasureModeAtMost
    assert constraints[1]["height"] == 100
    assert constraints[1]["heightMode"] == YGMeasureMode.YGMeasureModeExactly
    YGNodeFreeRecursive(root)


def test_flex_child_with_flex_basis():
    constraints = []
    root = YGNodeNew()
    YGNodeStyleSetHeight(root, 100)
    child = YGNodeNew()
    YGNodeStyleSetFlexGrow(child, 1)
    YGNodeStyleSetFlexBasis(child, 0)
    YGNodeSetContext(child, constraints)
    YGNodeSetMeasureFunc(child, _measure_size)
    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert len(constraints) == 1
    YGNodeFreeRecursive(root)
