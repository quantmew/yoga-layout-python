"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from dataclasses import dataclass

from ..YGEnums import YGUnit
from ..YGValue import YGValue
from ..numeric.FloatOptional import FloatOptional, inexactEquals as inexactEqualsFloatOptional
from ..numeric.Comparison import isUndefined, isinf


@dataclass(frozen=True)
class StyleLength:
    value_: FloatOptional = FloatOptional()
    unit_: YGUnit = YGUnit.YGUnitUndefined

    @staticmethod
    def points(value: float) -> "StyleLength":
        return (
            StyleLength.undefined()
            if isUndefined(value) or isinf(value)
            else StyleLength(FloatOptional(value), YGUnit.YGUnitPoint)
        )

    @staticmethod
    def percent(value: float) -> "StyleLength":
        return (
            StyleLength.undefined()
            if isUndefined(value) or isinf(value)
            else StyleLength(FloatOptional(value), YGUnit.YGUnitPercent)
        )

    @staticmethod
    def ofAuto() -> "StyleLength":
        return StyleLength(FloatOptional(), YGUnit.YGUnitAuto)

    @staticmethod
    def undefined() -> "StyleLength":
        return StyleLength(FloatOptional(), YGUnit.YGUnitUndefined)

    def isAuto(self) -> bool:
        return self.unit_ == YGUnit.YGUnitAuto

    def isUndefined(self) -> bool:
        return self.unit_ == YGUnit.YGUnitUndefined

    def isPoints(self) -> bool:
        return self.unit_ == YGUnit.YGUnitPoint

    def isPercent(self) -> bool:
        return self.unit_ == YGUnit.YGUnitPercent

    def isDefined(self) -> bool:
        return not self.isUndefined()

    def value(self) -> FloatOptional:
        return self.value_

    def resolve(self, referenceLength: float) -> FloatOptional:
        if self.unit_ == YGUnit.YGUnitPoint:
            return self.value_
        if self.unit_ == YGUnit.YGUnitPercent:
            return FloatOptional(self.value_.unwrap() * referenceLength * 0.01)
        return FloatOptional()

    def asYGValue(self) -> YGValue:
        return YGValue(self.value_.unwrap(), self.unit_)

    def inexactEquals(self, other: "StyleLength") -> bool:
        return self.unit_ == other.unit_ and inexactEqualsFloatOptional(
            self.value_, other.value_
        )


def inexactEquals(a: StyleLength, b: StyleLength) -> bool:
    return a.inexactEquals(b)
