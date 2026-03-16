import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import (  # noqa: E402
    YGDirection,
    YGNodeCalculateLayout,
    YGNodeFreeRecursive,
    YGNodeInsertChild,
    YGNodeNew,
    YGNodeSetContext,
    YGNodeSetDirtiedFunc,
    YGNodeStyleSetAlignItems,
    YGNodeStyleSetHeight,
    YGNodeStyleSetWidth,
)
from yoga.YGEnums import YGAlign  # noqa: E402


def _dirtied(node):
    dirtiedCount = node.getContext()
    dirtiedCount[0] += 1


def test_dirtied():
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    dirtiedCount = [0]
    YGNodeSetContext(root, dirtiedCount)
    YGNodeSetDirtiedFunc(root, _dirtied)

    assert dirtiedCount[0] == 0

    root.setDirty(True)
    assert dirtiedCount[0] == 1

    root.setDirty(True)
    assert dirtiedCount[0] == 1

    YGNodeFreeRecursive(root)


def test_dirtied_propagation():
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNew()
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 20)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNew()
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 20)
    YGNodeInsertChild(root, root_child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    dirtiedCount = [0]
    YGNodeSetContext(root, dirtiedCount)
    YGNodeSetDirtiedFunc(root, _dirtied)

    assert dirtiedCount[0] == 0

    root_child0.markDirtyAndPropagate()
    assert dirtiedCount[0] == 1

    root_child0.markDirtyAndPropagate()
    assert dirtiedCount[0] == 1

    YGNodeFreeRecursive(root)


def test_dirtied_hierarchy():
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNew()
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 20)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNew()
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 20)
    YGNodeInsertChild(root, root_child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    dirtiedCount = [0]
    YGNodeSetContext(root_child0, dirtiedCount)
    YGNodeSetDirtiedFunc(root_child0, _dirtied)

    assert dirtiedCount[0] == 0

    root.markDirtyAndPropagate()
    assert dirtiedCount[0] == 0

    root_child1.markDirtyAndPropagate()
    assert dirtiedCount[0] == 0

    root_child0.markDirtyAndPropagate()
    assert dirtiedCount[0] == 1

    YGNodeFreeRecursive(root)
