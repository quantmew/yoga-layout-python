"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from enum import IntEnum, IntFlag


class YGAlign(IntEnum):
    YGAlignAuto = 0
    YGAlignFlexStart = 1
    YGAlignCenter = 2
    YGAlignFlexEnd = 3
    YGAlignStretch = 4
    YGAlignBaseline = 5
    YGAlignSpaceBetween = 6
    YGAlignSpaceAround = 7
    YGAlignSpaceEvenly = 8
    YGAlignStart = 9
    YGAlignEnd = 10


class YGBoxSizing(IntEnum):
    YGBoxSizingBorderBox = 0
    YGBoxSizingContentBox = 1


class YGDimension(IntEnum):
    YGDimensionWidth = 0
    YGDimensionHeight = 1


class YGDirection(IntEnum):
    YGDirectionInherit = 0
    YGDirectionLTR = 1
    YGDirectionRTL = 2


class YGDisplay(IntEnum):
    YGDisplayFlex = 0
    YGDisplayNone = 1
    YGDisplayContents = 2
    YGDisplayGrid = 3


class YGEdge(IntEnum):
    YGEdgeLeft = 0
    YGEdgeTop = 1
    YGEdgeRight = 2
    YGEdgeBottom = 3
    YGEdgeStart = 4
    YGEdgeEnd = 5
    YGEdgeHorizontal = 6
    YGEdgeVertical = 7
    YGEdgeAll = 8


class YGErrata(IntFlag):
    YGErrataNone = 0
    YGErrataStretchFlexBasis = 1
    YGErrataAbsolutePositionWithoutInsetsExcludesPadding = 2
    YGErrataAbsolutePercentAgainstInnerSize = 4
    YGErrataAll = 2147483647
    YGErrataClassic = 2147483646


class YGExperimentalFeature(IntEnum):
    YGExperimentalFeatureWebFlexBasis = 0


class YGFlexDirection(IntEnum):
    YGFlexDirectionColumn = 0
    YGFlexDirectionColumnReverse = 1
    YGFlexDirectionRow = 2
    YGFlexDirectionRowReverse = 3


class YGGridTrackType(IntEnum):
    YGGridTrackTypeAuto = 0
    YGGridTrackTypePoints = 1
    YGGridTrackTypePercent = 2
    YGGridTrackTypeFr = 3
    YGGridTrackTypeMinmax = 4


class YGGutter(IntEnum):
    YGGutterColumn = 0
    YGGutterRow = 1
    YGGutterAll = 2


class YGJustify(IntEnum):
    YGJustifyAuto = 0
    YGJustifyFlexStart = 1
    YGJustifyCenter = 2
    YGJustifyFlexEnd = 3
    YGJustifySpaceBetween = 4
    YGJustifySpaceAround = 5
    YGJustifySpaceEvenly = 6
    YGJustifyStretch = 7
    YGJustifyStart = 8
    YGJustifyEnd = 9


class YGLogLevel(IntEnum):
    YGLogLevelError = 0
    YGLogLevelWarn = 1
    YGLogLevelInfo = 2
    YGLogLevelDebug = 3
    YGLogLevelVerbose = 4
    YGLogLevelFatal = 5


class YGMeasureMode(IntEnum):
    YGMeasureModeUndefined = 0
    YGMeasureModeExactly = 1
    YGMeasureModeAtMost = 2


class YGNodeType(IntEnum):
    YGNodeTypeDefault = 0
    YGNodeTypeText = 1


class YGOverflow(IntEnum):
    YGOverflowVisible = 0
    YGOverflowHidden = 1
    YGOverflowScroll = 2


class YGPositionType(IntEnum):
    YGPositionTypeStatic = 0
    YGPositionTypeRelative = 1
    YGPositionTypeAbsolute = 2


class YGUnit(IntEnum):
    YGUnitUndefined = 0
    YGUnitPoint = 1
    YGUnitPercent = 2
    YGUnitAuto = 3
    YGUnitMaxContent = 4
    YGUnitFitContent = 5
    YGUnitStretch = 6


class YGWrap(IntEnum):
    YGWrapNoWrap = 0
    YGWrapWrap = 1
    YGWrapWrapReverse = 2


def YGAlignToString(value: YGAlign) -> str:
    if value == YGAlign.YGAlignAuto:
        return "auto"
    if value == YGAlign.YGAlignFlexStart:
        return "flex-start"
    if value == YGAlign.YGAlignCenter:
        return "center"
    if value == YGAlign.YGAlignFlexEnd:
        return "flex-end"
    if value == YGAlign.YGAlignStretch:
        return "stretch"
    if value == YGAlign.YGAlignBaseline:
        return "baseline"
    if value == YGAlign.YGAlignSpaceBetween:
        return "space-between"
    if value == YGAlign.YGAlignSpaceAround:
        return "space-around"
    if value == YGAlign.YGAlignSpaceEvenly:
        return "space-evenly"
    if value == YGAlign.YGAlignStart:
        return "start"
    if value == YGAlign.YGAlignEnd:
        return "end"
    return "unknown"


def YGBoxSizingToString(value: YGBoxSizing) -> str:
    if value == YGBoxSizing.YGBoxSizingBorderBox:
        return "border-box"
    if value == YGBoxSizing.YGBoxSizingContentBox:
        return "content-box"
    return "unknown"


def YGDimensionToString(value: YGDimension) -> str:
    if value == YGDimension.YGDimensionWidth:
        return "width"
    if value == YGDimension.YGDimensionHeight:
        return "height"
    return "unknown"


def YGDirectionToString(value: YGDirection) -> str:
    if value == YGDirection.YGDirectionInherit:
        return "inherit"
    if value == YGDirection.YGDirectionLTR:
        return "ltr"
    if value == YGDirection.YGDirectionRTL:
        return "rtl"
    return "unknown"


def YGDisplayToString(value: YGDisplay) -> str:
    if value == YGDisplay.YGDisplayFlex:
        return "flex"
    if value == YGDisplay.YGDisplayNone:
        return "none"
    if value == YGDisplay.YGDisplayContents:
        return "contents"
    if value == YGDisplay.YGDisplayGrid:
        return "grid"
    return "unknown"


def YGEdgeToString(value: YGEdge) -> str:
    if value == YGEdge.YGEdgeLeft:
        return "left"
    if value == YGEdge.YGEdgeTop:
        return "top"
    if value == YGEdge.YGEdgeRight:
        return "right"
    if value == YGEdge.YGEdgeBottom:
        return "bottom"
    if value == YGEdge.YGEdgeStart:
        return "start"
    if value == YGEdge.YGEdgeEnd:
        return "end"
    if value == YGEdge.YGEdgeHorizontal:
        return "horizontal"
    if value == YGEdge.YGEdgeVertical:
        return "vertical"
    if value == YGEdge.YGEdgeAll:
        return "all"
    return "unknown"


def YGErrataToString(value: YGErrata) -> str:
    if value == YGErrata.YGErrataNone:
        return "none"
    if value == YGErrata.YGErrataStretchFlexBasis:
        return "stretch-flex-basis"
    if value == YGErrata.YGErrataAbsolutePositionWithoutInsetsExcludesPadding:
        return "absolute-position-without-insets-excludes-padding"
    if value == YGErrata.YGErrataAbsolutePercentAgainstInnerSize:
        return "absolute-percent-against-inner-size"
    if value == YGErrata.YGErrataAll:
        return "all"
    if value == YGErrata.YGErrataClassic:
        return "classic"
    return "unknown"


def YGExperimentalFeatureToString(value: YGExperimentalFeature) -> str:
    if value == YGExperimentalFeature.YGExperimentalFeatureWebFlexBasis:
        return "web-flex-basis"
    return "unknown"


def YGFlexDirectionToString(value: YGFlexDirection) -> str:
    if value == YGFlexDirection.YGFlexDirectionColumn:
        return "column"
    if value == YGFlexDirection.YGFlexDirectionColumnReverse:
        return "column-reverse"
    if value == YGFlexDirection.YGFlexDirectionRow:
        return "row"
    if value == YGFlexDirection.YGFlexDirectionRowReverse:
        return "row-reverse"
    return "unknown"


def YGGridTrackTypeToString(value: YGGridTrackType) -> str:
    if value == YGGridTrackType.YGGridTrackTypeAuto:
        return "auto"
    if value == YGGridTrackType.YGGridTrackTypePoints:
        return "points"
    if value == YGGridTrackType.YGGridTrackTypePercent:
        return "percent"
    if value == YGGridTrackType.YGGridTrackTypeFr:
        return "fr"
    if value == YGGridTrackType.YGGridTrackTypeMinmax:
        return "minmax"
    return "unknown"


def YGGutterToString(value: YGGutter) -> str:
    if value == YGGutter.YGGutterColumn:
        return "column"
    if value == YGGutter.YGGutterRow:
        return "row"
    if value == YGGutter.YGGutterAll:
        return "all"
    return "unknown"


def YGJustifyToString(value: YGJustify) -> str:
    if value == YGJustify.YGJustifyAuto:
        return "auto"
    if value == YGJustify.YGJustifyFlexStart:
        return "flex-start"
    if value == YGJustify.YGJustifyCenter:
        return "center"
    if value == YGJustify.YGJustifyFlexEnd:
        return "flex-end"
    if value == YGJustify.YGJustifySpaceBetween:
        return "space-between"
    if value == YGJustify.YGJustifySpaceAround:
        return "space-around"
    if value == YGJustify.YGJustifySpaceEvenly:
        return "space-evenly"
    if value == YGJustify.YGJustifyStretch:
        return "stretch"
    if value == YGJustify.YGJustifyStart:
        return "start"
    if value == YGJustify.YGJustifyEnd:
        return "end"
    return "unknown"


def YGLogLevelToString(value: YGLogLevel) -> str:
    if value == YGLogLevel.YGLogLevelError:
        return "error"
    if value == YGLogLevel.YGLogLevelWarn:
        return "warn"
    if value == YGLogLevel.YGLogLevelInfo:
        return "info"
    if value == YGLogLevel.YGLogLevelDebug:
        return "debug"
    if value == YGLogLevel.YGLogLevelVerbose:
        return "verbose"
    if value == YGLogLevel.YGLogLevelFatal:
        return "fatal"
    return "unknown"


def YGMeasureModeToString(value: YGMeasureMode) -> str:
    if value == YGMeasureMode.YGMeasureModeUndefined:
        return "undefined"
    if value == YGMeasureMode.YGMeasureModeExactly:
        return "exactly"
    if value == YGMeasureMode.YGMeasureModeAtMost:
        return "at-most"
    return "unknown"


def YGNodeTypeToString(value: YGNodeType) -> str:
    if value == YGNodeType.YGNodeTypeDefault:
        return "default"
    if value == YGNodeType.YGNodeTypeText:
        return "text"
    return "unknown"


def YGOverflowToString(value: YGOverflow) -> str:
    if value == YGOverflow.YGOverflowVisible:
        return "visible"
    if value == YGOverflow.YGOverflowHidden:
        return "hidden"
    if value == YGOverflow.YGOverflowScroll:
        return "scroll"
    return "unknown"


def YGPositionTypeToString(value: YGPositionType) -> str:
    if value == YGPositionType.YGPositionTypeStatic:
        return "static"
    if value == YGPositionType.YGPositionTypeRelative:
        return "relative"
    if value == YGPositionType.YGPositionTypeAbsolute:
        return "absolute"
    return "unknown"


def YGUnitToString(value: YGUnit) -> str:
    if value == YGUnit.YGUnitUndefined:
        return "undefined"
    if value == YGUnit.YGUnitPoint:
        return "point"
    if value == YGUnit.YGUnitPercent:
        return "percent"
    if value == YGUnit.YGUnitAuto:
        return "auto"
    if value == YGUnit.YGUnitMaxContent:
        return "max-content"
    if value == YGUnit.YGUnitFitContent:
        return "fit-content"
    if value == YGUnit.YGUnitStretch:
        return "stretch"
    return "unknown"


def YGWrapToString(value: YGWrap) -> str:
    if value == YGWrap.YGWrapNoWrap:
        return "no-wrap"
    if value == YGWrap.YGWrapWrap:
        return "wrap"
    if value == YGWrap.YGWrapWrapReverse:
        return "wrap-reverse"
    return "unknown"
