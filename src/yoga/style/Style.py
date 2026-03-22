"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .._cython_compat import cython

from ..algorithm.FlexDirection import (
    flexEndEdge,
    flexStartEdge,
    inlineEndEdge,
    inlineStartEdge,
    isRow,
)
from ..debug.AssertFatal import fatalWithMessage
from ..numeric.Comparison import maxOrDefined as maxOrDefinedFloat
from ..numeric.FloatMath import float32
from ..numeric.FloatOptional import FloatOptional
from ..YGEnums import (
    YGAlign,
    YGBoxSizing,
    YGDimension,
    YGDirection,
    YGDisplay,
    YGEdge,
    YGFlexDirection,
    YGGutter,
    YGJustify,
    YGOverflow,
    YGPositionType,
    YGWrap,
)
from .GridLine import GridLine
from .GridTrack import GridTrackList, GridTrackSize
from .StyleLength import StyleLength
from .StyleSizeLength import StyleSizeLength
from .StyleValueHandle import StyleValueHandle
from .StyleValuePool import StyleValuePool


def _normalize_float_optional(value: FloatOptional) -> FloatOptional:
    return FloatOptional() if value.isUndefined() else FloatOptional(float32(value.unwrap()))


def _normalize_style_length(value: StyleLength) -> StyleLength:
    if value.isUndefined():
        return StyleLength.undefined()
    if value.isAuto():
        return StyleLength.ofAuto()
    normalized_value = float32(value.value().unwrap())
    return StyleLength.points(normalized_value) if value.isPoints() else StyleLength.percent(normalized_value)


def _normalize_style_size_length(value: StyleSizeLength) -> StyleSizeLength:
    if value.isUndefined():
        return StyleSizeLength.undefined()
    if value.isAuto():
        return StyleSizeLength.ofAuto()
    if value.isMaxContent():
        return StyleSizeLength.ofMaxContent()
    if value.isFitContent():
        return StyleSizeLength.ofFitContent()
    if value.isStretch():
        stretch_value = value.value()
        return (
            StyleSizeLength.ofStretch()
            if stretch_value.isUndefined()
            else StyleSizeLength.stretch(float32(stretch_value.unwrap()))
        )
    value_unwrapped: float = value.value().unwrap()  # type: ignore[arg-type]
    normalized_value: float = float32(value_unwrapped)  # type: ignore[assignment]
    return (
        StyleSizeLength.points(normalized_value)
        if value.isPoints()
        else StyleSizeLength.percent(normalized_value)
    )


def normalize_style_value(value):
    if isinstance(value, FloatOptional):
        return _normalize_float_optional(value)
    if isinstance(value, StyleLength):
        return _normalize_style_length(value)
    if isinstance(value, StyleSizeLength):
        return _normalize_style_size_length(value)
    return value


def _new_handles(count: int) -> list[StyleValueHandle]:
    return [StyleValueHandle() for _ in range(count)]


def _new_auto_dimensions() -> list[StyleValueHandle]:
    return [StyleValueHandle.ofAuto() for _ in YGDimension]


def _numbers_equal(
    lhs_handle: StyleValueHandle,
    lhs_pool: StyleValuePool,
    rhs_handle: StyleValueHandle,
    rhs_pool: StyleValuePool,
) -> bool:
    return (lhs_handle.isUndefined() and rhs_handle.isUndefined()) or (
        lhs_pool.get_number(lhs_handle) == rhs_pool.get_number(rhs_handle)
    )


def _length_handles_equal(
    lhs_handle: StyleValueHandle,
    lhs_pool: StyleValuePool,
    rhs_handle: StyleValueHandle,
    rhs_pool: StyleValuePool,
) -> bool:
    return (lhs_handle.isUndefined() and rhs_handle.isUndefined()) or (
        lhs_pool.get_length(lhs_handle) == rhs_pool.get_length(rhs_handle)
    )


def _size_handles_equal(
    lhs_handle: StyleValueHandle,
    lhs_pool: StyleValuePool,
    rhs_handle: StyleValueHandle,
    rhs_pool: StyleValuePool,
) -> bool:
    return (lhs_handle.isUndefined() and rhs_handle.isUndefined()) or (
        lhs_pool.get_size(lhs_handle) == rhs_pool.get_size(rhs_handle)
    )


def _handle_arrays_equal(lhs: list[StyleValueHandle], rhs: list[StyleValueHandle], comparator) -> bool:
    return len(lhs) == len(rhs) and all(comparator(lhs_item, rhs_item) for lhs_item, rhs_item in zip(lhs, rhs))


@dataclass(eq=False)
class Style:
    Length = StyleLength
    SizeLength = StyleSizeLength

    DefaultFlexGrow = 0.0
    DefaultFlexShrink = 0.0
    WebDefaultFlexShrink = 1.0

    direction_: YGDirection = YGDirection.YGDirectionInherit
    flexDirection_: YGFlexDirection = YGFlexDirection.YGFlexDirectionColumn
    justifyContent_: YGJustify = YGJustify.YGJustifyFlexStart
    justifyItems_: YGJustify = YGJustify.YGJustifyStretch
    justifySelf_: YGJustify = YGJustify.YGJustifyAuto
    alignContent_: YGAlign = YGAlign.YGAlignFlexStart
    alignItems_: YGAlign = YGAlign.YGAlignStretch
    alignSelf_: YGAlign = YGAlign.YGAlignAuto
    positionType_: YGPositionType = YGPositionType.YGPositionTypeRelative
    flexWrap_: YGWrap = YGWrap.YGWrapNoWrap
    overflow_: YGOverflow = YGOverflow.YGOverflowVisible
    display_: YGDisplay = YGDisplay.YGDisplayFlex
    boxSizing_: YGBoxSizing = YGBoxSizing.YGBoxSizingBorderBox
    flex_: StyleValueHandle = field(default_factory=StyleValueHandle)
    flexGrow_: StyleValueHandle = field(default_factory=StyleValueHandle)
    flexShrink_: StyleValueHandle = field(default_factory=StyleValueHandle)
    flexBasis_: StyleValueHandle = field(default_factory=StyleValueHandle.ofAuto)
    margin_: list[StyleValueHandle] = field(default_factory=lambda: _new_handles(len(YGEdge)))
    position_: list[StyleValueHandle] = field(default_factory=lambda: _new_handles(len(YGEdge)))
    padding_: list[StyleValueHandle] = field(default_factory=lambda: _new_handles(len(YGEdge)))
    border_: list[StyleValueHandle] = field(default_factory=lambda: _new_handles(len(YGEdge)))
    gap_: list[StyleValueHandle] = field(default_factory=lambda: _new_handles(len(YGGutter)))
    dimensions_: list[StyleValueHandle] = field(default_factory=_new_auto_dimensions)
    minDimensions_: list[StyleValueHandle] = field(default_factory=lambda: _new_handles(len(YGDimension)))
    maxDimensions_: list[StyleValueHandle] = field(default_factory=lambda: _new_handles(len(YGDimension)))
    aspectRatio_: StyleValueHandle = field(default_factory=StyleValueHandle)
    gridTemplateColumns_: GridTrackList = field(default_factory=list)
    gridTemplateRows_: GridTrackList = field(default_factory=list)
    gridAutoColumns_: GridTrackList = field(default_factory=list)
    gridAutoRows_: GridTrackList = field(default_factory=list)
    gridColumnStart_: GridLine = field(default_factory=GridLine.auto_)
    gridColumnEnd_: GridLine = field(default_factory=GridLine.auto_)
    gridRowStart_: GridLine = field(default_factory=GridLine.auto_)
    gridRowEnd_: GridLine = field(default_factory=GridLine.auto_)
    pool_: StyleValuePool = field(default_factory=StyleValuePool)

    def direction(self) -> YGDirection:
        return self.direction_

    def setDirection(self, value: YGDirection) -> None:
        self.direction_ = value

    def flexDirection(self) -> YGFlexDirection:
        return self.flexDirection_

    def setFlexDirection(self, value: YGFlexDirection) -> None:
        self.flexDirection_ = value

    def justifyContent(self) -> YGJustify:
        return self.justifyContent_

    def setJustifyContent(self, value: YGJustify) -> None:
        self.justifyContent_ = value

    def justifyItems(self) -> YGJustify:
        return self.justifyItems_

    def setJustifyItems(self, value: YGJustify) -> None:
        self.justifyItems_ = value

    def justifySelf(self) -> YGJustify:
        return self.justifySelf_

    def setJustifySelf(self, value: YGJustify) -> None:
        self.justifySelf_ = value

    def alignContent(self) -> YGAlign:
        return self.alignContent_

    def setAlignContent(self, value: YGAlign) -> None:
        self.alignContent_ = value

    def alignItems(self) -> YGAlign:
        return self.alignItems_

    def setAlignItems(self, value: YGAlign) -> None:
        self.alignItems_ = value

    def alignSelf(self) -> YGAlign:
        return self.alignSelf_

    def setAlignSelf(self, value: YGAlign) -> None:
        self.alignSelf_ = value

    def positionType(self) -> YGPositionType:
        return self.positionType_

    def setPositionType(self, value: YGPositionType) -> None:
        self.positionType_ = value

    def flexWrap(self) -> YGWrap:
        return self.flexWrap_

    def setFlexWrap(self, value: YGWrap) -> None:
        self.flexWrap_ = value

    def overflow(self) -> YGOverflow:
        return self.overflow_

    def setOverflow(self, value: YGOverflow) -> None:
        self.overflow_ = value

    def display(self) -> YGDisplay:
        return self.display_

    def setDisplay(self, value: YGDisplay) -> None:
        self.display_ = value

    def flex(self) -> FloatOptional:
        return self.pool_.get_number(self.flex_)

    def setFlex(self, value: FloatOptional) -> None:
        self.pool_.store_number(self.flex_, _normalize_float_optional(value))

    def flexGrow(self) -> FloatOptional:
        return self.pool_.get_number(self.flexGrow_)

    def setFlexGrow(self, value: FloatOptional) -> None:
        self.pool_.store_number(self.flexGrow_, _normalize_float_optional(value))

    def flexShrink(self) -> FloatOptional:
        return self.pool_.get_number(self.flexShrink_)

    def setFlexShrink(self, value: FloatOptional) -> None:
        self.pool_.store_number(self.flexShrink_, _normalize_float_optional(value))

    def flexBasis(self) -> StyleSizeLength:
        return self.pool_.get_size(self.flexBasis_)

    def setFlexBasis(self, value: StyleSizeLength) -> None:
        self.pool_.store_size(self.flexBasis_, _normalize_style_size_length(value))

    def margin(self, edge: YGEdge) -> StyleLength:
        return self.pool_.get_length(self.margin_[edge])

    def setMargin(self, edge: YGEdge, value: StyleLength) -> None:
        self.pool_.store_length(self.margin_[edge], _normalize_style_length(value))

    def position(self, edge: YGEdge) -> StyleLength:
        return self.pool_.get_length(self.position_[edge])

    def setPosition(self, edge: YGEdge, value: StyleLength) -> None:
        self.pool_.store_length(self.position_[edge], _normalize_style_length(value))

    def padding(self, edge: YGEdge) -> StyleLength:
        return self.pool_.get_length(self.padding_[edge])

    def setPadding(self, edge: YGEdge, value: StyleLength) -> None:
        self.pool_.store_length(self.padding_[edge], _normalize_style_length(value))

    def border(self, edge: YGEdge) -> StyleLength:
        return self.pool_.get_length(self.border_[edge])

    def setBorder(self, edge: YGEdge, value: StyleLength) -> None:
        self.pool_.store_length(self.border_[edge], _normalize_style_length(value))

    def gap(self, gutter: YGGutter) -> StyleLength:
        return self.pool_.get_length(self.gap_[gutter])

    def setGap(self, gutter: YGGutter, value: StyleLength) -> None:
        self.pool_.store_length(self.gap_[gutter], _normalize_style_length(value))

    def dimension(self, axis: YGDimension) -> StyleSizeLength:
        return self.pool_.get_size(self.dimensions_[axis])

    def setDimension(self, axis: YGDimension, value: StyleSizeLength) -> None:
        self.pool_.store_size(self.dimensions_[axis], _normalize_style_size_length(value))

    def minDimension(self, axis: YGDimension) -> StyleSizeLength:
        return self.pool_.get_size(self.minDimensions_[axis])

    def setMinDimension(self, axis: YGDimension, value: StyleSizeLength) -> None:
        self.pool_.store_size(self.minDimensions_[axis], _normalize_style_size_length(value))

    def gridTemplateColumns(self) -> GridTrackList:
        return self.gridTemplateColumns_

    def setGridTemplateColumns(self, value: GridTrackList) -> None:
        self.gridTemplateColumns_ = list(value)

    def resizeGridTemplateColumns(self, count: int) -> None:
        if count < len(self.gridTemplateColumns_):
            del self.gridTemplateColumns_[count:]
        else:
            self.gridTemplateColumns_.extend(GridTrackSize.auto_() for _ in range(count - len(self.gridTemplateColumns_)))

    def setGridTemplateColumnAt(self, index: int, value: GridTrackSize) -> None:
        self.gridTemplateColumns_[index] = value

    def gridTemplateRows(self) -> GridTrackList:
        return self.gridTemplateRows_

    def setGridTemplateRows(self, value: GridTrackList) -> None:
        self.gridTemplateRows_ = list(value)

    def resizeGridTemplateRows(self, count: int) -> None:
        if count < len(self.gridTemplateRows_):
            del self.gridTemplateRows_[count:]
        else:
            self.gridTemplateRows_.extend(GridTrackSize.auto_() for _ in range(count - len(self.gridTemplateRows_)))

    def setGridTemplateRowAt(self, index: int, value: GridTrackSize) -> None:
        self.gridTemplateRows_[index] = value

    def gridAutoColumns(self) -> GridTrackList:
        return self.gridAutoColumns_

    def setGridAutoColumns(self, value: GridTrackList) -> None:
        self.gridAutoColumns_ = list(value)

    def resizeGridAutoColumns(self, count: int) -> None:
        if count < len(self.gridAutoColumns_):
            del self.gridAutoColumns_[count:]
        else:
            self.gridAutoColumns_.extend(GridTrackSize.auto_() for _ in range(count - len(self.gridAutoColumns_)))

    def setGridAutoColumnAt(self, index: int, value: GridTrackSize) -> None:
        self.gridAutoColumns_[index] = value

    def gridAutoRows(self) -> GridTrackList:
        return self.gridAutoRows_

    def setGridAutoRows(self, value: GridTrackList) -> None:
        self.gridAutoRows_ = list(value)

    def resizeGridAutoRows(self, count: int) -> None:
        if count < len(self.gridAutoRows_):
            del self.gridAutoRows_[count:]
        else:
            self.gridAutoRows_.extend(GridTrackSize.auto_() for _ in range(count - len(self.gridAutoRows_)))

    def setGridAutoRowAt(self, index: int, value: GridTrackSize) -> None:
        self.gridAutoRows_[index] = value

    def gridColumnStart(self) -> GridLine:
        return self.gridColumnStart_

    def setGridColumnStart(self, value: GridLine) -> None:
        self.gridColumnStart_ = value

    def gridColumnEnd(self) -> GridLine:
        return self.gridColumnEnd_

    def setGridColumnEnd(self, value: GridLine) -> None:
        self.gridColumnEnd_ = value

    def gridRowStart(self) -> GridLine:
        return self.gridRowStart_

    def setGridRowStart(self, value: GridLine) -> None:
        self.gridRowStart_ = value

    def gridRowEnd(self) -> GridLine:
        return self.gridRowEnd_

    def setGridRowEnd(self, value: GridLine) -> None:
        self.gridRowEnd_ = value

    def maxDimension(self, axis: YGDimension) -> StyleSizeLength:
        return self.pool_.get_size(self.maxDimensions_[axis])

    def setMaxDimension(self, axis: YGDimension, value: StyleSizeLength) -> None:
        self.pool_.store_size(self.maxDimensions_[axis], _normalize_style_size_length(value))

    def aspectRatio(self) -> FloatOptional:
        return self.pool_.get_number(self.aspectRatio_)

    def setAspectRatio(self, value: FloatOptional) -> None:
        normalized_value = _normalize_float_optional(value)
        unwrapped = normalized_value.unwrap()
        self.pool_.store_number(
            self.aspectRatio_,
            FloatOptional()
            if normalized_value == 0.0 or unwrapped == float("inf") or unwrapped == float("-inf")
            else normalized_value,
        )

    def boxSizing(self) -> YGBoxSizing:
        return self.boxSizing_

    def setBoxSizing(self, value: YGBoxSizing) -> None:
        self.boxSizing_ = value

    @cython.locals(dimensionPaddingAndBorderValue=cython.double)
    def resolvedMinDimension(
        self, direction: YGDirection, axis: YGDimension, referenceLength: float, ownerWidth: float
    ) -> FloatOptional:
        value = self.minDimension(axis).resolve(referenceLength)
        if self.boxSizing() == YGBoxSizing.YGBoxSizingBorderBox:
            return value

        dimensionPaddingAndBorderValue = self.computePaddingAndBorderForDimension(direction, axis, ownerWidth)
        dimensionPaddingAndBorder = FloatOptional(dimensionPaddingAndBorderValue)
        return value + (
            dimensionPaddingAndBorder if dimensionPaddingAndBorder.isDefined() else FloatOptional(0.0)
        )

    @cython.locals(dimensionPaddingAndBorderValue=cython.double)
    def resolvedMaxDimension(
        self, direction: YGDirection, axis: YGDimension, referenceLength: float, ownerWidth: float
    ) -> FloatOptional:
        value = self.maxDimension(axis).resolve(referenceLength)
        if self.boxSizing() == YGBoxSizing.YGBoxSizingBorderBox:
            return value

        dimensionPaddingAndBorderValue = self.computePaddingAndBorderForDimension(direction, axis, ownerWidth)
        dimensionPaddingAndBorder = FloatOptional(dimensionPaddingAndBorderValue)
        return value + (
            dimensionPaddingAndBorder if dimensionPaddingAndBorder.isDefined() else FloatOptional(0.0)
        )

    def horizontalInsetsDefined(self) -> bool:
        return (
            self.position_[YGEdge.YGEdgeLeft].isDefined()
            or self.position_[YGEdge.YGEdgeRight].isDefined()
            or self.position_[YGEdge.YGEdgeAll].isDefined()
            or self.position_[YGEdge.YGEdgeHorizontal].isDefined()
            or self.position_[YGEdge.YGEdgeStart].isDefined()
            or self.position_[YGEdge.YGEdgeEnd].isDefined()
        )

    def verticalInsetsDefined(self) -> bool:
        return (
            self.position_[YGEdge.YGEdgeTop].isDefined()
            or self.position_[YGEdge.YGEdgeBottom].isDefined()
            or self.position_[YGEdge.YGEdgeAll].isDefined()
            or self.position_[YGEdge.YGEdgeVertical].isDefined()
        )

    def isFlexStartPositionDefined(self, axis: YGFlexDirection, direction: YGDirection) -> bool:
        return self.computePosition(flexStartEdge(axis), direction).isDefined()

    def isFlexStartPositionAuto(self, axis: YGFlexDirection, direction: YGDirection) -> bool:
        return self.computePosition(flexStartEdge(axis), direction).isAuto()

    def isInlineStartPositionDefined(self, axis: YGFlexDirection, direction: YGDirection) -> bool:
        return self.computePosition(inlineStartEdge(axis, direction), direction).isDefined()

    def isInlineStartPositionAuto(self, axis: YGFlexDirection, direction: YGDirection) -> bool:
        return self.computePosition(inlineStartEdge(axis, direction), direction).isAuto()

    def isFlexEndPositionDefined(self, axis: YGFlexDirection, direction: YGDirection) -> bool:
        return self.computePosition(flexEndEdge(axis), direction).isDefined()

    def isFlexEndPositionAuto(self, axis: YGFlexDirection, direction: YGDirection) -> bool:
        return self.computePosition(flexEndEdge(axis), direction).isAuto()

    def isInlineEndPositionDefined(self, axis: YGFlexDirection, direction: YGDirection) -> bool:
        return self.computePosition(inlineEndEdge(axis, direction), direction).isDefined()

    def isInlineEndPositionAuto(self, axis: YGFlexDirection, direction: YGDirection) -> bool:
        return self.computePosition(inlineEndEdge(axis, direction), direction).isAuto()

    def computeFlexStartPosition(self, axis: YGFlexDirection, direction: YGDirection, axisSize: float) -> float:
        return self.computePosition(flexStartEdge(axis), direction).resolve(axisSize).unwrapOrDefault(0.0)

    def computeInlineStartPosition(self, axis: YGFlexDirection, direction: YGDirection, axisSize: float) -> float:
        return self.computePosition(inlineStartEdge(axis, direction), direction).resolve(axisSize).unwrapOrDefault(0.0)

    def computeFlexEndPosition(self, axis: YGFlexDirection, direction: YGDirection, axisSize: float) -> float:
        return self.computePosition(flexEndEdge(axis), direction).resolve(axisSize).unwrapOrDefault(0.0)

    def computeInlineEndPosition(self, axis: YGFlexDirection, direction: YGDirection, axisSize: float) -> float:
        return self.computePosition(inlineEndEdge(axis, direction), direction).resolve(axisSize).unwrapOrDefault(0.0)

    def computeFlexStartMargin(self, axis: YGFlexDirection, direction: YGDirection, widthSize: float) -> float:
        return self.computeMargin(flexStartEdge(axis), direction).resolve(widthSize).unwrapOrDefault(0.0)

    def computeInlineStartMargin(self, axis: YGFlexDirection, direction: YGDirection, widthSize: float) -> float:
        return self.computeMargin(inlineStartEdge(axis, direction), direction).resolve(widthSize).unwrapOrDefault(0.0)

    def computeFlexEndMargin(self, axis: YGFlexDirection, direction: YGDirection, widthSize: float) -> float:
        return self.computeMargin(flexEndEdge(axis), direction).resolve(widthSize).unwrapOrDefault(0.0)

    def computeInlineEndMargin(self, axis: YGFlexDirection, direction: YGDirection, widthSize: float) -> float:
        return self.computeMargin(inlineEndEdge(axis, direction), direction).resolve(widthSize).unwrapOrDefault(0.0)

    def computeFlexStartBorder(self, axis: YGFlexDirection, direction: YGDirection) -> float:
        return maxOrDefinedFloat(self.computeBorder(flexStartEdge(axis), direction).resolve(0.0).unwrap(), 0.0)

    def computeInlineStartBorder(self, axis: YGFlexDirection, direction: YGDirection) -> float:
        return maxOrDefinedFloat(self.computeBorder(inlineStartEdge(axis, direction), direction).resolve(0.0).unwrap(), 0.0)

    def computeFlexEndBorder(self, axis: YGFlexDirection, direction: YGDirection) -> float:
        return maxOrDefinedFloat(self.computeBorder(flexEndEdge(axis), direction).resolve(0.0).unwrap(), 0.0)

    def computeInlineEndBorder(self, axis: YGFlexDirection, direction: YGDirection) -> float:
        return maxOrDefinedFloat(self.computeBorder(inlineEndEdge(axis, direction), direction).resolve(0.0).unwrap(), 0.0)

    def computeFlexStartPadding(self, axis: YGFlexDirection, direction: YGDirection, widthSize: float) -> float:
        return maxOrDefinedFloat(self.computePadding(flexStartEdge(axis), direction).resolve(widthSize).unwrap(), 0.0)

    def computeInlineStartPadding(self, axis: YGFlexDirection, direction: YGDirection, widthSize: float) -> float:
        return maxOrDefinedFloat(self.computePadding(inlineStartEdge(axis, direction), direction).resolve(widthSize).unwrap(), 0.0)

    def computeFlexEndPadding(self, axis: YGFlexDirection, direction: YGDirection, widthSize: float) -> float:
        return maxOrDefinedFloat(self.computePadding(flexEndEdge(axis), direction).resolve(widthSize).unwrap(), 0.0)

    def computeInlineEndPadding(self, axis: YGFlexDirection, direction: YGDirection, widthSize: float) -> float:
        return maxOrDefinedFloat(self.computePadding(inlineEndEdge(axis, direction), direction).resolve(widthSize).unwrap(), 0.0)

    def computeInlineStartPaddingAndBorder(self, axis: YGFlexDirection, direction: YGDirection, widthSize: float) -> float:
        return self.computeInlineStartPadding(axis, direction, widthSize) + self.computeInlineStartBorder(axis, direction)

    def computeFlexStartPaddingAndBorder(self, axis: YGFlexDirection, direction: YGDirection, widthSize: float) -> float:
        return self.computeFlexStartPadding(axis, direction, widthSize) + self.computeFlexStartBorder(axis, direction)

    def computeInlineEndPaddingAndBorder(self, axis: YGFlexDirection, direction: YGDirection, widthSize: float) -> float:
        return self.computeInlineEndPadding(axis, direction, widthSize) + self.computeInlineEndBorder(axis, direction)

    def computeFlexEndPaddingAndBorder(self, axis: YGFlexDirection, direction: YGDirection, widthSize: float) -> float:
        return self.computeFlexEndPadding(axis, direction, widthSize) + self.computeFlexEndBorder(axis, direction)

    def computePaddingAndBorderForDimension(
        self, direction: YGDirection, dimension: YGDimension, widthSize: float
    ) -> float:
        flexDirectionForDimension = (
            YGFlexDirection.YGFlexDirectionRow
            if dimension == YGDimension.YGDimensionWidth
            else YGFlexDirection.YGFlexDirectionColumn
        )
        return self.computeFlexStartPaddingAndBorder(
            flexDirectionForDimension, direction, widthSize
        ) + self.computeFlexEndPaddingAndBorder(
            flexDirectionForDimension, direction, widthSize
        )

    def computeBorderForAxis(self, axis: YGFlexDirection) -> float:
        return self.computeInlineStartBorder(axis, YGDirection.YGDirectionLTR) + self.computeInlineEndBorder(
            axis, YGDirection.YGDirectionLTR
        )

    @cython.locals(startMargin=cython.double, endMargin=cython.double)
    def computeMarginForAxis(self, axis: YGFlexDirection, widthSize: float) -> float:
        startMargin = self.computeInlineStartMargin(axis, YGDirection.YGDirectionLTR, widthSize)
        endMargin = self.computeInlineEndMargin(axis, YGDirection.YGDirectionLTR, widthSize)
        return startMargin + endMargin

    def computeGapForAxis(self, axis: YGFlexDirection, ownerSize: float) -> float:
        gap = self.computeColumnGap() if isRow(axis) else self.computeRowGap()
        return maxOrDefinedFloat(gap.resolve(ownerSize).unwrap(), 0.0)

    def computeGapForDimension(self, dimension: YGDimension, ownerSize: float) -> float:
        gap = self.computeColumnGap() if dimension == YGDimension.YGDimensionWidth else self.computeRowGap()
        return maxOrDefinedFloat(gap.resolve(ownerSize).unwrap(), 0.0)

    def flexStartMarginIsAuto(self, axis: YGFlexDirection, direction: YGDirection) -> bool:
        margin = self.computeMargin(flexStartEdge(axis), direction)
        return margin.isAuto()

    def flexEndMarginIsAuto(self, axis: YGFlexDirection, direction: YGDirection) -> bool:
        margin = self.computeMargin(flexEndEdge(axis), direction)
        return margin.isAuto()

    def inlineStartMarginIsAuto(self, axis: YGFlexDirection, direction: YGDirection) -> bool:
        return self.computeMargin(inlineStartEdge(axis, direction), direction).isAuto()

    def inlineEndMarginIsAuto(self, axis: YGFlexDirection, direction: YGDirection) -> bool:
        return self.computeMargin(inlineEndEdge(axis, direction), direction).isAuto()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Style):
            return NotImplemented

        return (
            self.direction_ == other.direction_
            and self.flexDirection_ == other.flexDirection_
            and self.justifyContent_ == other.justifyContent_
            and self.justifyItems_ == other.justifyItems_
            and self.justifySelf_ == other.justifySelf_
            and self.alignContent_ == other.alignContent_
            and self.alignItems_ == other.alignItems_
            and self.alignSelf_ == other.alignSelf_
            and self.positionType_ == other.positionType_
            and self.flexWrap_ == other.flexWrap_
            and self.overflow_ == other.overflow_
            and self.display_ == other.display_
            and _numbers_equal(self.flex_, self.pool_, other.flex_, other.pool_)
            and _numbers_equal(self.flexGrow_, self.pool_, other.flexGrow_, other.pool_)
            and _numbers_equal(self.flexShrink_, self.pool_, other.flexShrink_, other.pool_)
            and _size_handles_equal(self.flexBasis_, self.pool_, other.flexBasis_, other.pool_)
            and _handle_arrays_equal(
                self.margin_,
                other.margin_,
                lambda lhs, rhs: _length_handles_equal(lhs, self.pool_, rhs, other.pool_),
            )
            and _handle_arrays_equal(
                self.position_,
                other.position_,
                lambda lhs, rhs: _length_handles_equal(lhs, self.pool_, rhs, other.pool_),
            )
            and _handle_arrays_equal(
                self.padding_,
                other.padding_,
                lambda lhs, rhs: _length_handles_equal(lhs, self.pool_, rhs, other.pool_),
            )
            and _handle_arrays_equal(
                self.border_,
                other.border_,
                lambda lhs, rhs: _length_handles_equal(lhs, self.pool_, rhs, other.pool_),
            )
            and _handle_arrays_equal(
                self.gap_,
                other.gap_,
                lambda lhs, rhs: _length_handles_equal(lhs, self.pool_, rhs, other.pool_),
            )
            and _handle_arrays_equal(
                self.dimensions_,
                other.dimensions_,
                lambda lhs, rhs: _size_handles_equal(lhs, self.pool_, rhs, other.pool_),
            )
            and _handle_arrays_equal(
                self.minDimensions_,
                other.minDimensions_,
                lambda lhs, rhs: _size_handles_equal(lhs, self.pool_, rhs, other.pool_),
            )
            and _handle_arrays_equal(
                self.maxDimensions_,
                other.maxDimensions_,
                lambda lhs, rhs: _size_handles_equal(lhs, self.pool_, rhs, other.pool_),
            )
            and _numbers_equal(self.aspectRatio_, self.pool_, other.aspectRatio_, other.pool_)
            and self.gridTemplateColumns_ == other.gridTemplateColumns_
            and self.gridTemplateRows_ == other.gridTemplateRows_
            and self.gridAutoColumns_ == other.gridAutoColumns_
            and self.gridAutoRows_ == other.gridAutoRows_
            and self.gridColumnStart_ == other.gridColumnStart_
            and self.gridColumnEnd_ == other.gridColumnEnd_
            and self.gridRowStart_ == other.gridRowStart_
            and self.gridRowEnd_ == other.gridRowEnd_
        )

    def computeColumnGap(self) -> StyleLength:
        if self.gap_[YGGutter.YGGutterColumn].isDefined():
            return self.pool_.get_length(self.gap_[YGGutter.YGGutterColumn])
        return self.pool_.get_length(self.gap_[YGGutter.YGGutterAll])

    def computeRowGap(self) -> StyleLength:
        if self.gap_[YGGutter.YGGutterRow].isDefined():
            return self.pool_.get_length(self.gap_[YGGutter.YGGutterRow])
        return self.pool_.get_length(self.gap_[YGGutter.YGGutterAll])

    def _computeLeftEdge(self, edges: list[StyleValueHandle], layoutDirection: YGDirection) -> StyleLength:
        if layoutDirection == YGDirection.YGDirectionLTR and edges[YGEdge.YGEdgeStart].isDefined():
            return self.pool_.get_length(edges[YGEdge.YGEdgeStart])
        if layoutDirection == YGDirection.YGDirectionRTL and edges[YGEdge.YGEdgeEnd].isDefined():
            return self.pool_.get_length(edges[YGEdge.YGEdgeEnd])
        if edges[YGEdge.YGEdgeLeft].isDefined():
            return self.pool_.get_length(edges[YGEdge.YGEdgeLeft])
        if edges[YGEdge.YGEdgeHorizontal].isDefined():
            return self.pool_.get_length(edges[YGEdge.YGEdgeHorizontal])
        return self.pool_.get_length(edges[YGEdge.YGEdgeAll])

    def _computeTopEdge(self, edges: list[StyleValueHandle]) -> StyleLength:
        if edges[YGEdge.YGEdgeTop].isDefined():
            return self.pool_.get_length(edges[YGEdge.YGEdgeTop])
        if edges[YGEdge.YGEdgeVertical].isDefined():
            return self.pool_.get_length(edges[YGEdge.YGEdgeVertical])
        return self.pool_.get_length(edges[YGEdge.YGEdgeAll])

    def _computeRightEdge(self, edges: list[StyleValueHandle], layoutDirection: YGDirection) -> StyleLength:
        if layoutDirection == YGDirection.YGDirectionLTR and edges[YGEdge.YGEdgeEnd].isDefined():
            return self.pool_.get_length(edges[YGEdge.YGEdgeEnd])
        if layoutDirection == YGDirection.YGDirectionRTL and edges[YGEdge.YGEdgeStart].isDefined():
            return self.pool_.get_length(edges[YGEdge.YGEdgeStart])
        if edges[YGEdge.YGEdgeRight].isDefined():
            return self.pool_.get_length(edges[YGEdge.YGEdgeRight])
        if edges[YGEdge.YGEdgeHorizontal].isDefined():
            return self.pool_.get_length(edges[YGEdge.YGEdgeHorizontal])
        return self.pool_.get_length(edges[YGEdge.YGEdgeAll])

    def _computeBottomEdge(self, edges: list[StyleValueHandle]) -> StyleLength:
        if edges[YGEdge.YGEdgeBottom].isDefined():
            return self.pool_.get_length(edges[YGEdge.YGEdgeBottom])
        if edges[YGEdge.YGEdgeVertical].isDefined():
            return self.pool_.get_length(edges[YGEdge.YGEdgeVertical])
        return self.pool_.get_length(edges[YGEdge.YGEdgeAll])

    def computePosition(self, edge: YGEdge, direction: YGDirection) -> StyleLength:
        if edge == YGEdge.YGEdgeLeft:
            return self._computeLeftEdge(self.position_, direction)
        if edge == YGEdge.YGEdgeTop:
            return self._computeTopEdge(self.position_)
        if edge == YGEdge.YGEdgeRight:
            return self._computeRightEdge(self.position_, direction)
        if edge == YGEdge.YGEdgeBottom:
            return self._computeBottomEdge(self.position_)
        fatalWithMessage("Invalid physical edge")
        raise AssertionError("Unreachable")  # type: ignore[return-value]

    def computeMargin(self, edge: YGEdge, direction: YGDirection) -> StyleLength:
        if edge == YGEdge.YGEdgeLeft:
            return self._computeLeftEdge(self.margin_, direction)
        if edge == YGEdge.YGEdgeTop:
            return self._computeTopEdge(self.margin_)
        if edge == YGEdge.YGEdgeRight:
            return self._computeRightEdge(self.margin_, direction)
        if edge == YGEdge.YGEdgeBottom:
            return self._computeBottomEdge(self.margin_)
        fatalWithMessage("Invalid physical edge")
        raise AssertionError("Unreachable")  # type: ignore[return-value]

    def computePadding(self, edge: YGEdge, direction: YGDirection) -> StyleLength:
        if edge == YGEdge.YGEdgeLeft:
            return self._computeLeftEdge(self.padding_, direction)
        if edge == YGEdge.YGEdgeTop:
            return self._computeTopEdge(self.padding_)
        if edge == YGEdge.YGEdgeRight:
            return self._computeRightEdge(self.padding_, direction)
        if edge == YGEdge.YGEdgeBottom:
            return self._computeBottomEdge(self.padding_)
        fatalWithMessage("Invalid physical edge")
        raise AssertionError("Unreachable")  # type: ignore[return-value]

    def computeBorder(self, edge: YGEdge, direction: YGDirection) -> StyleLength:
        if edge == YGEdge.YGEdgeLeft:
            return self._computeLeftEdge(self.border_, direction)
        if edge == YGEdge.YGEdgeTop:
            return self._computeTopEdge(self.border_)
        if edge == YGEdge.YGEdgeRight:
            return self._computeRightEdge(self.border_, direction)
        if edge == YGEdge.YGEdgeBottom:
            return self._computeBottomEdge(self.border_)
        fatalWithMessage("Invalid physical edge")
        raise AssertionError("Unreachable")  # type: ignore[return-value]
