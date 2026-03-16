import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import (  # noqa: E402
    YGConfigFree,
    YGConfigNew,
    YGDirection,
    YGNodeCalculateLayout,
    YGNodeClone,
    YGNodeFree,
    YGNodeFreeRecursive,
    YGNodeGetChild,
    YGNodeGetChildCount,
    YGNodeGetOwner,
    YGNodeInsertChild,
    YGNodeLayoutGetHeight,
    YGNodeLayoutGetLeft,
    YGNodeLayoutGetTop,
    YGNodeLayoutGetWidth,
    YGNodeNew,
    YGNodeNewWithConfig,
    YGNodeRemoveAllChildren,
    YGNodeRemoveChild,
    YGNodeStyleSetFlexBasis,
    YGNodeStyleSetFlexGrow,
    YGNodeStyleSetHeight,
    YGNodeStyleSetWidth,
    YGUndefined,
)
from yoga.node.Node import Node  # noqa: E402


def test_cloning_shared_root():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeStyleSetFlexBasis(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child1, 1)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100
    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 75
    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 75
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 25

    root2 = YGNodeClone(root)
    YGNodeStyleSetWidth(root2, 100)

    assert YGNodeGetChildCount(root2) == 2
    assert YGNodeGetChild(root2, 0) is root_child0
    assert YGNodeGetChild(root2, 1) is root_child1

    YGNodeCalculateLayout(root2, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)

    assert YGNodeGetChildCount(root2) == 2
    assert YGNodeGetChild(root2, 0) is root_child0
    assert YGNodeGetChild(root2, 1) is root_child1

    YGNodeStyleSetWidth(root2, 150)
    YGNodeStyleSetHeight(root2, 200)
    YGNodeCalculateLayout(root2, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)

    assert YGNodeGetChildCount(root2) == 2
    root2_child0 = YGNodeGetChild(root2, 0)
    root2_child1 = YGNodeGetChild(root2, 1)
    assert root2_child0 is not root_child0
    assert root2_child1 is not root_child1

    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 75
    assert YGNodeLayoutGetHeight(root_child1) == 25

    assert YGNodeLayoutGetWidth(root2) == 150
    assert YGNodeLayoutGetHeight(root2) == 200
    assert YGNodeLayoutGetHeight(root2_child0) == 125
    assert YGNodeLayoutGetHeight(root2_child1) == 75

    YGNodeFreeRecursive(root2)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_mutating_children_of_a_clone_clones_only_after_layout():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    assert YGNodeGetChildCount(root) == 0

    root2 = YGNodeClone(root)
    assert YGNodeGetChildCount(root2) == 0

    root2_child0 = YGNodeNewWithConfig(config)
    YGNodeInsertChild(root2, root2_child0, 0)

    assert YGNodeGetChildCount(root) == 0
    assert YGNodeGetChildCount(root2) == 1

    root3 = YGNodeClone(root2)
    assert YGNodeGetChildCount(root2) == 1
    assert YGNodeGetChildCount(root3) == 1
    assert YGNodeGetChild(root2, 0) is YGNodeGetChild(root3, 0)

    root3_child1 = YGNodeNewWithConfig(config)
    YGNodeInsertChild(root3, root3_child1, 1)
    assert YGNodeGetChildCount(root2) == 1
    assert YGNodeGetChildCount(root3) == 2
    assert YGNodeGetChild(root3, 1) is root3_child1
    assert YGNodeGetChild(root2, 0) is YGNodeGetChild(root3, 0)

    root4 = YGNodeClone(root3)
    assert YGNodeGetChild(root4, 1) is root3_child1

    YGNodeRemoveChild(root4, root3_child1)
    assert YGNodeGetChildCount(root3) == 2
    assert YGNodeGetChildCount(root4) == 1
    assert YGNodeGetChild(root3, 0) is YGNodeGetChild(root4, 0)

    YGNodeCalculateLayout(root4, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)
    assert YGNodeGetChild(root3, 0) is not YGNodeGetChild(root4, 0)
    YGNodeCalculateLayout(root3, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)
    assert YGNodeGetChild(root2, 0) is not YGNodeGetChild(root3, 0)

    YGNodeFreeRecursive(root4)
    YGNodeFreeRecursive(root3)
    YGNodeFreeRecursive(root2)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_cloning_two_levels():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child0, 1)
    YGNodeStyleSetFlexBasis(root_child0, 15)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexGrow(root_child1, 1)
    YGNodeInsertChild(root, root_child1, 1)

    root_child1_0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexBasis(root_child1_0, 10)
    YGNodeStyleSetFlexGrow(root_child1_0, 1)
    YGNodeInsertChild(root_child1, root_child1_0, 0)

    root_child1_1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexBasis(root_child1_1, 25)
    YGNodeInsertChild(root_child1, root_child1_1, 1)

    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetHeight(root_child0) == 40
    assert YGNodeLayoutGetHeight(root_child1) == 60
    assert YGNodeLayoutGetHeight(root_child1_0) == 35
    assert YGNodeLayoutGetHeight(root_child1_1) == 25

    root2_child0 = YGNodeClone(root_child0)
    root2_child1 = YGNodeClone(root_child1)
    root2 = YGNodeClone(root)

    YGNodeStyleSetFlexGrow(root2_child0, 0)
    YGNodeStyleSetFlexBasis(root2_child0, 40)

    YGNodeRemoveAllChildren(root2)
    YGNodeInsertChild(root2, root2_child0, 0)
    YGNodeInsertChild(root2, root2_child1, 1)
    assert YGNodeGetChildCount(root2) == 2

    YGNodeCalculateLayout(root2, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetHeight(root_child0) == 40
    assert YGNodeLayoutGetHeight(root_child1) == 60
    assert YGNodeLayoutGetHeight(root_child1_0) == 35
    assert YGNodeLayoutGetHeight(root_child1_1) == 25

    assert YGNodeLayoutGetHeight(root2_child0) == 40
    assert YGNodeLayoutGetHeight(root2_child1) == 60

    assert YGNodeGetChild(root2_child1, 0) is root_child1_0
    assert YGNodeGetChild(root2_child1, 1) is root_child1_1

    YGNodeFreeRecursive(root2)
    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def test_cloning_and_freeing():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    root_child0 = YGNodeNewWithConfig(config)
    YGNodeInsertChild(root, root_child0, 0)
    root_child1 = YGNodeNewWithConfig(config)
    YGNodeInsertChild(root, root_child1, 1)

    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)
    root2 = YGNodeClone(root)

    YGNodeFree(root)
    YGNodeCalculateLayout(root2, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)

    YGNodeFreeRecursive(root2)
    YGNodeFree(root_child0)
    YGNodeFree(root_child1)
    YGConfigFree(config)


def test_mixed_shared_and_owned_children():
    root0 = YGNodeNew()
    root1 = YGNodeNew()

    root0_child0 = YGNodeNew()
    root0_child0_0 = YGNodeNew()
    YGNodeInsertChild(root0, root0_child0, 0)
    YGNodeInsertChild(root0_child0, root0_child0_0, 0)

    root1_child0 = YGNodeNew()
    root1_child2 = YGNodeNew()
    YGNodeInsertChild(root1, root1_child0, 0)
    YGNodeInsertChild(root1, root1_child2, 1)

    children = list(root1.getChildren())
    children.insert(1, root0_child0)
    root1.setChildren(children)

    second_child = YGNodeGetChild(root1, 1)
    assert second_child is YGNodeGetChild(root0, 0)
    assert YGNodeGetChild(second_child, 0) is YGNodeGetChild(root0_child0, 0)

    YGNodeCalculateLayout(root1, YGUndefined, YGUndefined, YGDirection.YGDirectionLTR)
    second_child = YGNodeGetChild(root1, 1)
    assert second_child is not YGNodeGetChild(root0, 0)
    assert YGNodeGetOwner(second_child) is root1
    assert YGNodeGetChild(second_child, 0) is not YGNodeGetChild(root0_child0, 0)
    assert YGNodeGetOwner(YGNodeGetChild(second_child, 0)) is second_child

    YGNodeFreeRecursive(root1)
    YGNodeFreeRecursive(root0)
