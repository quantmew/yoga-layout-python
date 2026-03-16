import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import (  # noqa: E402
    YGDirection,
    YGFloatIsUndefined,
    YGNodeCalculateLayout,
    YGNodeFreeRecursive,
    YGNodeInsertChild,
    YGNodeIsDirty,
    YGNodeLayoutGetHeight,
    YGNodeLayoutGetLeft,
    YGNodeLayoutGetTop,
    YGNodeLayoutGetWidth,
    YGNodeNew,
    YGNodeRemoveChild,
    YGNodeStyleSetHeight,
    YGNodeStyleSetWidth,
)


def test_reset_layout_when_child_removed():
    root = YGNodeNew()

    root_child0 = YGNodeNew()
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeInsertChild(root, root_child0, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 100

    YGNodeRemoveChild(root, root_child0)

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGFloatIsUndefined(YGNodeLayoutGetWidth(root_child0))
    assert YGFloatIsUndefined(YGNodeLayoutGetHeight(root_child0))

    YGNodeFreeRecursive(root)
    YGNodeFreeRecursive(root_child0)


def test_removed_child_can_be_reused_with_valid_layout():
    root = YGNodeNew()
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 200)

    child = YGNodeNew()
    YGNodeStyleSetWidth(child, 100)
    YGNodeStyleSetHeight(child, 100)
    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetWidth(child) == 100
    assert YGNodeLayoutGetHeight(child) == 100

    YGNodeRemoveChild(root, child)

    assert YGFloatIsUndefined(YGNodeLayoutGetWidth(child))
    assert YGFloatIsUndefined(YGNodeLayoutGetHeight(child))
    assert YGNodeIsDirty(child) is True

    YGNodeInsertChild(root, child, 0)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetWidth(child) == 100
    assert YGNodeLayoutGetHeight(child) == 100
    assert YGNodeIsDirty(child) is False

    YGNodeFreeRecursive(root)
