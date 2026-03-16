"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

import math


def isUndefined(value: float) -> bool:
    return math.isnan(value)


def isDefined(value: float) -> bool:
    return not math.isnan(value)


def isinf(value: float) -> bool:
    return math.isinf(value)


def inexactEquals(a: float, b: float, tolerance: float = 0.0001) -> bool:
    if math.isnan(a) and math.isnan(b):
        return True
    if math.isnan(a) or math.isnan(b):
        return False
    return abs(a - b) < tolerance


def maxOrDefined(a: float, b: float) -> float:
    if isUndefined(a):
        return b
    if isUndefined(b):
        return a
    return max(a, b)


def minOrDefined(a: float, b: float) -> float:
    if isUndefined(a):
        return b
    if isUndefined(b):
        return a
    return min(a, b)
