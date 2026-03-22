# cython: infer_types=False
"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from .Comparison import (
    inexactEquals as inexactEqualsFloat,
)
from .Comparison import (
    isDefined,
    isUndefined,
)
from .Comparison import (
    maxOrDefined as maxOrDefinedFloat,
)

class FloatOptional:
    def __init__(self, value=float("nan")) -> None:
        self._value_box = (float(value),)

    @property
    def value(self):
        return self._value_box[0]

    def unwrap(self):
        return self.value

    def unwrapOrDefault(self, defaultValue):
        return defaultValue if self.isUndefined() else self.value

    def isUndefined(self) -> bool:
        return isUndefined(self.value)

    def isDefined(self) -> bool:
        return isDefined(self.value)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, FloatOptional):
            return self.value == other.value or (
                self.isUndefined() and other.isUndefined()
            )
        if isinstance(other, (float, int)):
            return self == FloatOptional(float(other))
        return NotImplemented

    def __add__(self, other: FloatOptional) -> FloatOptional:
        return FloatOptional(self.value + other.value)

    def __lt__(self, other: FloatOptional) -> bool:
        return self.value < other.value

    def __gt__(self, other: FloatOptional) -> bool:
        return self.value > other.value

    def __le__(self, other: FloatOptional) -> bool:
        return self < other or self == other

    def __ge__(self, other: FloatOptional) -> bool:
        return self > other or self == other

    def __repr__(self) -> str:
        return f"FloatOptional(value={self.value!r})"

def maxOrDefined(lhs: FloatOptional, rhs: FloatOptional) -> FloatOptional:
    return FloatOptional(maxOrDefinedFloat(lhs.unwrap(), rhs.unwrap()))


def inexactEquals(lhs: FloatOptional, rhs: FloatOptional) -> bool:
    return inexactEqualsFloat(lhs.unwrap(), rhs.unwrap())
