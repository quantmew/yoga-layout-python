"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from ..algorithm.SizingMode import SizingMode
from ..numeric.Comparison import inexactEquals, isDefined
from ..YGPixelGrid import YGRoundValueToPixelGrid


def sizeIsExactAndMatchesOldMeasuredSize(sizeMode: SizingMode, size: float, lastComputedSize: float) -> bool:
    return sizeMode == SizingMode.StretchFit and inexactEquals(size, lastComputedSize)


def oldSizeIsMaxContentAndStillFits(
    sizeMode: SizingMode,
    size: float,
    lastSizeMode: SizingMode,
    lastComputedSize: float,
) -> bool:
    return sizeMode == SizingMode.FitContent and lastSizeMode == SizingMode.MaxContent and (
        size >= lastComputedSize or inexactEquals(size, lastComputedSize)
    )


def newSizeIsStricterAndStillValid(
    sizeMode: SizingMode,
    size: float,
    lastSizeMode: SizingMode,
    lastSize: float,
    lastComputedSize: float,
) -> bool:
    return (
        lastSizeMode == SizingMode.FitContent
        and sizeMode == SizingMode.FitContent
        and isDefined(lastSize)
        and isDefined(size)
        and isDefined(lastComputedSize)
        and lastSize > size
        and (lastComputedSize <= size or inexactEquals(size, lastComputedSize))
    )


def canUseCachedMeasurement(
    widthMode: SizingMode,
    availableWidth: float,
    heightMode: SizingMode,
    availableHeight: float,
    lastWidthMode: SizingMode,
    lastAvailableWidth: float,
    lastHeightMode: SizingMode,
    lastAvailableHeight: float,
    lastComputedWidth: float,
    lastComputedHeight: float,
    marginRow: float,
    marginColumn: float,
    config,
) -> bool:
    if (isDefined(lastComputedHeight) and lastComputedHeight < 0) or (isDefined(lastComputedWidth) and lastComputedWidth < 0):
        return False

    pointScaleFactor = config.getPointScaleFactor() if config is not None else 0.0
    useRoundedComparison = config is not None and pointScaleFactor != 0
    effectiveWidth = YGRoundValueToPixelGrid(availableWidth, pointScaleFactor, False, False) if useRoundedComparison else availableWidth
    effectiveHeight = YGRoundValueToPixelGrid(availableHeight, pointScaleFactor, False, False) if useRoundedComparison else availableHeight
    effectiveLastWidth = YGRoundValueToPixelGrid(lastAvailableWidth, pointScaleFactor, False, False) if useRoundedComparison else lastAvailableWidth
    effectiveLastHeight = YGRoundValueToPixelGrid(lastAvailableHeight, pointScaleFactor, False, False) if useRoundedComparison else lastAvailableHeight

    hasSameWidthSpec = lastWidthMode == widthMode and inexactEquals(effectiveLastWidth, effectiveWidth)
    hasSameHeightSpec = lastHeightMode == heightMode and inexactEquals(effectiveLastHeight, effectiveHeight)

    widthIsCompatible = hasSameWidthSpec or sizeIsExactAndMatchesOldMeasuredSize(
        widthMode, availableWidth - marginRow, lastComputedWidth
    ) or oldSizeIsMaxContentAndStillFits(
        widthMode, availableWidth - marginRow, lastWidthMode, lastComputedWidth
    ) or newSizeIsStricterAndStillValid(
        widthMode, availableWidth - marginRow, lastWidthMode, lastAvailableWidth, lastComputedWidth
    )

    heightIsCompatible = hasSameHeightSpec or sizeIsExactAndMatchesOldMeasuredSize(
        heightMode, availableHeight - marginColumn, lastComputedHeight
    ) or oldSizeIsMaxContentAndStillFits(
        heightMode, availableHeight - marginColumn, lastHeightMode, lastComputedHeight
    ) or newSizeIsStricterAndStillValid(
        heightMode, availableHeight - marginColumn, lastHeightMode, lastAvailableHeight, lastComputedHeight
    )

    return widthIsCompatible and heightIsCompatible

