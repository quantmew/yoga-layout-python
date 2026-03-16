import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import (  # noqa: E402
    YGAlign,
    YGConfigFree,
    YGConfigNew,
    YGConfigSetErrata,
    YGDirection,
    YGDisplay,
    YGErrata,
    YGFlexDirection,
    YGNodeCalculateLayout,
    YGNodeFree,
    YGNodeFreeRecursive,
    YGNodeInsertChild,
    YGNodeIsDirty,
    YGNodeLayoutGetHeight,
    YGNodeLayoutGetWidth,
    YGNodeNew,
    YGNodeRemoveAllChildren,
    YGNodeRemoveChild,
    YGNodeSetConfig,
    YGNodeStyleSetAlignItems,
    YGNodeStyleSetDisplay,
    YGNodeStyleSetFlexDirection,
    YGNodeStyleSetFlexGrow,
    YGNodeStyleSetHeight,
    YGNodeStyleSetMinWidth,
    YGNodeStyleSetWidth,
)


def test_dirty_propagation():
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    child0 = YGNodeNew()
    YGNodeStyleSetWidth(child0, 50)
    YGNodeStyleSetHeight(child0, 20)
    YGNodeInsertChild(root, child0, 0)

    child1 = YGNodeNew()
    YGNodeStyleSetWidth(child1, 50)
    YGNodeStyleSetHeight(child1, 20)
    YGNodeInsertChild(root, child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    YGNodeStyleSetWidth(child0, 20)

    assert YGNodeIsDirty(child0) is True
    assert YGNodeIsDirty(child1) is False
    assert YGNodeIsDirty(root) is True

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeIsDirty(child0) is False
    assert YGNodeIsDirty(child1) is False
    assert YGNodeIsDirty(root) is False

    YGNodeFreeRecursive(root)


def test_dirty_propagation_only_if_prop_changed():
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    child0 = YGNodeNew()
    YGNodeStyleSetWidth(child0, 50)
    YGNodeStyleSetHeight(child0, 20)
    YGNodeInsertChild(root, child0, 0)

    child1 = YGNodeNew()
    YGNodeStyleSetWidth(child1, 50)
    YGNodeStyleSetHeight(child1, 20)
    YGNodeInsertChild(root, child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    YGNodeStyleSetWidth(child0, 50)

    assert YGNodeIsDirty(child0) is False
    assert YGNodeIsDirty(child1) is False
    assert YGNodeIsDirty(root) is False

    YGNodeFreeRecursive(root)


def test_dirty_propagation_changing_layout_config():
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    child0 = YGNodeNew()
    YGNodeStyleSetWidth(child0, 50)
    YGNodeStyleSetHeight(child0, 20)
    YGNodeInsertChild(root, child0, 0)

    child1 = YGNodeNew()
    YGNodeStyleSetWidth(child1, 50)
    YGNodeStyleSetHeight(child1, 20)
    YGNodeInsertChild(root, child1, 1)

    child00 = YGNodeNew()
    YGNodeStyleSetWidth(child00, 25)
    YGNodeStyleSetHeight(child00, 20)
    YGNodeInsertChild(root, child00, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert not YGNodeIsDirty(root)
    assert not YGNodeIsDirty(child0)
    assert not YGNodeIsDirty(child1)
    assert not YGNodeIsDirty(child00)

    newConfig = YGConfigNew()
    YGConfigSetErrata(newConfig, YGErrata.YGErrataStretchFlexBasis)
    YGNodeSetConfig(child0, newConfig)

    assert YGNodeIsDirty(root)
    assert YGNodeIsDirty(child0)
    assert not YGNodeIsDirty(child1)
    assert not YGNodeIsDirty(child00)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert not YGNodeIsDirty(root)
    assert not YGNodeIsDirty(child0)
    assert not YGNodeIsDirty(child1)
    assert not YGNodeIsDirty(child00)

    YGConfigFree(newConfig)
    YGNodeFreeRecursive(root)


def test_dirty_mark_all_children_as_dirty_when_display_changes():
    root = YGNodeNew()
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetHeight(root, 100)

    child0 = YGNodeNew()
    YGNodeStyleSetFlexGrow(child0, 1)
    child1 = YGNodeNew()
    YGNodeStyleSetFlexGrow(child1, 1)

    child1_child0 = YGNodeNew()
    child1_child0_child0 = YGNodeNew()
    YGNodeStyleSetWidth(child1_child0_child0, 8)
    YGNodeStyleSetHeight(child1_child0_child0, 16)

    YGNodeInsertChild(child1_child0, child1_child0_child0, 0)
    YGNodeInsertChild(child1, child1_child0, 0)
    YGNodeInsertChild(root, child0, 0)
    YGNodeInsertChild(root, child1, 0)

    YGNodeStyleSetDisplay(child0, YGDisplay.YGDisplayFlex)
    YGNodeStyleSetDisplay(child1, YGDisplay.YGDisplayNone)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetWidth(child1_child0_child0) == 0
    assert YGNodeLayoutGetHeight(child1_child0_child0) == 0

    YGNodeStyleSetDisplay(child0, YGDisplay.YGDisplayNone)
    YGNodeStyleSetDisplay(child1, YGDisplay.YGDisplayFlex)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert YGNodeLayoutGetWidth(child1_child0_child0) == 8
    assert YGNodeLayoutGetHeight(child1_child0_child0) == 16

    YGNodeFreeRecursive(root)


def test_dirty_node_only_if_children_are_actually_removed():
    root = YGNodeNew()
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)
    YGNodeStyleSetWidth(root, 50)
    YGNodeStyleSetHeight(root, 50)

    child0 = YGNodeNew()
    YGNodeStyleSetWidth(child0, 50)
    YGNodeStyleSetHeight(child0, 25)
    YGNodeInsertChild(root, child0, 0)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    child1 = YGNodeNew()
    YGNodeRemoveChild(root, child1)
    assert not YGNodeIsDirty(root)
    YGNodeFree(child1)

    YGNodeRemoveChild(root, child0)
    assert YGNodeIsDirty(root)
    YGNodeFree(child0)

    YGNodeFreeRecursive(root)


def test_dirty_node_only_if_undefined_values_gets_set_to_undefined():
    root = YGNodeNew()
    YGNodeStyleSetWidth(root, 50)
    YGNodeStyleSetHeight(root, 50)
    YGNodeStyleSetMinWidth(root, float("nan"))

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert not YGNodeIsDirty(root)

    YGNodeStyleSetMinWidth(root, float("nan"))
    assert not YGNodeIsDirty(root)

    YGNodeFreeRecursive(root)


def test_dirty_removed_child_nodes_when_removing_all():
    root = YGNodeNew()
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)

    child0 = YGNodeNew()
    YGNodeStyleSetWidth(child0, 50)
    YGNodeStyleSetHeight(child0, 25)
    YGNodeInsertChild(root, child0, 0)

    child1 = YGNodeNew()
    YGNodeStyleSetWidth(child1, 50)
    YGNodeStyleSetHeight(child1, 25)
    YGNodeInsertChild(root, child1, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert not YGNodeIsDirty(child0)
    assert not YGNodeIsDirty(child1)

    YGNodeRemoveAllChildren(root)
    assert YGNodeIsDirty(child0)
    assert YGNodeIsDirty(child1)

    YGNodeFree(child0)
    YGNodeFree(child1)
    YGNodeFreeRecursive(root)
