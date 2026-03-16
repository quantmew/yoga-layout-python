import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import (  # noqa: E402
    YGConfigFree,
    YGConfigGetDefault,
    YGConfigNew,
    YGDirection,
    YGNodeCalculateLayout,
    YGNodeClone,
    YGNodeFree,
    YGNodeFreeRecursive,
    YGNodeInsertChild,
    YGNodeNew,
    YGNodeNewWithConfig,
)
from yoga.event.event import Event, LayoutPassEndData  # noqa: E402


def test_new_node_has_event():
    events = []
    Event.reset()
    Event.subscribe(lambda node, eventType, eventData: events.append((node, eventType, eventData)))

    config = YGConfigGetDefault()
    node = YGNodeNew()

    eventNode, eventType, eventData = events[-1]
    assert eventNode is node
    assert eventType == Event.NodeAllocation
    assert eventData.config is config

    YGNodeFree(node)


def test_new_node_with_config_event():
    events = []
    Event.reset()
    Event.subscribe(lambda node, eventType, eventData: events.append((node, eventType, eventData)))

    config = YGConfigNew()
    node = YGNodeNewWithConfig(config)

    eventNode, eventType, eventData = events[-1]
    assert eventNode is node
    assert eventType == Event.NodeAllocation
    assert eventData.config is config

    YGNodeFree(node)
    YGConfigFree(config)


def test_clone_node_event():
    events = []
    Event.reset()
    Event.subscribe(lambda node, eventType, eventData: events.append((node, eventType, eventData)))

    config = YGConfigNew()
    node = YGNodeNewWithConfig(config)
    clone = YGNodeClone(node)

    eventNode, eventType, eventData = events[-1]
    assert eventNode is clone
    assert eventType == Event.NodeAllocation
    assert eventData.config is config

    YGNodeFree(node)
    YGNodeFree(clone)
    YGConfigFree(config)


def test_free_node_event():
    events = []
    Event.reset()
    Event.subscribe(lambda node, eventType, eventData: events.append((node, eventType, eventData)))

    config = YGConfigNew()
    node = YGNodeNewWithConfig(config)
    YGNodeFree(node)

    eventNode, eventType, eventData = events[-1]
    assert eventNode is node
    assert eventType == Event.NodeDeallocation
    assert eventData.config is config

    YGConfigFree(config)


def test_layout_events_single_node():
    events = []
    Event.reset()
    Event.subscribe(lambda node, eventType, eventData: events.append((node, eventType, eventData)))

    root = YGNodeNew()
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert events[1][0] is root
    assert events[1][1] == Event.LayoutPassStart

    assert events[2][0] is root
    assert events[2][1] == Event.NodeLayout

    assert events[3][0] is root
    assert events[3][1] == Event.LayoutPassEnd

    layoutData = events[3][2]
    assert isinstance(layoutData, LayoutPassEndData)
    assert layoutData.layoutData.layouts == 1
    assert layoutData.layoutData.measures == 0
    assert layoutData.layoutData.maxMeasureCache == 1

    YGNodeFree(root)


def test_layout_events_counts_cache_hits_single_node_layout():
    events = []
    Event.reset()
    Event.subscribe(lambda node, eventType, eventData: events.append((node, eventType, eventData)))

    root = YGNodeNew()
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert events[4][0] is root
    assert events[4][1] == Event.LayoutPassStart

    assert events[6][0] is root
    assert events[6][1] == Event.LayoutPassEnd

    layoutData = events[6][2]
    assert isinstance(layoutData, LayoutPassEndData)
    assert layoutData.layoutData.layouts == 0
    assert layoutData.layoutData.measures == 0
    assert layoutData.layoutData.cachedLayouts == 1
    assert layoutData.layoutData.cachedMeasures == 0

    YGNodeFree(root)


def test_layout_events_counts_multi_node_layout():
    events = []
    Event.reset()
    Event.subscribe(lambda node, eventType, eventData: events.append((node, eventType, eventData)))

    root = YGNodeNew()
    childA = YGNodeNew()
    YGNodeInsertChild(root, childA, 0)
    childB = YGNodeNew()
    YGNodeInsertChild(root, childB, 1)

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert events[3][0] is root
    assert events[3][1] == Event.LayoutPassStart

    assert events[11][0] is root
    assert events[11][1] == Event.LayoutPassEnd

    layoutData = events[11][2]
    assert isinstance(layoutData, LayoutPassEndData)
    assert layoutData.layoutData.layouts == 3
    assert layoutData.layoutData.measures == 4
    assert layoutData.layoutData.maxMeasureCache == 3

    YGNodeFreeRecursive(root)
