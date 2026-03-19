"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from dataclasses import dataclass, field
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


@dataclass
class LayoutData:
    layouts: int = 0
    measures: int = 0
    maxMeasureCache: int = 0
    cachedLayouts: int = 0
    cachedMeasures: int = 0
    measureCallbacks: int = 0
    measureCallbackReasonsCount: list[int] = field(
        default_factory=lambda: [0] * int(LayoutPassReason.COUNT)
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


@dataclass(frozen=True)
class EventData:
    pass


@dataclass(frozen=True)
class NodeAllocationData(EventData):
    config: Any = None


@dataclass(frozen=True)
class NodeDeallocationData(EventData):
    config: Any = None


@dataclass(frozen=True)
class LayoutPassEndData(EventData):
    layoutData: LayoutData | None = None


@dataclass(frozen=True)
class MeasureCallbackEndData(EventData):
    width: float
    widthMeasureMode: Any
    height: float
    heightMeasureMode: Any
    measuredWidth: float
    measuredHeight: float
    reason: LayoutPassReason


@dataclass(frozen=True)
class NodeLayoutData(EventData):
    layoutType: LayoutType


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
