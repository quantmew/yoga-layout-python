import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import (  # noqa: E402
    YGDisplay,
    YGNodeFreeRecursive,
    YGNodeInsertChild,
    YGNodeNew,
    YGNodeStyleSetDisplay,
)


def test_layoutable_children_single_contents_node():
    root = YGNodeNew()
    root_child0 = YGNodeNew()
    root_child1 = YGNodeNew()
    root_child2 = YGNodeNew()
    root_grandchild0 = YGNodeNew()
    root_grandchild1 = YGNodeNew()

    YGNodeInsertChild(root, root_child0, 0)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeInsertChild(root_child1, root_grandchild0, 0)
    YGNodeInsertChild(root_child1, root_grandchild1, 1)
    YGNodeStyleSetDisplay(root_child1, YGDisplay.YGDisplayContents)

    assert list(root.getLayoutChildren()) == [
        root_child0,
        root_grandchild0,
        root_grandchild1,
        root_child2,
    ]

    YGNodeFreeRecursive(root)


def test_layoutable_children_multiple_contents_nodes():
    root = YGNodeNew()
    children = [YGNodeNew() for _ in range(3)]
    grandchildren = [YGNodeNew() for _ in range(6)]

    for index, child in enumerate(children):
        YGNodeInsertChild(root, child, index)
    YGNodeInsertChild(children[0], grandchildren[0], 0)
    YGNodeInsertChild(children[0], grandchildren[1], 1)
    YGNodeInsertChild(children[1], grandchildren[2], 0)
    YGNodeInsertChild(children[1], grandchildren[3], 1)
    YGNodeInsertChild(children[2], grandchildren[4], 0)
    YGNodeInsertChild(children[2], grandchildren[5], 1)

    for child in children:
        YGNodeStyleSetDisplay(child, YGDisplay.YGDisplayContents)

    assert list(root.getLayoutChildren()) == grandchildren

    YGNodeFreeRecursive(root)


def test_layoutable_children_nested_contents_nodes():
    root = YGNodeNew()
    root_child0 = YGNodeNew()
    root_child1 = YGNodeNew()
    root_child2 = YGNodeNew()
    root_grandchild0 = YGNodeNew()
    root_grandchild1 = YGNodeNew()
    root_great_grandchild0 = YGNodeNew()
    root_great_grandchild1 = YGNodeNew()

    YGNodeInsertChild(root, root_child0, 0)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeInsertChild(root_child1, root_grandchild0, 0)
    YGNodeInsertChild(root_child1, root_grandchild1, 1)
    YGNodeInsertChild(root_grandchild1, root_great_grandchild0, 0)
    YGNodeInsertChild(root_grandchild1, root_great_grandchild1, 1)

    YGNodeStyleSetDisplay(root_child1, YGDisplay.YGDisplayContents)
    YGNodeStyleSetDisplay(root_grandchild1, YGDisplay.YGDisplayContents)

    assert list(root.getLayoutChildren()) == [
        root_child0,
        root_grandchild0,
        root_great_grandchild0,
        root_great_grandchild1,
        root_child2,
    ]

    YGNodeFreeRecursive(root)


def test_layoutable_children_contents_leaf_node():
    root = YGNodeNew()
    root_child0 = YGNodeNew()
    root_child1 = YGNodeNew()
    root_child2 = YGNodeNew()

    YGNodeInsertChild(root, root_child0, 0)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeStyleSetDisplay(root_child1, YGDisplay.YGDisplayContents)

    assert list(root.getLayoutChildren()) == [root_child0, root_child2]

    YGNodeFreeRecursive(root)


def test_layoutable_children_contents_root_node():
    root = YGNodeNew()
    root_child0 = YGNodeNew()
    root_child1 = YGNodeNew()
    root_child2 = YGNodeNew()

    YGNodeInsertChild(root, root_child0, 0)
    YGNodeInsertChild(root, root_child1, 1)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeStyleSetDisplay(root, YGDisplay.YGDisplayContents)

    assert list(root.getLayoutChildren()) == [root_child0, root_child1, root_child2]

    YGNodeFreeRecursive(root)
