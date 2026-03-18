"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from ..algorithm.FlexDirection import (
    dimension,
    inlineEndEdge,
    inlineStartEdge,
    isRow,
    resolveCrossDirection,
    resolveDirection as resolveFlexDirection,
)
from ..YGEnums import (
    YGAlign,
    YGBoxSizing,
    YGDimension,
    YGDirection,
    YGDisplay,
    YGEdge,
    YGFlexDirection,
    YGMeasureMode,
    YGNodeType,
    YGPositionType,
)
from ..config.Config import Config, configUpdateInvalidatesLayout, getDefaultConfig
from ..debug.AssertFatal import assertFatal, assertFatalWithConfig, assertFatalWithNode
from ..debug.Log import log
from ..YGEnums import YGLogLevel
from ..numeric.Comparison import inexactEquals, isDefined, isUndefined, maxOrDefined
from ..numeric.FloatOptional import FloatOptional
from ..style.Style import Style
from ..style.StyleSizeLength import StyleSizeLength, inexactEquals as inexactEqualsStyleSizeLength
from .LayoutableChildren import LayoutableChildren
from .LayoutResults import LayoutResults


MeasureFunc = Callable[["Node", float, YGMeasureMode, float, YGMeasureMode], Any]
BaselineFunc = Callable[["Node", float, float], float]
DirtiedFunc = Callable[["Node"], None]


def _coerce_measure_result(size: Any):
    if hasattr(size, "width") and hasattr(size, "height"):
        width = size.width
        height = size.height
    elif isinstance(size, dict):
        width = size["width"]
        height = size["height"]
    elif isinstance(size, (list, tuple)) and len(size) == 2:
        width, height = size
    else:
        raise TypeError(
            "Measure function must return an object with width/height, a mapping with "
            "'width'/'height', or a 2-item sequence."
        )

    from ..YGNode import YGSize

    return YGSize(width=float(width), height=float(height))


@dataclass(eq=False)
class Node:
    hasNewLayout_: bool = True
    isReferenceBaseline_: bool = False
    isDirty_: bool = True
    alwaysFormsContainingBlock_: bool = False
    nodeType_: YGNodeType = YGNodeType.YGNodeTypeDefault
    context_: Any = None
    measureFunc_: MeasureFunc | None = None
    baselineFunc_: BaselineFunc | None = None
    dirtiedFunc_: DirtiedFunc | None = None
    style_: Style = field(default_factory=Style)
    layout_: LayoutResults = field(default_factory=LayoutResults)
    lineIndex_: int = 0
    contentsChildrenCount_: int = 0
    owner_: "Node | None" = None
    children_: list["Node"] = field(default_factory=list)
    config_: Config = field(default_factory=getDefaultConfig)
    processedDimensions_: dict[YGDimension, StyleSizeLength] = field(
        default_factory=lambda: {
            YGDimension.YGDimensionWidth: StyleSizeLength.undefined(),
            YGDimension.YGDimensionHeight: StyleSizeLength.undefined(),
        }
    )

    def __post_init__(self) -> None:
        if self.config_ is None:
            raise ValueError("Attempting to construct Node with null config")
        if self.config_.useWebDefaults():
            self.useWebDefaults()

    def useWebDefaults(self) -> None:
        self.style_.setFlexDirection(YGFlexDirection.YGFlexDirectionRow)
        self.style_.setAlignContent(YGAlign.YGAlignStretch)

    def getContext(self) -> Any:
        return self.context_

    def alwaysFormsContainingBlock(self) -> bool:
        return self.alwaysFormsContainingBlock_

    def getHasNewLayout(self) -> bool:
        return self.hasNewLayout_

    def getNodeType(self) -> YGNodeType:
        return self.nodeType_

    def hasMeasureFunc(self) -> bool:
        return self.measureFunc_ is not None

    def measure(
        self,
        availableWidth: float,
        widthMode: YGMeasureMode,
        availableHeight: float,
        heightMode: YGMeasureMode,
    ):
        assert self.measureFunc_ is not None
        size = _coerce_measure_result(
            self.measureFunc_(self, availableWidth, widthMode, availableHeight, heightMode)
        )

        if isUndefined(size.height) or size.height < 0 or isUndefined(size.width) or size.width < 0:
            log(
                self,
                YGLogLevel.YGLogLevelWarn,
                "Measure function returned an invalid dimension to Yoga: [width=%f, height=%f]",
                size.width,
                size.height,
            )
            from ..YGNode import YGSize

            return YGSize(
                width=maxOrDefined(0.0, size.width),
                height=maxOrDefined(0.0, size.height),
            )

        return size

    def hasBaselineFunc(self) -> bool:
        return self.baselineFunc_ is not None

    def baseline(self, width: float, height: float) -> float:
        assert self.baselineFunc_ is not None
        return self.baselineFunc_(self, width, height)

    def dimensionWithMargin(self, axis: YGFlexDirection, widthSize: float) -> float:
        return self.getLayout().measuredDimension(
            YGDimension.YGDimensionWidth if isRow(axis) else YGDimension.YGDimensionHeight
        ) + self.style_.computeMarginForAxis(axis, widthSize)

    def isLayoutDimensionDefined(self, axis: YGFlexDirection) -> bool:
        value = self.getLayout().measuredDimension(
            YGDimension.YGDimensionWidth if isRow(axis) else YGDimension.YGDimensionHeight
        )
        return isDefined(value) and value >= 0.0

    def hasContentsChildren(self) -> bool:
        return self.contentsChildrenCount_ != 0

    def getDirtiedFunc(self) -> DirtiedFunc | None:
        return self.dirtiedFunc_

    def style(self) -> Style:
        return self.style_

    def getLayout(self) -> LayoutResults:
        return self.layout_

    def getLineIndex(self) -> int:
        return self.lineIndex_

    def isReferenceBaseline(self) -> bool:
        return self.isReferenceBaseline_

    def getOwner(self) -> "Node | None":
        return self.owner_

    def getChildren(self) -> list["Node"]:
        return self.children_

    def getChild(self, index: int) -> "Node":
        return self.children_[index]

    def getChildCount(self) -> int:
        return len(self.children_)

    def getLayoutChildren(self):
        return LayoutableChildren(self)

    def getLayoutChildCount(self) -> int:
        return sum(1 for _ in self.getLayoutChildren())

    def getConfig(self) -> Config:
        return self.config_

    def isDirty(self) -> bool:
        return self.isDirty_

    def getProcessedDimension(self, dimension: YGDimension) -> StyleSizeLength:
        return self.processedDimensions_[dimension]

    def hasDefiniteLength(self, dimension: YGDimension, ownerSize: float) -> bool:
        usedValue = self.getProcessedDimension(dimension).resolve(ownerSize)
        return usedValue.isDefined() and usedValue.unwrap() >= 0.0

    def hasErrata(self, errata) -> bool:
        return self.config_.hasErrata(errata)

    def getResolvedDimension(
        self,
        direction: YGDirection,
        dimension: YGDimension,
        referenceLength: float,
        ownerWidth: float,
    ) -> FloatOptional:
        value = self.getProcessedDimension(dimension).resolve(referenceLength)
        if self.style_.boxSizing() == YGBoxSizing.YGBoxSizingBorderBox:
            return value

        dimensionPaddingAndBorder = FloatOptional(
            self.style_.computePaddingAndBorderForDimension(direction, dimension, ownerWidth)
        )
        return value + (
            dimensionPaddingAndBorder if dimensionPaddingAndBorder.isDefined() else FloatOptional(0.0)
        )

    def setContext(self, context: Any) -> None:
        self.context_ = context

    def setAlwaysFormsContainingBlock(self, value: bool) -> None:
        self.alwaysFormsContainingBlock_ = value

    def setHasNewLayout(self, value: bool) -> None:
        self.hasNewLayout_ = value

    def setNodeType(self, value: YGNodeType) -> None:
        self.nodeType_ = value

    def setMeasureFunc(self, measureFunc: MeasureFunc | None) -> None:
        if measureFunc is None:
            # TODO: t18095186 Move nodeType to opt-in function and mark appropriate
            # places in Litho
            self.setNodeType(YGNodeType.YGNodeTypeDefault)
        else:
            assertFatalWithNode(
                self,
                not self.children_,
                "Cannot set measure function: Nodes with measure functions cannot have children.",
            )
            # TODO: t18095186 Move nodeType to opt-in function and mark appropriate
            # places in Litho
            self.setNodeType(YGNodeType.YGNodeTypeText)
        self.measureFunc_ = measureFunc

    def setBaselineFunc(self, baselineFunc: BaselineFunc | None) -> None:
        self.baselineFunc_ = baselineFunc

    def setDirtiedFunc(self, dirtiedFunc: DirtiedFunc | None) -> None:
        self.dirtiedFunc_ = dirtiedFunc

    def setStyle(self, style: Style) -> None:
        self.style_ = style

    def setLayout(self, layout: LayoutResults) -> None:
        self.layout_ = layout

    def setLineIndex(self, lineIndex: int) -> None:
        self.lineIndex_ = lineIndex

    def setIsReferenceBaseline(self, value: bool) -> None:
        self.isReferenceBaseline_ = value

    def setOwner(self, owner: "Node | None") -> None:
        self.owner_ = owner

    def setConfig(self, config: Config) -> None:
        assertFatal(config is not None, "Attempting to set a null config on a Node")
        assertFatalWithConfig(
            config,
            config.useWebDefaults() == self.config_.useWebDefaults(),
            "UseWebDefaults may not be changed after constructing a Node",
        )
        if configUpdateInvalidatesLayout(self.config_, config):
            self.markDirtyAndPropagate()
            self.layout_.configVersion = 0
        else:
            # If the config is functionally the same, then align the configVersion so
            # that we can reuse the layout cache
            self.layout_.configVersion = config.getVersion()
        self.config_ = config

    def setDirty(self, isDirty: bool) -> None:
        if self.isDirty_ == isDirty:
            return
        self.isDirty_ = isDirty
        if isDirty and self.dirtiedFunc_ is not None:
            self.dirtiedFunc_(self)

    def setChildren(self, children: list["Node"]) -> None:
        self.children_ = children
        self.contentsChildrenCount_ = 0
        for child in children:
            if child.style().display() == YGDisplay.YGDisplayContents:
                self.contentsChildrenCount_ += 1

    def setLayoutLastOwnerDirection(self, direction: YGDirection) -> None:
        self.layout_.lastOwnerDirection = direction

    def setLayoutComputedFlexBasis(self, computedFlexBasis: FloatOptional) -> None:
        self.layout_.computedFlexBasis = computedFlexBasis

    def setLayoutComputedFlexBasisGeneration(self, generation: int) -> None:
        self.layout_.computedFlexBasisGeneration = generation

    def setLayoutMeasuredDimension(self, measuredDimension: float, dimension: YGDimension) -> None:
        self.layout_.setMeasuredDimension(dimension, measuredDimension)

    def setLayoutHadOverflow(self, hadOverflow: bool) -> None:
        self.layout_.setHadOverflow(hadOverflow)

    def setLayoutDimension(self, value: float, dimension: YGDimension) -> None:
        self.layout_.setDimension(dimension, value)
        self.layout_.setRawDimension(dimension, value)

    def setLayoutDirection(self, direction: YGDirection) -> None:
        self.layout_.setDirection(direction)

    def setLayoutMargin(self, margin: float, edge: YGEdge) -> None:
        self.layout_.setMargin(edge, margin)

    def setLayoutBorder(self, border: float, edge: YGEdge) -> None:
        self.layout_.setBorder(edge, border)

    def setLayoutPadding(self, padding: float, edge: YGEdge) -> None:
        self.layout_.setPadding(edge, padding)

    def setLayoutPosition(self, position: float, edge: YGEdge) -> None:
        self.layout_.setPosition(edge, position)

    def processFlexBasis(self) -> StyleSizeLength:
        flexBasis = self.style_.flexBasis()
        if not flexBasis.isAuto() and not flexBasis.isUndefined():
            return flexBasis
        if self.style_.flex().isDefined() and self.style_.flex().unwrap() > 0.0:
            return StyleSizeLength.ofAuto() if self.config_.useWebDefaults() else StyleSizeLength.points(0)
        return StyleSizeLength.ofAuto()

    def resolveFlexBasis(
        self,
        direction: YGDirection,
        flexDirection: YGFlexDirection,
        referenceLength: float,
        ownerWidth: float,
    ) -> FloatOptional:
        value = self.processFlexBasis().resolve(referenceLength)
        if self.style_.boxSizing() == YGBoxSizing.YGBoxSizingBorderBox:
            return value
        dim = dimension(flexDirection)
        dimensionPaddingAndBorder = FloatOptional(
            self.style_.computePaddingAndBorderForDimension(direction, dim, ownerWidth)
        )
        return value + (
            dimensionPaddingAndBorder if dimensionPaddingAndBorder.isDefined() else FloatOptional(0.0)
        )

    def processDimensions(self) -> None:
        for dimension in (YGDimension.YGDimensionWidth, YGDimension.YGDimensionHeight):
            if (
                self.style_.maxDimension(dimension).isDefined()
                and inexactEqualsStyleSizeLength(
                    self.style_.maxDimension(dimension), self.style_.minDimension(dimension)
                )
            ):
                self.processedDimensions_[dimension] = self.style_.maxDimension(dimension)
            else:
                self.processedDimensions_[dimension] = self.style_.dimension(dimension)

    def resolveDirection(self, ownerDirection: YGDirection) -> YGDirection:
        if self.style_.direction() == YGDirection.YGDirectionInherit:
            return ownerDirection if ownerDirection != YGDirection.YGDirectionInherit else YGDirection.YGDirectionLTR
        return self.style_.direction()

    # If both left and right are defined, then use left. Otherwise return +left or
    # -right depending on which is defined. Ignore statically positioned nodes as
    # insets do not apply to them.
    def relativePosition(self, axis: YGFlexDirection, direction: YGDirection, axisSize: float) -> float:
        if self.style_.positionType() == YGPositionType.YGPositionTypeStatic:
            return 0.0
        if self.style_.isInlineStartPositionDefined(axis, direction) and not self.style_.isInlineStartPositionAuto(axis, direction):
            return self.style_.computeInlineStartPosition(axis, direction, axisSize)
        return -1.0 * self.style_.computeInlineEndPosition(axis, direction, axisSize)

    def setPosition(self, direction: YGDirection, ownerWidth: float, ownerHeight: float) -> None:
        # Root nodes should be always layouted as LTR, so we don't return negative
        # values.
        directionRespectingRoot = direction if self.owner_ is not None else YGDirection.YGDirectionLTR
        mainAxis = resolveFlexDirection(self.style_.flexDirection(), directionRespectingRoot)
        crossAxis = resolveCrossDirection(mainAxis, directionRespectingRoot)
        # In the case of position static these are just 0. See:
        # https://www.w3.org/TR/css-position-3/#valdef-position-static
        relativePositionMain = self.relativePosition(
            mainAxis,
            directionRespectingRoot,
            ownerWidth if isRow(mainAxis) else ownerHeight,
        )
        relativePositionCross = self.relativePosition(
            crossAxis,
            directionRespectingRoot,
            ownerHeight if isRow(mainAxis) else ownerWidth,
        )
        mainAxisLeadingEdge = inlineStartEdge(mainAxis, direction)
        mainAxisTrailingEdge = inlineEndEdge(mainAxis, direction)
        crossAxisLeadingEdge = inlineStartEdge(crossAxis, direction)
        crossAxisTrailingEdge = inlineEndEdge(crossAxis, direction)
        self.setLayoutPosition(
            self.style_.computeInlineStartMargin(mainAxis, direction, ownerWidth) + relativePositionMain,
            mainAxisLeadingEdge,
        )
        self.setLayoutPosition(
            self.style_.computeInlineEndMargin(mainAxis, direction, ownerWidth) + relativePositionMain,
            mainAxisTrailingEdge,
        )
        self.setLayoutPosition(
            self.style_.computeInlineStartMargin(crossAxis, direction, ownerWidth) + relativePositionCross,
            crossAxisLeadingEdge,
        )
        self.setLayoutPosition(
            self.style_.computeInlineEndMargin(crossAxis, direction, ownerWidth) + relativePositionCross,
            crossAxisTrailingEdge,
        )

    def clearChildren(self) -> None:
        self.children_.clear()
        self.contentsChildrenCount_ = 0

    def replaceChild(self, child_or_old_child: "Node", index_or_new_child) -> None:
        if isinstance(index_or_new_child, int):
            child = child_or_old_child
            index = index_or_new_child
            previousChild = self.children_[index]
            if (
                previousChild.style().display() == YGDisplay.YGDisplayContents
                and child.style().display() != YGDisplay.YGDisplayContents
            ):
                self.contentsChildrenCount_ -= 1
            elif (
                previousChild.style().display() != YGDisplay.YGDisplayContents
                and child.style().display() == YGDisplay.YGDisplayContents
            ):
                self.contentsChildrenCount_ += 1

            self.children_[index] = child
            return

        oldChild = child_or_old_child
        newChild = index_or_new_child
        if (
            oldChild.style().display() == YGDisplay.YGDisplayContents
            and newChild.style().display() != YGDisplay.YGDisplayContents
        ):
            self.contentsChildrenCount_ -= 1
        elif (
            oldChild.style().display() != YGDisplay.YGDisplayContents
            and newChild.style().display() == YGDisplay.YGDisplayContents
        ):
            self.contentsChildrenCount_ += 1

        for index, child in enumerate(self.children_):
            if child == oldChild:
                self.children_[index] = newChild
                break

    def insertChild(self, child: "Node", index: int) -> None:
        self.children_.insert(index, child)
        if child.style().display() == YGDisplay.YGDisplayContents:
            self.contentsChildrenCount_ += 1

    def removeChild(self, child_or_index) -> bool:
        if isinstance(child_or_index, int):
            child = self.children_[child_or_index]
            if child.style().display() == YGDisplay.YGDisplayContents:
                self.contentsChildrenCount_ -= 1
            del self.children_[child_or_index]
            return True

        child = child_or_index
        if child in self.children_:
            if child.style().display() == YGDisplay.YGDisplayContents:
                self.contentsChildrenCount_ -= 1
            self.children_.remove(child)
            return True
        return False

    def cloneChildrenIfNeeded(self) -> None:
        for index, child in enumerate(self.children_):
            if child.getOwner() != self:
                child = self.config_.cloneNode(child, self, index)
                self.children_[index] = child
                child.setOwner(self)

                if child.hasContentsChildren():
                    child.cloneContentsChildrenIfNeeded()

    def cloneContentsChildrenIfNeeded(self) -> None:
        for index, child in enumerate(self.children_):
            if child.style().display() == YGDisplay.YGDisplayContents and child.getOwner() != self:
                child = self.config_.cloneNode(child, self, index)
                self.children_[index] = child
                child.setOwner(self)
                child.cloneChildrenIfNeeded()

    def markDirtyAndPropagate(self) -> None:
        if not self.isDirty_:
            self.setDirty(True)
            self.setLayoutComputedFlexBasis(FloatOptional())
            if self.owner_ is not None:
                self.owner_.markDirtyAndPropagate()

    def resolveFlexGrow(self) -> float:
        # Root nodes flexGrow should always be 0
        if self.owner_ is None:
            return 0.0
        if self.style_.flexGrow().isDefined():
            return self.style_.flexGrow().unwrap()
        if self.style_.flex().isDefined() and self.style_.flex().unwrap() > 0.0:
            return self.style_.flex().unwrap()
        return Style.DefaultFlexGrow

    def resolveFlexShrink(self) -> float:
        if self.owner_ is None:
            return 0.0
        if self.style_.flexShrink().isDefined():
            return self.style_.flexShrink().unwrap()
        if not self.config_.useWebDefaults() and self.style_.flex().isDefined() and self.style_.flex().unwrap() < 0.0:
            return -self.style_.flex().unwrap()
        return Style.WebDefaultFlexShrink if self.config_.useWebDefaults() else Style.DefaultFlexShrink

    def isNodeFlexible(self) -> bool:
        return self.style_.positionType() != YGPositionType.YGPositionTypeAbsolute and (
            self.resolveFlexGrow() != 0.0 or self.resolveFlexShrink() != 0.0
        )

    def reset(self) -> None:
        assertFatalWithNode(
            self,
            not self.children_,
            "Cannot reset a node which still has children attached",
        )
        assertFatalWithNode(
            self,
            self.owner_ is None,
            "Cannot reset a node still attached to a owner",
        )
        replacement = Node(config_=self.config_)
        for field_name in self.__dataclass_fields__:
            setattr(self, field_name, getattr(replacement, field_name))
