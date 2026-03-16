import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import (  # noqa: E402
    YGDirection,
    YGDisplay,
    YGEdge,
    YGFlexDirection,
    YGNodeCalculateLayout,
    YGNodeFreeRecursive,
    YGNodeInsertChild,
    YGNodeLayoutGetMargin,
    YGNodeLayoutGetPadding,
    YGNodeNew,
    YGNodeStyleSetDisplay,
    YGNodeStyleSetFlexDirection,
    YGNodeStyleSetHeight,
    YGNodeStyleSetMargin,
    YGNodeStyleSetPadding,
    YGNodeStyleSetWidth,
)


def test_zero_out_layout():
    root = YGNodeNew()
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 200)

    child = YGNodeNew()
    YGNodeInsertChild(root, child, 0)
    YGNodeStyleSetWidth(child, 100)
    YGNodeStyleSetHeight(child, 100)
    YGNodeStyleSetMargin(child, YGEdge.YGEdgeTop, 10)
    YGNodeStyleSetPadding(child, YGEdge.YGEdgeTop, 10)

    YGNodeCalculateLayout(root, 100, 100, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetMargin(child, YGEdge.YGEdgeTop) == 10
    assert YGNodeLayoutGetPadding(child, YGEdge.YGEdgeTop) == 10

    YGNodeStyleSetDisplay(child, YGDisplay.YGDisplayNone)
    YGNodeCalculateLayout(root, 100, 100, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetMargin(child, YGEdge.YGEdgeTop) == 0
    assert YGNodeLayoutGetPadding(child, YGEdge.YGEdgeTop) == 0

    YGNodeFreeRecursive(root)
