import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import (  # noqa: E402
    YGDirection,
    YGFlexDirection,
    YGNodeCalculateLayout,
    YGNodeCopyStyle,
    YGNodeFree,
    YGNodeNew,
    YGNodeStyleGetFlexDirection,
    YGNodeStyleGetFlexGrow,
    YGNodeStyleGetFlexShrink,
    YGNodeStyleGetMaxHeight,
    YGNodeStyleSetFlexDirection,
    YGNodeStyleSetFlexGrow,
    YGNodeStyleSetFlexShrink,
    YGNodeStyleSetMaxHeight,
    YGUndefined,
)


def test_copy_style_same():
    node0 = YGNodeNew()
    node1 = YGNodeNew()
    YGNodeCopyStyle(node0, node1)
    YGNodeFree(node0)
    YGNodeFree(node1)


def test_copy_style_modified():
    node0 = YGNodeNew()
    assert YGNodeStyleGetFlexDirection(node0) == YGFlexDirection.YGFlexDirectionColumn
    assert not (YGNodeStyleGetMaxHeight(node0).unit != 0)

    node1 = YGNodeNew()
    YGNodeStyleSetFlexDirection(node1, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetMaxHeight(node1, 10)

    YGNodeCopyStyle(node0, node1)
    assert YGNodeStyleGetFlexDirection(node0) == YGFlexDirection.YGFlexDirectionRow
    assert YGNodeStyleGetMaxHeight(node0).value == 10

    YGNodeFree(node0)
    YGNodeFree(node1)


def test_copy_style_modified_same():
    node0 = YGNodeNew()
    YGNodeStyleSetFlexDirection(node0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetMaxHeight(node0, 10)
    YGNodeCalculateLayout(node0, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)

    node1 = YGNodeNew()
    YGNodeStyleSetFlexDirection(node1, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetMaxHeight(node1, 10)

    YGNodeCopyStyle(node0, node1)

    YGNodeFree(node0)
    YGNodeFree(node1)


def test_initialise_flex_shrink_flex_grow():
    node0 = YGNodeNew()
    YGNodeStyleSetFlexShrink(node0, 1)
    assert YGNodeStyleGetFlexShrink(node0) == 1

    YGNodeStyleSetFlexShrink(node0, YGUndefined)
    YGNodeStyleSetFlexGrow(node0, 3)
    assert YGNodeStyleGetFlexShrink(node0) == 0
    assert YGNodeStyleGetFlexGrow(node0) == 3

    YGNodeStyleSetFlexGrow(node0, YGUndefined)
    YGNodeStyleSetFlexShrink(node0, 3)
    assert YGNodeStyleGetFlexGrow(node0) == 0
    assert YGNodeStyleGetFlexShrink(node0) == 3
    YGNodeFree(node0)
