import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import YGConfigFree, YGConfigNew, YGNodeFree  # noqa: E402
from yoga.node.Node import Node  # noqa: E402

_CLONED_NODE = Node()


def _clone_node(_node, _owner, _child_index):
    return _CLONED_NODE


def _do_not_clone(_node, _owner, _child_index):
    return None


def test_uses_values_provided_by_cloning_callback():
    config = YGConfigNew()
    config.setCloneNodeCallback(_clone_node)

    node = Node()
    owner = Node()
    clone = config.cloneNode(node, owner, 0)

    assert clone is _CLONED_NODE

    YGConfigFree(config)


def test_falls_back_to_regular_cloning_if_callback_returns_null():
    config = YGConfigNew()
    config.setCloneNodeCallback(_do_not_clone)

    node = Node()
    owner = Node()
    clone = config.cloneNode(node, owner, 0)

    assert clone is not None
    YGNodeFree(clone)
    YGConfigFree(config)
