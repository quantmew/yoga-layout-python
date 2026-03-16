"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from dataclasses import dataclass
import math

from .YGEnums import YGUnit


YGUndefined = float("nan")


@dataclass(frozen=True)
class YGValue:
    value: float
    unit: YGUnit

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, YGValue):
            return NotImplemented
        if self.unit != other.unit:
            return False
        if self.unit in {
            YGUnit.YGUnitUndefined,
            YGUnit.YGUnitAuto,
            YGUnit.YGUnitFitContent,
            YGUnit.YGUnitMaxContent,
            YGUnit.YGUnitStretch,
        }:
            return True
        return self.value == other.value

    def __neg__(self) -> "YGValue":
        return YGValue(-self.value, self.unit)


YGValueAuto = YGValue(YGUndefined, YGUnit.YGUnitAuto)
YGValueUndefined = YGValue(YGUndefined, YGUnit.YGUnitUndefined)
YGValueZero = YGValue(0.0, YGUnit.YGUnitPoint)


def YGFloatIsUndefined(value: float) -> bool:
    return math.isnan(value)
