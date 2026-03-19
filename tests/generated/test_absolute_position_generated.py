import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from yoga import *  # noqa: E402,F403


def test_absolute_layout_width_height_start_top():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 10)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeStart, 10)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeTop, 10)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 10
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 80
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_absolute_layout_width_height_left_auto_right():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 10)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPositionAuto(root_child0, YGEdge.YGEdgeLeft)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeRight, 10)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 80
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 80
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_absolute_layout_width_height_left_right_auto():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 10)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeLeft, 10)
    YGNodeStyleSetPositionAuto(root_child0, YGEdge.YGEdgeRight)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 10
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 10
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_absolute_layout_width_height_left_auto_right_auto():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 10)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPositionAuto(root_child0, YGEdge.YGEdgeLeft)
    YGNodeStyleSetPositionAuto(root_child0, YGEdge.YGEdgeRight)
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

def test_absolute_layout_width_height_end_bottom():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 10)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeEnd, 10)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 80
    assert YGNodeLayoutGetTop(root_child0) == 80
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 10
    assert YGNodeLayoutGetTop(root_child0) == 80
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_absolute_layout_start_top_end_bottom():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeStart, 10)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeEnd, 10)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 10
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 80
    assert YGNodeLayoutGetHeight(root_child0) == 80

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 10
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 80
    assert YGNodeLayoutGetHeight(root_child0) == 80

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_absolute_layout_width_height_start_top_end_bottom():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 10)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeStart, 10)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeEnd, 10)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 10
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 80
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_do_not_clamp_height_of_absolute_node_to_height_of_its_overflow_hidden_parent():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 50)
    YGNodeStyleSetWidth(root, 50)
    YGNodeStyleSetOverflow(root, YGOverflow.YGOverflowHidden)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeStart, 0)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeTop, 0)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 100)
    YGNodeStyleSetHeight(root_child0_child0, 100)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 50
    assert YGNodeLayoutGetHeight(root) == 50

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 50
    assert YGNodeLayoutGetHeight(root) == 50

    assert YGNodeLayoutGetLeft(root_child0) == -50
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0_child0) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_absolute_layout_within_border():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 10)
    YGNodeStyleSetMargin(root, YGEdge.YGEdgeAll, 10)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeAll, 10)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeLeft, 0)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeTop, 0)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child1, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 50)
    YGNodeStyleSetPosition(root_child1, YGEdge.YGEdgeRight, 0)
    YGNodeStyleSetPosition(root_child1, YGEdge.YGEdgeBottom, 0)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child2, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root_child2, 50)
    YGNodeStyleSetHeight(root_child2, 50)
    YGNodeStyleSetPosition(root_child2, YGEdge.YGEdgeLeft, 0)
    YGNodeStyleSetPosition(root_child2, YGEdge.YGEdgeTop, 0)
    YGNodeStyleSetMargin(root_child2, YGEdge.YGEdgeAll, 10)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child3, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root_child3, 50)
    YGNodeStyleSetHeight(root_child3, 50)
    YGNodeStyleSetPosition(root_child3, YGEdge.YGEdgeRight, 0)
    YGNodeStyleSetPosition(root_child3, YGEdge.YGEdgeBottom, 0)
    YGNodeStyleSetMargin(root_child3, YGEdge.YGEdgeAll, 10)
    YGNodeInsertChild(root, root_child3, 3)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 10
    assert YGNodeLayoutGetTop(root) == 10
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 10
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 50

    assert YGNodeLayoutGetLeft(root_child2) == 20
    assert YGNodeLayoutGetTop(root_child2) == 20
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 50

    assert YGNodeLayoutGetLeft(root_child3) == 30
    assert YGNodeLayoutGetTop(root_child3) == 30
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 10
    assert YGNodeLayoutGetTop(root) == 10
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 10
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 50

    assert YGNodeLayoutGetLeft(root_child2) == 20
    assert YGNodeLayoutGetTop(root_child2) == 20
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 50

    assert YGNodeLayoutGetLeft(root_child3) == 30
    assert YGNodeLayoutGetTop(root_child3) == 30
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_absolute_layout_align_items_and_justify_content_center():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 110)
    YGNodeStyleSetFlexGrow(root, 1)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyCenter)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root_child0, 60)
    YGNodeStyleSetHeight(root_child0, 40)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 110
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 25
    assert YGNodeLayoutGetTop(root_child0) == 30
    assert YGNodeLayoutGetWidth(root_child0) == 60
    assert YGNodeLayoutGetHeight(root_child0) == 40

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 110
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 25
    assert YGNodeLayoutGetTop(root_child0) == 30
    assert YGNodeLayoutGetWidth(root_child0) == 60
    assert YGNodeLayoutGetHeight(root_child0) == 40

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_absolute_layout_align_items_and_justify_content_flex_end():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 110)
    YGNodeStyleSetFlexGrow(root, 1)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexEnd)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyFlexEnd)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root_child0, 60)
    YGNodeStyleSetHeight(root_child0, 40)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 110
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 60
    assert YGNodeLayoutGetWidth(root_child0) == 60
    assert YGNodeLayoutGetHeight(root_child0) == 40

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 110
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 60
    assert YGNodeLayoutGetWidth(root_child0) == 60
    assert YGNodeLayoutGetHeight(root_child0) == 40

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_absolute_layout_justify_content_center():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 110)
    YGNodeStyleSetFlexGrow(root, 1)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyCenter)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root_child0, 60)
    YGNodeStyleSetHeight(root_child0, 40)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 110
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 30
    assert YGNodeLayoutGetWidth(root_child0) == 60
    assert YGNodeLayoutGetHeight(root_child0) == 40

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 110
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 30
    assert YGNodeLayoutGetWidth(root_child0) == 60
    assert YGNodeLayoutGetHeight(root_child0) == 40

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_absolute_layout_align_items_center():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 110)
    YGNodeStyleSetFlexGrow(root, 1)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root_child0, 60)
    YGNodeStyleSetHeight(root_child0, 40)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 110
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 25
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 60
    assert YGNodeLayoutGetHeight(root_child0) == 40

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 110
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 25
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 60
    assert YGNodeLayoutGetHeight(root_child0) == 40

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_absolute_layout_align_items_center_on_child_only():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 110)
    YGNodeStyleSetFlexGrow(root, 1)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root_child0, 60)
    YGNodeStyleSetHeight(root_child0, 40)
    YGNodeStyleSetAlignSelf(root_child0, YGAlign.YGAlignCenter)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 110
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 25
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 60
    assert YGNodeLayoutGetHeight(root_child0) == 40

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 110
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 25
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 60
    assert YGNodeLayoutGetHeight(root_child0) == 40

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_absolute_layout_align_items_and_justify_content_center_and_top_position():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 110)
    YGNodeStyleSetFlexGrow(root, 1)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyCenter)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root_child0, 60)
    YGNodeStyleSetHeight(root_child0, 40)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeTop, 10)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 110
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 25
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 60
    assert YGNodeLayoutGetHeight(root_child0) == 40

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 110
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 25
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 60
    assert YGNodeLayoutGetHeight(root_child0) == 40

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_absolute_layout_align_items_and_justify_content_center_and_bottom_position():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 110)
    YGNodeStyleSetFlexGrow(root, 1)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyCenter)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root_child0, 60)
    YGNodeStyleSetHeight(root_child0, 40)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeBottom, 10)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 110
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 25
    assert YGNodeLayoutGetTop(root_child0) == 50
    assert YGNodeLayoutGetWidth(root_child0) == 60
    assert YGNodeLayoutGetHeight(root_child0) == 40

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 110
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 25
    assert YGNodeLayoutGetTop(root_child0) == 50
    assert YGNodeLayoutGetWidth(root_child0) == 60
    assert YGNodeLayoutGetHeight(root_child0) == 40

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_absolute_layout_align_items_and_justify_content_center_and_left_position():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 110)
    YGNodeStyleSetFlexGrow(root, 1)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyCenter)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root_child0, 60)
    YGNodeStyleSetHeight(root_child0, 40)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 110
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 5
    assert YGNodeLayoutGetTop(root_child0) == 30
    assert YGNodeLayoutGetWidth(root_child0) == 60
    assert YGNodeLayoutGetHeight(root_child0) == 40

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 110
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 5
    assert YGNodeLayoutGetTop(root_child0) == 30
    assert YGNodeLayoutGetWidth(root_child0) == 60
    assert YGNodeLayoutGetHeight(root_child0) == 40

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_absolute_layout_align_items_and_justify_content_center_and_right_position():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetWidth(root, 110)
    YGNodeStyleSetFlexGrow(root, 1)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyCenter)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root_child0, 60)
    YGNodeStyleSetHeight(root_child0, 40)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeRight, 5)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 110
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 45
    assert YGNodeLayoutGetTop(root_child0) == 30
    assert YGNodeLayoutGetWidth(root_child0) == 60
    assert YGNodeLayoutGetHeight(root_child0) == 40

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 110
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 45
    assert YGNodeLayoutGetTop(root_child0) == 30
    assert YGNodeLayoutGetWidth(root_child0) == 60
    assert YGNodeLayoutGetHeight(root_child0) == 40

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_position_root_with_rtl_should_position_withoutdirection():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 52)
    YGNodeStyleSetWidth(root, 52)
    YGNodeStyleSetPosition(root, YGEdge.YGEdgeLeft, 72)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 72
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 52
    assert YGNodeLayoutGetHeight(root) == 52

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 72
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 52
    assert YGNodeLayoutGetHeight(root) == 52

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_absolute_layout_percentage_bottom_based_on_parent_height():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 200)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPositionPercent(root_child0, YGEdge.YGEdgeTop, 50)
    YGNodeStyleSetWidth(root_child0, 10)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child1, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPositionPercent(root_child1, YGEdge.YGEdgeBottom, 50)
    YGNodeStyleSetWidth(root_child1, 10)
    YGNodeStyleSetHeight(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child2, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetPositionPercent(root_child2, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetWidth(root_child2, 10)
    YGNodeStyleSetPositionPercent(root_child2, YGEdge.YGEdgeBottom, 10)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 90
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 20
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 160

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 90
    assert YGNodeLayoutGetTop(root_child1) == 90
    assert YGNodeLayoutGetWidth(root_child1) == 10
    assert YGNodeLayoutGetHeight(root_child1) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 90
    assert YGNodeLayoutGetTop(root_child2) == 20
    assert YGNodeLayoutGetWidth(root_child2) == 10
    assert YGNodeLayoutGetHeight(root_child2) == 160

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_absolute_layout_in_wrap_reverse_column_container():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrapReverse)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 20)
    YGNodeStyleSetHeight(root_child0, 20)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 80
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_absolute_layout_in_wrap_reverse_row_container():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrapReverse)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 20)
    YGNodeStyleSetHeight(root_child0, 20)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 80
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 80
    assert YGNodeLayoutGetTop(root_child0) == 80
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_absolute_layout_in_wrap_reverse_column_container_flex_end():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrapReverse)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 20)
    YGNodeStyleSetHeight(root_child0, 20)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetAlignSelf(root_child0, YGAlign.YGAlignFlexEnd)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 80
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_absolute_layout_in_wrap_reverse_row_container_flex_end():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrapReverse)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 20)
    YGNodeStyleSetHeight(root_child0, 20)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetAlignSelf(root_child0, YGAlign.YGAlignFlexEnd)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 80
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 20
    assert YGNodeLayoutGetHeight(root_child0) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_percent_absolute_position_infinite_height():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 300)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 300)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child1, 20)
    YGNodeStyleSetHeightPercent(root_child1, 20)
    YGNodeStyleSetPositionPercent(root_child1, YGEdge.YGEdgeLeft, 20)
    YGNodeStyleSetPositionPercent(root_child1, YGEdge.YGEdgeTop, 20)
    YGNodeStyleSetPositionType(root_child1, YGPositionType.YGPositionTypeAbsolute)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 0

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 300
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child1) == 60
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 60
    assert YGNodeLayoutGetHeight(root_child1) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 0

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 300
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child1) == 60
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 60
    assert YGNodeLayoutGetHeight(root_child1) == 0

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_absolute_layout_percentage_height_based_on_padded_parent():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeTop, 10)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetHeightPercent(root_child0, 50)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 20
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 45

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 20
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 45

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_absolute_layout_percentage_height_based_on_padded_parent_and_align_items_center():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyCenter)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeTop, 20)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeBottom, 20)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetHeightPercent(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 25
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 25
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_absolute_layout_padding_left():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 200)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeLeft, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 150
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_absolute_layout_padding_right():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 200)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeRight, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_absolute_layout_padding_top():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 200)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeTop, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 150
    assert YGNodeLayoutGetTop(root_child0) == 100
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_absolute_layout_padding_bottom():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 200)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeBottom, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 150
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_absolute_layout_padding():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeAll, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeStyleSetWidth(root_child0_child0, 200)
    YGNodeStyleSetHeight(root_child0_child0, 200)
    YGNodeStyleSetPadding(root_child0_child0, YGEdge.YGEdgeAll, 50)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 220
    assert YGNodeLayoutGetHeight(root) == 220

    assert YGNodeLayoutGetLeft(root_child0) == 10
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 220
    assert YGNodeLayoutGetHeight(root) == 220

    assert YGNodeLayoutGetLeft(root_child0) == 10
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 100
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_absolute_layout_border():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeAll, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeStyleSetWidth(root_child0_child0, 200)
    YGNodeStyleSetHeight(root_child0_child0, 200)
    YGNodeStyleSetBorder(root_child0_child0, YGEdge.YGEdgeAll, 10)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root_child0_child0_child0, 50)
    YGNodeStyleSetHeight(root_child0_child0_child0, 50)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 220
    assert YGNodeLayoutGetHeight(root) == 220

    assert YGNodeLayoutGetLeft(root_child0) == 10
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 10
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 220
    assert YGNodeLayoutGetHeight(root) == 220

    assert YGNodeLayoutGetLeft(root_child0) == 10
    assert YGNodeLayoutGetTop(root_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0) == 200

    assert YGNodeLayoutGetLeft(root_child0_child0_child0) == 140
    assert YGNodeLayoutGetTop(root_child0_child0_child0) == 10
    assert YGNodeLayoutGetWidth(root_child0_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_absolute_layout_column_reverse_margin_border():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 200)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionColumnReverse)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeLeft, 5)
    YGNodeStyleSetPosition(root_child0, YGEdge.YGEdgeRight, 3)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeRight, 4)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeLeft, 3)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeRight, 7)
    YGNodeStyleSetBorder(root_child0, YGEdge.YGEdgeLeft, 1)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 8
    assert YGNodeLayoutGetTop(root_child0) == 150
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 200

    assert YGNodeLayoutGetLeft(root_child0) == 143
    assert YGNodeLayoutGetTop(root_child0) == 150
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

