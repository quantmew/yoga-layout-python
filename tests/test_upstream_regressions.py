import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import (  # noqa: E402
    YGDirection,
    YGDisplay,
    YGEdge,
    YGNodeCalculateLayout,
    YGNodeClone,
    YGNodeFree,
    YGNodeInsertChild,
    YGNodeLayoutGetHeight,
    YGNodeLayoutGetLeft,
    YGNodeLayoutGetPadding,
    YGNodeLayoutGetRight,
    YGNodeLayoutGetWidth,
    YGNodeNew,
    YGNodeSetMeasureFunc,
    YGNodeStyleSetDirection,
    YGNodeStyleSetDisplay,
    YGNodeStyleSetPadding,
    YGNodeStyleSetWidth,
    YGSize,
)
from yoga.algorithm.SizingMode import SizingMode  # noqa: E402
from yoga.event.event import Event  # noqa: E402
from yoga.node.CachedMeasurement import CachedMeasurement  # noqa: E402


def test_measure_invalid_dimensions_are_clamped_like_upstream():
    node = YGNodeNew()
    YGNodeSetMeasureFunc(
        node,
        lambda _node, _w, _wm, _h, _hm: YGSize(width=-5.0, height=10.0),
    )

    YGNodeCalculateLayout(node, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetWidth(node) == 0.0
    assert YGNodeLayoutGetHeight(node) == 10.0


def test_layout_padding_start_end_are_resolved_by_direction():
    node = YGNodeNew()
    YGNodeStyleSetDirection(node, YGDirection.YGDirectionRTL)
    YGNodeStyleSetWidth(node, 100.0)
    YGNodeStyleSetPadding(node, YGEdge.YGEdgeStart, 7.0)

    YGNodeCalculateLayout(node, 100.0, float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetPadding(node, YGEdge.YGEdgeStart) == 7.0
    assert YGNodeLayoutGetPadding(node, YGEdge.YGEdgeRight) == 7.0
    assert YGNodeLayoutGetPadding(node, YGEdge.YGEdgeLeft) == 0.0


def test_cached_measurement_equality_treats_undefined_like_upstream():
    lhs = CachedMeasurement(
        availableWidth=math.nan,
        availableHeight=math.nan,
        widthSizingMode=SizingMode.MaxContent,
        heightSizingMode=SizingMode.FitContent,
        computedWidth=math.nan,
        computedHeight=42.0,
    )
    rhs = CachedMeasurement(
        availableWidth=math.nan,
        availableHeight=math.nan,
        widthSizingMode=SizingMode.MaxContent,
        heightSizingMode=SizingMode.FitContent,
        computedWidth=math.nan,
        computedHeight=42.0,
    )

    assert lhs == rhs


def test_layoutable_children_skips_display_contents_nodes():
    root = YGNodeNew()
    contents = YGNodeNew()
    leaf = YGNodeNew()

    YGNodeStyleSetDisplay(contents, YGDisplay.YGDisplayContents)
    YGNodeInsertChild(root, contents, 0)
    YGNodeInsertChild(contents, leaf, 0)

    layout_children = list(root.getLayoutChildren())

    assert layout_children == [leaf]


def test_node_allocation_and_deallocation_events_follow_upstream_paths():
    events = []

    Event.reset()
    Event.subscribe(lambda _node, eventType, _data: events.append(eventType))

    node = YGNodeNew()
    clone = YGNodeClone(node)
    YGNodeFree(clone)
    YGNodeFree(node)

    assert events == [
        Event.NodeAllocation,
        Event.NodeAllocation,
        Event.NodeDeallocation,
        Event.NodeDeallocation,
    ]
