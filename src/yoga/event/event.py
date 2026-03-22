"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from enum import IntEnum
from typing import Any


class LayoutType(IntEnum):
    kLayout = 0
    kMeasure = 1
    kCachedLayout = 2
    kCachedMeasure = 3


class LayoutPassReason(IntEnum):
    kInitial = 0
    kAbsLayout = 1
    kStretch = 2
    kMultilineStretch = 3
    kFlexLayout = 4
    kMeasureChild = 5
    kAbsMeasureChild = 6
    kFlexMeasure = 7
    kGridLayout = 8
    COUNT = 9


class LayoutData:
    __slots__ = (
        "layouts",
        "measures",
        "maxMeasureCache",
        "cachedLayouts",
        "cachedMeasures",
        "measureCallbacks",
        "measureCallbackReasonsCount",
    )

    def __init__(
        self,
        layouts: int = 0,
        measures: int = 0,
        maxMeasureCache: int = 0,
        cachedLayouts: int = 0,
        cachedMeasures: int = 0,
        measureCallbacks: int = 0,
        measureCallbackReasonsCount: list[int] | None = None,
    ) -> None:
        self.layouts = layouts
        self.measures = measures
        self.maxMeasureCache = maxMeasureCache
        self.cachedLayouts = cachedLayouts
        self.cachedMeasures = cachedMeasures
        self.measureCallbacks = measureCallbacks
        self.measureCallbackReasonsCount = (
            [0] * int(LayoutPassReason.COUNT)
            if measureCallbackReasonsCount is None
            else measureCallbackReasonsCount
        )


def LayoutPassReasonToString(value: LayoutPassReason) -> str:
    names = {
        LayoutPassReason.kInitial: "initial",
        LayoutPassReason.kAbsLayout: "abs_layout",
        LayoutPassReason.kStretch: "stretch",
        LayoutPassReason.kMultilineStretch: "multiline_stretch",
        LayoutPassReason.kFlexLayout: "flex_layout",
        LayoutPassReason.kMeasureChild: "measure",
        LayoutPassReason.kAbsMeasureChild: "abs_measure",
        LayoutPassReason.kFlexMeasure: "flex_measure",
        LayoutPassReason.kGridLayout: "grid_layout",
    }
    return names.get(value, "unknown")


class EventData:
    __slots__ = ()


class NodeAllocationData(EventData):
    __slots__ = ("config",)

    def __init__(self, config: Any = None) -> None:
        self.config = config


class NodeDeallocationData(EventData):
    __slots__ = ("config",)

    def __init__(self, config: Any = None) -> None:
        self.config = config


class LayoutPassEndData(EventData):
    __slots__ = ("layoutData",)

    def __init__(self, layoutData: LayoutData | None = None) -> None:
        self.layoutData = layoutData


class MeasureCallbackEndData(EventData):
    __slots__ = (
        "width",
        "widthMeasureMode",
        "height",
        "heightMeasureMode",
        "measuredWidth",
        "measuredHeight",
        "reason",
    )

    def __init__(
        self,
        width: float,
        widthMeasureMode: Any,
        height: float,
        heightMeasureMode: Any,
        measuredWidth: float,
        measuredHeight: float,
        reason: LayoutPassReason,
    ) -> None:
        self.width = width
        self.widthMeasureMode = widthMeasureMode
        self.height = height
        self.heightMeasureMode = heightMeasureMode
        self.measuredWidth = measuredWidth
        self.measuredHeight = measuredHeight
        self.reason = reason


class NodeLayoutData(EventData):
    __slots__ = ("layoutType",)

    def __init__(self, layoutType: LayoutType) -> None:
        self.layoutType = layoutType


class Event:
    NodeAllocation = "NodeAllocation"
    NodeDeallocation = "NodeDeallocation"
    NodeLayout = "NodeLayout"
    LayoutPassStart = "LayoutPassStart"
    LayoutPassEnd = "LayoutPassEnd"
    MeasureCallbackStart = "MeasureCallbackStart"
    MeasureCallbackEnd = "MeasureCallbackEnd"
    NodeBaselineStart = "NodeBaselineStart"
    NodeBaselineEnd = "NodeBaselineEnd"

    _subscribers: list = []

    @staticmethod
    def reset() -> None:
        Event._subscribers.clear()

    @staticmethod
    def subscribe(subscriber) -> None:
        Event._subscribers.append(subscriber)

    @staticmethod
    def publish(node=None, eventType=None, eventData: EventData | None = None) -> None:
        for subscriber in Event._subscribers:
            subscriber(node, eventType, eventData)
