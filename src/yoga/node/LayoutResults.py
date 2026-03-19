"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from ..numeric.Comparison import inexactEquals, isUndefined
from ..numeric.FloatMath import float32
from ..numeric.FloatOptional import FloatOptional
from ..YGEnums import YGDimension, YGDirection, YGEdge
from .CachedMeasurement import CachedMeasurement


@dataclass
class LayoutResults:
    MaxCachedMeasurements = 8

    computedFlexBasisGeneration: int = 0
    computedFlexBasis: FloatOptional = field(default_factory=FloatOptional)
    generationCount: int = 0
    configVersion: int = 0
    lastOwnerDirection: YGDirection = YGDirection.YGDirectionInherit
    nextCachedMeasurementsIndex: int = 0
    cachedMeasurements: list[CachedMeasurement] = field(
        default_factory=lambda: [CachedMeasurement() for _ in range(LayoutResults.MaxCachedMeasurements)]
    )
    cachedLayout: CachedMeasurement = field(default_factory=CachedMeasurement)
    direction_: YGDirection = YGDirection.YGDirectionInherit
    hadOverflow_: bool = False
    dimensions_: dict[YGDimension, float] = field(
        default_factory=lambda: {
            YGDimension.YGDimensionWidth: float("nan"),
            YGDimension.YGDimensionHeight: float("nan"),
        }
    )
    measuredDimensions_: dict[YGDimension, float] = field(
        default_factory=lambda: {
            YGDimension.YGDimensionWidth: float("nan"),
            YGDimension.YGDimensionHeight: float("nan"),
        }
    )
    rawDimensions_: dict[YGDimension, float] = field(
        default_factory=lambda: {
            YGDimension.YGDimensionWidth: float("nan"),
            YGDimension.YGDimensionHeight: float("nan"),
        }
    )
    position_: dict[YGEdge, float] = field(
        default_factory=lambda: {
            YGEdge.YGEdgeLeft: 0.0,
            YGEdge.YGEdgeTop: 0.0,
            YGEdge.YGEdgeRight: 0.0,
            YGEdge.YGEdgeBottom: 0.0,
        }
    )
    margin_: dict[YGEdge, float] = field(
        default_factory=lambda: {
            YGEdge.YGEdgeLeft: 0.0,
            YGEdge.YGEdgeTop: 0.0,
            YGEdge.YGEdgeRight: 0.0,
            YGEdge.YGEdgeBottom: 0.0,
        }
    )
    border_: dict[YGEdge, float] = field(
        default_factory=lambda: {
            YGEdge.YGEdgeLeft: 0.0,
            YGEdge.YGEdgeTop: 0.0,
            YGEdge.YGEdgeRight: 0.0,
            YGEdge.YGEdgeBottom: 0.0,
        }
    )
    padding_: dict[YGEdge, float] = field(
        default_factory=lambda: {
            YGEdge.YGEdgeLeft: 0.0,
            YGEdge.YGEdgeTop: 0.0,
            YGEdge.YGEdgeRight: 0.0,
            YGEdge.YGEdgeBottom: 0.0,
        }
    )

    def direction(self) -> YGDirection:
        return self.direction_

    def setDirection(self, direction: YGDirection) -> None:
        self.direction_ = direction

    def hadOverflow(self) -> bool:
        return self.hadOverflow_

    def setHadOverflow(self, hadOverflow: bool) -> None:
        self.hadOverflow_ = hadOverflow

    def dimension(self, axis: YGDimension) -> float:
        return self.dimensions_[axis]

    def setDimension(self, axis: YGDimension, dimension: float) -> None:
        self.dimensions_[axis] = float32(dimension)

    def measuredDimension(self, axis: YGDimension) -> float:
        return self.measuredDimensions_[axis]

    def rawDimension(self, axis: YGDimension) -> float:
        return self.rawDimensions_[axis]

    def setMeasuredDimension(self, axis: YGDimension, dimension: float) -> None:
        self.measuredDimensions_[axis] = float32(dimension)

    def setRawDimension(self, axis: YGDimension, dimension: float) -> None:
        self.rawDimensions_[axis] = float32(dimension)

    def position(self, edge: YGEdge) -> float:
        return self.position_[edge]

    def setPosition(self, edge: YGEdge, dimension: float) -> None:
        self.position_[edge] = float32(dimension)

    def margin(self, edge: YGEdge) -> float:
        return self.margin_[edge]

    def setMargin(self, edge: YGEdge, dimension: float) -> None:
        self.margin_[edge] = float32(dimension)

    def border(self, edge: YGEdge) -> float:
        return self.border_[edge]

    def setBorder(self, edge: YGEdge, dimension: float) -> None:
        self.border_[edge] = float32(dimension)

    def padding(self, edge: YGEdge) -> float:
        return self.padding_[edge]

    def setPadding(self, edge: YGEdge, dimension: float) -> None:
        self.padding_[edge] = float32(dimension)

    def __eq__(self, layout: object) -> bool:
        if not isinstance(layout, LayoutResults):
            return NotImplemented

        isEqual = (
            inexactEquals(
                self.position_[YGEdge.YGEdgeLeft], layout.position_[YGEdge.YGEdgeLeft]
            )
            and inexactEquals(
                self.position_[YGEdge.YGEdgeTop], layout.position_[YGEdge.YGEdgeTop]
            )
            and inexactEquals(
                self.position_[YGEdge.YGEdgeRight], layout.position_[YGEdge.YGEdgeRight]
            )
            and inexactEquals(
                self.position_[YGEdge.YGEdgeBottom], layout.position_[YGEdge.YGEdgeBottom]
            )
            and inexactEquals(
                self.dimensions_[YGDimension.YGDimensionWidth],
                layout.dimensions_[YGDimension.YGDimensionWidth],
            )
            and inexactEquals(
                self.dimensions_[YGDimension.YGDimensionHeight],
                layout.dimensions_[YGDimension.YGDimensionHeight],
            )
            and inexactEquals(
                self.margin_[YGEdge.YGEdgeLeft], layout.margin_[YGEdge.YGEdgeLeft]
            )
            and inexactEquals(
                self.margin_[YGEdge.YGEdgeTop], layout.margin_[YGEdge.YGEdgeTop]
            )
            and inexactEquals(
                self.margin_[YGEdge.YGEdgeRight], layout.margin_[YGEdge.YGEdgeRight]
            )
            and inexactEquals(
                self.margin_[YGEdge.YGEdgeBottom], layout.margin_[YGEdge.YGEdgeBottom]
            )
            and inexactEquals(
                self.border_[YGEdge.YGEdgeLeft], layout.border_[YGEdge.YGEdgeLeft]
            )
            and inexactEquals(
                self.border_[YGEdge.YGEdgeTop], layout.border_[YGEdge.YGEdgeTop]
            )
            and inexactEquals(
                self.border_[YGEdge.YGEdgeRight], layout.border_[YGEdge.YGEdgeRight]
            )
            and inexactEquals(
                self.border_[YGEdge.YGEdgeBottom], layout.border_[YGEdge.YGEdgeBottom]
            )
            and inexactEquals(
                self.padding_[YGEdge.YGEdgeLeft], layout.padding_[YGEdge.YGEdgeLeft]
            )
            and inexactEquals(
                self.padding_[YGEdge.YGEdgeTop], layout.padding_[YGEdge.YGEdgeTop]
            )
            and inexactEquals(
                self.padding_[YGEdge.YGEdgeRight], layout.padding_[YGEdge.YGEdgeRight]
            )
            and inexactEquals(
                self.padding_[YGEdge.YGEdgeBottom], layout.padding_[YGEdge.YGEdgeBottom]
            )
            and self.direction() == layout.direction()
            and self.hadOverflow() == layout.hadOverflow()
            and self.lastOwnerDirection == layout.lastOwnerDirection
            and self.configVersion == layout.configVersion
            and self.nextCachedMeasurementsIndex == layout.nextCachedMeasurementsIndex
            and self.cachedLayout == layout.cachedLayout
            and self.computedFlexBasis == layout.computedFlexBasis
        )

        for i in range(LayoutResults.MaxCachedMeasurements):
            if not isEqual:
                break
            isEqual = self.cachedMeasurements[i] == layout.cachedMeasurements[i]

        measuredWidth = self.measuredDimensions_[YGDimension.YGDimensionWidth]
        layoutMeasuredWidth = layout.measuredDimensions_[YGDimension.YGDimensionWidth]
        if not isUndefined(measuredWidth) or not isUndefined(layoutMeasuredWidth):
            isEqual = isEqual and measuredWidth == layoutMeasuredWidth

        measuredHeight = self.measuredDimensions_[YGDimension.YGDimensionHeight]
        layoutMeasuredHeight = layout.measuredDimensions_[YGDimension.YGDimensionHeight]
        if not isUndefined(measuredHeight) or not isUndefined(layoutMeasuredHeight):
            isEqual = isEqual and measuredHeight == layoutMeasuredHeight

        return isEqual
