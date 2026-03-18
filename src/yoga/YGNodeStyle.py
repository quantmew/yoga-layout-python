"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from copy import deepcopy

from .YGEnums import YGBoxSizing, YGDimension, YGEdge, YGGridTrackType, YGGutter
from .YGValue import YGUndefined, YGValue
from .debug.AssertFatal import fatalWithMessage
from .node.Node import Node
from .numeric.FloatOptional import FloatOptional
from .style.GridLine import GridLine
from .style.GridTrack import GridTrackSize
from .style.Style import Style, normalize_style_value
from .style.StyleLength import StyleLength
from .style.StyleSizeLength import StyleSizeLength


def _updateStyle(node: Node, getter: str, setter: str, value) -> None:
    style = node.style()
    normalized_value = normalize_style_value(value)
    if getattr(style, getter)() != normalized_value:
        getattr(style, setter)(normalized_value)
        node.markDirtyAndPropagate()


def _updateIndexedStyle(node: Node, getter: str, setter: str, index, value) -> None:
    style = node.style()
    normalized_value = normalize_style_value(value)
    if getattr(style, getter)(index) != normalized_value:
        getattr(style, setter)(index, normalized_value)
        node.markDirtyAndPropagate()


def _gridTrackSizeFromTypeAndValue(type: YGGridTrackType, value: float) -> GridTrackSize:
    if type == YGGridTrackType.YGGridTrackTypePoints:
        return GridTrackSize.length(value)
    if type == YGGridTrackType.YGGridTrackTypePercent:
        return GridTrackSize.percent(value)
    if type == YGGridTrackType.YGGridTrackTypeFr:
        return GridTrackSize.fr(value)
    if type == YGGridTrackType.YGGridTrackTypeAuto:
        return GridTrackSize.auto_()
    if type == YGGridTrackType.YGGridTrackTypeMinmax:
        return GridTrackSize.auto_()
    fatalWithMessage("Unknown YGGridTrackType")


def _styleSizeLengthFromTypeAndValue(
    type: YGGridTrackType, value: float
) -> StyleSizeLength:
    if type == YGGridTrackType.YGGridTrackTypePoints:
        return StyleSizeLength.points(value)
    if type == YGGridTrackType.YGGridTrackTypePercent:
        return StyleSizeLength.percent(value)
    if type == YGGridTrackType.YGGridTrackTypeFr:
        return StyleSizeLength.stretch(value)
    if type == YGGridTrackType.YGGridTrackTypeAuto:
        return StyleSizeLength.ofAuto()
    if type == YGGridTrackType.YGGridTrackTypeMinmax:
        return StyleSizeLength.ofAuto()
    fatalWithMessage("Unknown YGGridTrackType")


def YGNodeCopyStyle(dstNode: Node, srcNode: Node) -> None:
    dst = dstNode
    src = srcNode

    if dst.style() != src.style():
        dst.setStyle(deepcopy(src.style()))
        dst.markDirtyAndPropagate()


def YGNodeStyleSetDirection(node: Node, value) -> None:
    _updateStyle(node, "direction", "setDirection", value)


def YGNodeStyleGetDirection(node: Node):
    return node.style().direction()


def YGNodeStyleSetFlexDirection(node: Node, flexDirection) -> None:
    _updateStyle(node, "flexDirection", "setFlexDirection", flexDirection)


def YGNodeStyleGetFlexDirection(node: Node):
    return node.style().flexDirection()


def YGNodeStyleSetJustifyContent(node: Node, justifyContent) -> None:
    _updateStyle(node, "justifyContent", "setJustifyContent", justifyContent)


def YGNodeStyleGetJustifyContent(node: Node):
    return node.style().justifyContent()


def YGNodeStyleSetJustifyItems(node: Node, justifyItems) -> None:
    _updateStyle(node, "justifyItems", "setJustifyItems", justifyItems)


def YGNodeStyleGetJustifyItems(node: Node):
    return node.style().justifyItems()


def YGNodeStyleSetJustifySelf(node: Node, justifySelf) -> None:
    _updateStyle(node, "justifySelf", "setJustifySelf", justifySelf)


def YGNodeStyleGetJustifySelf(node: Node):
    return node.style().justifySelf()


def YGNodeStyleSetAlignContent(node: Node, alignContent) -> None:
    _updateStyle(node, "alignContent", "setAlignContent", alignContent)


def YGNodeStyleGetAlignContent(node: Node):
    return node.style().alignContent()


def YGNodeStyleSetAlignItems(node: Node, alignItems) -> None:
    _updateStyle(node, "alignItems", "setAlignItems", alignItems)


def YGNodeStyleGetAlignItems(node: Node):
    return node.style().alignItems()


def YGNodeStyleSetAlignSelf(node: Node, alignSelf) -> None:
    _updateStyle(node, "alignSelf", "setAlignSelf", alignSelf)


def YGNodeStyleGetAlignSelf(node: Node):
    return node.style().alignSelf()


def YGNodeStyleSetPositionType(node: Node, positionType) -> None:
    _updateStyle(node, "positionType", "setPositionType", positionType)


def YGNodeStyleGetPositionType(node: Node):
    return node.style().positionType()


def YGNodeStyleSetFlexWrap(node: Node, flexWrap) -> None:
    _updateStyle(node, "flexWrap", "setFlexWrap", flexWrap)


def YGNodeStyleGetFlexWrap(node: Node):
    return node.style().flexWrap()


def YGNodeStyleSetOverflow(node: Node, overflow) -> None:
    _updateStyle(node, "overflow", "setOverflow", overflow)


def YGNodeStyleGetOverflow(node: Node):
    return node.style().overflow()


def YGNodeStyleSetDisplay(node: Node, display) -> None:
    _updateStyle(node, "display", "setDisplay", display)


def YGNodeStyleGetDisplay(node: Node):
    return node.style().display()


def YGNodeStyleSetFlex(node: Node, flex: float) -> None:
    _updateStyle(node, "flex", "setFlex", FloatOptional(flex))


def YGNodeStyleGetFlex(node: Node) -> float:
    flex = node.style().flex()
    return YGUndefined if flex.isUndefined() else flex.unwrap()


def YGNodeStyleSetFlexGrow(node: Node, flexGrow: float) -> None:
    _updateStyle(node, "flexGrow", "setFlexGrow", FloatOptional(flexGrow))


def YGNodeStyleGetFlexGrow(node: Node) -> float:
    flexGrow = node.style().flexGrow()
    return Style.DefaultFlexGrow if flexGrow.isUndefined() else flexGrow.unwrap()


def YGNodeStyleSetFlexShrink(node: Node, flexShrink: float) -> None:
    _updateStyle(node, "flexShrink", "setFlexShrink", FloatOptional(flexShrink))


def YGNodeStyleGetFlexShrink(node: Node) -> float:
    flexShrink = node.style().flexShrink()
    if flexShrink.isUndefined():
        return (
            Style.WebDefaultFlexShrink
            if node.getConfig().useWebDefaults()
            else Style.DefaultFlexShrink
        )
    return flexShrink.unwrap()


def YGNodeStyleSetFlexBasis(node: Node, flexBasis: float) -> None:
    _updateStyle(node, "flexBasis", "setFlexBasis", StyleSizeLength.points(flexBasis))


def YGNodeStyleSetFlexBasisPercent(node: Node, flexBasisPercent: float) -> None:
    _updateStyle(
        node, "flexBasis", "setFlexBasis", StyleSizeLength.percent(flexBasisPercent)
    )


def YGNodeStyleSetFlexBasisAuto(node: Node) -> None:
    _updateStyle(node, "flexBasis", "setFlexBasis", StyleSizeLength.ofAuto())


def YGNodeStyleSetFlexBasisMaxContent(node: Node) -> None:
    _updateStyle(node, "flexBasis", "setFlexBasis", StyleSizeLength.ofMaxContent())


def YGNodeStyleSetFlexBasisFitContent(node: Node) -> None:
    _updateStyle(node, "flexBasis", "setFlexBasis", StyleSizeLength.ofFitContent())


def YGNodeStyleSetFlexBasisStretch(node: Node) -> None:
    _updateStyle(node, "flexBasis", "setFlexBasis", StyleSizeLength.ofStretch())


def YGNodeStyleGetFlexBasis(node: Node) -> YGValue:
    return node.style().flexBasis().asYGValue()


def YGNodeStyleSetPosition(node: Node, edge: YGEdge, points: float) -> None:
    _updateIndexedStyle(node, "position", "setPosition", edge, StyleLength.points(points))


def YGNodeStyleSetPositionPercent(node: Node, edge: YGEdge, percent: float) -> None:
    _updateIndexedStyle(
        node, "position", "setPosition", edge, StyleLength.percent(percent)
    )


def YGNodeStyleSetPositionAuto(node: Node, edge: YGEdge) -> None:
    _updateIndexedStyle(node, "position", "setPosition", edge, StyleLength.ofAuto())


def YGNodeStyleGetPosition(node: Node, edge: YGEdge) -> YGValue:
    return node.style().position(edge).asYGValue()


def YGNodeStyleSetMargin(node: Node, edge: YGEdge, points: float) -> None:
    _updateIndexedStyle(node, "margin", "setMargin", edge, StyleLength.points(points))


def YGNodeStyleSetMarginPercent(node: Node, edge: YGEdge, percent: float) -> None:
    _updateIndexedStyle(node, "margin", "setMargin", edge, StyleLength.percent(percent))


def YGNodeStyleSetMarginAuto(node: Node, edge: YGEdge) -> None:
    _updateIndexedStyle(node, "margin", "setMargin", edge, StyleLength.ofAuto())


def YGNodeStyleGetMargin(node: Node, edge: YGEdge) -> YGValue:
    return node.style().margin(edge).asYGValue()


def YGNodeStyleSetPadding(node: Node, edge: YGEdge, points: float) -> None:
    _updateIndexedStyle(
        node, "padding", "setPadding", edge, StyleLength.points(points)
    )


def YGNodeStyleSetPaddingPercent(node: Node, edge: YGEdge, percent: float) -> None:
    _updateIndexedStyle(
        node, "padding", "setPadding", edge, StyleLength.percent(percent)
    )


def YGNodeStyleGetPadding(node: Node, edge: YGEdge) -> YGValue:
    return node.style().padding(edge).asYGValue()


def YGNodeStyleSetBorder(node: Node, edge: YGEdge, border: float) -> None:
    _updateIndexedStyle(node, "border", "setBorder", edge, StyleLength.points(border))


def YGNodeStyleGetBorder(node: Node, edge: YGEdge) -> float:
    border = node.style().border(edge)
    if border.isUndefined() or border.isAuto():
        return YGUndefined
    return border.asYGValue().value


def YGNodeStyleSetGap(node: Node, gutter: YGGutter, gapLength: float) -> None:
    _updateIndexedStyle(node, "gap", "setGap", gutter, StyleLength.points(gapLength))


def YGNodeStyleSetGapPercent(node: Node, gutter: YGGutter, percent: float) -> None:
    _updateIndexedStyle(node, "gap", "setGap", gutter, StyleLength.percent(percent))


def YGNodeStyleGetGap(node: Node, gutter: YGGutter) -> YGValue:
    return node.style().gap(gutter).asYGValue()


def YGNodeStyleSetAspectRatio(node: Node, aspectRatio: float) -> None:
    _updateStyle(node, "aspectRatio", "setAspectRatio", FloatOptional(aspectRatio))


def YGNodeStyleGetAspectRatio(node: Node) -> float:
    aspectRatio = node.style().aspectRatio()
    return YGUndefined if aspectRatio.isUndefined() else aspectRatio.unwrap()


def YGNodeStyleSetBoxSizing(node: Node, boxSizing: YGBoxSizing) -> None:
    _updateStyle(node, "boxSizing", "setBoxSizing", boxSizing)


def YGNodeStyleGetBoxSizing(node: Node) -> YGBoxSizing:
    return node.style().boxSizing()


def YGNodeStyleSetWidth(node: Node, points: float) -> None:
    _updateIndexedStyle(
        node,
        "dimension",
        "setDimension",
        YGDimension.YGDimensionWidth,
        StyleSizeLength.points(points),
    )


def YGNodeStyleSetWidthPercent(node: Node, percent: float) -> None:
    _updateIndexedStyle(
        node,
        "dimension",
        "setDimension",
        YGDimension.YGDimensionWidth,
        StyleSizeLength.percent(percent),
    )


def YGNodeStyleSetWidthAuto(node: Node) -> None:
    _updateIndexedStyle(
        node,
        "dimension",
        "setDimension",
        YGDimension.YGDimensionWidth,
        StyleSizeLength.ofAuto(),
    )


def YGNodeStyleSetWidthMaxContent(node: Node) -> None:
    _updateIndexedStyle(
        node,
        "dimension",
        "setDimension",
        YGDimension.YGDimensionWidth,
        StyleSizeLength.ofMaxContent(),
    )


def YGNodeStyleSetWidthFitContent(node: Node) -> None:
    _updateIndexedStyle(
        node,
        "dimension",
        "setDimension",
        YGDimension.YGDimensionWidth,
        StyleSizeLength.ofFitContent(),
    )


def YGNodeStyleSetWidthStretch(node: Node) -> None:
    _updateIndexedStyle(
        node,
        "dimension",
        "setDimension",
        YGDimension.YGDimensionWidth,
        StyleSizeLength.ofStretch(),
    )


def YGNodeStyleGetWidth(node: Node) -> YGValue:
    return node.style().dimension(YGDimension.YGDimensionWidth).asYGValue()


def YGNodeStyleSetHeight(node: Node, points: float) -> None:
    _updateIndexedStyle(
        node,
        "dimension",
        "setDimension",
        YGDimension.YGDimensionHeight,
        StyleSizeLength.points(points),
    )


def YGNodeStyleSetHeightPercent(node: Node, percent: float) -> None:
    _updateIndexedStyle(
        node,
        "dimension",
        "setDimension",
        YGDimension.YGDimensionHeight,
        StyleSizeLength.percent(percent),
    )


def YGNodeStyleSetHeightAuto(node: Node) -> None:
    _updateIndexedStyle(
        node,
        "dimension",
        "setDimension",
        YGDimension.YGDimensionHeight,
        StyleSizeLength.ofAuto(),
    )


def YGNodeStyleSetHeightMaxContent(node: Node) -> None:
    _updateIndexedStyle(
        node,
        "dimension",
        "setDimension",
        YGDimension.YGDimensionHeight,
        StyleSizeLength.ofMaxContent(),
    )


def YGNodeStyleSetHeightFitContent(node: Node) -> None:
    _updateIndexedStyle(
        node,
        "dimension",
        "setDimension",
        YGDimension.YGDimensionHeight,
        StyleSizeLength.ofFitContent(),
    )


def YGNodeStyleSetHeightStretch(node: Node) -> None:
    _updateIndexedStyle(
        node,
        "dimension",
        "setDimension",
        YGDimension.YGDimensionHeight,
        StyleSizeLength.ofStretch(),
    )


def YGNodeStyleGetHeight(node: Node) -> YGValue:
    return node.style().dimension(YGDimension.YGDimensionHeight).asYGValue()


def YGNodeStyleSetMinWidth(node: Node, minWidth: float) -> None:
    _updateIndexedStyle(
        node,
        "minDimension",
        "setMinDimension",
        YGDimension.YGDimensionWidth,
        StyleSizeLength.points(minWidth),
    )


def YGNodeStyleSetMinWidthPercent(node: Node, minWidth: float) -> None:
    _updateIndexedStyle(
        node,
        "minDimension",
        "setMinDimension",
        YGDimension.YGDimensionWidth,
        StyleSizeLength.percent(minWidth),
    )


def YGNodeStyleSetMinWidthMaxContent(node: Node) -> None:
    _updateIndexedStyle(
        node,
        "minDimension",
        "setMinDimension",
        YGDimension.YGDimensionWidth,
        StyleSizeLength.ofMaxContent(),
    )


def YGNodeStyleSetMinWidthFitContent(node: Node) -> None:
    _updateIndexedStyle(
        node,
        "minDimension",
        "setMinDimension",
        YGDimension.YGDimensionWidth,
        StyleSizeLength.ofFitContent(),
    )


def YGNodeStyleSetMinWidthStretch(node: Node) -> None:
    _updateIndexedStyle(
        node,
        "minDimension",
        "setMinDimension",
        YGDimension.YGDimensionWidth,
        StyleSizeLength.ofStretch(),
    )


def YGNodeStyleGetMinWidth(node: Node) -> YGValue:
    return node.style().minDimension(YGDimension.YGDimensionWidth).asYGValue()


def YGNodeStyleSetMinHeight(node: Node, minHeight: float) -> None:
    _updateIndexedStyle(
        node,
        "minDimension",
        "setMinDimension",
        YGDimension.YGDimensionHeight,
        StyleSizeLength.points(minHeight),
    )


def YGNodeStyleSetMinHeightPercent(node: Node, minHeight: float) -> None:
    _updateIndexedStyle(
        node,
        "minDimension",
        "setMinDimension",
        YGDimension.YGDimensionHeight,
        StyleSizeLength.percent(minHeight),
    )


def YGNodeStyleSetMinHeightMaxContent(node: Node) -> None:
    _updateIndexedStyle(
        node,
        "minDimension",
        "setMinDimension",
        YGDimension.YGDimensionHeight,
        StyleSizeLength.ofMaxContent(),
    )


def YGNodeStyleSetMinHeightFitContent(node: Node) -> None:
    _updateIndexedStyle(
        node,
        "minDimension",
        "setMinDimension",
        YGDimension.YGDimensionHeight,
        StyleSizeLength.ofFitContent(),
    )


def YGNodeStyleSetMinHeightStretch(node: Node) -> None:
    _updateIndexedStyle(
        node,
        "minDimension",
        "setMinDimension",
        YGDimension.YGDimensionHeight,
        StyleSizeLength.ofStretch(),
    )


def YGNodeStyleGetMinHeight(node: Node) -> YGValue:
    return node.style().minDimension(YGDimension.YGDimensionHeight).asYGValue()


def YGNodeStyleSetMaxWidth(node: Node, maxWidth: float) -> None:
    _updateIndexedStyle(
        node,
        "maxDimension",
        "setMaxDimension",
        YGDimension.YGDimensionWidth,
        StyleSizeLength.points(maxWidth),
    )


def YGNodeStyleSetMaxWidthPercent(node: Node, maxWidth: float) -> None:
    _updateIndexedStyle(
        node,
        "maxDimension",
        "setMaxDimension",
        YGDimension.YGDimensionWidth,
        StyleSizeLength.percent(maxWidth),
    )


def YGNodeStyleSetMaxWidthMaxContent(node: Node) -> None:
    _updateIndexedStyle(
        node,
        "maxDimension",
        "setMaxDimension",
        YGDimension.YGDimensionWidth,
        StyleSizeLength.ofMaxContent(),
    )


def YGNodeStyleSetMaxWidthFitContent(node: Node) -> None:
    _updateIndexedStyle(
        node,
        "maxDimension",
        "setMaxDimension",
        YGDimension.YGDimensionWidth,
        StyleSizeLength.ofFitContent(),
    )


def YGNodeStyleSetMaxWidthStretch(node: Node) -> None:
    _updateIndexedStyle(
        node,
        "maxDimension",
        "setMaxDimension",
        YGDimension.YGDimensionWidth,
        StyleSizeLength.ofStretch(),
    )


def YGNodeStyleGetMaxWidth(node: Node) -> YGValue:
    return node.style().maxDimension(YGDimension.YGDimensionWidth).asYGValue()


def YGNodeStyleSetMaxHeight(node: Node, maxHeight: float) -> None:
    _updateIndexedStyle(
        node,
        "maxDimension",
        "setMaxDimension",
        YGDimension.YGDimensionHeight,
        StyleSizeLength.points(maxHeight),
    )


def YGNodeStyleSetMaxHeightPercent(node: Node, maxHeight: float) -> None:
    _updateIndexedStyle(
        node,
        "maxDimension",
        "setMaxDimension",
        YGDimension.YGDimensionHeight,
        StyleSizeLength.percent(maxHeight),
    )


def YGNodeStyleSetMaxHeightMaxContent(node: Node) -> None:
    _updateIndexedStyle(
        node,
        "maxDimension",
        "setMaxDimension",
        YGDimension.YGDimensionHeight,
        StyleSizeLength.ofMaxContent(),
    )


def YGNodeStyleSetMaxHeightFitContent(node: Node) -> None:
    _updateIndexedStyle(
        node,
        "maxDimension",
        "setMaxDimension",
        YGDimension.YGDimensionHeight,
        StyleSizeLength.ofFitContent(),
    )


def YGNodeStyleSetMaxHeightStretch(node: Node) -> None:
    _updateIndexedStyle(
        node,
        "maxDimension",
        "setMaxDimension",
        YGDimension.YGDimensionHeight,
        StyleSizeLength.ofStretch(),
    )


def YGNodeStyleGetMaxHeight(node: Node) -> YGValue:
    return node.style().maxDimension(YGDimension.YGDimensionHeight).asYGValue()


# Grid Item Placement Properties


def YGNodeStyleSetGridColumnStart(node: Node, gridColumnStart: int) -> None:
    _updateStyle(
        node,
        "gridColumnStart",
        "setGridColumnStart",
        GridLine.fromInteger(gridColumnStart),
    )


def YGNodeStyleSetGridColumnStartAuto(node: Node) -> None:
    _updateStyle(node, "gridColumnStart", "setGridColumnStart", GridLine.auto_())


def YGNodeStyleSetGridColumnStartSpan(node: Node, span: int) -> None:
    _updateStyle(node, "gridColumnStart", "setGridColumnStart", GridLine.span(span))


def YGNodeStyleGetGridColumnStart(node: Node) -> int:
    gridLine = node.style().gridColumnStart()
    return gridLine.integer if gridLine.isInteger() else 0


def YGNodeStyleSetGridColumnEnd(node: Node, gridColumnEnd: int) -> None:
    _updateStyle(
        node, "gridColumnEnd", "setGridColumnEnd", GridLine.fromInteger(gridColumnEnd)
    )


def YGNodeStyleSetGridColumnEndAuto(node: Node) -> None:
    _updateStyle(node, "gridColumnEnd", "setGridColumnEnd", GridLine.auto_())


def YGNodeStyleSetGridColumnEndSpan(node: Node, span: int) -> None:
    _updateStyle(node, "gridColumnEnd", "setGridColumnEnd", GridLine.span(span))


def YGNodeStyleGetGridColumnEnd(node: Node) -> int:
    gridLine = node.style().gridColumnEnd()
    return gridLine.integer if gridLine.isInteger() else 0


def YGNodeStyleSetGridRowStart(node: Node, gridRowStart: int) -> None:
    _updateStyle(
        node, "gridRowStart", "setGridRowStart", GridLine.fromInteger(gridRowStart)
    )


def YGNodeStyleSetGridRowStartAuto(node: Node) -> None:
    _updateStyle(node, "gridRowStart", "setGridRowStart", GridLine.auto_())


def YGNodeStyleSetGridRowStartSpan(node: Node, span: int) -> None:
    _updateStyle(node, "gridRowStart", "setGridRowStart", GridLine.span(span))


def YGNodeStyleGetGridRowStart(node: Node) -> int:
    gridLine = node.style().gridRowStart()
    return gridLine.integer if gridLine.isInteger() else 0


def YGNodeStyleSetGridRowEnd(node: Node, gridRowEnd: int) -> None:
    _updateStyle(node, "gridRowEnd", "setGridRowEnd", GridLine.fromInteger(gridRowEnd))


def YGNodeStyleSetGridRowEndAuto(node: Node) -> None:
    _updateStyle(node, "gridRowEnd", "setGridRowEnd", GridLine.auto_())


def YGNodeStyleSetGridRowEndSpan(node: Node, span: int) -> None:
    _updateStyle(node, "gridRowEnd", "setGridRowEnd", GridLine.span(span))


def YGNodeStyleGetGridRowEnd(node: Node) -> int:
    gridLine = node.style().gridRowEnd()
    return gridLine.integer if gridLine.isInteger() else 0


# Grid Container Properties


# GridTemplateColumns
def YGNodeStyleSetGridTemplateColumnsCount(node: Node, count: int) -> None:
    node.style().resizeGridTemplateColumns(count)
    node.markDirtyAndPropagate()


def YGNodeStyleSetGridTemplateColumn(
    node: Node, index: int, type: YGGridTrackType, value: float
) -> None:
    node.style().setGridTemplateColumnAt(index, _gridTrackSizeFromTypeAndValue(type, value))
    node.markDirtyAndPropagate()


def YGNodeStyleSetGridTemplateColumnMinMax(
    node: Node,
    index: int,
    minType: YGGridTrackType,
    minValue: float,
    maxType: YGGridTrackType,
    maxValue: float,
) -> None:
    node.style().setGridTemplateColumnAt(
        index,
        GridTrackSize.minmax(
            _styleSizeLengthFromTypeAndValue(minType, minValue),
            _styleSizeLengthFromTypeAndValue(maxType, maxValue),
        ),
    )
    node.markDirtyAndPropagate()


# GridTemplateRows
def YGNodeStyleSetGridTemplateRowsCount(node: Node, count: int) -> None:
    node.style().resizeGridTemplateRows(count)
    node.markDirtyAndPropagate()


def YGNodeStyleSetGridTemplateRow(
    node: Node, index: int, type: YGGridTrackType, value: float
) -> None:
    node.style().setGridTemplateRowAt(index, _gridTrackSizeFromTypeAndValue(type, value))
    node.markDirtyAndPropagate()


def YGNodeStyleSetGridTemplateRowMinMax(
    node: Node,
    index: int,
    minType: YGGridTrackType,
    minValue: float,
    maxType: YGGridTrackType,
    maxValue: float,
) -> None:
    node.style().setGridTemplateRowAt(
        index,
        GridTrackSize.minmax(
            _styleSizeLengthFromTypeAndValue(minType, minValue),
            _styleSizeLengthFromTypeAndValue(maxType, maxValue),
        ),
    )
    node.markDirtyAndPropagate()


# GridAutoColumns
def YGNodeStyleSetGridAutoColumnsCount(node: Node, count: int) -> None:
    node.style().resizeGridAutoColumns(count)
    node.markDirtyAndPropagate()


def YGNodeStyleSetGridAutoColumn(
    node: Node, index: int, type: YGGridTrackType, value: float
) -> None:
    node.style().setGridAutoColumnAt(index, _gridTrackSizeFromTypeAndValue(type, value))
    node.markDirtyAndPropagate()


def YGNodeStyleSetGridAutoColumnMinMax(
    node: Node,
    index: int,
    minType: YGGridTrackType,
    minValue: float,
    maxType: YGGridTrackType,
    maxValue: float,
) -> None:
    node.style().setGridAutoColumnAt(
        index,
        GridTrackSize.minmax(
            _styleSizeLengthFromTypeAndValue(minType, minValue),
            _styleSizeLengthFromTypeAndValue(maxType, maxValue),
        ),
    )
    node.markDirtyAndPropagate()


# GridAutoRows
def YGNodeStyleSetGridAutoRowsCount(node: Node, count: int) -> None:
    node.style().resizeGridAutoRows(count)
    node.markDirtyAndPropagate()


def YGNodeStyleSetGridAutoRow(
    node: Node, index: int, type: YGGridTrackType, value: float
) -> None:
    node.style().setGridAutoRowAt(index, _gridTrackSizeFromTypeAndValue(type, value))
    node.markDirtyAndPropagate()


def YGNodeStyleSetGridAutoRowMinMax(
    node: Node,
    index: int,
    minType: YGGridTrackType,
    minValue: float,
    maxType: YGGridTrackType,
    maxValue: float,
) -> None:
    node.style().setGridAutoRowAt(
        index,
        GridTrackSize.minmax(
            _styleSizeLengthFromTypeAndValue(minType, minValue),
            _styleSizeLengthFromTypeAndValue(maxType, maxValue),
        ),
    )
    node.markDirtyAndPropagate()
