"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum


class GridLineType(IntEnum):
    Auto = 0
    Integer = 1
    Span = 2


@dataclass(frozen=True)
class GridLine:
    type: GridLineType = GridLineType.Auto
    integer: int = 0

    @staticmethod
    def auto_() -> GridLine:
        return GridLine(GridLineType.Auto, 0)

    @staticmethod
    def fromInteger(value: int) -> GridLine:
        return GridLine(GridLineType.Integer, value)

    @staticmethod
    def span(value: int) -> GridLine:
        return GridLine(GridLineType.Span, value)

    def isAuto(self) -> bool:
        return self.type == GridLineType.Auto

    def isInteger(self) -> bool:
        return self.type == GridLineType.Integer

    def isSpan(self) -> bool:
        return self.type == GridLineType.Span
