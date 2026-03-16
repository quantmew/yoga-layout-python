import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import (  # noqa: E402
    YGNodeFree,
    YGNodeFreeRecursive,
    YGNodeGetChild,
    YGNodeGetChildCount,
    YGNodeGetOwner,
    YGNodeNew,
    YGNodeSetChildren,
)


def _get_children(node):
    return [YGNodeGetChild(node, i) for i in range(YGNodeGetChildCount(node))]


def test_set_children_adds_children_to_parent():
    root = YGNodeNew()
    child0 = YGNodeNew()
    child1 = YGNodeNew()
    YGNodeSetChildren(root, [child0, child1], 2)
    assert _get_children(root) == [child0, child1]
    assert [YGNodeGetOwner(child0), YGNodeGetOwner(child1)] == [root, root]
    YGNodeFreeRecursive(root)


def test_set_children_to_empty_removes_old_children():
    root = YGNodeNew()
    child0 = YGNodeNew()
    child1 = YGNodeNew()
    YGNodeSetChildren(root, [child0, child1], 2)
    YGNodeSetChildren(root, None, 0)
    assert _get_children(root) == []
    assert [YGNodeGetOwner(child0), YGNodeGetOwner(child1)] == [None, None]
    YGNodeFreeRecursive(root)


def test_set_children_replaces_non_common_children():
    root = YGNodeNew()
    child0 = YGNodeNew()
    child1 = YGNodeNew()
    YGNodeSetChildren(root, [child0, child1], 2)

    child2 = YGNodeNew()
    child3 = YGNodeNew()
    YGNodeSetChildren(root, [child2, child3], 2)

    assert _get_children(root) == [child2, child3]
    assert [YGNodeGetOwner(child0), YGNodeGetOwner(child1)] == [None, None]

    YGNodeFreeRecursive(root)
    YGNodeFree(child0)
    YGNodeFree(child1)


def test_set_children_keeps_and_reorders_common_children():
    root = YGNodeNew()
    child0 = YGNodeNew()
    child1 = YGNodeNew()
    child2 = YGNodeNew()
    YGNodeSetChildren(root, [child0, child1, child2], 3)

    child3 = YGNodeNew()
    YGNodeSetChildren(root, [child2, child1, child3], 3)

    assert _get_children(root) == [child2, child1, child3]
    assert [
        YGNodeGetOwner(child0),
        YGNodeGetOwner(child1),
        YGNodeGetOwner(child2),
        YGNodeGetOwner(child3),
    ] == [None, root, root, root]

    YGNodeFreeRecursive(root)
    YGNodeFree(child0)
