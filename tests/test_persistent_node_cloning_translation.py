import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import (  # noqa: E402
    YGConfigFree,
    YGConfigNew,
    YGConfigSetCloneNodeFunc,
    YGDirection,
    YGDisplay,
    YGNodeCalculateLayout,
    YGNodeClone,
    YGNodeFree,
    YGNodeGetContext,
    YGNodeGetOwner,
    YGNodeNewWithConfig,
    YGNodeSetContext,
    YGNodeStyleSetDisplay,
    YGNodeStyleSetHeight,
    YGNodeStyleSetPositionType,
    YGNodeStyleSetWidth,
    YGPositionType,
)


class NodeWrapper:
    def __init__(self, config, children=None):
        self.node = YGNodeNewWithConfig(config)
        self.children = list(children or [])
        YGNodeSetContext(self.node, self)

        private_node = self.node
        for child in self.children:
            private_child = child.node
            if YGNodeGetOwner(child.node) is None:
                private_child.setOwner(private_node)
            private_node.insertChild(private_child, private_node.getChildCount())

    @classmethod
    def clone(cls, other, children=None):
        wrapper = cls.__new__(cls)
        wrapper.node = YGNodeClone(other.node)
        wrapper.children = list(other.children if children is None else children)
        YGNodeSetContext(wrapper.node, wrapper)

        private_node = wrapper.node
        private_node.setOwner(None)
        if children is not None:
            private_node.setChildren([])
            private_node.setDirty(True)
            for child in wrapper.children:
                private_child = child.node
                if YGNodeGetOwner(child.node) is None:
                    private_child.setOwner(private_node)
                private_node.insertChild(private_child, private_node.getChildCount())
        return wrapper

    def free(self):
        YGNodeFree(self.node)


def test_changing_sibling_height_does_not_clone_neighbors():
    config = YGConfigNew()
    cloned_nodes = []

    def on_clone(old_node, owner, child_index):
        wrapper = YGNodeGetContext(owner)
        old = YGNodeGetContext(old_node)
        wrapper.children[child_index] = NodeWrapper.clone(old)
        clone = wrapper.children[child_index]
        cloned_nodes.append(old)
        return clone.node

    YGConfigSetCloneNodeFunc(config, on_clone)

    sibling = NodeWrapper(config)
    YGNodeStyleSetHeight(sibling.node, 1)

    d = NodeWrapper(config)
    c = NodeWrapper(config, [d])
    b = NodeWrapper(config, [c])
    a = NodeWrapper(config, [b])
    YGNodeStyleSetHeight(a.node, 1)

    scroll_content_view = NodeWrapper(config, [sibling, a])
    YGNodeStyleSetPositionType(
        scroll_content_view.node, YGPositionType.YGPositionTypeAbsolute
    )

    scroll_view = NodeWrapper(config, [scroll_content_view])
    YGNodeStyleSetWidth(scroll_view.node, 100)
    YGNodeStyleSetHeight(scroll_view.node, 100)

    cloned_nodes.clear()
    YGNodeCalculateLayout(
        scroll_view.node, float("nan"), float("nan"), YGDirection.YGDirectionLTR
    )
    assert cloned_nodes == []

    sibling_prime = NodeWrapper(config)
    YGNodeStyleSetHeight(sibling_prime.node, 2)

    scroll_content_view_prime = NodeWrapper.clone(
        scroll_content_view, [sibling_prime, a]
    )
    scroll_view_prime = NodeWrapper.clone(scroll_view, [scroll_content_view_prime])

    cloned_nodes.clear()
    YGNodeCalculateLayout(
        scroll_view_prime.node, float("nan"), float("nan"), YGDirection.YGDirectionLTR
    )

    assert len(cloned_nodes) == 1
    assert cloned_nodes[0] is a

    scroll_view_prime.free()
    scroll_content_view_prime.free()
    sibling_prime.free()
    scroll_view.free()
    scroll_content_view.free()
    a.free()
    b.free()
    c.free()
    d.free()
    sibling.free()
    YGConfigFree(config)


def test_clone_leaf_display_contents_node():
    config = YGConfigNew()
    cloned_nodes = []

    def on_clone(old_node, owner, child_index):
        wrapper = YGNodeGetContext(owner)
        old = YGNodeGetContext(old_node)
        wrapper.children[child_index] = NodeWrapper.clone(old)
        clone = wrapper.children[child_index]
        cloned_nodes.append(old)
        return clone.node

    YGConfigSetCloneNodeFunc(config, on_clone)

    b = NodeWrapper(config)
    a = NodeWrapper(config, [b])
    YGNodeStyleSetDisplay(b.node, YGDisplay.YGDisplayContents)

    cloned_nodes.clear()
    YGNodeCalculateLayout(a.node, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    assert cloned_nodes == []

    a_prime = NodeWrapper(config, [b])
    cloned_nodes.clear()
    YGNodeCalculateLayout(a_prime.node, 100, 100, YGDirection.YGDirectionLTR)

    assert len(cloned_nodes) == 1
    assert cloned_nodes[0] is b

    a_prime.free()
    a.free()
    b.free()
    YGConfigFree(config)
