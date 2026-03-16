import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import (  # noqa: E402
    YGDirection,
    YGNodeCalculateLayout,
    YGNodeClone,
    YGNodeFreeRecursive,
    YGNodeGetChild,
    YGNodeGetChildCount,
    YGNodeGetOwner,
    YGNodeInsertChild,
    YGNodeNew,
    YGNodeStyleSetHeight,
    YGNodeStyleSetPositionType,
    YGNodeStyleSetWidth,
    YGNodeStyleSetWidthPercent,
    YGPositionType,
)


def _recursively_assert_proper_node_ownership(node):
    for index in range(YGNodeGetChildCount(node)):
        child = YGNodeGetChild(node, index)
        assert YGNodeGetOwner(child) is node
        _recursively_assert_proper_node_ownership(child)


def test_absolute_node_cloned_with_static_parent():
    root = YGNodeNew()
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNew()
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeStyleSetWidth(root_child0, 10)
    YGNodeStyleSetHeight(root_child0, 10)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNew()
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidthPercent(root_child0_child0, 1)
    YGNodeStyleSetHeight(root_child0_child0, 1)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    clonedRoot = YGNodeClone(root)
    YGNodeStyleSetWidth(clonedRoot, 110)
    YGNodeCalculateLayout(clonedRoot, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    _recursively_assert_proper_node_ownership(clonedRoot)

    YGNodeFreeRecursive(root)
    YGNodeFreeRecursive(clonedRoot)


def test_absolute_node_cloned_with_static_ancestors():
    root = YGNodeNew()
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    root_child0 = YGNodeNew()
    YGNodeStyleSetPositionType(root_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNew()
    YGNodeStyleSetPositionType(root_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeStyleSetWidth(root_child0_child0, 40)
    YGNodeStyleSetHeight(root_child0_child0, 40)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child0_child0 = YGNodeNew()
    YGNodeStyleSetPositionType(root_child0_child0_child0, YGPositionType.YGPositionTypeStatic)
    YGNodeStyleSetWidth(root_child0_child0_child0, 30)
    YGNodeStyleSetHeight(root_child0_child0_child0, 30)
    YGNodeInsertChild(root_child0_child0, root_child0_child0_child0, 0)

    abs_child = YGNodeNew()
    YGNodeStyleSetPositionType(abs_child, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidthPercent(abs_child, 1)
    YGNodeStyleSetHeight(abs_child, 1)
    YGNodeInsertChild(root_child0_child0_child0, abs_child, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    clonedRoot = YGNodeClone(root)
    YGNodeStyleSetWidth(clonedRoot, 110)
    YGNodeCalculateLayout(clonedRoot, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    _recursively_assert_proper_node_ownership(clonedRoot)

    YGNodeFreeRecursive(root)
    YGNodeFreeRecursive(clonedRoot)
