"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from dataclasses import dataclass

from .StyleSizeLength import StyleSizeLength


@dataclass
class GridTrackSize:
    minSizingFunction: StyleSizeLength
    maxSizingFunction: StyleSizeLength
    baseSize: float = 0.0
    growthLimit: float = 0.0
    infinitelyGrowable: bool = False

    @staticmethod
    def auto_() -> "GridTrackSize":
        auto = StyleSizeLength.ofAuto()
        return GridTrackSize(auto, auto)

    @staticmethod
    def length(points: float) -> "GridTrackSize":
        length = StyleSizeLength.points(points)
        return GridTrackSize(length, length)

    @staticmethod
    def fr(fraction: float) -> "GridTrackSize":
        return GridTrackSize(StyleSizeLength.ofAuto(), StyleSizeLength.stretch(fraction))

    @staticmethod
    def percent(percentage: float) -> "GridTrackSize":
        value = StyleSizeLength.percent(percentage)
        return GridTrackSize(value, value)

    @staticmethod
    def minmax(minimum: StyleSizeLength, maximum: StyleSizeLength) -> "GridTrackSize":
        return GridTrackSize(minimum, maximum)


GridTrackList = list[GridTrackSize]
