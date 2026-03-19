import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from yoga import *  # noqa: E402,F403


def _assert_layout(node, left, top, width, height):
    assert YGNodeLayoutGetLeft(node) == left
    assert YGNodeLayoutGetTop(node) == top
    assert YGNodeLayoutGetWidth(node) == width
    assert YGNodeLayoutGetHeight(node) == height

def test_align_content_flex_start_nowrap():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 140)
    YGNodeStyleSetHeight(root, 120)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_flex_start_wrap():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 140)
    YGNodeStyleSetHeight(root, 120)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 50)
    YGNodeStyleSetHeight(root_child2, 10)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 50)
    YGNodeStyleSetHeight(root_child3, 10)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 50)
    YGNodeStyleSetHeight(root_child4, 10)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 10
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 10

    assert YGNodeLayoutGetLeft(root_child3) == 50
    assert YGNodeLayoutGetTop(root_child3) == 10
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 10

    assert YGNodeLayoutGetLeft(root_child4) == 0
    assert YGNodeLayoutGetTop(root_child4) == 20
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 90
    assert YGNodeLayoutGetTop(root_child2) == 10
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 10

    assert YGNodeLayoutGetLeft(root_child3) == 40
    assert YGNodeLayoutGetTop(root_child3) == 10
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 10

    assert YGNodeLayoutGetLeft(root_child4) == 90
    assert YGNodeLayoutGetTop(root_child4) == 20
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_flex_start_wrap_singleline():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 140)
    YGNodeStyleSetHeight(root, 120)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_flex_start_wrapped_negative_space():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 320)
    YGNodeStyleSetHeight(root, 320)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 60)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeStyleSetJustifyContent(root_child0, YGJustify.YGJustifyCenter)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child0, 80)
    YGNodeStyleSetHeight(root_child0_child0, 20)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child1, 80)
    YGNodeStyleSetHeight(root_child0_child1, 20)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child2, 80)
    YGNodeStyleSetHeight(root_child0_child2, 20)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 320
    assert YGNodeLayoutGetHeight(root) == 320

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 60
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 20
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 160
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child1) == 20
    assert YGNodeLayoutGetTop(root_child0_child1) == 20
    assert YGNodeLayoutGetWidth(root_child0_child1) == 160
    assert YGNodeLayoutGetHeight(root_child0_child1) == 20

    assert YGNodeLayoutGetLeft(root_child0_child2) == 20
    assert YGNodeLayoutGetTop(root_child0_child2) == 40
    assert YGNodeLayoutGetWidth(root_child0_child2) == 160
    assert YGNodeLayoutGetHeight(root_child0_child2) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 320
    assert YGNodeLayoutGetHeight(root) == 320

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 60
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 20
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 160
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child1) == 20
    assert YGNodeLayoutGetTop(root_child0_child1) == 20
    assert YGNodeLayoutGetWidth(root_child0_child1) == 160
    assert YGNodeLayoutGetHeight(root_child0_child1) == 20

    assert YGNodeLayoutGetLeft(root_child0_child2) == 20
    assert YGNodeLayoutGetTop(root_child0_child2) == 40
    assert YGNodeLayoutGetWidth(root_child0_child2) == 160
    assert YGNodeLayoutGetHeight(root_child0_child2) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_flex_start_wrapped_negative_space_gap():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 320)
    YGNodeStyleSetHeight(root, 320)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 60)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeStyleSetJustifyContent(root_child0, YGJustify.YGJustifyCenter)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeStyleSetGap(root_child0, YGGutter.YGGutterAll, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child0, 80)
    YGNodeStyleSetHeight(root_child0_child0, 20)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child1, 80)
    YGNodeStyleSetHeight(root_child0_child1, 20)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child2, 80)
    YGNodeStyleSetHeight(root_child0_child2, 20)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 320
    assert YGNodeLayoutGetHeight(root) == 320

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 60
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 20
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 160
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child1) == 20
    assert YGNodeLayoutGetTop(root_child0_child1) == 30
    assert YGNodeLayoutGetWidth(root_child0_child1) == 160
    assert YGNodeLayoutGetHeight(root_child0_child1) == 20

    assert YGNodeLayoutGetLeft(root_child0_child2) == 20
    assert YGNodeLayoutGetTop(root_child0_child2) == 60
    assert YGNodeLayoutGetWidth(root_child0_child2) == 160
    assert YGNodeLayoutGetHeight(root_child0_child2) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 320
    assert YGNodeLayoutGetHeight(root) == 320

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 60
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 20
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 160
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child1) == 20
    assert YGNodeLayoutGetTop(root_child0_child1) == 30
    assert YGNodeLayoutGetWidth(root_child0_child1) == 160
    assert YGNodeLayoutGetHeight(root_child0_child1) == 20

    assert YGNodeLayoutGetLeft(root_child0_child2) == 20
    assert YGNodeLayoutGetTop(root_child0_child2) == 60
    assert YGNodeLayoutGetWidth(root_child0_child2) == 160
    assert YGNodeLayoutGetHeight(root_child0_child2) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_flex_start_without_height_on_children():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 50)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 50)
    YGNodeStyleSetHeight(root_child3, 10)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 50)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 10
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 0

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 10
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 10

    assert YGNodeLayoutGetLeft(root_child4) == 0
    assert YGNodeLayoutGetTop(root_child4) == 20
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 50
    assert YGNodeLayoutGetTop(root_child2) == 10
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 0

    assert YGNodeLayoutGetLeft(root_child3) == 50
    assert YGNodeLayoutGetTop(root_child3) == 10
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 10

    assert YGNodeLayoutGetLeft(root_child4) == 50
    assert YGNodeLayoutGetTop(root_child4) == 20
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 0

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_flex_start_with_flex():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 120)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeStyleSetFlexBasisPercent(root_child0, 0)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetFlexGrow(root_child1, 1)
    YGNodeStyleSetFlexBasisPercent(root_child1, 0)
    YGNodeStyleSetHeight(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 50)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 50)
    YGNodeStyleSetFlexGrow(root_child3, 1)
    YGNodeStyleSetFlexShrink(root_child3, 1)
    YGNodeStyleSetFlexBasisPercent(root_child3, 0)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 50)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 40

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 40

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 80
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 0

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 80
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 40

    assert YGNodeLayoutGetLeft(root_child4) == 0
    assert YGNodeLayoutGetTop(root_child4) == 120
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 40

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 40
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 40

    assert YGNodeLayoutGetLeft(root_child2) == 50
    assert YGNodeLayoutGetTop(root_child2) == 80
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 0

    assert YGNodeLayoutGetLeft(root_child3) == 50
    assert YGNodeLayoutGetTop(root_child3) == 80
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 40

    assert YGNodeLayoutGetLeft(root_child4) == 50
    assert YGNodeLayoutGetTop(root_child4) == 120
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 0

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_flex_end_nowrap():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 140)
    YGNodeStyleSetHeight(root, 120)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignFlexEnd)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_flex_end_wrap():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 140)
    YGNodeStyleSetHeight(root, 120)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignFlexEnd)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 50)
    YGNodeStyleSetHeight(root_child2, 10)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 50)
    YGNodeStyleSetHeight(root_child3, 10)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 50)
    YGNodeStyleSetHeight(root_child4, 10)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 90
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 90
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 100
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 10

    assert YGNodeLayoutGetLeft(root_child3) == 50
    assert YGNodeLayoutGetTop(root_child3) == 100
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 10

    assert YGNodeLayoutGetLeft(root_child4) == 0
    assert YGNodeLayoutGetTop(root_child4) == 110
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 90
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 90
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 90
    assert YGNodeLayoutGetTop(root_child2) == 100
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 10

    assert YGNodeLayoutGetLeft(root_child3) == 40
    assert YGNodeLayoutGetTop(root_child3) == 100
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 10

    assert YGNodeLayoutGetLeft(root_child4) == 90
    assert YGNodeLayoutGetTop(root_child4) == 110
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_flex_end_wrap_singleline():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 140)
    YGNodeStyleSetHeight(root, 120)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignFlexEnd)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 110
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 110
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 110
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 110
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_flex_end_wrapped_negative_space():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 320)
    YGNodeStyleSetHeight(root, 320)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 60)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root_child0, YGAlign.YGAlignFlexEnd)
    YGNodeStyleSetJustifyContent(root_child0, YGJustify.YGJustifyCenter)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child0, 80)
    YGNodeStyleSetHeight(root_child0_child0, 20)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child1, 80)
    YGNodeStyleSetHeight(root_child0_child1, 20)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child2, 80)
    YGNodeStyleSetHeight(root_child0_child2, 20)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 320
    assert YGNodeLayoutGetHeight(root) == 320

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 60
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 20
    assert YGNodeLayoutGetTop(root_child0_child0) == -50
    assert YGNodeLayoutGetWidth(root_child0_child0) == 160
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child1) == 20
    assert YGNodeLayoutGetTop(root_child0_child1) == -30
    assert YGNodeLayoutGetWidth(root_child0_child1) == 160
    assert YGNodeLayoutGetHeight(root_child0_child1) == 20

    assert YGNodeLayoutGetLeft(root_child0_child2) == 20
    assert YGNodeLayoutGetTop(root_child0_child2) == -10
    assert YGNodeLayoutGetWidth(root_child0_child2) == 160
    assert YGNodeLayoutGetHeight(root_child0_child2) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 320
    assert YGNodeLayoutGetHeight(root) == 320

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 60
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 20
    assert YGNodeLayoutGetTop(root_child0_child0) == -50
    assert YGNodeLayoutGetWidth(root_child0_child0) == 160
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child1) == 20
    assert YGNodeLayoutGetTop(root_child0_child1) == -30
    assert YGNodeLayoutGetWidth(root_child0_child1) == 160
    assert YGNodeLayoutGetHeight(root_child0_child1) == 20

    assert YGNodeLayoutGetLeft(root_child0_child2) == 20
    assert YGNodeLayoutGetTop(root_child0_child2) == -10
    assert YGNodeLayoutGetWidth(root_child0_child2) == 160
    assert YGNodeLayoutGetHeight(root_child0_child2) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_flex_end_wrapped_negative_space_gap():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 320)
    YGNodeStyleSetHeight(root, 320)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 60)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root_child0, YGAlign.YGAlignFlexEnd)
    YGNodeStyleSetJustifyContent(root_child0, YGJustify.YGJustifyCenter)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeStyleSetGap(root_child0, YGGutter.YGGutterAll, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child0, 80)
    YGNodeStyleSetHeight(root_child0_child0, 20)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child1, 80)
    YGNodeStyleSetHeight(root_child0_child1, 20)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child2, 80)
    YGNodeStyleSetHeight(root_child0_child2, 20)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 320
    assert YGNodeLayoutGetHeight(root) == 320

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 60
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 20
    assert YGNodeLayoutGetTop(root_child0_child0) == -70
    assert YGNodeLayoutGetWidth(root_child0_child0) == 160
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child1) == 20
    assert YGNodeLayoutGetTop(root_child0_child1) == -40
    assert YGNodeLayoutGetWidth(root_child0_child1) == 160
    assert YGNodeLayoutGetHeight(root_child0_child1) == 20

    assert YGNodeLayoutGetLeft(root_child0_child2) == 20
    assert YGNodeLayoutGetTop(root_child0_child2) == -10
    assert YGNodeLayoutGetWidth(root_child0_child2) == 160
    assert YGNodeLayoutGetHeight(root_child0_child2) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 320
    assert YGNodeLayoutGetHeight(root) == 320

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 60
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 20
    assert YGNodeLayoutGetTop(root_child0_child0) == -70
    assert YGNodeLayoutGetWidth(root_child0_child0) == 160
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child1) == 20
    assert YGNodeLayoutGetTop(root_child0_child1) == -40
    assert YGNodeLayoutGetWidth(root_child0_child1) == 160
    assert YGNodeLayoutGetHeight(root_child0_child1) == 20

    assert YGNodeLayoutGetLeft(root_child0_child2) == 20
    assert YGNodeLayoutGetTop(root_child0_child2) == -10
    assert YGNodeLayoutGetWidth(root_child0_child2) == 160
    assert YGNodeLayoutGetHeight(root_child0_child2) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_center_nowrap():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 140)
    YGNodeStyleSetHeight(root, 120)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignCenter)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_center_wrap():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 140)
    YGNodeStyleSetHeight(root, 120)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignCenter)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 50)
    YGNodeStyleSetHeight(root_child2, 10)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 50)
    YGNodeStyleSetHeight(root_child3, 10)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 50)
    YGNodeStyleSetHeight(root_child4, 10)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 45
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 45
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 55
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 10

    assert YGNodeLayoutGetLeft(root_child3) == 50
    assert YGNodeLayoutGetTop(root_child3) == 55
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 10

    assert YGNodeLayoutGetLeft(root_child4) == 0
    assert YGNodeLayoutGetTop(root_child4) == 65
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 45
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 45
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 90
    assert YGNodeLayoutGetTop(root_child2) == 55
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 10

    assert YGNodeLayoutGetLeft(root_child3) == 40
    assert YGNodeLayoutGetTop(root_child3) == 55
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 10

    assert YGNodeLayoutGetLeft(root_child4) == 90
    assert YGNodeLayoutGetTop(root_child4) == 65
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_center_wrap_singleline():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 140)
    YGNodeStyleSetHeight(root, 120)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignCenter)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 55
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 55
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 55
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 55
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_center_wrapped_negative_space():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 320)
    YGNodeStyleSetHeight(root, 320)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 60)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root_child0, YGAlign.YGAlignCenter)
    YGNodeStyleSetJustifyContent(root_child0, YGJustify.YGJustifyCenter)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child0, 80)
    YGNodeStyleSetHeight(root_child0_child0, 20)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child1, 80)
    YGNodeStyleSetHeight(root_child0_child1, 20)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child2, 80)
    YGNodeStyleSetHeight(root_child0_child2, 20)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 320
    assert YGNodeLayoutGetHeight(root) == 320

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 60
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 20
    assert YGNodeLayoutGetTop(root_child0_child0) == -25
    assert YGNodeLayoutGetWidth(root_child0_child0) == 160
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child1) == 20
    assert YGNodeLayoutGetTop(root_child0_child1) == -5
    assert YGNodeLayoutGetWidth(root_child0_child1) == 160
    assert YGNodeLayoutGetHeight(root_child0_child1) == 20

    assert YGNodeLayoutGetLeft(root_child0_child2) == 20
    assert YGNodeLayoutGetTop(root_child0_child2) == 15
    assert YGNodeLayoutGetWidth(root_child0_child2) == 160
    assert YGNodeLayoutGetHeight(root_child0_child2) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 320
    assert YGNodeLayoutGetHeight(root) == 320

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 60
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 20
    assert YGNodeLayoutGetTop(root_child0_child0) == -25
    assert YGNodeLayoutGetWidth(root_child0_child0) == 160
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child1) == 20
    assert YGNodeLayoutGetTop(root_child0_child1) == -5
    assert YGNodeLayoutGetWidth(root_child0_child1) == 160
    assert YGNodeLayoutGetHeight(root_child0_child1) == 20

    assert YGNodeLayoutGetLeft(root_child0_child2) == 20
    assert YGNodeLayoutGetTop(root_child0_child2) == 15
    assert YGNodeLayoutGetWidth(root_child0_child2) == 160
    assert YGNodeLayoutGetHeight(root_child0_child2) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_center_wrapped_negative_space_gap():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 320)
    YGNodeStyleSetHeight(root, 320)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 60)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root_child0, YGAlign.YGAlignCenter)
    YGNodeStyleSetJustifyContent(root_child0, YGJustify.YGJustifyCenter)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeStyleSetGap(root_child0, YGGutter.YGGutterAll, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child0, 80)
    YGNodeStyleSetHeight(root_child0_child0, 20)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child1, 80)
    YGNodeStyleSetHeight(root_child0_child1, 20)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child2, 80)
    YGNodeStyleSetHeight(root_child0_child2, 20)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 320
    assert YGNodeLayoutGetHeight(root) == 320

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 60
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 20
    assert YGNodeLayoutGetTop(root_child0_child0) == -35
    assert YGNodeLayoutGetWidth(root_child0_child0) == 160
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child1) == 20
    assert YGNodeLayoutGetTop(root_child0_child1) == -5
    assert YGNodeLayoutGetWidth(root_child0_child1) == 160
    assert YGNodeLayoutGetHeight(root_child0_child1) == 20

    assert YGNodeLayoutGetLeft(root_child0_child2) == 20
    assert YGNodeLayoutGetTop(root_child0_child2) == 25
    assert YGNodeLayoutGetWidth(root_child0_child2) == 160
    assert YGNodeLayoutGetHeight(root_child0_child2) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 320
    assert YGNodeLayoutGetHeight(root) == 320

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 60
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 20
    assert YGNodeLayoutGetTop(root_child0_child0) == -35
    assert YGNodeLayoutGetWidth(root_child0_child0) == 160
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child1) == 20
    assert YGNodeLayoutGetTop(root_child0_child1) == -5
    assert YGNodeLayoutGetWidth(root_child0_child1) == 160
    assert YGNodeLayoutGetHeight(root_child0_child1) == 20

    assert YGNodeLayoutGetLeft(root_child0_child2) == 20
    assert YGNodeLayoutGetTop(root_child0_child2) == 25
    assert YGNodeLayoutGetWidth(root_child0_child2) == 160
    assert YGNodeLayoutGetHeight(root_child0_child2) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_space_between_nowrap():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 140)
    YGNodeStyleSetHeight(root, 120)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignSpaceBetween)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_space_between_wrap():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 140)
    YGNodeStyleSetHeight(root, 120)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignSpaceBetween)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 50)
    YGNodeStyleSetHeight(root_child2, 10)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 50)
    YGNodeStyleSetHeight(root_child3, 10)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 50)
    YGNodeStyleSetHeight(root_child4, 10)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 55
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 10

    assert YGNodeLayoutGetLeft(root_child3) == 50
    assert YGNodeLayoutGetTop(root_child3) == 55
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 10

    assert YGNodeLayoutGetLeft(root_child4) == 0
    assert YGNodeLayoutGetTop(root_child4) == 110
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 90
    assert YGNodeLayoutGetTop(root_child2) == 55
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 10

    assert YGNodeLayoutGetLeft(root_child3) == 40
    assert YGNodeLayoutGetTop(root_child3) == 55
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 10

    assert YGNodeLayoutGetLeft(root_child4) == 90
    assert YGNodeLayoutGetTop(root_child4) == 110
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_space_between_wrap_singleline():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 140)
    YGNodeStyleSetHeight(root, 120)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignSpaceBetween)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_space_between_wrapped_negative_space():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 320)
    YGNodeStyleSetHeight(root, 320)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 60)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root_child0, YGAlign.YGAlignSpaceBetween)
    YGNodeStyleSetJustifyContent(root_child0, YGJustify.YGJustifyCenter)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child0, 80)
    YGNodeStyleSetHeight(root_child0_child0, 20)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child1, 80)
    YGNodeStyleSetHeight(root_child0_child1, 20)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child2, 80)
    YGNodeStyleSetHeight(root_child0_child2, 20)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 320
    assert YGNodeLayoutGetHeight(root) == 320

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 60
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 20
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 160
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child1) == 20
    assert YGNodeLayoutGetTop(root_child0_child1) == 20
    assert YGNodeLayoutGetWidth(root_child0_child1) == 160
    assert YGNodeLayoutGetHeight(root_child0_child1) == 20

    assert YGNodeLayoutGetLeft(root_child0_child2) == 20
    assert YGNodeLayoutGetTop(root_child0_child2) == 40
    assert YGNodeLayoutGetWidth(root_child0_child2) == 160
    assert YGNodeLayoutGetHeight(root_child0_child2) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 320
    assert YGNodeLayoutGetHeight(root) == 320

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 60
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 20
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 160
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child1) == 20
    assert YGNodeLayoutGetTop(root_child0_child1) == 20
    assert YGNodeLayoutGetWidth(root_child0_child1) == 160
    assert YGNodeLayoutGetHeight(root_child0_child1) == 20

    assert YGNodeLayoutGetLeft(root_child0_child2) == 20
    assert YGNodeLayoutGetTop(root_child0_child2) == 40
    assert YGNodeLayoutGetWidth(root_child0_child2) == 160
    assert YGNodeLayoutGetHeight(root_child0_child2) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_space_between_wrapped_negative_space_row_reverse():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 320)
    YGNodeStyleSetHeight(root, 320)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 60)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root_child0, YGAlign.YGAlignSpaceBetween)
    YGNodeStyleSetJustifyContent(root_child0, YGJustify.YGJustifyCenter)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child0, 80)
    YGNodeStyleSetHeight(root_child0_child0, 20)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child1, 80)
    YGNodeStyleSetHeight(root_child0_child1, 20)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child2, 80)
    YGNodeStyleSetHeight(root_child0_child2, 20)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 320
    assert YGNodeLayoutGetHeight(root) == 320

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 60
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 20
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 160
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child1) == 20
    assert YGNodeLayoutGetTop(root_child0_child1) == 20
    assert YGNodeLayoutGetWidth(root_child0_child1) == 160
    assert YGNodeLayoutGetHeight(root_child0_child1) == 20

    assert YGNodeLayoutGetLeft(root_child0_child2) == 20
    assert YGNodeLayoutGetTop(root_child0_child2) == 40
    assert YGNodeLayoutGetWidth(root_child0_child2) == 160
    assert YGNodeLayoutGetHeight(root_child0_child2) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 320
    assert YGNodeLayoutGetHeight(root) == 320

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 60
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 20
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 160
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child1) == 20
    assert YGNodeLayoutGetTop(root_child0_child1) == 20
    assert YGNodeLayoutGetWidth(root_child0_child1) == 160
    assert YGNodeLayoutGetHeight(root_child0_child1) == 20

    assert YGNodeLayoutGetLeft(root_child0_child2) == 20
    assert YGNodeLayoutGetTop(root_child0_child2) == 40
    assert YGNodeLayoutGetWidth(root_child0_child2) == 160
    assert YGNodeLayoutGetHeight(root_child0_child2) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_space_between_wrapped_negative_space_gap():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 320)
    YGNodeStyleSetHeight(root, 320)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 60)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root_child0, YGAlign.YGAlignSpaceBetween)
    YGNodeStyleSetJustifyContent(root_child0, YGJustify.YGJustifyCenter)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeStyleSetGap(root_child0, YGGutter.YGGutterAll, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child0, 80)
    YGNodeStyleSetHeight(root_child0_child0, 20)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child1, 80)
    YGNodeStyleSetHeight(root_child0_child1, 20)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child2, 80)
    YGNodeStyleSetHeight(root_child0_child2, 20)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 320
    assert YGNodeLayoutGetHeight(root) == 320

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 60
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 20
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 160
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child1) == 20
    assert YGNodeLayoutGetTop(root_child0_child1) == 30
    assert YGNodeLayoutGetWidth(root_child0_child1) == 160
    assert YGNodeLayoutGetHeight(root_child0_child1) == 20

    assert YGNodeLayoutGetLeft(root_child0_child2) == 20
    assert YGNodeLayoutGetTop(root_child0_child2) == 60
    assert YGNodeLayoutGetWidth(root_child0_child2) == 160
    assert YGNodeLayoutGetHeight(root_child0_child2) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 320
    assert YGNodeLayoutGetHeight(root) == 320

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 60
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 20
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 160
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child1) == 20
    assert YGNodeLayoutGetTop(root_child0_child1) == 30
    assert YGNodeLayoutGetWidth(root_child0_child1) == 160
    assert YGNodeLayoutGetHeight(root_child0_child1) == 20

    assert YGNodeLayoutGetLeft(root_child0_child2) == 20
    assert YGNodeLayoutGetTop(root_child0_child2) == 60
    assert YGNodeLayoutGetWidth(root_child0_child2) == 160
    assert YGNodeLayoutGetHeight(root_child0_child2) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_space_around_nowrap():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 140)
    YGNodeStyleSetHeight(root, 120)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignSpaceAround)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_space_around_wrap():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 140)
    YGNodeStyleSetHeight(root, 120)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignSpaceAround)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 50)
    YGNodeStyleSetHeight(root_child2, 10)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 50)
    YGNodeStyleSetHeight(root_child3, 10)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 50)
    YGNodeStyleSetHeight(root_child4, 10)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 15
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 15
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 55
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 10

    assert YGNodeLayoutGetLeft(root_child3) == 50
    assert YGNodeLayoutGetTop(root_child3) == 55
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 10

    assert YGNodeLayoutGetLeft(root_child4) == 0
    assert YGNodeLayoutGetTop(root_child4) == 95
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 15
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 15
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 90
    assert YGNodeLayoutGetTop(root_child2) == 55
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 10

    assert YGNodeLayoutGetLeft(root_child3) == 40
    assert YGNodeLayoutGetTop(root_child3) == 55
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 10

    assert YGNodeLayoutGetLeft(root_child4) == 90
    assert YGNodeLayoutGetTop(root_child4) == 95
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_space_around_wrap_singleline():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 140)
    YGNodeStyleSetHeight(root, 120)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignSpaceAround)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 55
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 55
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 55
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 55
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_space_around_wrapped_negative_space():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 320)
    YGNodeStyleSetHeight(root, 320)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 60)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root_child0, YGAlign.YGAlignSpaceAround)
    YGNodeStyleSetJustifyContent(root_child0, YGJustify.YGJustifyCenter)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child0, 80)
    YGNodeStyleSetHeight(root_child0_child0, 20)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child1, 80)
    YGNodeStyleSetHeight(root_child0_child1, 20)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child2, 80)
    YGNodeStyleSetHeight(root_child0_child2, 20)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 320
    assert YGNodeLayoutGetHeight(root) == 320

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 60
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 20
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 160
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child1) == 20
    assert YGNodeLayoutGetTop(root_child0_child1) == 20
    assert YGNodeLayoutGetWidth(root_child0_child1) == 160
    assert YGNodeLayoutGetHeight(root_child0_child1) == 20

    assert YGNodeLayoutGetLeft(root_child0_child2) == 20
    assert YGNodeLayoutGetTop(root_child0_child2) == 40
    assert YGNodeLayoutGetWidth(root_child0_child2) == 160
    assert YGNodeLayoutGetHeight(root_child0_child2) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 320
    assert YGNodeLayoutGetHeight(root) == 320

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 60
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 20
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 160
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child1) == 20
    assert YGNodeLayoutGetTop(root_child0_child1) == 20
    assert YGNodeLayoutGetWidth(root_child0_child1) == 160
    assert YGNodeLayoutGetHeight(root_child0_child1) == 20

    assert YGNodeLayoutGetLeft(root_child0_child2) == 20
    assert YGNodeLayoutGetTop(root_child0_child2) == 40
    assert YGNodeLayoutGetWidth(root_child0_child2) == 160
    assert YGNodeLayoutGetHeight(root_child0_child2) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_space_around_wrapped_negative_space_row_reverse():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 320)
    YGNodeStyleSetHeight(root, 320)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 60)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRowReverse)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root_child0, YGAlign.YGAlignSpaceAround)
    YGNodeStyleSetJustifyContent(root_child0, YGJustify.YGJustifyCenter)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child0, 80)
    YGNodeStyleSetHeight(root_child0_child0, 20)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child1, 80)
    YGNodeStyleSetHeight(root_child0_child1, 20)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child2, 80)
    YGNodeStyleSetHeight(root_child0_child2, 20)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 320
    assert YGNodeLayoutGetHeight(root) == 320

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 60
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 20
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 160
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child1) == 20
    assert YGNodeLayoutGetTop(root_child0_child1) == 20
    assert YGNodeLayoutGetWidth(root_child0_child1) == 160
    assert YGNodeLayoutGetHeight(root_child0_child1) == 20

    assert YGNodeLayoutGetLeft(root_child0_child2) == 20
    assert YGNodeLayoutGetTop(root_child0_child2) == 40
    assert YGNodeLayoutGetWidth(root_child0_child2) == 160
    assert YGNodeLayoutGetHeight(root_child0_child2) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 320
    assert YGNodeLayoutGetHeight(root) == 320

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 60
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 20
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 160
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child1) == 20
    assert YGNodeLayoutGetTop(root_child0_child1) == 20
    assert YGNodeLayoutGetWidth(root_child0_child1) == 160
    assert YGNodeLayoutGetHeight(root_child0_child1) == 20

    assert YGNodeLayoutGetLeft(root_child0_child2) == 20
    assert YGNodeLayoutGetTop(root_child0_child2) == 40
    assert YGNodeLayoutGetWidth(root_child0_child2) == 160
    assert YGNodeLayoutGetHeight(root_child0_child2) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_space_around_wrapped_negative_space_gap():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 320)
    YGNodeStyleSetHeight(root, 320)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 60)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root_child0, YGAlign.YGAlignSpaceAround)
    YGNodeStyleSetJustifyContent(root_child0, YGJustify.YGJustifyCenter)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeStyleSetGap(root_child0, YGGutter.YGGutterAll, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child0, 80)
    YGNodeStyleSetHeight(root_child0_child0, 20)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child1, 80)
    YGNodeStyleSetHeight(root_child0_child1, 20)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child2, 80)
    YGNodeStyleSetHeight(root_child0_child2, 20)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 320
    assert YGNodeLayoutGetHeight(root) == 320

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 60
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 20
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 160
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child1) == 20
    assert YGNodeLayoutGetTop(root_child0_child1) == 30
    assert YGNodeLayoutGetWidth(root_child0_child1) == 160
    assert YGNodeLayoutGetHeight(root_child0_child1) == 20

    assert YGNodeLayoutGetLeft(root_child0_child2) == 20
    assert YGNodeLayoutGetTop(root_child0_child2) == 60
    assert YGNodeLayoutGetWidth(root_child0_child2) == 160
    assert YGNodeLayoutGetHeight(root_child0_child2) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 320
    assert YGNodeLayoutGetHeight(root) == 320

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 60
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 20
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 160
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child1) == 20
    assert YGNodeLayoutGetTop(root_child0_child1) == 30
    assert YGNodeLayoutGetWidth(root_child0_child1) == 160
    assert YGNodeLayoutGetHeight(root_child0_child1) == 20

    assert YGNodeLayoutGetLeft(root_child0_child2) == 20
    assert YGNodeLayoutGetTop(root_child0_child2) == 60
    assert YGNodeLayoutGetWidth(root_child0_child2) == 160
    assert YGNodeLayoutGetHeight(root_child0_child2) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_space_evenly_nowrap():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 140)
    YGNodeStyleSetHeight(root, 120)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignSpaceEvenly)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_space_evenly_wrap():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 140)
    YGNodeStyleSetHeight(root, 120)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignSpaceEvenly)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 50)
    YGNodeStyleSetHeight(root_child2, 10)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 50)
    YGNodeStyleSetHeight(root_child3, 10)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 50)
    YGNodeStyleSetHeight(root_child4, 10)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 23
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 23
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 55
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 10

    assert YGNodeLayoutGetLeft(root_child3) == 50
    assert YGNodeLayoutGetTop(root_child3) == 55
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 10

    assert YGNodeLayoutGetLeft(root_child4) == 0
    assert YGNodeLayoutGetTop(root_child4) == 88
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 23
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 23
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    assert YGNodeLayoutGetLeft(root_child2) == 90
    assert YGNodeLayoutGetTop(root_child2) == 55
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 10

    assert YGNodeLayoutGetLeft(root_child3) == 40
    assert YGNodeLayoutGetTop(root_child3) == 55
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 10

    assert YGNodeLayoutGetLeft(root_child4) == 90
    assert YGNodeLayoutGetTop(root_child4) == 88
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_space_evenly_wrap_singleline():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 140)
    YGNodeStyleSetHeight(root, 120)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignSpaceEvenly)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 10)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 55
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 55
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 140
    assert YGNodeLayoutGetHeight(root) == 120

    assert YGNodeLayoutGetLeft(root_child0) == 90
    assert YGNodeLayoutGetTop(root_child0) == 55
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 55
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_space_evenly_wrapped_negative_space():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 320)
    YGNodeStyleSetHeight(root, 320)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 60)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root_child0, YGAlign.YGAlignSpaceEvenly)
    YGNodeStyleSetJustifyContent(root_child0, YGJustify.YGJustifyCenter)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child0, 80)
    YGNodeStyleSetHeight(root_child0_child0, 20)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child1, 80)
    YGNodeStyleSetHeight(root_child0_child1, 20)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child2, 80)
    YGNodeStyleSetHeight(root_child0_child2, 20)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 320
    assert YGNodeLayoutGetHeight(root) == 320

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 60
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 20
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 160
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child1) == 20
    assert YGNodeLayoutGetTop(root_child0_child1) == 20
    assert YGNodeLayoutGetWidth(root_child0_child1) == 160
    assert YGNodeLayoutGetHeight(root_child0_child1) == 20

    assert YGNodeLayoutGetLeft(root_child0_child2) == 20
    assert YGNodeLayoutGetTop(root_child0_child2) == 40
    assert YGNodeLayoutGetWidth(root_child0_child2) == 160
    assert YGNodeLayoutGetHeight(root_child0_child2) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 320
    assert YGNodeLayoutGetHeight(root) == 320

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 60
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 20
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 160
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child1) == 20
    assert YGNodeLayoutGetTop(root_child0_child1) == 20
    assert YGNodeLayoutGetWidth(root_child0_child1) == 160
    assert YGNodeLayoutGetHeight(root_child0_child1) == 20

    assert YGNodeLayoutGetLeft(root_child0_child2) == 20
    assert YGNodeLayoutGetTop(root_child0_child2) == 40
    assert YGNodeLayoutGetWidth(root_child0_child2) == 160
    assert YGNodeLayoutGetHeight(root_child0_child2) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_space_evenly_wrapped_negative_space_gap():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 320)
    YGNodeStyleSetHeight(root, 320)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 60)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root_child0, YGAlign.YGAlignSpaceEvenly)
    YGNodeStyleSetJustifyContent(root_child0, YGJustify.YGJustifyCenter)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeStyleSetGap(root_child0, YGGutter.YGGutterAll, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child0, 80)
    YGNodeStyleSetHeight(root_child0_child0, 20)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child1, 80)
    YGNodeStyleSetHeight(root_child0_child1, 20)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthPercent(root_child0_child2, 80)
    YGNodeStyleSetHeight(root_child0_child2, 20)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 320
    assert YGNodeLayoutGetHeight(root) == 320

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 60
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 20
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 160
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child1) == 20
    assert YGNodeLayoutGetTop(root_child0_child1) == 30
    assert YGNodeLayoutGetWidth(root_child0_child1) == 160
    assert YGNodeLayoutGetHeight(root_child0_child1) == 20

    assert YGNodeLayoutGetLeft(root_child0_child2) == 20
    assert YGNodeLayoutGetTop(root_child0_child2) == 60
    assert YGNodeLayoutGetWidth(root_child0_child2) == 160
    assert YGNodeLayoutGetHeight(root_child0_child2) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 320
    assert YGNodeLayoutGetHeight(root) == 320

    assert YGNodeLayoutGetLeft(root_child0) == 60
    assert YGNodeLayoutGetTop(root_child0) == 60
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 20
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 160
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child1) == 20
    assert YGNodeLayoutGetTop(root_child0_child1) == 30
    assert YGNodeLayoutGetWidth(root_child0_child1) == 160
    assert YGNodeLayoutGetHeight(root_child0_child1) == 20

    assert YGNodeLayoutGetLeft(root_child0_child2) == 20
    assert YGNodeLayoutGetTop(root_child0_child2) == 60
    assert YGNodeLayoutGetWidth(root_child0_child2) == 160
    assert YGNodeLayoutGetHeight(root_child0_child2) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_stretch():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 150)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignStretch)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 50)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 50)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 50)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 150
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 0

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 0

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 0
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 0

    assert YGNodeLayoutGetLeft(root_child4) == 0
    assert YGNodeLayoutGetTop(root_child4) == 0
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 0

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 150
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 0

    assert YGNodeLayoutGetLeft(root_child1) == 100
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 0

    assert YGNodeLayoutGetLeft(root_child2) == 100
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 0

    assert YGNodeLayoutGetLeft(root_child3) == 100
    assert YGNodeLayoutGetTop(root_child3) == 0
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 0

    assert YGNodeLayoutGetLeft(root_child4) == 100
    assert YGNodeLayoutGetTop(root_child4) == 0
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 0

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_stretch_row():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 150)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignStretch)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 50)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 50)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 50)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 150
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 50

    assert YGNodeLayoutGetLeft(root_child2) == 100
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 50

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 50
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 50

    assert YGNodeLayoutGetLeft(root_child4) == 50
    assert YGNodeLayoutGetTop(root_child4) == 50
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 150
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 50

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 50

    assert YGNodeLayoutGetLeft(root_child3) == 100
    assert YGNodeLayoutGetTop(root_child3) == 50
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 50

    assert YGNodeLayoutGetLeft(root_child4) == 50
    assert YGNodeLayoutGetTop(root_child4) == 50
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_stretch_row_with_children():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 150)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignStretch)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0_child0, 1)
    YGNodeStyleSetFlexShrink(root_child0_child0, 1)
    YGNodeStyleSetFlexBasisPercent(root_child0_child0, 0)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 50)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 50)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 50)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 150
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 50

    assert YGNodeLayoutGetLeft(root_child2) == 100
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 50

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 50
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 50

    assert YGNodeLayoutGetLeft(root_child4) == 50
    assert YGNodeLayoutGetTop(root_child4) == 50
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 150
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 50

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 50

    assert YGNodeLayoutGetLeft(root_child3) == 100
    assert YGNodeLayoutGetTop(root_child3) == 50
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 50

    assert YGNodeLayoutGetLeft(root_child4) == 50
    assert YGNodeLayoutGetTop(root_child4) == 50
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_stretch_row_with_flex():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 150)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignStretch)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetFlexGrow(root_child1, 1)
    YGNodeStyleSetFlexShrink(root_child1, 1)
    YGNodeStyleSetFlexBasisPercent(root_child1, 0)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 50)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 50)
    YGNodeStyleSetFlexGrow(root_child3, 1)
    YGNodeStyleSetFlexShrink(root_child3, 1)
    YGNodeStyleSetFlexBasisPercent(root_child3, 0)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 50)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 150
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 0
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 50
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 100

    assert YGNodeLayoutGetLeft(root_child3) == 100
    assert YGNodeLayoutGetTop(root_child3) == 0
    assert YGNodeLayoutGetWidth(root_child3) == 0
    assert YGNodeLayoutGetHeight(root_child3) == 100

    assert YGNodeLayoutGetLeft(root_child4) == 100
    assert YGNodeLayoutGetTop(root_child4) == 0
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 150
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 100
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 0
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 50
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 100

    assert YGNodeLayoutGetLeft(root_child3) == 50
    assert YGNodeLayoutGetTop(root_child3) == 0
    assert YGNodeLayoutGetWidth(root_child3) == 0
    assert YGNodeLayoutGetHeight(root_child3) == 100

    assert YGNodeLayoutGetLeft(root_child4) == 0
    assert YGNodeLayoutGetTop(root_child4) == 0
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_stretch_row_with_flex_no_shrink():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 150)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignStretch)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetFlexGrow(root_child1, 1)
    YGNodeStyleSetFlexShrink(root_child1, 1)
    YGNodeStyleSetFlexBasisPercent(root_child1, 0)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 50)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 50)
    YGNodeStyleSetFlexGrow(root_child3, 1)
    YGNodeStyleSetFlexBasisPercent(root_child3, 0)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 50)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 150
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 0
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 50
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 100

    assert YGNodeLayoutGetLeft(root_child3) == 100
    assert YGNodeLayoutGetTop(root_child3) == 0
    assert YGNodeLayoutGetWidth(root_child3) == 0
    assert YGNodeLayoutGetHeight(root_child3) == 100

    assert YGNodeLayoutGetLeft(root_child4) == 100
    assert YGNodeLayoutGetTop(root_child4) == 0
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 150
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 100
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 0
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 50
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 100

    assert YGNodeLayoutGetLeft(root_child3) == 50
    assert YGNodeLayoutGetTop(root_child3) == 0
    assert YGNodeLayoutGetWidth(root_child3) == 0
    assert YGNodeLayoutGetHeight(root_child3) == 100

    assert YGNodeLayoutGetLeft(root_child4) == 0
    assert YGNodeLayoutGetTop(root_child4) == 0
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_stretch_row_with_margin():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 150)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignStretch)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetMargin(root_child1, YGEdge.YGEdgeAll, 10)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 50)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 50)
    YGNodeStyleSetMargin(root_child3, YGEdge.YGEdgeAll, 10)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 50)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 150
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 40

    assert YGNodeLayoutGetLeft(root_child1) == 60
    assert YGNodeLayoutGetTop(root_child1) == 10
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 40
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 40

    assert YGNodeLayoutGetLeft(root_child3) == 60
    assert YGNodeLayoutGetTop(root_child3) == 50
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 20

    assert YGNodeLayoutGetLeft(root_child4) == 0
    assert YGNodeLayoutGetTop(root_child4) == 80
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 150
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 40

    assert YGNodeLayoutGetLeft(root_child1) == 40
    assert YGNodeLayoutGetTop(root_child1) == 10
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 100
    assert YGNodeLayoutGetTop(root_child2) == 40
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 40

    assert YGNodeLayoutGetLeft(root_child3) == 40
    assert YGNodeLayoutGetTop(root_child3) == 50
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 20

    assert YGNodeLayoutGetLeft(root_child4) == 100
    assert YGNodeLayoutGetTop(root_child4) == 80
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_stretch_row_with_padding():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 150)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignStretch)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetPadding(root_child1, YGEdge.YGEdgeAll, 10)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 50)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 50)
    YGNodeStyleSetPadding(root_child3, YGEdge.YGEdgeAll, 10)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 50)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 150
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 50

    assert YGNodeLayoutGetLeft(root_child2) == 100
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 50

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 50
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 50

    assert YGNodeLayoutGetLeft(root_child4) == 50
    assert YGNodeLayoutGetTop(root_child4) == 50
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 150
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 50

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 50

    assert YGNodeLayoutGetLeft(root_child3) == 100
    assert YGNodeLayoutGetTop(root_child3) == 50
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 50

    assert YGNodeLayoutGetLeft(root_child4) == 50
    assert YGNodeLayoutGetTop(root_child4) == 50
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_stretch_row_with_single_row():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 150)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignStretch)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 150
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
    assert YGNodeLayoutGetWidth(root) == 150
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_stretch_row_with_fixed_height():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 150)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignStretch)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 60)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 50)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 50)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 50)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 150
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 80

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 60

    assert YGNodeLayoutGetLeft(root_child2) == 100
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 80

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 80
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 20

    assert YGNodeLayoutGetLeft(root_child4) == 50
    assert YGNodeLayoutGetTop(root_child4) == 80
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 150
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 80

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 60

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 80

    assert YGNodeLayoutGetLeft(root_child3) == 100
    assert YGNodeLayoutGetTop(root_child3) == 80
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 20

    assert YGNodeLayoutGetLeft(root_child4) == 50
    assert YGNodeLayoutGetTop(root_child4) == 80
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_stretch_row_with_max_height():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 150)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignStretch)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetMaxHeight(root_child1, 20)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 50)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 50)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 50)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 150
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 100
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 50

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 50
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 50

    assert YGNodeLayoutGetLeft(root_child4) == 50
    assert YGNodeLayoutGetTop(root_child4) == 50
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 150
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 20

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 50

    assert YGNodeLayoutGetLeft(root_child3) == 100
    assert YGNodeLayoutGetTop(root_child3) == 50
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 50

    assert YGNodeLayoutGetLeft(root_child4) == 50
    assert YGNodeLayoutGetTop(root_child4) == 50
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_stretch_row_with_min_height():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 150)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignStretch)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetMinHeight(root_child1, 80)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 50)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child3, 50)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child4, 50)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 150
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 90

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 90

    assert YGNodeLayoutGetLeft(root_child2) == 100
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 90

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 90
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 10

    assert YGNodeLayoutGetLeft(root_child4) == 50
    assert YGNodeLayoutGetTop(root_child4) == 90
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 150
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 90

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 90

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 90

    assert YGNodeLayoutGetLeft(root_child3) == 100
    assert YGNodeLayoutGetTop(root_child3) == 90
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 10

    assert YGNodeLayoutGetLeft(root_child4) == 50
    assert YGNodeLayoutGetTop(root_child4) == 90
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_stretch_column():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 150)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignStretch)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0_child0, 1)
    YGNodeStyleSetFlexShrink(root_child0_child0, 1)
    YGNodeStyleSetFlexBasisPercent(root_child0_child0, 0)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1, 50)
    YGNodeStyleSetFlexGrow(root_child1, 1)
    YGNodeStyleSetFlexShrink(root_child1, 1)
    YGNodeStyleSetFlexBasisPercent(root_child1, 0)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child2, 50)
    YGNodeInsertChild(root, root_child2, 2)

    root_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child3, 50)
    YGNodeInsertChild(root, root_child3, 3)

    root_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child4, 50)
    YGNodeInsertChild(root, root_child4, 4)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 150

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 50
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 0

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 50
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 50

    assert YGNodeLayoutGetLeft(root_child3) == 0
    assert YGNodeLayoutGetTop(root_child3) == 100
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 50

    assert YGNodeLayoutGetLeft(root_child4) == 50
    assert YGNodeLayoutGetTop(root_child4) == 0
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 150

    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 50
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 0

    assert YGNodeLayoutGetLeft(root_child2) == 50
    assert YGNodeLayoutGetTop(root_child2) == 50
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 50

    assert YGNodeLayoutGetLeft(root_child3) == 50
    assert YGNodeLayoutGetTop(root_child3) == 100
    assert YGNodeLayoutGetWidth(root_child3) == 50
    assert YGNodeLayoutGetHeight(root_child3) == 50

    assert YGNodeLayoutGetLeft(root_child4) == 0
    assert YGNodeLayoutGetTop(root_child4) == 0
    assert YGNodeLayoutGetWidth(root_child4) == 50
    assert YGNodeLayoutGetHeight(root_child4) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_stretch_is_not_overriding_align_items():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignStretch)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetAlignItems(root_child0, YGAlign.YGAlignCenter)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetAlignContent(root_child0, YGAlign.YGAlignStretch)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0_child0, 10)
    YGNodeStyleSetWidth(root_child0_child0, 10)
    YGNodeStyleSetAlignContent(root_child0_child0, YGAlign.YGAlignStretch)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 45
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 90
    assert YGNodeLayoutGetTop(root_child0_child0) == 45
    assert YGNodeLayoutGetWidth(root_child0_child0) == 10
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_stretch_with_min_cross_axis():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 500)
    YGNodeStyleSetMinHeight(root, 500)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignStretch)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 400)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 400)
    YGNodeStyleSetHeight(root_child1, 200)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 500

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 250
    assert YGNodeLayoutGetWidth(root_child1) == 400
    assert YGNodeLayoutGetHeight(root_child1) == 200

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 500

    assert YGNodeLayoutGetLeft(root_child0) == 100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child1) == 100
    assert YGNodeLayoutGetTop(root_child1) == 250
    assert YGNodeLayoutGetWidth(root_child1) == 400
    assert YGNodeLayoutGetHeight(root_child1) == 200

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_stretch_with_max_cross_axis():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 500)
    YGNodeStyleSetMaxHeight(root, 500)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignStretch)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 400)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 400)
    YGNodeStyleSetHeight(root_child1, 200)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 400

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 200
    assert YGNodeLayoutGetWidth(root_child1) == 400
    assert YGNodeLayoutGetHeight(root_child1) == 200

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 400

    assert YGNodeLayoutGetLeft(root_child0) == 100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child1) == 100
    assert YGNodeLayoutGetTop(root_child1) == 200
    assert YGNodeLayoutGetWidth(root_child1) == 400
    assert YGNodeLayoutGetHeight(root_child1) == 200

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_stretch_with_max_cross_axis_and_border_padding():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 500)
    YGNodeStyleSetMaxHeight(root, 500)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignStretch)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 5)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeAll, 2)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 400)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 400)
    YGNodeStyleSetHeight(root_child1, 200)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 414

    assert YGNodeLayoutGetLeft(root_child0) == 7
    assert YGNodeLayoutGetTop(root_child0) == 7
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child1) == 7
    assert YGNodeLayoutGetTop(root_child1) == 207
    assert YGNodeLayoutGetWidth(root_child1) == 400
    assert YGNodeLayoutGetHeight(root_child1) == 200

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 414

    assert YGNodeLayoutGetLeft(root_child0) == 93
    assert YGNodeLayoutGetTop(root_child0) == 7
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child1) == 93
    assert YGNodeLayoutGetTop(root_child1) == 207
    assert YGNodeLayoutGetWidth(root_child1) == 400
    assert YGNodeLayoutGetHeight(root_child1) == 200

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_space_evenly_with_min_cross_axis():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 500)
    YGNodeStyleSetMinHeight(root, 500)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignSpaceEvenly)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 400)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 400)
    YGNodeStyleSetHeight(root_child1, 200)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 500

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 33
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 267
    assert YGNodeLayoutGetWidth(root_child1) == 400
    assert YGNodeLayoutGetHeight(root_child1) == 200

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 500

    assert YGNodeLayoutGetLeft(root_child0) == 100
    assert YGNodeLayoutGetTop(root_child0) == 33
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child1) == 100
    assert YGNodeLayoutGetTop(root_child1) == 267
    assert YGNodeLayoutGetWidth(root_child1) == 400
    assert YGNodeLayoutGetHeight(root_child1) == 200

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_space_evenly_with_max_cross_axis():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 500)
    YGNodeStyleSetMaxHeight(root, 500)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignSpaceEvenly)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 400)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 400)
    YGNodeStyleSetHeight(root_child1, 200)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 400

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 200
    assert YGNodeLayoutGetWidth(root_child1) == 400
    assert YGNodeLayoutGetHeight(root_child1) == 200

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 400

    assert YGNodeLayoutGetLeft(root_child0) == 100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child1) == 100
    assert YGNodeLayoutGetTop(root_child1) == 200
    assert YGNodeLayoutGetWidth(root_child1) == 400
    assert YGNodeLayoutGetHeight(root_child1) == 200

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_space_evenly_with_max_cross_axis_violated():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 500)
    YGNodeStyleSetMaxHeight(root, 300)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignSpaceEvenly)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 400)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 400)
    YGNodeStyleSetHeight(root_child1, 200)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 200
    assert YGNodeLayoutGetWidth(root_child1) == 400
    assert YGNodeLayoutGetHeight(root_child1) == 200

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 100
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child1) == 100
    assert YGNodeLayoutGetTop(root_child1) == 200
    assert YGNodeLayoutGetWidth(root_child1) == 400
    assert YGNodeLayoutGetHeight(root_child1) == 200

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_space_evenly_with_max_cross_axis_violated_padding_and_border():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 500)
    YGNodeStyleSetMaxHeight(root, 300)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignSpaceEvenly)
    YGNodeStyleSetBorder(root, YGEdge.YGEdgeAll, 5)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeAll, 2)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 400)
    YGNodeStyleSetHeight(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 400)
    YGNodeStyleSetHeight(root_child1, 200)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 7
    assert YGNodeLayoutGetTop(root_child0) == 7
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child1) == 7
    assert YGNodeLayoutGetTop(root_child1) == 207
    assert YGNodeLayoutGetWidth(root_child1) == 400
    assert YGNodeLayoutGetHeight(root_child1) == 200

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 93
    assert YGNodeLayoutGetTop(root_child0) == 7
    assert YGNodeLayoutGetWidth(root_child0) == 400
    assert YGNodeLayoutGetHeight(root_child0) == 200

    assert YGNodeLayoutGetLeft(root_child1) == 93
    assert YGNodeLayoutGetTop(root_child1) == 207
    assert YGNodeLayoutGetWidth(root_child1) == 400
    assert YGNodeLayoutGetHeight(root_child1) == 200

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_space_around_and_align_items_flex_end_with_flex_wrap():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 300)
    YGNodeStyleSetHeight(root, 300)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignSpaceAround)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexEnd)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeStyleSetWidth(root_child0, 150)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1, 100)
    YGNodeStyleSetWidth(root_child1, 120)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child2, 50)
    YGNodeStyleSetWidth(root_child2, 120)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 88
    assert YGNodeLayoutGetWidth(root_child0) == 150
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 150
    assert YGNodeLayoutGetTop(root_child1) == 38
    assert YGNodeLayoutGetWidth(root_child1) == 120
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 213
    assert YGNodeLayoutGetWidth(root_child2) == 120
    assert YGNodeLayoutGetHeight(root_child2) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 150
    assert YGNodeLayoutGetTop(root_child0) == 88
    assert YGNodeLayoutGetWidth(root_child0) == 150
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 30
    assert YGNodeLayoutGetTop(root_child1) == 38
    assert YGNodeLayoutGetWidth(root_child1) == 120
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 180
    assert YGNodeLayoutGetTop(root_child2) == 213
    assert YGNodeLayoutGetWidth(root_child2) == 120
    assert YGNodeLayoutGetHeight(root_child2) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_space_around_and_align_items_center_with_flex_wrap():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 300)
    YGNodeStyleSetHeight(root, 300)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignSpaceAround)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeStyleSetWidth(root_child0, 150)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1, 100)
    YGNodeStyleSetWidth(root_child1, 120)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child2, 50)
    YGNodeStyleSetWidth(root_child2, 120)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 63
    assert YGNodeLayoutGetWidth(root_child0) == 150
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 150
    assert YGNodeLayoutGetTop(root_child1) == 38
    assert YGNodeLayoutGetWidth(root_child1) == 120
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 213
    assert YGNodeLayoutGetWidth(root_child2) == 120
    assert YGNodeLayoutGetHeight(root_child2) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 150
    assert YGNodeLayoutGetTop(root_child0) == 63
    assert YGNodeLayoutGetWidth(root_child0) == 150
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 30
    assert YGNodeLayoutGetTop(root_child1) == 38
    assert YGNodeLayoutGetWidth(root_child1) == 120
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 180
    assert YGNodeLayoutGetTop(root_child2) == 213
    assert YGNodeLayoutGetWidth(root_child2) == 120
    assert YGNodeLayoutGetHeight(root_child2) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_space_around_and_align_items_flex_start_with_flex_wrap():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 300)
    YGNodeStyleSetHeight(root, 300)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignSpaceAround)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeStyleSetWidth(root_child0, 150)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1, 100)
    YGNodeStyleSetWidth(root_child1, 120)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child2, 50)
    YGNodeStyleSetWidth(root_child2, 120)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 38
    assert YGNodeLayoutGetWidth(root_child0) == 150
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 150
    assert YGNodeLayoutGetTop(root_child1) == 38
    assert YGNodeLayoutGetWidth(root_child1) == 120
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 213
    assert YGNodeLayoutGetWidth(root_child2) == 120
    assert YGNodeLayoutGetHeight(root_child2) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 150
    assert YGNodeLayoutGetTop(root_child0) == 38
    assert YGNodeLayoutGetWidth(root_child0) == 150
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 30
    assert YGNodeLayoutGetTop(root_child1) == 38
    assert YGNodeLayoutGetWidth(root_child1) == 120
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 180
    assert YGNodeLayoutGetTop(root_child2) == 213
    assert YGNodeLayoutGetWidth(root_child2) == 120
    assert YGNodeLayoutGetHeight(root_child2) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_flex_start_stretch_doesnt_influence_line_box_dim():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 400)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeTop, 20)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeBottom, 20)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeLeft, 20)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeRight, 20)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeRight, 20)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child1, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root_child1, YGWrap.YGWrapWrap)
    YGNodeStyleSetFlexShrink(root_child1, 1)
    YGNodeStyleSetFlexGrow(root_child1, 1)
    YGNodeInsertChild(root, root_child1, 1)

    root_child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1_child0, 30)
    YGNodeStyleSetWidth(root_child1_child0, 30)
    YGNodeStyleSetMargin(root_child1_child0, YGEdge.YGEdgeRight, 20)
    YGNodeInsertChild(root_child1, root_child1_child0, 0)

    root_child1_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1_child1, 30)
    YGNodeStyleSetWidth(root_child1_child1, 30)
    YGNodeStyleSetMargin(root_child1_child1, YGEdge.YGEdgeRight, 20)
    YGNodeInsertChild(root_child1, root_child1_child1, 1)

    root_child1_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1_child2, 30)
    YGNodeStyleSetWidth(root_child1_child2, 30)
    YGNodeStyleSetMargin(root_child1_child2, YGEdge.YGEdgeRight, 20)
    YGNodeInsertChild(root_child1, root_child1_child2, 2)

    root_child1_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1_child3, 30)
    YGNodeStyleSetWidth(root_child1_child3, 30)
    YGNodeStyleSetMargin(root_child1_child3, YGEdge.YGEdgeRight, 20)
    YGNodeInsertChild(root_child1, root_child1_child3, 3)

    root_child1_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1_child4, 30)
    YGNodeStyleSetWidth(root_child1_child4, 30)
    YGNodeStyleSetMargin(root_child1_child4, YGEdge.YGEdgeRight, 20)
    YGNodeInsertChild(root_child1, root_child1_child4, 4)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child2, 50)
    YGNodeStyleSetWidth(root_child2, 50)
    YGNodeStyleSetMargin(root_child2, YGEdge.YGEdgeLeft, 20)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 400
    assert YGNodeLayoutGetHeight(root) == 140

    assert YGNodeLayoutGetLeft(root_child0) == 20
    assert YGNodeLayoutGetTop(root_child0) == 20
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 140
    assert YGNodeLayoutGetTop(root_child1) == 20
    assert YGNodeLayoutGetWidth(root_child1) == 170
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child1_child0) == 0
    assert YGNodeLayoutGetTop(root_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child1_child0) == 30
    assert YGNodeLayoutGetHeight(root_child1_child0) == 30

    assert YGNodeLayoutGetLeft(root_child1_child1) == 50
    assert YGNodeLayoutGetTop(root_child1_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1_child1) == 30
    assert YGNodeLayoutGetHeight(root_child1_child1) == 30

    assert YGNodeLayoutGetLeft(root_child1_child2) == 100
    assert YGNodeLayoutGetTop(root_child1_child2) == 0
    assert YGNodeLayoutGetWidth(root_child1_child2) == 30
    assert YGNodeLayoutGetHeight(root_child1_child2) == 30

    assert YGNodeLayoutGetLeft(root_child1_child3) == 0
    assert YGNodeLayoutGetTop(root_child1_child3) == 30
    assert YGNodeLayoutGetWidth(root_child1_child3) == 30
    assert YGNodeLayoutGetHeight(root_child1_child3) == 30

    assert YGNodeLayoutGetLeft(root_child1_child4) == 50
    assert YGNodeLayoutGetTop(root_child1_child4) == 30
    assert YGNodeLayoutGetWidth(root_child1_child4) == 30
    assert YGNodeLayoutGetHeight(root_child1_child4) == 30

    assert YGNodeLayoutGetLeft(root_child2) == 330
    assert YGNodeLayoutGetTop(root_child2) == 20
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 400
    assert YGNodeLayoutGetHeight(root) == 140

    assert YGNodeLayoutGetLeft(root_child0) == 260
    assert YGNodeLayoutGetTop(root_child0) == 20
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 90
    assert YGNodeLayoutGetTop(root_child1) == 20
    assert YGNodeLayoutGetWidth(root_child1) == 170
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child1_child0) == 120
    assert YGNodeLayoutGetTop(root_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child1_child0) == 30
    assert YGNodeLayoutGetHeight(root_child1_child0) == 30

    assert YGNodeLayoutGetLeft(root_child1_child1) == 70
    assert YGNodeLayoutGetTop(root_child1_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1_child1) == 30
    assert YGNodeLayoutGetHeight(root_child1_child1) == 30

    assert YGNodeLayoutGetLeft(root_child1_child2) == 20
    assert YGNodeLayoutGetTop(root_child1_child2) == 0
    assert YGNodeLayoutGetWidth(root_child1_child2) == 30
    assert YGNodeLayoutGetHeight(root_child1_child2) == 30

    assert YGNodeLayoutGetLeft(root_child1_child3) == 120
    assert YGNodeLayoutGetTop(root_child1_child3) == 30
    assert YGNodeLayoutGetWidth(root_child1_child3) == 30
    assert YGNodeLayoutGetHeight(root_child1_child3) == 30

    assert YGNodeLayoutGetLeft(root_child1_child4) == 70
    assert YGNodeLayoutGetTop(root_child1_child4) == 30
    assert YGNodeLayoutGetWidth(root_child1_child4) == 30
    assert YGNodeLayoutGetHeight(root_child1_child4) == 30

    assert YGNodeLayoutGetLeft(root_child2) == 40
    assert YGNodeLayoutGetTop(root_child2) == 20
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_stretch_stretch_does_influence_line_box_dim():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 400)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeTop, 20)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeBottom, 20)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeLeft, 20)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeRight, 20)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeRight, 20)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child1, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root_child1, YGWrap.YGWrapWrap)
    YGNodeStyleSetFlexShrink(root_child1, 1)
    YGNodeStyleSetFlexGrow(root_child1, 1)
    YGNodeStyleSetAlignContent(root_child1, YGAlign.YGAlignStretch)
    YGNodeInsertChild(root, root_child1, 1)

    root_child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1_child0, 30)
    YGNodeStyleSetWidth(root_child1_child0, 30)
    YGNodeStyleSetMargin(root_child1_child0, YGEdge.YGEdgeRight, 20)
    YGNodeInsertChild(root_child1, root_child1_child0, 0)

    root_child1_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1_child1, 30)
    YGNodeStyleSetWidth(root_child1_child1, 30)
    YGNodeStyleSetMargin(root_child1_child1, YGEdge.YGEdgeRight, 20)
    YGNodeInsertChild(root_child1, root_child1_child1, 1)

    root_child1_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1_child2, 30)
    YGNodeStyleSetWidth(root_child1_child2, 30)
    YGNodeStyleSetMargin(root_child1_child2, YGEdge.YGEdgeRight, 20)
    YGNodeInsertChild(root_child1, root_child1_child2, 2)

    root_child1_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1_child3, 30)
    YGNodeStyleSetWidth(root_child1_child3, 30)
    YGNodeStyleSetMargin(root_child1_child3, YGEdge.YGEdgeRight, 20)
    YGNodeInsertChild(root_child1, root_child1_child3, 3)

    root_child1_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1_child4, 30)
    YGNodeStyleSetWidth(root_child1_child4, 30)
    YGNodeStyleSetMargin(root_child1_child4, YGEdge.YGEdgeRight, 20)
    YGNodeInsertChild(root_child1, root_child1_child4, 4)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child2, 50)
    YGNodeStyleSetWidth(root_child2, 50)
    YGNodeStyleSetMargin(root_child2, YGEdge.YGEdgeLeft, 20)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 400
    assert YGNodeLayoutGetHeight(root) == 140

    assert YGNodeLayoutGetLeft(root_child0) == 20
    assert YGNodeLayoutGetTop(root_child0) == 20
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 140
    assert YGNodeLayoutGetTop(root_child1) == 20
    assert YGNodeLayoutGetWidth(root_child1) == 170
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child1_child0) == 0
    assert YGNodeLayoutGetTop(root_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child1_child0) == 30
    assert YGNodeLayoutGetHeight(root_child1_child0) == 30

    assert YGNodeLayoutGetLeft(root_child1_child1) == 50
    assert YGNodeLayoutGetTop(root_child1_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1_child1) == 30
    assert YGNodeLayoutGetHeight(root_child1_child1) == 30

    assert YGNodeLayoutGetLeft(root_child1_child2) == 100
    assert YGNodeLayoutGetTop(root_child1_child2) == 0
    assert YGNodeLayoutGetWidth(root_child1_child2) == 30
    assert YGNodeLayoutGetHeight(root_child1_child2) == 30

    assert YGNodeLayoutGetLeft(root_child1_child3) == 0
    assert YGNodeLayoutGetTop(root_child1_child3) == 50
    assert YGNodeLayoutGetWidth(root_child1_child3) == 30
    assert YGNodeLayoutGetHeight(root_child1_child3) == 30

    assert YGNodeLayoutGetLeft(root_child1_child4) == 50
    assert YGNodeLayoutGetTop(root_child1_child4) == 50
    assert YGNodeLayoutGetWidth(root_child1_child4) == 30
    assert YGNodeLayoutGetHeight(root_child1_child4) == 30

    assert YGNodeLayoutGetLeft(root_child2) == 330
    assert YGNodeLayoutGetTop(root_child2) == 20
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 400
    assert YGNodeLayoutGetHeight(root) == 140

    assert YGNodeLayoutGetLeft(root_child0) == 260
    assert YGNodeLayoutGetTop(root_child0) == 20
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 90
    assert YGNodeLayoutGetTop(root_child1) == 20
    assert YGNodeLayoutGetWidth(root_child1) == 170
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child1_child0) == 120
    assert YGNodeLayoutGetTop(root_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child1_child0) == 30
    assert YGNodeLayoutGetHeight(root_child1_child0) == 30

    assert YGNodeLayoutGetLeft(root_child1_child1) == 70
    assert YGNodeLayoutGetTop(root_child1_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1_child1) == 30
    assert YGNodeLayoutGetHeight(root_child1_child1) == 30

    assert YGNodeLayoutGetLeft(root_child1_child2) == 20
    assert YGNodeLayoutGetTop(root_child1_child2) == 0
    assert YGNodeLayoutGetWidth(root_child1_child2) == 30
    assert YGNodeLayoutGetHeight(root_child1_child2) == 30

    assert YGNodeLayoutGetLeft(root_child1_child3) == 120
    assert YGNodeLayoutGetTop(root_child1_child3) == 50
    assert YGNodeLayoutGetWidth(root_child1_child3) == 30
    assert YGNodeLayoutGetHeight(root_child1_child3) == 30

    assert YGNodeLayoutGetLeft(root_child1_child4) == 70
    assert YGNodeLayoutGetTop(root_child1_child4) == 50
    assert YGNodeLayoutGetWidth(root_child1_child4) == 30
    assert YGNodeLayoutGetHeight(root_child1_child4) == 30

    assert YGNodeLayoutGetLeft(root_child2) == 40
    assert YGNodeLayoutGetTop(root_child2) == 20
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_space_evenly_stretch_does_influence_line_box_dim():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 400)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeTop, 20)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeBottom, 20)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeLeft, 20)
    YGNodeStyleSetPadding(root, YGEdge.YGEdgeRight, 20)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetMargin(root_child0, YGEdge.YGEdgeRight, 20)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child1, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root_child1, YGWrap.YGWrapWrap)
    YGNodeStyleSetFlexShrink(root_child1, 1)
    YGNodeStyleSetFlexGrow(root_child1, 1)
    YGNodeStyleSetAlignContent(root_child1, YGAlign.YGAlignStretch)
    YGNodeInsertChild(root, root_child1, 1)

    root_child1_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1_child0, 30)
    YGNodeStyleSetWidth(root_child1_child0, 30)
    YGNodeStyleSetMargin(root_child1_child0, YGEdge.YGEdgeRight, 20)
    YGNodeInsertChild(root_child1, root_child1_child0, 0)

    root_child1_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1_child1, 30)
    YGNodeStyleSetWidth(root_child1_child1, 30)
    YGNodeStyleSetMargin(root_child1_child1, YGEdge.YGEdgeRight, 20)
    YGNodeInsertChild(root_child1, root_child1_child1, 1)

    root_child1_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1_child2, 30)
    YGNodeStyleSetWidth(root_child1_child2, 30)
    YGNodeStyleSetMargin(root_child1_child2, YGEdge.YGEdgeRight, 20)
    YGNodeInsertChild(root_child1, root_child1_child2, 2)

    root_child1_child3 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1_child3, 30)
    YGNodeStyleSetWidth(root_child1_child3, 30)
    YGNodeStyleSetMargin(root_child1_child3, YGEdge.YGEdgeRight, 20)
    YGNodeInsertChild(root_child1, root_child1_child3, 3)

    root_child1_child4 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1_child4, 30)
    YGNodeStyleSetWidth(root_child1_child4, 30)
    YGNodeStyleSetMargin(root_child1_child4, YGEdge.YGEdgeRight, 20)
    YGNodeInsertChild(root_child1, root_child1_child4, 4)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child2, 50)
    YGNodeStyleSetWidth(root_child2, 50)
    YGNodeStyleSetMargin(root_child2, YGEdge.YGEdgeLeft, 20)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 400
    assert YGNodeLayoutGetHeight(root) == 140

    assert YGNodeLayoutGetLeft(root_child0) == 20
    assert YGNodeLayoutGetTop(root_child0) == 20
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 140
    assert YGNodeLayoutGetTop(root_child1) == 20
    assert YGNodeLayoutGetWidth(root_child1) == 170
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child1_child0) == 0
    assert YGNodeLayoutGetTop(root_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child1_child0) == 30
    assert YGNodeLayoutGetHeight(root_child1_child0) == 30

    assert YGNodeLayoutGetLeft(root_child1_child1) == 50
    assert YGNodeLayoutGetTop(root_child1_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1_child1) == 30
    assert YGNodeLayoutGetHeight(root_child1_child1) == 30

    assert YGNodeLayoutGetLeft(root_child1_child2) == 100
    assert YGNodeLayoutGetTop(root_child1_child2) == 0
    assert YGNodeLayoutGetWidth(root_child1_child2) == 30
    assert YGNodeLayoutGetHeight(root_child1_child2) == 30

    assert YGNodeLayoutGetLeft(root_child1_child3) == 0
    assert YGNodeLayoutGetTop(root_child1_child3) == 50
    assert YGNodeLayoutGetWidth(root_child1_child3) == 30
    assert YGNodeLayoutGetHeight(root_child1_child3) == 30

    assert YGNodeLayoutGetLeft(root_child1_child4) == 50
    assert YGNodeLayoutGetTop(root_child1_child4) == 50
    assert YGNodeLayoutGetWidth(root_child1_child4) == 30
    assert YGNodeLayoutGetHeight(root_child1_child4) == 30

    assert YGNodeLayoutGetLeft(root_child2) == 330
    assert YGNodeLayoutGetTop(root_child2) == 20
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 400
    assert YGNodeLayoutGetHeight(root) == 140

    assert YGNodeLayoutGetLeft(root_child0) == 260
    assert YGNodeLayoutGetTop(root_child0) == 20
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child1) == 90
    assert YGNodeLayoutGetTop(root_child1) == 20
    assert YGNodeLayoutGetWidth(root_child1) == 170
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child1_child0) == 120
    assert YGNodeLayoutGetTop(root_child1_child0) == 0
    assert YGNodeLayoutGetWidth(root_child1_child0) == 30
    assert YGNodeLayoutGetHeight(root_child1_child0) == 30

    assert YGNodeLayoutGetLeft(root_child1_child1) == 70
    assert YGNodeLayoutGetTop(root_child1_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1_child1) == 30
    assert YGNodeLayoutGetHeight(root_child1_child1) == 30

    assert YGNodeLayoutGetLeft(root_child1_child2) == 20
    assert YGNodeLayoutGetTop(root_child1_child2) == 0
    assert YGNodeLayoutGetWidth(root_child1_child2) == 30
    assert YGNodeLayoutGetHeight(root_child1_child2) == 30

    assert YGNodeLayoutGetLeft(root_child1_child3) == 120
    assert YGNodeLayoutGetTop(root_child1_child3) == 50
    assert YGNodeLayoutGetWidth(root_child1_child3) == 30
    assert YGNodeLayoutGetHeight(root_child1_child3) == 30

    assert YGNodeLayoutGetLeft(root_child1_child4) == 70
    assert YGNodeLayoutGetTop(root_child1_child4) == 50
    assert YGNodeLayoutGetWidth(root_child1_child4) == 30
    assert YGNodeLayoutGetHeight(root_child1_child4) == 30

    assert YGNodeLayoutGetLeft(root_child2) == 40
    assert YGNodeLayoutGetTop(root_child2) == 20
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_stretch_and_align_items_flex_end_with_flex_wrap():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 300)
    YGNodeStyleSetHeight(root, 300)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignStretch)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexEnd)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeStyleSetWidth(root_child0, 150)
    YGNodeStyleSetAlignSelf(root_child0, YGAlign.YGAlignFlexStart)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1, 100)
    YGNodeStyleSetWidth(root_child1, 120)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child2, 50)
    YGNodeStyleSetWidth(root_child2, 120)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 150
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 150
    assert YGNodeLayoutGetTop(root_child1) == 75
    assert YGNodeLayoutGetWidth(root_child1) == 120
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 250
    assert YGNodeLayoutGetWidth(root_child2) == 120
    assert YGNodeLayoutGetHeight(root_child2) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 150
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 150
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 30
    assert YGNodeLayoutGetTop(root_child1) == 75
    assert YGNodeLayoutGetWidth(root_child1) == 120
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 180
    assert YGNodeLayoutGetTop(root_child2) == 250
    assert YGNodeLayoutGetWidth(root_child2) == 120
    assert YGNodeLayoutGetHeight(root_child2) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_stretch_and_align_items_flex_start_with_flex_wrap():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 300)
    YGNodeStyleSetHeight(root, 300)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignStretch)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeStyleSetWidth(root_child0, 150)
    YGNodeStyleSetAlignSelf(root_child0, YGAlign.YGAlignFlexEnd)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1, 100)
    YGNodeStyleSetWidth(root_child1, 120)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child2, 50)
    YGNodeStyleSetWidth(root_child2, 120)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 125
    assert YGNodeLayoutGetWidth(root_child0) == 150
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 150
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 120
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 175
    assert YGNodeLayoutGetWidth(root_child2) == 120
    assert YGNodeLayoutGetHeight(root_child2) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 150
    assert YGNodeLayoutGetTop(root_child0) == 125
    assert YGNodeLayoutGetWidth(root_child0) == 150
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 30
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 120
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 180
    assert YGNodeLayoutGetTop(root_child2) == 175
    assert YGNodeLayoutGetWidth(root_child2) == 120
    assert YGNodeLayoutGetHeight(root_child2) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_stretch_and_align_items_center_with_flex_wrap():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 300)
    YGNodeStyleSetHeight(root, 300)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignStretch)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeStyleSetWidth(root_child0, 150)
    YGNodeStyleSetAlignSelf(root_child0, YGAlign.YGAlignFlexEnd)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1, 100)
    YGNodeStyleSetWidth(root_child1, 120)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child2, 50)
    YGNodeStyleSetWidth(root_child2, 120)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 125
    assert YGNodeLayoutGetWidth(root_child0) == 150
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 150
    assert YGNodeLayoutGetTop(root_child1) == 38
    assert YGNodeLayoutGetWidth(root_child1) == 120
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 213
    assert YGNodeLayoutGetWidth(root_child2) == 120
    assert YGNodeLayoutGetHeight(root_child2) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 150
    assert YGNodeLayoutGetTop(root_child0) == 125
    assert YGNodeLayoutGetWidth(root_child0) == 150
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 30
    assert YGNodeLayoutGetTop(root_child1) == 38
    assert YGNodeLayoutGetWidth(root_child1) == 120
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 180
    assert YGNodeLayoutGetTop(root_child2) == 213
    assert YGNodeLayoutGetWidth(root_child2) == 120
    assert YGNodeLayoutGetHeight(root_child2) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_align_content_stretch_and_align_items_stretch_with_flex_wrap():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 300)
    YGNodeStyleSetHeight(root, 300)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)
    YGNodeStyleSetAlignContent(root, YGAlign.YGAlignStretch)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeStyleSetWidth(root_child0, 150)
    YGNodeStyleSetAlignSelf(root_child0, YGAlign.YGAlignFlexEnd)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child1, 100)
    YGNodeStyleSetWidth(root_child1, 120)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeight(root_child2, 50)
    YGNodeStyleSetWidth(root_child2, 120)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 125
    assert YGNodeLayoutGetWidth(root_child0) == 150
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 150
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 120
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 175
    assert YGNodeLayoutGetWidth(root_child2) == 120
    assert YGNodeLayoutGetHeight(root_child2) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 300
    assert YGNodeLayoutGetHeight(root) == 300

    assert YGNodeLayoutGetLeft(root_child0) == 150
    assert YGNodeLayoutGetTop(root_child0) == 125
    assert YGNodeLayoutGetWidth(root_child0) == 150
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 30
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 120
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 180
    assert YGNodeLayoutGetTop(root_child2) == 175
    assert YGNodeLayoutGetWidth(root_child2) == 120
    assert YGNodeLayoutGetHeight(root_child2) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)
