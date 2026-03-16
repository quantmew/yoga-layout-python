import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import (  # noqa: E402
    YGDirection,
    YGEdge,
    YGFlexDirection,
    YGNodeCalculateLayout,
    YGNodeFreeRecursive,
    YGNodeInsertChild,
    YGNodeLayoutGetBottom,
    YGNodeLayoutGetLeft,
    YGNodeLayoutGetRight,
    YGNodeLayoutGetTop,
    YGNodeNew,
    YGNodeStyleSetFlexDirection,
    YGNodeStyleSetFlexGrow,
    YGNodeStyleSetHeight,
    YGNodeStyleSetMargin,
    YGNodeStyleSetWidth,
)


def _make_root(direction):
    root = YGNodeNew()
    YGNodeStyleSetFlexDirection(root, direction)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    return root


def _make_flex_child():
    child = YGNodeNew()
    YGNodeStyleSetFlexGrow(child, 1)
    return child


def test_start_overrides():
    root = _make_root(YGFlexDirection.YGFlexDirectionRow)
    child = _make_flex_child()
    YGNodeStyleSetMargin(child, YGEdge.YGEdgeStart, 10)
    YGNodeStyleSetMargin(child, YGEdge.YGEdgeLeft, 20)
    YGNodeStyleSetMargin(child, YGEdge.YGEdgeRight, 20)
    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetLeft(child) == 10
    assert YGNodeLayoutGetRight(child) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetLeft(child) == 20
    assert YGNodeLayoutGetRight(child) == 10
    YGNodeFreeRecursive(root)


def test_end_overrides():
    root = _make_root(YGFlexDirection.YGFlexDirectionRow)
    child = _make_flex_child()
    YGNodeStyleSetMargin(child, YGEdge.YGEdgeEnd, 10)
    YGNodeStyleSetMargin(child, YGEdge.YGEdgeLeft, 20)
    YGNodeStyleSetMargin(child, YGEdge.YGEdgeRight, 20)
    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetLeft(child) == 20
    assert YGNodeLayoutGetRight(child) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetLeft(child) == 10
    assert YGNodeLayoutGetRight(child) == 20
    YGNodeFreeRecursive(root)


def test_horizontal_overridden():
    root = _make_root(YGFlexDirection.YGFlexDirectionRow)
    child = _make_flex_child()
    YGNodeStyleSetMargin(child, YGEdge.YGEdgeHorizontal, 10)
    YGNodeStyleSetMargin(child, YGEdge.YGEdgeLeft, 20)
    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetLeft(child) == 20
    assert YGNodeLayoutGetRight(child) == 10
    YGNodeFreeRecursive(root)


def test_vertical_overridden():
    root = _make_root(YGFlexDirection.YGFlexDirectionColumn)
    child = _make_flex_child()
    YGNodeStyleSetMargin(child, YGEdge.YGEdgeVertical, 10)
    YGNodeStyleSetMargin(child, YGEdge.YGEdgeTop, 20)
    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetTop(child) == 20
    assert YGNodeLayoutGetBottom(child) == 10
    YGNodeFreeRecursive(root)


def test_horizontal_overrides_all():
    root = _make_root(YGFlexDirection.YGFlexDirectionColumn)
    child = _make_flex_child()
    YGNodeStyleSetMargin(child, YGEdge.YGEdgeHorizontal, 10)
    YGNodeStyleSetMargin(child, YGEdge.YGEdgeAll, 20)
    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetLeft(child) == 10
    assert YGNodeLayoutGetTop(child) == 20
    assert YGNodeLayoutGetRight(child) == 10
    assert YGNodeLayoutGetBottom(child) == 20
    YGNodeFreeRecursive(root)


def test_vertical_overrides_all():
    root = _make_root(YGFlexDirection.YGFlexDirectionColumn)
    child = _make_flex_child()
    YGNodeStyleSetMargin(child, YGEdge.YGEdgeVertical, 10)
    YGNodeStyleSetMargin(child, YGEdge.YGEdgeAll, 20)
    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetLeft(child) == 20
    assert YGNodeLayoutGetTop(child) == 10
    assert YGNodeLayoutGetRight(child) == 20
    assert YGNodeLayoutGetBottom(child) == 10
    YGNodeFreeRecursive(root)


def test_all_overridden():
    root = _make_root(YGFlexDirection.YGFlexDirectionColumn)
    child = _make_flex_child()
    YGNodeStyleSetMargin(child, YGEdge.YGEdgeLeft, 10)
    YGNodeStyleSetMargin(child, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetMargin(child, YGEdge.YGEdgeRight, 10)
    YGNodeStyleSetMargin(child, YGEdge.YGEdgeBottom, 10)
    YGNodeStyleSetMargin(child, YGEdge.YGEdgeAll, 20)
    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetLeft(child) == 10
    assert YGNodeLayoutGetTop(child) == 10
    assert YGNodeLayoutGetRight(child) == 10
    assert YGNodeLayoutGetBottom(child) == 10
    YGNodeFreeRecursive(root)
