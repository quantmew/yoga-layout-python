"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from dataclasses import dataclass

from ..algorithm.SizingMode import SizingMode
from ..numeric.Comparison import isUndefined


@dataclass
class CachedMeasurement:
    availableWidth: float = -1.0
    availableHeight: float = -1.0
    widthSizingMode: SizingMode = SizingMode.MaxContent
    heightSizingMode: SizingMode = SizingMode.MaxContent
    computedWidth: float = -1.0
    computedHeight: float = -1.0

    def __eq__(self, measurement: object) -> bool:
        if not isinstance(measurement, CachedMeasurement):
            return NotImplemented

        isEqual = (
            self.widthSizingMode == measurement.widthSizingMode
            and self.heightSizingMode == measurement.heightSizingMode
        )

        if not isUndefined(self.availableWidth) or not isUndefined(
            measurement.availableWidth
        ):
            isEqual = isEqual and self.availableWidth == measurement.availableWidth
        if not isUndefined(self.availableHeight) or not isUndefined(
            measurement.availableHeight
        ):
            isEqual = isEqual and self.availableHeight == measurement.availableHeight
        if not isUndefined(self.computedWidth) or not isUndefined(
            measurement.computedWidth
        ):
            isEqual = isEqual and self.computedWidth == measurement.computedWidth
        if not isUndefined(self.computedHeight) or not isUndefined(
            measurement.computedHeight
        ):
            isEqual = isEqual and self.computedHeight == measurement.computedHeight

        return isEqual
