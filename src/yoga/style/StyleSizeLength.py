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
class StyleSizeLength:
    value_: FloatOptional = FloatOptional()
    unit_: YGUnit = YGUnit.YGUnitUndefined

    @staticmethod
    def points(value: float) -> "StyleSizeLength":
        return (
            StyleSizeLength.undefined()
            if isUndefined(value) or isinf(value)
            else StyleSizeLength(FloatOptional(value), YGUnit.YGUnitPoint)
        )

    @staticmethod
    def percent(value: float) -> "StyleSizeLength":
        return (
            StyleSizeLength.undefined()
            if isUndefined(value) or isinf(value)
            else StyleSizeLength(FloatOptional(value), YGUnit.YGUnitPercent)
        )

    @staticmethod
    def stretch(fraction: float) -> "StyleSizeLength":
        return (
            StyleSizeLength.undefined()
            if isUndefined(fraction) or isinf(fraction)
            else StyleSizeLength(FloatOptional(fraction), YGUnit.YGUnitStretch)
        )

    @staticmethod
    def ofAuto() -> "StyleSizeLength":
        return StyleSizeLength(FloatOptional(), YGUnit.YGUnitAuto)

    @staticmethod
    def ofMaxContent() -> "StyleSizeLength":
        return StyleSizeLength(FloatOptional(), YGUnit.YGUnitMaxContent)

    @staticmethod
    def ofFitContent() -> "StyleSizeLength":
        return StyleSizeLength(FloatOptional(), YGUnit.YGUnitFitContent)

    @staticmethod
    def ofStretch() -> "StyleSizeLength":
        return StyleSizeLength(FloatOptional(), YGUnit.YGUnitStretch)

    @staticmethod
    def undefined() -> "StyleSizeLength":
        return StyleSizeLength(FloatOptional(), YGUnit.YGUnitUndefined)

    def isAuto(self) -> bool:
        return self.unit_ == YGUnit.YGUnitAuto

    def isMaxContent(self) -> bool:
        return self.unit_ == YGUnit.YGUnitMaxContent

    def isFitContent(self) -> bool:
        return self.unit_ == YGUnit.YGUnitFitContent

    def isStretch(self) -> bool:
        return self.unit_ == YGUnit.YGUnitStretch

    def isUndefined(self) -> bool:
        return self.unit_ == YGUnit.YGUnitUndefined

    def isDefined(self) -> bool:
        return not self.isUndefined()

    def isPoints(self) -> bool:
        return self.unit_ == YGUnit.YGUnitPoint

    def isPercent(self) -> bool:
        return self.unit_ == YGUnit.YGUnitPercent

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

    def inexactEquals(self, other: "StyleSizeLength") -> bool:
        return self.unit_ == other.unit_ and inexactEqualsFloatOptional(
            self.value_, other.value_
        )


def inexactEquals(a: StyleSizeLength, b: StyleSizeLength) -> bool:
    return a.inexactEquals(b)
