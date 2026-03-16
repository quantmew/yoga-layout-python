"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from ..algorithm.FlexDirection import (
    flexEndEdge,
    flexStartEdge,
    inlineEndEdge,
    inlineStartEdge,
    isRow,
)
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
from ..debug.AssertFatal import fatalWithMessage
from ..numeric.FloatOptional import FloatOptional
from ..numeric.Comparison import maxOrDefined
from .GridLine import GridLine
from .GridTrack import GridTrackList, GridTrackSize
from .StyleLength import StyleLength
from .StyleSizeLength import StyleSizeLength


@dataclass
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
    flex_: FloatOptional = FloatOptional()
    flexGrow_: FloatOptional = FloatOptional()
    flexShrink_: FloatOptional = FloatOptional()
    flexBasis_: StyleSizeLength = StyleSizeLength.ofAuto()
    margin_: dict[YGEdge, StyleLength] = field(
        default_factory=lambda: {edge: StyleLength.undefined() for edge in YGEdge}
    )
    position_: dict[YGEdge, StyleLength] = field(
        default_factory=lambda: {edge: StyleLength.undefined() for edge in YGEdge}
    )
    padding_: dict[YGEdge, StyleLength] = field(
        default_factory=lambda: {edge: StyleLength.undefined() for edge in YGEdge}
    )
    border_: dict[YGEdge, StyleLength] = field(
        default_factory=lambda: {edge: StyleLength.undefined() for edge in YGEdge}
    )
    gap_: dict[YGGutter, StyleLength] = field(
        default_factory=lambda: {gutter: StyleLength.undefined() for gutter in YGGutter}
    )
    dimensions_: dict[YGDimension, StyleSizeLength] = field(
        default_factory=lambda: {
            YGDimension.YGDimensionWidth: StyleSizeLength.ofAuto(),
            YGDimension.YGDimensionHeight: StyleSizeLength.ofAuto(),
        }
    )
    minDimensions_: dict[YGDimension, StyleSizeLength] = field(
        default_factory=lambda: {dimension: StyleSizeLength.undefined() for dimension in YGDimension}
    )
    maxDimensions_: dict[YGDimension, StyleSizeLength] = field(
        default_factory=lambda: {dimension: StyleSizeLength.undefined() for dimension in YGDimension}
    )
    aspectRatio_: FloatOptional = FloatOptional()
    gridTemplateColumns_: GridTrackList = field(default_factory=list)
    gridTemplateRows_: GridTrackList = field(default_factory=list)
    gridAutoColumns_: GridTrackList = field(default_factory=list)
    gridAutoRows_: GridTrackList = field(default_factory=list)
    gridColumnStart_: GridLine = field(default_factory=GridLine.auto_)
    gridColumnEnd_: GridLine = field(default_factory=GridLine.auto_)
    gridRowStart_: GridLine = field(default_factory=GridLine.auto_)
    gridRowEnd_: GridLine = field(default_factory=GridLine.auto_)

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
        return self.flex_

    def setFlex(self, value: FloatOptional) -> None:
        self.flex_ = value

    def flexGrow(self) -> FloatOptional:
        return self.flexGrow_

    def setFlexGrow(self, value: FloatOptional) -> None:
        self.flexGrow_ = value

    def flexShrink(self) -> FloatOptional:
        return self.flexShrink_

    def setFlexShrink(self, value: FloatOptional) -> None:
        self.flexShrink_ = value

    def flexBasis(self) -> StyleSizeLength:
        return self.flexBasis_

    def setFlexBasis(self, value: StyleSizeLength) -> None:
        self.flexBasis_ = value

    def margin(self, edge: YGEdge) -> StyleLength:
        return self.margin_[edge]

    def setMargin(self, edge: YGEdge, value: StyleLength) -> None:
        self.margin_[edge] = value

    def position(self, edge: YGEdge) -> StyleLength:
        return self.position_[edge]

    def setPosition(self, edge: YGEdge, value: StyleLength) -> None:
        self.position_[edge] = value

    def padding(self, edge: YGEdge) -> StyleLength:
        return self.padding_[edge]

    def setPadding(self, edge: YGEdge, value: StyleLength) -> None:
        self.padding_[edge] = value

    def border(self, edge: YGEdge) -> StyleLength:
        return self.border_[edge]

    def setBorder(self, edge: YGEdge, value: StyleLength) -> None:
        self.border_[edge] = value

    def gap(self, gutter: YGGutter) -> StyleLength:
        return self.gap_[gutter]

    def setGap(self, gutter: YGGutter, value: StyleLength) -> None:
        self.gap_[gutter] = value

    def dimension(self, axis: YGDimension) -> StyleSizeLength:
        return self.dimensions_[axis]

    def setDimension(self, axis: YGDimension, value: StyleSizeLength) -> None:
        self.dimensions_[axis] = value

    def minDimension(self, axis: YGDimension) -> StyleSizeLength:
        return self.minDimensions_[axis]

    def setMinDimension(self, axis: YGDimension, value: StyleSizeLength) -> None:
        self.minDimensions_[axis] = value

    # Grid Container Properties
    def maxDimension(self, axis: YGDimension) -> StyleSizeLength:
        return self.maxDimensions_[axis]

    def setMaxDimension(self, axis: YGDimension, value: StyleSizeLength) -> None:
        self.maxDimensions_[axis] = value

    def aspectRatio(self) -> FloatOptional:
        return self.aspectRatio_

    def setAspectRatio(self, value: FloatOptional) -> None:
        unwrapped = value.unwrap()
        self.aspectRatio_ = (
            FloatOptional()
            if value == 0.0 or unwrapped == float("inf") or unwrapped == float("-inf")
            else value
        )

    def boxSizing(self) -> YGBoxSizing:
        return self.boxSizing_

    def setBoxSizing(self, value: YGBoxSizing) -> None:
        self.boxSizing_ = value

    # Grid Item Properties
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

    def resizeGridTemplateColumns(self, count: int) -> None:
        self.gridTemplateColumns_ = [GridTrackSize.auto_() for _ in range(count)]

    def setGridTemplateColumnAt(self, index: int, value: GridTrackSize) -> None:
        self.gridTemplateColumns_[index] = value

    def resizeGridTemplateRows(self, count: int) -> None:
        self.gridTemplateRows_ = [GridTrackSize.auto_() for _ in range(count)]

    def setGridTemplateRowAt(self, index: int, value: GridTrackSize) -> None:
        self.gridTemplateRows_[index] = value

    def resizeGridAutoColumns(self, count: int) -> None:
        self.gridAutoColumns_ = [GridTrackSize.auto_() for _ in range(count)]

    def setGridAutoColumnAt(self, index: int, value: GridTrackSize) -> None:
        self.gridAutoColumns_[index] = value

    def resizeGridAutoRows(self, count: int) -> None:
        self.gridAutoRows_ = [GridTrackSize.auto_() for _ in range(count)]

    def setGridAutoRowAt(self, index: int, value: GridTrackSize) -> None:
        self.gridAutoRows_[index] = value

    def computeGapForAxis(self, axis: YGFlexDirection, ownerSize: float) -> float:
        if isRow(axis):
            gap = self.computeColumnGap()
        else:
            gap = self.computeRowGap()
        return maxOrDefined(gap.resolve(ownerSize).unwrap(), 0.0)

    def computeGapForDimension(self, dimension: YGDimension, ownerSize: float) -> float:
        gap = self.computeColumnGap() if dimension == YGDimension.YGDimensionWidth else self.computeRowGap()
        return maxOrDefined(gap.resolve(ownerSize).unwrap(), 0.0)

    def computeColumnGap(self) -> StyleLength:
        if self.gap_[YGGutter.YGGutterColumn].isDefined():
            return self.gap_[YGGutter.YGGutterColumn]
        else:
            return self.gap_[YGGutter.YGGutterAll]

    def computeRowGap(self) -> StyleLength:
        if self.gap_[YGGutter.YGGutterRow].isDefined():
            return self.gap_[YGGutter.YGGutterRow]
        else:
            return self.gap_[YGGutter.YGGutterAll]

    def _computeLeftEdge(self, edges: dict[YGEdge, StyleLength], layoutDirection: YGDirection) -> StyleLength:
        if layoutDirection == YGDirection.YGDirectionLTR and edges[YGEdge.YGEdgeStart].isDefined():
            return edges[YGEdge.YGEdgeStart]
        elif layoutDirection == YGDirection.YGDirectionRTL and edges[YGEdge.YGEdgeEnd].isDefined():
            return edges[YGEdge.YGEdgeEnd]
        elif edges[YGEdge.YGEdgeLeft].isDefined():
            return edges[YGEdge.YGEdgeLeft]
        elif edges[YGEdge.YGEdgeHorizontal].isDefined():
            return edges[YGEdge.YGEdgeHorizontal]
        else:
            return edges[YGEdge.YGEdgeAll]

    def _computeTopEdge(self, edges: dict[YGEdge, StyleLength]) -> StyleLength:
        if edges[YGEdge.YGEdgeTop].isDefined():
            return edges[YGEdge.YGEdgeTop]
        elif edges[YGEdge.YGEdgeVertical].isDefined():
            return edges[YGEdge.YGEdgeVertical]
        else:
            return edges[YGEdge.YGEdgeAll]

    def _computeRightEdge(self, edges: dict[YGEdge, StyleLength], layoutDirection: YGDirection) -> StyleLength:
        if layoutDirection == YGDirection.YGDirectionLTR and edges[YGEdge.YGEdgeEnd].isDefined():
            return edges[YGEdge.YGEdgeEnd]
        elif layoutDirection == YGDirection.YGDirectionRTL and edges[YGEdge.YGEdgeStart].isDefined():
            return edges[YGEdge.YGEdgeStart]
        elif edges[YGEdge.YGEdgeRight].isDefined():
            return edges[YGEdge.YGEdgeRight]
        elif edges[YGEdge.YGEdgeHorizontal].isDefined():
            return edges[YGEdge.YGEdgeHorizontal]
        else:
            return edges[YGEdge.YGEdgeAll]

    def _computeBottomEdge(self, edges: dict[YGEdge, StyleLength]) -> StyleLength:
        if edges[YGEdge.YGEdgeBottom].isDefined():
            return edges[YGEdge.YGEdgeBottom]
        elif edges[YGEdge.YGEdgeVertical].isDefined():
            return edges[YGEdge.YGEdgeVertical]
        else:
            return edges[YGEdge.YGEdgeAll]

    def computePosition(self, edge, direction: YGDirection) -> StyleLength:
        if edge == YGEdge.YGEdgeLeft:
            return self._computeLeftEdge(self.position_, direction)
        if edge == YGEdge.YGEdgeTop:
            return self._computeTopEdge(self.position_)
        if edge == YGEdge.YGEdgeRight:
            return self._computeRightEdge(self.position_, direction)
        if edge == YGEdge.YGEdgeBottom:
            return self._computeBottomEdge(self.position_)
        fatalWithMessage("Invalid physical edge")

    def computeMargin(self, edge, direction: YGDirection) -> StyleLength:
        if edge == YGEdge.YGEdgeLeft:
            return self._computeLeftEdge(self.margin_, direction)
        if edge == YGEdge.YGEdgeTop:
            return self._computeTopEdge(self.margin_)
        if edge == YGEdge.YGEdgeRight:
            return self._computeRightEdge(self.margin_, direction)
        if edge == YGEdge.YGEdgeBottom:
            return self._computeBottomEdge(self.margin_)
        fatalWithMessage("Invalid physical edge")

    def computePadding(self, edge, direction: YGDirection) -> StyleLength:
        if edge == YGEdge.YGEdgeLeft:
            return self._computeLeftEdge(self.padding_, direction)
        if edge == YGEdge.YGEdgeTop:
            return self._computeTopEdge(self.padding_)
        if edge == YGEdge.YGEdgeRight:
            return self._computeRightEdge(self.padding_, direction)
        if edge == YGEdge.YGEdgeBottom:
            return self._computeBottomEdge(self.padding_)
        fatalWithMessage("Invalid physical edge")

    def computeBorder(self, edge, direction: YGDirection) -> StyleLength:
        if edge == YGEdge.YGEdgeLeft:
            return self._computeLeftEdge(self.border_, direction)
        if edge == YGEdge.YGEdgeTop:
            return self._computeTopEdge(self.border_)
        if edge == YGEdge.YGEdgeRight:
            return self._computeRightEdge(self.border_, direction)
        if edge == YGEdge.YGEdgeBottom:
            return self._computeBottomEdge(self.border_)
        fatalWithMessage("Invalid physical edge")

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
        return maxOrDefined(self.computeBorder(flexStartEdge(axis), direction).resolve(0.0).unwrap(), 0.0)

    def computeInlineStartBorder(self, axis: YGFlexDirection, direction: YGDirection) -> float:
        return maxOrDefined(self.computeBorder(inlineStartEdge(axis, direction), direction).resolve(0.0).unwrap(), 0.0)

    def computeFlexEndBorder(self, axis: YGFlexDirection, direction: YGDirection) -> float:
        return maxOrDefined(self.computeBorder(flexEndEdge(axis), direction).resolve(0.0).unwrap(), 0.0)

    def computeInlineEndBorder(self, axis: YGFlexDirection, direction: YGDirection) -> float:
        return maxOrDefined(self.computeBorder(inlineEndEdge(axis, direction), direction).resolve(0.0).unwrap(), 0.0)

    def computeFlexStartPadding(self, axis: YGFlexDirection, direction: YGDirection, widthSize: float) -> float:
        return maxOrDefined(self.computePadding(flexStartEdge(axis), direction).resolve(widthSize).unwrap(), 0.0)

    def computeInlineStartPadding(self, axis: YGFlexDirection, direction: YGDirection, widthSize: float) -> float:
        return maxOrDefined(self.computePadding(inlineStartEdge(axis, direction), direction).resolve(widthSize).unwrap(), 0.0)

    def computeFlexEndPadding(self, axis: YGFlexDirection, direction: YGDirection, widthSize: float) -> float:
        return maxOrDefined(self.computePadding(flexEndEdge(axis), direction).resolve(widthSize).unwrap(), 0.0)

    def computeInlineEndPadding(self, axis: YGFlexDirection, direction: YGDirection, widthSize: float) -> float:
        return maxOrDefined(self.computePadding(inlineEndEdge(axis, direction), direction).resolve(widthSize).unwrap(), 0.0)

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
        flexDirectionForDimension = YGFlexDirection.YGFlexDirectionRow if dimension == YGDimension.YGDimensionWidth else YGFlexDirection.YGFlexDirectionColumn
        return self.computeFlexStartPaddingAndBorder(
            flexDirectionForDimension, direction, widthSize
        ) + self.computeFlexEndPaddingAndBorder(
            flexDirectionForDimension, direction, widthSize
        )

    def computeMarginForAxis(self, axis: YGFlexDirection, widthSize: float) -> float:
        # The total margin for a given axis does not depend on the direction,
        # so hardcoding LTR here avoids piping direction into this function.
        return self.computeInlineStartMargin(axis, YGDirection.YGDirectionLTR, widthSize) + self.computeInlineEndMargin(
            axis, YGDirection.YGDirectionLTR, widthSize
        )

    def computeBorderForAxis(self, axis: YGFlexDirection) -> float:
        return self.computeInlineStartBorder(axis, YGDirection.YGDirectionLTR) + self.computeInlineEndBorder(
            axis, YGDirection.YGDirectionLTR
        )

    def resolvedMinDimension(
        self, direction: YGDirection, axis: YGDimension, referenceLength: float, ownerWidth: float
    ) -> FloatOptional:
        value = self.minDimension(axis).resolve(referenceLength)
        if self.boxSizing() == YGBoxSizing.YGBoxSizingBorderBox:
            return value

        dimensionPaddingAndBorder = FloatOptional(
            self.computePaddingAndBorderForDimension(direction, axis, ownerWidth)
        )

        return value + (
            dimensionPaddingAndBorder if dimensionPaddingAndBorder.isDefined() else FloatOptional(0.0)
        )

    def resolvedMaxDimension(
        self, direction: YGDirection, axis: YGDimension, referenceLength: float, ownerWidth: float
    ) -> FloatOptional:
        value = self.maxDimension(axis).resolve(referenceLength)
        if self.boxSizing() == YGBoxSizing.YGBoxSizingBorderBox:
            return value

        dimensionPaddingAndBorder = FloatOptional(
            self.computePaddingAndBorderForDimension(direction, axis, ownerWidth)
        )

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

    def flexStartMarginIsAuto(self, axis: YGFlexDirection, direction: YGDirection) -> bool:
        return self.computeMargin(flexStartEdge(axis), direction).isAuto()

    def flexEndMarginIsAuto(self, axis: YGFlexDirection, direction: YGDirection) -> bool:
        return self.computeMargin(flexEndEdge(axis), direction).isAuto()

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
            and self.flex_ == other.flex_
            and self.flexGrow_ == other.flexGrow_
            and self.flexShrink_ == other.flexShrink_
            and self.flexBasis_ == other.flexBasis_
            and self.margin_ == other.margin_
            and self.position_ == other.position_
            and self.padding_ == other.padding_
            and self.border_ == other.border_
            and self.gap_ == other.gap_
            and self.dimensions_ == other.dimensions_
            and self.minDimensions_ == other.minDimensions_
            and self.maxDimensions_ == other.maxDimensions_
            and self.aspectRatio_ == other.aspectRatio_
            and self.gridTemplateColumns_ == other.gridTemplateColumns_
            and self.gridTemplateRows_ == other.gridTemplateRows_
            and self.gridAutoColumns_ == other.gridAutoColumns_
            and self.gridAutoRows_ == other.gridAutoRows_
            and self.gridColumnStart_ == other.gridColumnStart_
            and self.gridColumnEnd_ == other.gridColumnEnd_
            and self.gridRowStart_ == other.gridRowStart_
            and self.gridRowEnd_ == other.gridRowEnd_
        )
