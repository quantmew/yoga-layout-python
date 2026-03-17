"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from struct import pack, unpack


def float32(value: float) -> float:
    return unpack("!f", pack("!f", float(value)))[0]


def floatDivision(numerator: float, denominator: float) -> float:
    if denominator != 0:
        return numerator / denominator
    if numerator > 0:
        return float("inf")
    if numerator < 0:
        return float("-inf")
    return float("nan")
