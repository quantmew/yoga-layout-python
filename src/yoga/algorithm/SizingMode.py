"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from enum import Enum

from ..debug.AssertFatal import fatalWithMessage
from ..YGEnums import YGMeasureMode


class SizingMode(Enum):
    StretchFit = 0
    MaxContent = 1
    FitContent = 2


def measureMode(mode: SizingMode) -> YGMeasureMode:
    if mode == SizingMode.StretchFit:
        return YGMeasureMode.YGMeasureModeExactly
    if mode == SizingMode.MaxContent:
        return YGMeasureMode.YGMeasureModeUndefined
    if mode == SizingMode.FitContent:
        return YGMeasureMode.YGMeasureModeAtMost
    fatalWithMessage("Invalid SizingMode")


def sizingMode(mode: YGMeasureMode) -> SizingMode:
    if mode == YGMeasureMode.YGMeasureModeExactly:
        return SizingMode.StretchFit
    if mode == YGMeasureMode.YGMeasureModeUndefined:
        return SizingMode.MaxContent
    if mode == YGMeasureMode.YGMeasureModeAtMost:
        return SizingMode.FitContent
    fatalWithMessage("Invalid MeasureMode")
