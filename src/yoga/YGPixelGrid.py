"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

import math


def YGRoundValueToPixelGrid(
    value: float, pointScaleFactor: float, forceCeil: bool, forceFloor: bool
) -> float:
    if pointScaleFactor == 0:
        return value
    scaledValue = value * pointScaleFactor
    fractial = math.fmod(scaledValue, 1.0)
    if fractial < 0:
        fractial += 1.0
    if math.isclose(fractial, 0.0, abs_tol=1e-4):
        scaledValue = scaledValue - fractial
    elif math.isclose(fractial, 1.0, abs_tol=1e-4):
        scaledValue = scaledValue - fractial + 1.0
    elif forceCeil:
        scaledValue = scaledValue - fractial + 1.0
    elif forceFloor:
        scaledValue = scaledValue - fractial
    else:
        scaledValue = scaledValue - fractial + (
            1.0
            if not math.isnan(fractial)
            and (fractial > 0.5 or math.isclose(fractial, 0.5, abs_tol=1e-4))
            else 0.0
        )
    return float("nan") if math.isnan(scaledValue) or math.isnan(pointScaleFactor) else scaledValue / pointScaleFactor
