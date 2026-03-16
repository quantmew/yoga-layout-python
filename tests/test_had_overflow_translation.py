import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import (  # noqa: E402
    YGConfigFree,
    YGConfigNew,
    YGDirection,
    YGEdge,
    YGFlexDirection,
    YGNodeCalculateLayout,
    YGNodeFreeRecursive,
    YGNodeInsertChild,
    YGNodeLayoutGetHadOverflow,
    YGNodeNewWithConfig,
    YGNodeStyleSetFlexDirection,
    YGNodeStyleSetFlexShrink,
    YGNodeStyleSetFlexWrap,
    YGNodeStyleSetHeight,
    YGNodeStyleSetMargin,
    YGNodeStyleSetWidth,
    YGWrap,
)


def _make_root():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionColumn)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapNoWrap)
    return config, root


def test_children_overflow_no_wrap_and_no_flex_children():
    config, root = _make_root()
    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child0, 80)
    YGNodeStyleSetHeight(child0, 40)
    YGNodeStyleSetMargin(child0, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetMargin(child0, YGEdge.YGEdgeBottom, 15)
    YGNodeInsertChild(root, child0, 0)
    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child1, 80)
    YGNodeStyleSetHeight(child1, 40)
    YGNodeStyleSetMargin(child1, YGEdge.YGEdgeBottom, 5)
    YGNodeInsertChild(root, child1, 1)
    YGNodeCalculateLayout(root, 200, 100, YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetHadOverflow(root) is True
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_spacing_overflow_no_wrap_and_no_flex_children():
    config, root = _make_root()
    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child0, 80)
    YGNodeStyleSetHeight(child0, 40)
    YGNodeStyleSetMargin(child0, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetMargin(child0, YGEdge.YGEdgeBottom, 10)
    YGNodeInsertChild(root, child0, 0)
    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child1, 80)
    YGNodeStyleSetHeight(child1, 40)
    YGNodeStyleSetMargin(child1, YGEdge.YGEdgeBottom, 5)
    YGNodeInsertChild(root, child1, 1)
    YGNodeCalculateLayout(root, 200, 100, YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetHadOverflow(root) is True
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_no_overflow_no_wrap_and_flex_children():
    config, root = _make_root()
    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child0, 80)
    YGNodeStyleSetHeight(child0, 40)
    YGNodeStyleSetMargin(child0, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetMargin(child0, YGEdge.YGEdgeBottom, 10)
    YGNodeInsertChild(root, child0, 0)
    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child1, 80)
    YGNodeStyleSetHeight(child1, 40)
    YGNodeStyleSetMargin(child1, YGEdge.YGEdgeBottom, 5)
    YGNodeStyleSetFlexShrink(child1, 1)
    YGNodeInsertChild(root, child1, 1)
    YGNodeCalculateLayout(root, 200, 100, YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetHadOverflow(root) is False
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_hadOverflow_gets_reset_if_not_logger_valid():
    config, root = _make_root()
    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child0, 80)
    YGNodeStyleSetHeight(child0, 40)
    YGNodeStyleSetMargin(child0, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetMargin(child0, YGEdge.YGEdgeBottom, 10)
    YGNodeInsertChild(root, child0, 0)
    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child1, 80)
    YGNodeStyleSetHeight(child1, 40)
    YGNodeStyleSetMargin(child1, YGEdge.YGEdgeBottom, 5)
    YGNodeInsertChild(root, child1, 1)
    YGNodeCalculateLayout(root, 200, 100, YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetHadOverflow(root) is True
    YGNodeStyleSetFlexShrink(child1, 1)
    YGNodeCalculateLayout(root, 200, 100, YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetHadOverflow(root) is False
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_spacing_overflow_in_nested_nodes():
    config, root = _make_root()
    child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child0, 80)
    YGNodeStyleSetHeight(child0, 40)
    YGNodeStyleSetMargin(child0, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetMargin(child0, YGEdge.YGEdgeBottom, 10)
    YGNodeInsertChild(root, child0, 0)
    child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child1, 80)
    YGNodeStyleSetHeight(child1, 40)
    YGNodeInsertChild(root, child1, 1)
    child1_1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(child1_1, 80)
    YGNodeStyleSetHeight(child1_1, 40)
    YGNodeStyleSetMargin(child1_1, YGEdge.YGEdgeBottom, 5)
    YGNodeInsertChild(child1, child1_1, 0)
    YGNodeCalculateLayout(root, 200, 100, YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetHadOverflow(root) is True
    YGNodeFreeRecursive(root)
    YGConfigFree(config)
