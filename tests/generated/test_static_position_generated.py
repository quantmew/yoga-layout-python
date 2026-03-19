import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from yoga import *  # noqa: E402,F403


def _assert_layout(node, left, top, width, height):
    assert YGNodeLayoutGetLeft(node) == left
    assert YGNodeLayoutGetTop(node) == top
    assert YGNodeLayoutGetWidth(node) == width
    assert YGNodeLayoutGetHeight(node) == height

def test_static_position_insets_have_no_effect_left_top():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeTop, 50)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeLeft, 50)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_insets_have_no_effect_right_bottom():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeBottom, 50)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeRight, 50)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_absolute_child_insets_relative_to_positioned_ancestor():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeLeft, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPosition(root_child0_child0_child0, YGEdge.YGEdgeTop, 50)
    YGNodeStyleSetPosition(root_child0_child0_child0, YGEdge.YGEdgeLeft, 50)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == -50
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == -50
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_absolute_child_insets_relative_to_positioned_ancestor_row_reverse():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPosition(root_child0_child0_child0, YGEdge.YGEdgeTop, 50)
    YGNodeStyleSetPosition(root_child0_child0_child0, YGEdge.YGEdgeLeft, 50)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == -50
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_column_reverse_static_position_absolute_child_insets_relative_to_positioned_ancestor_row_reverse():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeStyleSetFlexDirection(root_child0_child0, YGFlexDirection.YGFlexDirectionColumnReverse)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPosition(root_child0_child0_child0, YGEdge.YGEdgeTop, 50)
    YGNodeStyleSetPosition(root_child0_child0_child0, YGEdge.YGEdgeLeft, 50)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == -50
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_absolute_child_insets_relative_to_positioned_ancestor_row():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPosition(root_child0_child0_child0, YGEdge.YGEdgeTop, 50)
    YGNodeStyleSetPosition(root_child0_child0_child0, YGEdge.YGEdgeRight, 50)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_column_reverse_static_position_absolute_child_insets_relative_to_positioned_ancestor_row():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeStyleSetFlexDirection(root_child0_child0, YGFlexDirection.YGFlexDirectionColumnReverse)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPosition(root_child0_child0_child0, YGEdge.YGEdgeTop, 50)
    YGNodeStyleSetPosition(root_child0_child0_child0, YGEdge.YGEdgeRight, 50)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_absolute_child_insets_relative_to_positioned_ancestor_column_reverse():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionColumnReverse)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPosition(root_child0_child0_child0, YGEdge.YGEdgeTop, 50)
    YGNodeStyleSetPosition(root_child0_child0_child0, YGEdge.YGEdgeRight, 50)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == -50
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == -50
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_column_reverse_static_position_absolute_child_insets_relative_to_positioned_ancestor_column_reverse():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionColumnReverse)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeStyleSetFlexDirection(root_child0_child0, YGFlexDirection.YGFlexDirectionColumnReverse)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPosition(root_child0_child0_child0, YGEdge.YGEdgeTop, 50)
    YGNodeStyleSetPosition(root_child0_child0_child0, YGEdge.YGEdgeRight, 50)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == -50
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == -50
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_absolute_child_insets_relative_to_positioned_ancestor_deep():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeLeft, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0_child0, 100)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeLeft, 100)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)

    root_child0_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0_child0_child0, 100)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 100)
    YGNodeStyleSetPositionType(root_child0_child0_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0_child0_child0, root_child0_child0_child0_child0, 0)

    root_child0_child0_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0_child0_child0_child0, 100)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 100)
    YGNodeStyleSetPositionType(root_child0_child0_child0_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0_child0_child0_child0, root_child0_child0_child0_child0_child0, 0)

    root_child0_child0_child0_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0_child0_child0_child0, 50)
    YGNodeStyleSetWidth(root_child0_child0_child0_child0_child0_child0, 50)
    YGNodeStyleSetPositionType(root_child0_child0_child0_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPosition(root_child0_child0_child0_child0_child0_child0, YGEdge.YGEdgeTop, 50)
    YGNodeStyleSetPosition(root_child0_child0_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 50)
    YGNodeInsertChild(root_child0_child0_child0_child0_child0, root_child0_child0_child0_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0_child0_child0_child0) == -350
    assert YGNodeLayoutGetTop(root_child0_child0_child0_child0_child0_child0) == 50
    assert YGNodeLayoutGetWidth(root_child0_child0_child0_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0_child0_child0_child0) == -50
    assert YGNodeLayoutGetTop(root_child0_child0_child0_child0_child0_child0) == 50
    assert YGNodeLayoutGetWidth(root_child0_child0_child0_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_absolute_child_width_percentage():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidthPercent(root_child0_child0_child0, 50)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_relative_child_width_percentage():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidthPercent(root_child0_child0_child0, 50)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_static_child_width_percentage():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidthPercent(root_child0_child0_child0, 50)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_absolute_child_height_percentage():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeightPercent(root_child0_child0_child0, 50)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_relative_child_height_percentage():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeightPercent(root_child0_child0_child0, 50)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_static_child_height_percentage():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeightPercent(root_child0_child0_child0, 50)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_absolute_child_left_percentage():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeStyleSetPositionPercent(root_child0_child0_child0, YGEdge.YGEdgeLeft, 50)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_relative_child_left_percentage():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeStyleSetPositionPercent(root_child0_child0_child0, YGEdge.YGEdgeLeft, 50)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_static_child_left_percentage():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeStyleSetPositionPercent(root_child0_child0_child0, YGEdge.YGEdgeLeft, 50)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_absolute_child_right_percentage():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeStyleSetPositionPercent(root_child0_child0_child0, YGEdge.YGEdgeRight, 50)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == -50
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_relative_child_right_percentage():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeStyleSetPositionPercent(root_child0_child0_child0, YGEdge.YGEdgeRight, 50)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == -50
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_static_child_right_percentage():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeStyleSetPositionPercent(root_child0_child0_child0, YGEdge.YGEdgeRight, 50)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_absolute_child_top_percentage():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeStyleSetPositionPercent(root_child0_child0_child0, YGEdge.YGEdgeTop, 50)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_relative_child_top_percentage():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeStyleSetPositionPercent(root_child0_child0_child0, YGEdge.YGEdgeTop, 50)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_static_child_top_percentage():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeStyleSetPositionPercent(root_child0_child0_child0, YGEdge.YGEdgeTop, 50)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_absolute_child_bottom_percentage():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeStyleSetPositionPercent(root_child0_child0_child0, YGEdge.YGEdgeBottom, 50)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_relative_child_bottom_percentage():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeStyleSetPositionPercent(root_child0_child0_child0, YGEdge.YGEdgeBottom, 50)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == -50
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == -50
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_static_child_bottom_percentage():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeStyleSetPositionPercent(root_child0_child0_child0, YGEdge.YGEdgeBottom, 50)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_absolute_child_margin_percentage():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeStyleSetMarginPercent(root_child0_child0_child0, YGEdge.YGEdgeAll, 50)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == -50
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_relative_child_margin_percentage():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeStyleSetMarginPercent(root_child0_child0_child0, YGEdge.YGEdgeAll, 50)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_static_child_margin_percentage():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeStyleSetMarginPercent(root_child0_child0_child0, YGEdge.YGEdgeAll, 50)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_absolute_child_padding_percentage():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeStyleSetPaddingPercent(root_child0_child0_child0, YGEdge.YGEdgeAll, 50)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 200

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == -100
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 200

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_relative_child_padding_percentage():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeStyleSetPaddingPercent(root_child0_child0_child0, YGEdge.YGEdgeAll, 50)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_static_child_padding_percentage():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeStyleSetPaddingPercent(root_child0_child0_child0, YGEdge.YGEdgeAll, 50)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_absolute_child_border_percentage():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_relative_child_border_percentage():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_static_child_border_percentage():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_absolute_child_containing_block_padding_box():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 400)
    YGNodeStyleSetHeight(root_child0, 400)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeAll, 100)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidthPercent(root_child0_child0_child0, 50)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 400
    assert YGNodeLayoutGetHeight(root) == 400

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 400

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 400
    assert YGNodeLayoutGetHeight(root) == 400

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 400

    assert YGNodeLayoutGetLeft(root_child0_child0) == 200
    assert YGNodeLayoutGetTop(root_child0_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == -100
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_relative_child_containing_block_padding_box():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 400)
    YGNodeStyleSetHeight(root_child0, 400)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeAll, 100)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidthPercent(root_child0_child0_child0, 50)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 400
    assert YGNodeLayoutGetHeight(root) == 400

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 400

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 400
    assert YGNodeLayoutGetHeight(root) == 400

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 400

    assert YGNodeLayoutGetLeft(root_child0_child0) == 200
    assert YGNodeLayoutGetTop(root_child0_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_static_child_containing_block_padding_box():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 400)
    YGNodeStyleSetHeight(root_child0, 400)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeAll, 100)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidthPercent(root_child0_child0_child0, 50)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 400
    assert YGNodeLayoutGetHeight(root) == 400

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 400

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 400
    assert YGNodeLayoutGetHeight(root) == 400

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 400

    assert YGNodeLayoutGetLeft(root_child0_child0) == 200
    assert YGNodeLayoutGetTop(root_child0_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_absolute_child_containing_block_content_box():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 400)
    YGNodeStyleSetHeight(root_child0, 400)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeAll, 100)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 50)
    YGNodeStyleSetWidthPercent(root_child0_child0, 50)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 400
    assert YGNodeLayoutGetHeight(root) == 400

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 400

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 400
    assert YGNodeLayoutGetHeight(root) == 400

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 400

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_relative_child_containing_block_content_box():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 400)
    YGNodeStyleSetHeight(root_child0, 400)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeAll, 100)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 50)
    YGNodeStyleSetWidthPercent(root_child0_child0, 50)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 400
    assert YGNodeLayoutGetHeight(root) == 400

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 400

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 400
    assert YGNodeLayoutGetHeight(root) == 400

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 400

    assert YGNodeLayoutGetLeft(root_child0_child0) == 200
    assert YGNodeLayoutGetTop(root_child0_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_static_child_containing_block_content_box():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 400)
    YGNodeStyleSetHeight(root_child0, 400)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeAll, 100)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 50)
    YGNodeStyleSetWidthPercent(root_child0_child0, 50)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 400
    assert YGNodeLayoutGetHeight(root) == 400

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 400

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 400
    assert YGNodeLayoutGetHeight(root) == 400

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 400

    assert YGNodeLayoutGetLeft(root_child0_child0) == 200
    assert YGNodeLayoutGetTop(root_child0_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_containing_block_padding_and_border():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 400)
    YGNodeStyleSetHeight(root_child0, 400)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeTop, 8)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeRight, 1)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeBottom, 4)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeTop, 5)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeRight, 7)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeBottom, 4)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeightPercent(root_child0_child0_child0, 61)
    YGNodeStyleSetWidthPercent(root_child0_child0_child0, 41)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 400
    assert YGNodeLayoutGetHeight(root) == 400

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 400

    assert YGNodeLayoutGetLeft(root_child0_child0) == 11
    assert YGNodeLayoutGetTop(root_child0_child0) == 13
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 160
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 239

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 400
    assert YGNodeLayoutGetHeight(root) == 400

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 400

    assert YGNodeLayoutGetLeft(root_child0_child0) == 292
    assert YGNodeLayoutGetTop(root_child0_child0) == 13
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == -60
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 160
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 239

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_amalgamation():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 500)
    YGNodeStyleSetHeight(root_child0, 500)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeTop, 5)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeLeft, 4)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeRight, 7)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeBottom, 8)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeTop, 9)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeRight, 11)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeBottom, 13)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 200)
    YGNodeStyleSetWidth(root_child0_child0, 200)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeRight, 3)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeRight, 2)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeTop, 7)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeBottom, 4)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeLeft, 1)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeightPercent(root_child0_child0_child0, 63)
    YGNodeStyleSetWidthPercent(root_child0_child0_child0, 41)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPosition(root_child0_child0_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPosition(root_child0_child0_child0, YGEdge.YGEdgeRight, 12)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 513
    assert YGNodeLayoutGetHeight(root) == 506

    assert YGNodeLayoutGetLeft(root_child0) == 4
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 500
    assert YGNodeLayoutGetHeight(root_child0) == 500

    assert YGNodeLayoutGetLeft(root_child0_child0) == 15
    assert YGNodeLayoutGetTop(root_child0_child0) == 21
    assert YGNodeLayoutGetWidth(root_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 1
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 306

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 513
    assert YGNodeLayoutGetHeight(root) == 506

    assert YGNodeLayoutGetLeft(root_child0) == 4
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 500
    assert YGNodeLayoutGetHeight(root_child0) == 500

    assert YGNodeLayoutGetLeft(root_child0_child0) == 279
    assert YGNodeLayoutGetTop(root_child0_child0) == 21
    assert YGNodeLayoutGetWidth(root_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == -2
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 306

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_no_position_amalgamation():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 500)
    YGNodeStyleSetHeight(root_child0, 500)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeTop, 5)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeLeft, 4)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeRight, 7)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeBottom, 8)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeTop, 9)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeRight, 11)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeBottom, 13)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 200)
    YGNodeStyleSetWidth(root_child0_child0, 200)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeRight, 3)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeRight, 2)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeTop, 7)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeBottom, 4)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeLeft, 1)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeightPercent(root_child0_child0_child0, 63)
    YGNodeStyleSetWidthPercent(root_child0_child0_child0, 41)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 513
    assert YGNodeLayoutGetHeight(root) == 506

    assert YGNodeLayoutGetLeft(root_child0) == 4
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 500
    assert YGNodeLayoutGetHeight(root_child0) == 500

    assert YGNodeLayoutGetLeft(root_child0_child0) == 15
    assert YGNodeLayoutGetTop(root_child0_child0) == 21
    assert YGNodeLayoutGetWidth(root_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 18
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 306

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 513
    assert YGNodeLayoutGetHeight(root) == 506

    assert YGNodeLayoutGetLeft(root_child0) == 4
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 500
    assert YGNodeLayoutGetHeight(root_child0) == 500

    assert YGNodeLayoutGetLeft(root_child0_child0) == 279
    assert YGNodeLayoutGetTop(root_child0_child0) == 21
    assert YGNodeLayoutGetWidth(root_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == -15
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 306

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_zero_for_inset_amalgamation():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 500)
    YGNodeStyleSetHeight(root_child0, 500)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeTop, 5)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeLeft, 4)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeRight, 7)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeBottom, 8)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeTop, 9)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeRight, 11)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeBottom, 13)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 200)
    YGNodeStyleSetWidth(root_child0_child0, 200)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeRight, 3)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeRight, 2)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeTop, 7)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeBottom, 4)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeLeft, 1)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeightPercent(root_child0_child0_child0, 63)
    YGNodeStyleSetWidthPercent(root_child0_child0_child0, 41)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPositionPercent(root_child0_child0_child0, YGEdge.YGEdgeLeft, 0)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 513
    assert YGNodeLayoutGetHeight(root) == 506

    assert YGNodeLayoutGetLeft(root_child0) == 4
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 500
    assert YGNodeLayoutGetHeight(root_child0) == 500

    assert YGNodeLayoutGetLeft(root_child0_child0) == 15
    assert YGNodeLayoutGetTop(root_child0_child0) == 21
    assert YGNodeLayoutGetWidth(root_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == -1
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 306

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 513
    assert YGNodeLayoutGetHeight(root) == 506

    assert YGNodeLayoutGetLeft(root_child0) == 4
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 500
    assert YGNodeLayoutGetHeight(root_child0) == 500

    assert YGNodeLayoutGetLeft(root_child0_child0) == 279
    assert YGNodeLayoutGetTop(root_child0_child0) == 21
    assert YGNodeLayoutGetWidth(root_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == -265
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 306

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_start_inset_amalgamation():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 500)
    YGNodeStyleSetHeight(root_child0, 500)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeTop, 5)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeLeft, 4)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeRight, 7)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeBottom, 8)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeTop, 9)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeRight, 11)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeBottom, 13)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 200)
    YGNodeStyleSetWidth(root_child0_child0, 200)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeRight, 3)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeRight, 2)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeTop, 7)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeBottom, 4)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeLeft, 1)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeightPercent(root_child0_child0_child0, 63)
    YGNodeStyleSetWidthPercent(root_child0_child0_child0, 41)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPosition(root_child0_child0_child0, YGEdge.YGEdgeStart, 12)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 513
    assert YGNodeLayoutGetHeight(root) == 506

    assert YGNodeLayoutGetLeft(root_child0) == 4
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 500
    assert YGNodeLayoutGetHeight(root_child0) == 500

    assert YGNodeLayoutGetLeft(root_child0_child0) == 15
    assert YGNodeLayoutGetTop(root_child0_child0) == 21
    assert YGNodeLayoutGetWidth(root_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 11
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 306

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 513
    assert YGNodeLayoutGetHeight(root) == 506

    assert YGNodeLayoutGetLeft(root_child0) == 4
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 500
    assert YGNodeLayoutGetHeight(root_child0) == 500

    assert YGNodeLayoutGetLeft(root_child0_child0) == 279
    assert YGNodeLayoutGetTop(root_child0_child0) == 21
    assert YGNodeLayoutGetWidth(root_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == -2
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 306

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_end_inset_amalgamation():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 500)
    YGNodeStyleSetHeight(root_child0, 500)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeTop, 5)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeLeft, 4)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeRight, 7)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeBottom, 8)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeTop, 9)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeRight, 11)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeBottom, 13)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 200)
    YGNodeStyleSetWidth(root_child0_child0, 200)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeRight, 3)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeRight, 2)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeTop, 7)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeBottom, 4)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeLeft, 1)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeightPercent(root_child0_child0_child0, 63)
    YGNodeStyleSetWidthPercent(root_child0_child0_child0, 41)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPosition(root_child0_child0_child0, YGEdge.YGEdgeEnd, 4)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 513
    assert YGNodeLayoutGetHeight(root) == 506

    assert YGNodeLayoutGetLeft(root_child0) == 4
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 500
    assert YGNodeLayoutGetHeight(root_child0) == 500

    assert YGNodeLayoutGetLeft(root_child0_child0) == 15
    assert YGNodeLayoutGetTop(root_child0_child0) == 21
    assert YGNodeLayoutGetWidth(root_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 270
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 306

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 513
    assert YGNodeLayoutGetHeight(root) == 506

    assert YGNodeLayoutGetLeft(root_child0) == 4
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 500
    assert YGNodeLayoutGetHeight(root_child0) == 500

    assert YGNodeLayoutGetLeft(root_child0_child0) == 279
    assert YGNodeLayoutGetTop(root_child0_child0) == 21
    assert YGNodeLayoutGetWidth(root_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == -261
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 306

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_row_reverse_amalgamation():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeTop, 5)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeLeft, 4)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeRight, 7)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeBottom, 8)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeTop, 9)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeRight, 11)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeBottom, 13)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeRight, 3)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeRight, 2)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeTop, 7)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeBottom, 4)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeLeft, 1)
    YGNodeStyleSetFlexDirection(root_child0_child0, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeightPercent(root_child0_child0_child0, 12)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)

    root_child0_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0_child0_child0, 100)
    YGNodeStyleSetHeight(root_child0_child0_child0_child0, 50)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0_child0, root_child0_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 69
    assert YGNodeLayoutGetHeight(root) == 79

    assert YGNodeLayoutGetLeft(root_child0) == 4
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 56
    assert YGNodeLayoutGetHeight(root_child0) == 73

    assert YGNodeLayoutGetLeft(root_child0_child0) == 15
    assert YGNodeLayoutGetTop(root_child0_child0) == 21
    assert YGNodeLayoutGetWidth(root_child0_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0) == 22

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == -128
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 133
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 23

    assert YGNodeLayoutGetLeft(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetTop(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 69
    assert YGNodeLayoutGetHeight(root) == 79

    assert YGNodeLayoutGetLeft(root_child0) == 4
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 56
    assert YGNodeLayoutGetHeight(root_child0) == 73

    assert YGNodeLayoutGetLeft(root_child0_child0) == 15
    assert YGNodeLayoutGetTop(root_child0_child0) == 21
    assert YGNodeLayoutGetWidth(root_child0_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0) == 22

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 18
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 133
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 23

    assert YGNodeLayoutGetLeft(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetTop(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_column_reverse_amalgamation():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeTop, 5)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeLeft, 4)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeRight, 7)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeBottom, 8)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeTop, 9)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeRight, 11)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeBottom, 13)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeRight, 3)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeRight, 2)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeTop, 7)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeBottom, 4)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeLeft, 1)
    YGNodeStyleSetFlexDirection(root_child0_child0, YGFlexDirection.YGFlexDirectionColumnReverse)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidthPercent(root_child0_child0_child0, 21)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)

    root_child0_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0_child0_child0, 100)
    YGNodeStyleSetHeight(root_child0_child0_child0_child0, 50)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0_child0, root_child0_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 69
    assert YGNodeLayoutGetHeight(root) == 79

    assert YGNodeLayoutGetLeft(root_child0) == 4
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 56
    assert YGNodeLayoutGetHeight(root_child0) == 73

    assert YGNodeLayoutGetLeft(root_child0_child0) == 15
    assert YGNodeLayoutGetTop(root_child0_child0) == 21
    assert YGNodeLayoutGetWidth(root_child0_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0) == 22

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 18
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == -82
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetTop(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 69
    assert YGNodeLayoutGetHeight(root) == 79

    assert YGNodeLayoutGetLeft(root_child0) == 4
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 56
    assert YGNodeLayoutGetHeight(root_child0) == 73

    assert YGNodeLayoutGetLeft(root_child0_child0) == 15
    assert YGNodeLayoutGetTop(root_child0_child0) == 21
    assert YGNodeLayoutGetWidth(root_child0_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0) == 22

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == -15
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == -82
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child0_child0) == -97
    assert YGNodeLayoutGetTop(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_justify_flex_start_amalgamation():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeTop, 5)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeLeft, 4)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeRight, 7)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeBottom, 8)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeTop, 9)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeRight, 11)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeBottom, 13)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeRight, 3)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeRight, 2)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeTop, 7)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeBottom, 4)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeLeft, 1)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidthPercent(root_child0_child0_child0, 21)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)

    root_child0_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0_child0_child0, 100)
    YGNodeStyleSetHeight(root_child0_child0_child0_child0, 50)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0_child0, root_child0_child0_child0_child0, 0)

    root_child0_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child0_child1, 10)
    YGNodeStyleSetMargin(root_child0_child0_child1, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child1, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child1, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child1, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child1, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child1, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child1, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child1, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child1, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child1, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child1, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child1, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child1, 1)

    root_child0_child0_child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0_child1_child0, 100)
    YGNodeStyleSetHeight(root_child0_child0_child1_child0, 50)
    YGNodeStyleSetMargin(root_child0_child0_child1_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child1_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child1_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child1_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child1_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child1_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child1_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child1_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child1_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child1_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child1_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child1_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0_child1, root_child0_child0_child1_child0, 0)

    root_child0_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child0_child2, 10)
    YGNodeStyleSetMargin(root_child0_child0_child2, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child2, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child2, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child2, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child2, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child2, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child2, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child2, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child2, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child2, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child2, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child2, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child2, 2)

    root_child0_child0_child2_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0_child2_child0, 100)
    YGNodeStyleSetHeight(root_child0_child0_child2_child0, 50)
    YGNodeStyleSetMargin(root_child0_child0_child2_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child2_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child2_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child2_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child2_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child2_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child2_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child2_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child2_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child2_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child2_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child2_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0_child2, root_child0_child0_child2_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 215
    assert YGNodeLayoutGetHeight(root) == 301

    assert YGNodeLayoutGetLeft(root_child0) == 4
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 202
    assert YGNodeLayoutGetHeight(root_child0) == 295

    assert YGNodeLayoutGetLeft(root_child0_child0) == 15
    assert YGNodeLayoutGetTop(root_child0_child0) == 21
    assert YGNodeLayoutGetWidth(root_child0_child0) == 166
    assert YGNodeLayoutGetHeight(root_child0_child0) == 244

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 18
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetTop(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0_child1) == 18
    assert YGNodeLayoutGetTop(root_child0_child0_child1) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child1) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child1) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child1_child0) == 16
    assert YGNodeLayoutGetTop(root_child0_child0_child1_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child1_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child1_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0_child2) == 18
    assert YGNodeLayoutGetTop(root_child0_child0_child2) == 140
    assert YGNodeLayoutGetWidth(root_child0_child0_child2) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child2) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child2_child0) == 16
    assert YGNodeLayoutGetTop(root_child0_child0_child2_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child2_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child2_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 215
    assert YGNodeLayoutGetHeight(root) == 301

    assert YGNodeLayoutGetLeft(root_child0) == 4
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 202
    assert YGNodeLayoutGetHeight(root_child0) == 295

    assert YGNodeLayoutGetLeft(root_child0_child0) == 15
    assert YGNodeLayoutGetTop(root_child0_child0) == 21
    assert YGNodeLayoutGetWidth(root_child0_child0) == 166
    assert YGNodeLayoutGetHeight(root_child0_child0) == 244

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 111
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child0_child0) == -77
    assert YGNodeLayoutGetTop(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0_child1) == 131
    assert YGNodeLayoutGetTop(root_child0_child0_child1) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child1) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child1) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child1_child0) == -97
    assert YGNodeLayoutGetTop(root_child0_child0_child1_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child1_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child1_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0_child2) == 131
    assert YGNodeLayoutGetTop(root_child0_child0_child2) == 140
    assert YGNodeLayoutGetWidth(root_child0_child0_child2) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child2) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child2_child0) == -97
    assert YGNodeLayoutGetTop(root_child0_child0_child2_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child2_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child2_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_justify_flex_start_position_set_amalgamation():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeTop, 5)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeLeft, 4)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeRight, 7)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeBottom, 8)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeTop, 9)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeRight, 11)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeBottom, 13)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeRight, 3)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeRight, 2)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeTop, 7)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeBottom, 4)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeLeft, 1)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidthPercent(root_child0_child0_child0, 21)
    YGNodeStyleSetPosition(root_child0_child0_child0, YGEdge.YGEdgeRight, 30)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)

    root_child0_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0_child0_child0, 100)
    YGNodeStyleSetHeight(root_child0_child0_child0_child0, 50)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0_child0, root_child0_child0_child0_child0, 0)

    root_child0_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child0_child1, 10)
    YGNodeStyleSetMargin(root_child0_child0_child1, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child1, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child1, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child1, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child1, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child1, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child1, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child1, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child1, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child1, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child1, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child1, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child1, 1)

    root_child0_child0_child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0_child1_child0, 100)
    YGNodeStyleSetHeight(root_child0_child0_child1_child0, 50)
    YGNodeStyleSetMargin(root_child0_child0_child1_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child1_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child1_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child1_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child1_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child1_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child1_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child1_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child1_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child1_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child1_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child1_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0_child1, root_child0_child0_child1_child0, 0)

    root_child0_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child0_child2, 10)
    YGNodeStyleSetMargin(root_child0_child0_child2, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child2, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child2, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child2, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child2, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child2, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child2, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child2, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child2, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child2, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child2, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child2, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child2, 2)

    root_child0_child0_child2_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0_child2_child0, 100)
    YGNodeStyleSetHeight(root_child0_child0_child2_child0, 50)
    YGNodeStyleSetMargin(root_child0_child0_child2_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child2_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child2_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child2_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child2_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child2_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child2_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child2_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child2_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child2_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child2_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child2_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0_child2, root_child0_child0_child2_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 215
    assert YGNodeLayoutGetHeight(root) == 301

    assert YGNodeLayoutGetLeft(root_child0) == 4
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 202
    assert YGNodeLayoutGetHeight(root_child0) == 295

    assert YGNodeLayoutGetLeft(root_child0_child0) == 15
    assert YGNodeLayoutGetTop(root_child0_child0) == 21
    assert YGNodeLayoutGetWidth(root_child0_child0) == 166
    assert YGNodeLayoutGetHeight(root_child0_child0) == 244

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 106
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetTop(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0_child1) == 18
    assert YGNodeLayoutGetTop(root_child0_child0_child1) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child1) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child1) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child1_child0) == 16
    assert YGNodeLayoutGetTop(root_child0_child0_child1_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child1_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child1_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0_child2) == 18
    assert YGNodeLayoutGetTop(root_child0_child0_child2) == 140
    assert YGNodeLayoutGetWidth(root_child0_child0_child2) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child2) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child2_child0) == 16
    assert YGNodeLayoutGetTop(root_child0_child0_child2_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child2_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child2_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 215
    assert YGNodeLayoutGetHeight(root) == 301

    assert YGNodeLayoutGetLeft(root_child0) == 4
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 202
    assert YGNodeLayoutGetHeight(root_child0) == 295

    assert YGNodeLayoutGetLeft(root_child0_child0) == 15
    assert YGNodeLayoutGetTop(root_child0_child0) == 21
    assert YGNodeLayoutGetWidth(root_child0_child0) == 166
    assert YGNodeLayoutGetHeight(root_child0_child0) == 244

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 106
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child0_child0) == -77
    assert YGNodeLayoutGetTop(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0_child1) == 131
    assert YGNodeLayoutGetTop(root_child0_child0_child1) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child1) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child1) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child1_child0) == -97
    assert YGNodeLayoutGetTop(root_child0_child0_child1_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child1_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child1_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0_child2) == 131
    assert YGNodeLayoutGetTop(root_child0_child0_child2) == 140
    assert YGNodeLayoutGetWidth(root_child0_child0_child2) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child2) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child2_child0) == -97
    assert YGNodeLayoutGetTop(root_child0_child0_child2_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child2_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child2_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_no_definite_size_amalgamation():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeTop, 5)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeLeft, 4)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeRight, 7)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeBottom, 8)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeTop, 9)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeRight, 11)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeBottom, 13)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeRight, 3)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeRight, 2)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeTop, 7)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeBottom, 4)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeLeft, 1)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPositionPercent(root_child0_child0_child0, YGEdge.YGEdgeLeft, 23)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)

    root_child0_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0_child0_child0, 100)
    YGNodeStyleSetHeight(root_child0_child0_child0_child0, 50)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0_child0, root_child0_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 69
    assert YGNodeLayoutGetHeight(root) == 79

    assert YGNodeLayoutGetLeft(root_child0) == 4
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 56
    assert YGNodeLayoutGetHeight(root_child0) == 73

    assert YGNodeLayoutGetLeft(root_child0_child0) == 15
    assert YGNodeLayoutGetTop(root_child0_child0) == 21
    assert YGNodeLayoutGetWidth(root_child0_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0) == 22

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 9
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 133
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetTop(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 69
    assert YGNodeLayoutGetHeight(root) == 79

    assert YGNodeLayoutGetLeft(root_child0) == 4
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 56
    assert YGNodeLayoutGetHeight(root_child0) == 73

    assert YGNodeLayoutGetLeft(root_child0_child0) == 15
    assert YGNodeLayoutGetTop(root_child0_child0) == 21
    assert YGNodeLayoutGetWidth(root_child0_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0) == 22

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 9
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 133
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetTop(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_both_insets_set_amalgamation():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeTop, 5)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeLeft, 4)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeRight, 7)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeBottom, 8)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeTop, 9)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeRight, 11)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeBottom, 13)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeRight, 3)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeRight, 2)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeTop, 7)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeBottom, 4)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeLeft, 1)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPositionPercent(root_child0_child0_child0, YGEdge.YGEdgeLeft, 23)
    YGNodeStyleSetPosition(root_child0_child0_child0, YGEdge.YGEdgeRight, 13)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)

    root_child0_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0_child0_child0, 100)
    YGNodeStyleSetHeight(root_child0_child0_child0_child0, 50)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0_child0, root_child0_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 69
    assert YGNodeLayoutGetHeight(root) == 79

    assert YGNodeLayoutGetLeft(root_child0) == 4
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 56
    assert YGNodeLayoutGetHeight(root_child0) == 73

    assert YGNodeLayoutGetLeft(root_child0_child0) == 15
    assert YGNodeLayoutGetTop(root_child0_child0) == 21
    assert YGNodeLayoutGetWidth(root_child0_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0) == 22

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 9
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetTop(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 69
    assert YGNodeLayoutGetHeight(root) == 79

    assert YGNodeLayoutGetLeft(root_child0) == 4
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 56
    assert YGNodeLayoutGetHeight(root_child0) == 73

    assert YGNodeLayoutGetLeft(root_child0_child0) == 15
    assert YGNodeLayoutGetTop(root_child0_child0) == 21
    assert YGNodeLayoutGetWidth(root_child0_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0) == 22

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == -3
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child0_child0) == -97
    assert YGNodeLayoutGetTop(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_justify_center_amalgamation():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeTop, 5)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeLeft, 4)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeRight, 7)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeBottom, 8)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeTop, 9)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeRight, 11)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeBottom, 13)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeRight, 3)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeRight, 2)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeTop, 7)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeBottom, 4)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeLeft, 1)
    YGNodeStyleSetJustifyContent(root_child0_child0, YGJustify.YGJustifyCenter)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidthPercent(root_child0_child0_child0, 21)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)

    root_child0_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0_child0_child0, 100)
    YGNodeStyleSetHeight(root_child0_child0_child0_child0, 50)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0_child0, root_child0_child0_child0_child0, 0)

    root_child0_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child0_child1, 10)
    YGNodeStyleSetMargin(root_child0_child0_child1, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child1, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child1, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child1, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child1, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child1, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child1, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child1, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child1, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child1, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child1, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child1, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child1, 1)

    root_child0_child0_child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0_child1_child0, 100)
    YGNodeStyleSetHeight(root_child0_child0_child1_child0, 50)
    YGNodeStyleSetMargin(root_child0_child0_child1_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child1_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child1_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child1_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child1_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child1_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child1_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child1_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child1_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child1_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child1_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child1_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0_child1, root_child0_child0_child1_child0, 0)

    root_child0_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child0_child2, 10)
    YGNodeStyleSetMargin(root_child0_child0_child2, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child2, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child2, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child2, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child2, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child2, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child2, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child2, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child2, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child2, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child2, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child2, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child2, 2)

    root_child0_child0_child2_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0_child2_child0, 100)
    YGNodeStyleSetHeight(root_child0_child0_child2_child0, 50)
    YGNodeStyleSetMargin(root_child0_child0_child2_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child2_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child2_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child2_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child2_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child2_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child2_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child2_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child2_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child2_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child2_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child2_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0_child2, root_child0_child0_child2_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 215
    assert YGNodeLayoutGetHeight(root) == 301

    assert YGNodeLayoutGetLeft(root_child0) == 4
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 202
    assert YGNodeLayoutGetHeight(root_child0) == 295

    assert YGNodeLayoutGetLeft(root_child0_child0) == 15
    assert YGNodeLayoutGetTop(root_child0_child0) == 21
    assert YGNodeLayoutGetWidth(root_child0_child0) == 166
    assert YGNodeLayoutGetHeight(root_child0_child0) == 244

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 18
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 85
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetTop(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0_child1) == 18
    assert YGNodeLayoutGetTop(root_child0_child0_child1) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child1) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child1) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child1_child0) == 16
    assert YGNodeLayoutGetTop(root_child0_child0_child1_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child1_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child1_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0_child2) == 18
    assert YGNodeLayoutGetTop(root_child0_child0_child2) == 140
    assert YGNodeLayoutGetWidth(root_child0_child0_child2) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child2) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child2_child0) == 16
    assert YGNodeLayoutGetTop(root_child0_child0_child2_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child2_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child2_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 215
    assert YGNodeLayoutGetHeight(root) == 301

    assert YGNodeLayoutGetLeft(root_child0) == 4
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 202
    assert YGNodeLayoutGetHeight(root_child0) == 295

    assert YGNodeLayoutGetLeft(root_child0_child0) == 15
    assert YGNodeLayoutGetTop(root_child0_child0) == 21
    assert YGNodeLayoutGetWidth(root_child0_child0) == 166
    assert YGNodeLayoutGetHeight(root_child0_child0) == 244

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 111
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 85
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child0_child0) == -77
    assert YGNodeLayoutGetTop(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0_child1) == 131
    assert YGNodeLayoutGetTop(root_child0_child0_child1) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child1) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child1) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child1_child0) == -97
    assert YGNodeLayoutGetTop(root_child0_child0_child1_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child1_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child1_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0_child2) == 131
    assert YGNodeLayoutGetTop(root_child0_child0_child2) == 140
    assert YGNodeLayoutGetWidth(root_child0_child0_child2) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child2) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child2_child0) == -97
    assert YGNodeLayoutGetTop(root_child0_child0_child2_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child2_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child2_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_justify_flex_end_amalgamation():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeTop, 5)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeLeft, 4)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeRight, 7)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeBottom, 8)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeTop, 9)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeRight, 11)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeBottom, 13)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeRight, 3)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeRight, 2)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeTop, 7)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeBottom, 4)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeLeft, 1)
    YGNodeStyleSetJustifyContent(root_child0_child0, YGJustify.YGJustifyFlexEnd)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidthPercent(root_child0_child0_child0, 21)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)

    root_child0_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0_child0_child0, 100)
    YGNodeStyleSetHeight(root_child0_child0_child0_child0, 50)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0_child0, root_child0_child0_child0_child0, 0)

    root_child0_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child0_child1, 10)
    YGNodeStyleSetMargin(root_child0_child0_child1, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child1, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child1, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child1, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child1, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child1, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child1, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child1, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child1, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child1, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child1, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child1, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child1, 1)

    root_child0_child0_child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0_child1_child0, 100)
    YGNodeStyleSetHeight(root_child0_child0_child1_child0, 50)
    YGNodeStyleSetMargin(root_child0_child0_child1_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child1_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child1_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child1_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child1_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child1_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child1_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child1_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child1_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child1_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child1_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child1_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0_child1, root_child0_child0_child1_child0, 0)

    root_child0_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child0_child2, 10)
    YGNodeStyleSetMargin(root_child0_child0_child2, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child2, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child2, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child2, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child2, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child2, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child2, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child2, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child2, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child2, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child2, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child2, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child2, 2)

    root_child0_child0_child2_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0_child2_child0, 100)
    YGNodeStyleSetHeight(root_child0_child0_child2_child0, 50)
    YGNodeStyleSetMargin(root_child0_child0_child2_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child2_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child2_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child2_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child2_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child2_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child2_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child2_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child2_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child2_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child2_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child2_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0_child2, root_child0_child0_child2_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 215
    assert YGNodeLayoutGetHeight(root) == 301

    assert YGNodeLayoutGetLeft(root_child0) == 4
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 202
    assert YGNodeLayoutGetHeight(root_child0) == 295

    assert YGNodeLayoutGetLeft(root_child0_child0) == 15
    assert YGNodeLayoutGetTop(root_child0_child0) == 21
    assert YGNodeLayoutGetWidth(root_child0_child0) == 166
    assert YGNodeLayoutGetHeight(root_child0_child0) == 244

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 18
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 140
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetTop(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0_child1) == 18
    assert YGNodeLayoutGetTop(root_child0_child0_child1) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child1) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child1) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child1_child0) == 16
    assert YGNodeLayoutGetTop(root_child0_child0_child1_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child1_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child1_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0_child2) == 18
    assert YGNodeLayoutGetTop(root_child0_child0_child2) == 140
    assert YGNodeLayoutGetWidth(root_child0_child0_child2) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child2) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child2_child0) == 16
    assert YGNodeLayoutGetTop(root_child0_child0_child2_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child2_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child2_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 215
    assert YGNodeLayoutGetHeight(root) == 301

    assert YGNodeLayoutGetLeft(root_child0) == 4
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 202
    assert YGNodeLayoutGetHeight(root_child0) == 295

    assert YGNodeLayoutGetLeft(root_child0_child0) == 15
    assert YGNodeLayoutGetTop(root_child0_child0) == 21
    assert YGNodeLayoutGetWidth(root_child0_child0) == 166
    assert YGNodeLayoutGetHeight(root_child0_child0) == 244

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 111
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 140
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child0_child0) == -77
    assert YGNodeLayoutGetTop(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0_child1) == 131
    assert YGNodeLayoutGetTop(root_child0_child0_child1) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child1) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child1) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child1_child0) == -97
    assert YGNodeLayoutGetTop(root_child0_child0_child1_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child1_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child1_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0_child2) == 131
    assert YGNodeLayoutGetTop(root_child0_child0_child2) == 140
    assert YGNodeLayoutGetWidth(root_child0_child0_child2) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child2) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child2_child0) == -97
    assert YGNodeLayoutGetTop(root_child0_child0_child2_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child2_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child2_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_align_flex_start_amalgamation():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeTop, 5)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeLeft, 4)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeRight, 7)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeBottom, 8)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeTop, 9)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeRight, 11)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeBottom, 13)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeRight, 3)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeRight, 2)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeTop, 7)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeBottom, 4)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeLeft, 1)
    YGNodeStyleSetAlignItems(root_child0_child0, YGAlign.YGAlignFlexStart)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidthPercent(root_child0_child0_child0, 21)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)

    root_child0_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0_child0_child0, 100)
    YGNodeStyleSetHeight(root_child0_child0_child0_child0, 50)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0_child0, root_child0_child0_child0_child0, 0)

    root_child0_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child0_child1, 10)
    YGNodeStyleSetMargin(root_child0_child0_child1, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child1, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child1, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child1, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child1, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child1, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child1, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child1, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child1, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child1, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child1, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child1, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child1, 1)

    root_child0_child0_child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0_child1_child0, 100)
    YGNodeStyleSetHeight(root_child0_child0_child1_child0, 50)
    YGNodeStyleSetMargin(root_child0_child0_child1_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child1_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child1_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child1_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child1_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child1_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child1_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child1_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child1_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child1_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child1_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child1_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0_child1, root_child0_child0_child1_child0, 0)

    root_child0_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child0_child2, 10)
    YGNodeStyleSetMargin(root_child0_child0_child2, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child2, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child2, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child2, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child2, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child2, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child2, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child2, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child2, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child2, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child2, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child2, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child2, 2)

    root_child0_child0_child2_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0_child2_child0, 100)
    YGNodeStyleSetHeight(root_child0_child0_child2_child0, 50)
    YGNodeStyleSetMargin(root_child0_child0_child2_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child2_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child2_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child2_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child2_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child2_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child2_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child2_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child2_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child2_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child2_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child2_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0_child2, root_child0_child0_child2_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 215
    assert YGNodeLayoutGetHeight(root) == 301

    assert YGNodeLayoutGetLeft(root_child0) == 4
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 202
    assert YGNodeLayoutGetHeight(root_child0) == 295

    assert YGNodeLayoutGetLeft(root_child0_child0) == 15
    assert YGNodeLayoutGetTop(root_child0_child0) == 21
    assert YGNodeLayoutGetWidth(root_child0_child0) == 166
    assert YGNodeLayoutGetHeight(root_child0_child0) == 244

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 18
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetTop(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0_child1) == 18
    assert YGNodeLayoutGetTop(root_child0_child0_child1) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child1) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child1) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child1_child0) == 16
    assert YGNodeLayoutGetTop(root_child0_child0_child1_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child1_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child1_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0_child2) == 18
    assert YGNodeLayoutGetTop(root_child0_child0_child2) == 140
    assert YGNodeLayoutGetWidth(root_child0_child0_child2) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child2) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child2_child0) == 16
    assert YGNodeLayoutGetTop(root_child0_child0_child2_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child2_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child2_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 215
    assert YGNodeLayoutGetHeight(root) == 301

    assert YGNodeLayoutGetLeft(root_child0) == 4
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 202
    assert YGNodeLayoutGetHeight(root_child0) == 295

    assert YGNodeLayoutGetLeft(root_child0_child0) == 15
    assert YGNodeLayoutGetTop(root_child0_child0) == 21
    assert YGNodeLayoutGetWidth(root_child0_child0) == 166
    assert YGNodeLayoutGetHeight(root_child0_child0) == 244

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 111
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child0_child0) == -77
    assert YGNodeLayoutGetTop(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0_child1) == 131
    assert YGNodeLayoutGetTop(root_child0_child0_child1) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child1) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child1) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child1_child0) == -97
    assert YGNodeLayoutGetTop(root_child0_child0_child1_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child1_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child1_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0_child2) == 131
    assert YGNodeLayoutGetTop(root_child0_child0_child2) == 140
    assert YGNodeLayoutGetWidth(root_child0_child0_child2) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child2) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child2_child0) == -97
    assert YGNodeLayoutGetTop(root_child0_child0_child2_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child2_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child2_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_align_center_amalgamation():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeTop, 5)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeLeft, 4)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeRight, 7)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeBottom, 8)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeTop, 9)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeRight, 11)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeBottom, 13)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeRight, 3)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeRight, 2)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeTop, 7)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeBottom, 4)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeLeft, 1)
    YGNodeStyleSetAlignItems(root_child0_child0, YGAlign.YGAlignCenter)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidthPercent(root_child0_child0_child0, 21)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)

    root_child0_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0_child0_child0, 100)
    YGNodeStyleSetHeight(root_child0_child0_child0_child0, 50)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0_child0, root_child0_child0_child0_child0, 0)

    root_child0_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child0_child1, 10)
    YGNodeStyleSetMargin(root_child0_child0_child1, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child1, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child1, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child1, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child1, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child1, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child1, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child1, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child1, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child1, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child1, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child1, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child1, 1)

    root_child0_child0_child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0_child1_child0, 100)
    YGNodeStyleSetHeight(root_child0_child0_child1_child0, 50)
    YGNodeStyleSetMargin(root_child0_child0_child1_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child1_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child1_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child1_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child1_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child1_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child1_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child1_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child1_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child1_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child1_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child1_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0_child1, root_child0_child0_child1_child0, 0)

    root_child0_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child0_child2, 10)
    YGNodeStyleSetMargin(root_child0_child0_child2, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child2, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child2, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child2, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child2, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child2, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child2, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child2, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child2, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child2, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child2, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child2, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child2, 2)

    root_child0_child0_child2_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0_child2_child0, 100)
    YGNodeStyleSetHeight(root_child0_child0_child2_child0, 50)
    YGNodeStyleSetMargin(root_child0_child0_child2_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child2_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child2_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child2_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child2_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child2_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child2_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child2_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child2_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child2_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child2_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child2_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0_child2, root_child0_child0_child2_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 215
    assert YGNodeLayoutGetHeight(root) == 301

    assert YGNodeLayoutGetLeft(root_child0) == 4
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 202
    assert YGNodeLayoutGetHeight(root_child0) == 295

    assert YGNodeLayoutGetLeft(root_child0_child0) == 15
    assert YGNodeLayoutGetTop(root_child0_child0) == 21
    assert YGNodeLayoutGetWidth(root_child0_child0) == 166
    assert YGNodeLayoutGetHeight(root_child0_child0) == 244

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 65
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 39
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetTop(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0_child1) == 75
    assert YGNodeLayoutGetTop(root_child0_child0_child1) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child1) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child1) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child1_child0) == 16
    assert YGNodeLayoutGetTop(root_child0_child0_child1_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child1_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child1_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0_child2) == 75
    assert YGNodeLayoutGetTop(root_child0_child0_child2) == 140
    assert YGNodeLayoutGetWidth(root_child0_child0_child2) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child2) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child2_child0) == 16
    assert YGNodeLayoutGetTop(root_child0_child0_child2_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child2_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child2_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 215
    assert YGNodeLayoutGetHeight(root) == 301

    assert YGNodeLayoutGetLeft(root_child0) == 4
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 202
    assert YGNodeLayoutGetHeight(root_child0) == 295

    assert YGNodeLayoutGetLeft(root_child0_child0) == 15
    assert YGNodeLayoutGetTop(root_child0_child0) == 21
    assert YGNodeLayoutGetWidth(root_child0_child0) == 166
    assert YGNodeLayoutGetHeight(root_child0_child0) == 244

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 65
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 39
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child0_child0) == -77
    assert YGNodeLayoutGetTop(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0_child1) == 75
    assert YGNodeLayoutGetTop(root_child0_child0_child1) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child1) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child1) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child1_child0) == -97
    assert YGNodeLayoutGetTop(root_child0_child0_child1_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child1_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child1_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0_child2) == 75
    assert YGNodeLayoutGetTop(root_child0_child0_child2) == 140
    assert YGNodeLayoutGetWidth(root_child0_child0_child2) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child2) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child2_child0) == -97
    assert YGNodeLayoutGetTop(root_child0_child0_child2_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child2_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child2_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_align_flex_end_amalgamation():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeTop, 5)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeLeft, 4)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeRight, 7)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeBottom, 8)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeTop, 9)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeRight, 11)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeBottom, 13)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeTop, 6)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeRight, 3)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetMargin(root_child0_child0, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeRight, 2)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeLeft, 8)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeTop, 7)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeRight, 9)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeBottom, 4)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeLeft, 1)
    YGNodeStyleSetAlignItems(root_child0_child0, YGAlign.YGAlignFlexEnd)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidthPercent(root_child0_child0_child0, 21)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)

    root_child0_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0_child0_child0, 100)
    YGNodeStyleSetHeight(root_child0_child0_child0_child0, 50)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child0_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0_child0, root_child0_child0_child0_child0, 0)

    root_child0_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child0_child1, 10)
    YGNodeStyleSetMargin(root_child0_child0_child1, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child1, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child1, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child1, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child1, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child1, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child1, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child1, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child1, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child1, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child1, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child1, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child1, 1)

    root_child0_child0_child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0_child1_child0, 100)
    YGNodeStyleSetHeight(root_child0_child0_child1_child0, 50)
    YGNodeStyleSetMargin(root_child0_child0_child1_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child1_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child1_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child1_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child1_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child1_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child1_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child1_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child1_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child1_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child1_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child1_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0_child1, root_child0_child0_child1_child0, 0)

    root_child0_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child0_child2, 10)
    YGNodeStyleSetMargin(root_child0_child0_child2, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child2, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child2, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child2, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child2, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child2, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child2, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child2, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child2, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child2, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child2, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child2, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child2, 2)

    root_child0_child0_child2_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0_child2_child0, 100)
    YGNodeStyleSetHeight(root_child0_child0_child2_child0, 50)
    YGNodeStyleSetMargin(root_child0_child0_child2_child0, YGEdge.YGEdgeTop, 12)
    YGNodeStyleSetMargin(root_child0_child0_child2_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0_child0_child2_child0, YGEdge.YGEdgeBottom, 7)
    YGNodeStyleSetMargin(root_child0_child0_child2_child0, YGEdge.YGEdgeLeft, 9)
    YGNodeStyleSetBorder(root_child0_child0_child2_child0, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetBorder(root_child0_child0_child2_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetBorder(root_child0_child0_child2_child0, YGEdge.YGEdgeBottom, 9)
    YGNodeStyleSetBorder(root_child0_child0_child2_child0, YGEdge.YGEdgeLeft, 2)
    YGNodeStyleSetPadding(root_child0_child0_child2_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetPadding(root_child0_child0_child2_child0, YGEdge.YGEdgeRight, 8)
    YGNodeStyleSetPadding(root_child0_child0_child2_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetPadding(root_child0_child0_child2_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root_child0_child0_child2, root_child0_child0_child2_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 215
    assert YGNodeLayoutGetHeight(root) == 301

    assert YGNodeLayoutGetLeft(root_child0) == 4
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 202
    assert YGNodeLayoutGetHeight(root_child0) == 295

    assert YGNodeLayoutGetLeft(root_child0_child0) == 15
    assert YGNodeLayoutGetTop(root_child0_child0) == 21
    assert YGNodeLayoutGetWidth(root_child0_child0) == 166
    assert YGNodeLayoutGetHeight(root_child0_child0) == 244

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 111
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetTop(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0_child1) == 131
    assert YGNodeLayoutGetTop(root_child0_child0_child1) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child1) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child1) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child1_child0) == 16
    assert YGNodeLayoutGetTop(root_child0_child0_child1_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child1_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child1_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0_child2) == 131
    assert YGNodeLayoutGetTop(root_child0_child0_child2) == 140
    assert YGNodeLayoutGetWidth(root_child0_child0_child2) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child2) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child2_child0) == 16
    assert YGNodeLayoutGetTop(root_child0_child0_child2_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child2_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child2_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 215
    assert YGNodeLayoutGetHeight(root) == 301

    assert YGNodeLayoutGetLeft(root_child0) == 4
    assert YGNodeLayoutGetTop(root_child0) == 5
    assert YGNodeLayoutGetWidth(root_child0) == 202
    assert YGNodeLayoutGetHeight(root_child0) == 295

    assert YGNodeLayoutGetLeft(root_child0_child0) == 15
    assert YGNodeLayoutGetTop(root_child0_child0) == 21
    assert YGNodeLayoutGetWidth(root_child0_child0) == 166
    assert YGNodeLayoutGetHeight(root_child0_child0) == 244

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 18
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child0_child0) == -77
    assert YGNodeLayoutGetTop(root_child0_child0_child0_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0_child1) == 18
    assert YGNodeLayoutGetTop(root_child0_child0_child1) == 29
    assert YGNodeLayoutGetWidth(root_child0_child0_child1) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child1) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child1_child0) == -97
    assert YGNodeLayoutGetTop(root_child0_child0_child1_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child1_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child1_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0_child2) == 18
    assert YGNodeLayoutGetTop(root_child0_child0_child2) == 140
    assert YGNodeLayoutGetWidth(root_child0_child0_child2) == 20
    assert YGNodeLayoutGetHeight(root_child0_child0_child2) == 92

    assert YGNodeLayoutGetLeft(root_child0_child0_child2_child0) == -97
    assert YGNodeLayoutGetTop(root_child0_child0_child2_child0) == 16
    assert YGNodeLayoutGetWidth(root_child0_child0_child2_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0_child2_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_static_root():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root, 200)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeStatic)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeTop, 1)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeRight, 11)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeBottom, 4)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeLeft, 6)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeightPercent(root_child0, 50)
    YGNodeStyleSetWidthPercent(root_child0, 50)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeTop, 3)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeRight, 2)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeLeft, 4)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeTop, 7)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeRight, 5)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeBottom, 4)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeLeft, 3)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeTop, 11)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeRight, 15)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeBottom, 1)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeLeft, 12)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 18
    assert YGNodeLayoutGetTop(root_child0) == 12
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 24
    assert YGNodeLayoutGetTop(root_child0) == 12
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_static_position_absolute_child_multiple():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 400)
    YGNodeStyleSetHeight(root_child0, 400)
    YGNodeStyleSetPadding(root_child0, YGEdge.YGEdgeAll, 100)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeStyleSetWidthPercent(root_child0_child0_child0, 10)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child1, 100)
    YGNodeStyleSetWidth(root_child0_child1, 100)
    YGNodeStyleSetPositionType(root_child0_child1, YGPositionType.YGPositionTypeStatic)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child1_child0, 50)
    YGNodeStyleSetWidthPercent(root_child0_child1_child0, 50)
    YGNodeStyleSetPositionType(root_child0_child1_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeInsertChild(root_child0_child1, root_child0_child1_child0, 0)

    root_child0_child1_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child1_child1, 50)
    YGNodeStyleSetWidthPercent(root_child0_child1_child1, 50)
    YGNodeStyleSetPositionType(root_child0_child1_child1, YGPositionType.YGPositionTypeAbsolute)
    YGNodeInsertChild(root_child0_child1, root_child0_child1_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child2, 50)
    YGNodeStyleSetWidth(root_child0_child2, 25)
    YGNodeStyleSetPositionType(root_child0_child2, YGPositionType.YGPositionTypeAbsolute)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 400
    assert YGNodeLayoutGetHeight(root) == 400

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 400

    assert YGNodeLayoutGetLeft(root_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 100
    assert YGNodeLayoutGetTop(root_child0_child1) == 200
    assert YGNodeLayoutGetWidth(root_child0_child1) == 100
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child1_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child1_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1_child1) == 200
    assert YGNodeLayoutGetHeight(root_child0_child1_child1) == 50

    assert YGNodeLayoutGetLeft(root_child0_child2) == 100
    assert YGNodeLayoutGetTop(root_child0_child2) == 100
    assert YGNodeLayoutGetWidth(root_child0_child2) == 25
    assert YGNodeLayoutGetHeight(root_child0_child2) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 400
    assert YGNodeLayoutGetHeight(root) == 400

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 400

    assert YGNodeLayoutGetLeft(root_child0_child0) == 200
    assert YGNodeLayoutGetTop(root_child0_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 60
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 40
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 200
    assert YGNodeLayoutGetTop(root_child0_child1) == 200
    assert YGNodeLayoutGetWidth(root_child0_child1) == 100
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child1_child0) == -100
    assert YGNodeLayoutGetTop(root_child0_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child1_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1_child1) == -100
    assert YGNodeLayoutGetTop(root_child0_child1_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1_child1) == 200
    assert YGNodeLayoutGetHeight(root_child0_child1_child1) == 50

    assert YGNodeLayoutGetLeft(root_child0_child2) == 275
    assert YGNodeLayoutGetTop(root_child0_child2) == 100
    assert YGNodeLayoutGetWidth(root_child0_child2) == 25
    assert YGNodeLayoutGetHeight(root_child0_child2) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)
