import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import (  # noqa: E402
    YGDirection,
    YGEdge,
    YGNodeCalculateLayout,
    YGNodeFreeRecursive,
    YGNodeLayoutGetMargin,
    YGNodeNew,
    YGNodeStyleSetHeight,
    YGNodeStyleSetMargin,
    YGNodeStyleSetMarginPercent,
    YGNodeStyleSetWidth,
)


def test_computed_layout_margin():
    root = YGNodeNew()
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetMarginPercent(root, YGEdge.YGEdgeStart, 10)

    YGNodeCalculateLayout(root, 100, 100, YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetMargin(root, YGEdge.YGEdgeLeft) == 10
    assert YGNodeLayoutGetMargin(root, YGEdge.YGEdgeRight) == 0

    YGNodeCalculateLayout(root, 100, 100, YGDirection.YGDirectionRTL)
    assert YGNodeLayoutGetMargin(root, YGEdge.YGEdgeLeft) == 0
    assert YGNodeLayoutGetMargin(root, YGEdge.YGEdgeRight) == 10

    YGNodeFreeRecursive(root)


def test_margin_side_overrides_horizontal_and_vertical():
    edges = (
        YGEdge.YGEdgeTop,
        YGEdge.YGEdgeBottom,
        YGEdge.YGEdgeStart,
        YGEdge.YGEdgeEnd,
        YGEdge.YGEdgeLeft,
        YGEdge.YGEdgeRight,
    )

    for edgeValue in (0.0, 1.0):
        for edge in edges:
            horizontalOrVertical = (
                YGEdge.YGEdgeVertical
                if edge in (YGEdge.YGEdgeTop, YGEdge.YGEdgeBottom)
                else YGEdge.YGEdgeHorizontal
            )
            root = YGNodeNew()
            YGNodeStyleSetWidth(root, 100)
            YGNodeStyleSetHeight(root, 100)
            YGNodeStyleSetMargin(root, horizontalOrVertical, 10)
            YGNodeStyleSetMargin(root, edge, edgeValue)

            YGNodeCalculateLayout(root, 100, 100, YGDirection.YGDirectionLTR)
            assert YGNodeLayoutGetMargin(root, edge) == edgeValue

            YGNodeFreeRecursive(root)


def test_margin_side_overrides_all():
    edges = (
        YGEdge.YGEdgeTop,
        YGEdge.YGEdgeBottom,
        YGEdge.YGEdgeStart,
        YGEdge.YGEdgeEnd,
        YGEdge.YGEdgeLeft,
        YGEdge.YGEdgeRight,
    )

    for edgeValue in (0.0, 1.0):
        for edge in edges:
            root = YGNodeNew()
            YGNodeStyleSetWidth(root, 100)
            YGNodeStyleSetHeight(root, 100)
            YGNodeStyleSetMargin(root, YGEdge.YGEdgeAll, 10)
            YGNodeStyleSetMargin(root, edge, edgeValue)

            YGNodeCalculateLayout(root, 100, 100, YGDirection.YGDirectionLTR)
            assert YGNodeLayoutGetMargin(root, edge) == edgeValue

            YGNodeFreeRecursive(root)


def test_margin_horizontal_and_vertical_overrides_all():
    directions = (YGEdge.YGEdgeHorizontal, YGEdge.YGEdgeVertical)

    for directionValue in (0.0, 1.0):
        for direction in directions:
            root = YGNodeNew()
            YGNodeStyleSetWidth(root, 100)
            YGNodeStyleSetHeight(root, 100)
            YGNodeStyleSetMargin(root, YGEdge.YGEdgeAll, 10)
            YGNodeStyleSetMargin(root, direction, directionValue)

            YGNodeCalculateLayout(root, 100, 100, YGDirection.YGDirectionLTR)

            if direction == YGEdge.YGEdgeVertical:
                assert YGNodeLayoutGetMargin(root, YGEdge.YGEdgeTop) == directionValue
                assert YGNodeLayoutGetMargin(root, YGEdge.YGEdgeBottom) == directionValue
            else:
                assert YGNodeLayoutGetMargin(root, YGEdge.YGEdgeStart) == directionValue
                assert YGNodeLayoutGetMargin(root, YGEdge.YGEdgeEnd) == directionValue
                assert YGNodeLayoutGetMargin(root, YGEdge.YGEdgeLeft) == directionValue
                assert YGNodeLayoutGetMargin(root, YGEdge.YGEdgeRight) == directionValue

            YGNodeFreeRecursive(root)
