"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..algorithm.FlexDirection import isColumn
from ..YGEnums import YGAlign, YGDisplay, YGJustify

if TYPE_CHECKING:
    from ..node.Node import Node


def resolveChildAlignment(node: Node, child: Node) -> YGAlign:
    align = node.style().alignItems() if child.style().alignSelf() == YGAlign.YGAlignAuto else child.style().alignSelf()
    if node.style().display() == YGDisplay.YGDisplayFlex and align == YGAlign.YGAlignBaseline and isColumn(node.style().flexDirection()):
        return YGAlign.YGAlignFlexStart
    return align  # type: ignore[return-value]


def resolveChildJustification(node: Node, child: Node) -> YGJustify:
    return node.style().justifyItems() if child.style().justifySelf() == YGJustify.YGJustifyAuto else child.style().justifySelf()  # type: ignore[return-value]


def fallbackAlignment(align: YGAlign | YGJustify) -> YGAlign | YGJustify:
    if align in (YGAlign.YGAlignSpaceBetween, YGAlign.YGAlignStretch):
        return YGAlign.YGAlignFlexStart
    if align in (YGAlign.YGAlignSpaceAround, YGAlign.YGAlignSpaceEvenly):
        return YGAlign.YGAlignFlexStart
    if align == YGJustify.YGJustifySpaceBetween:
        return YGJustify.YGJustifyFlexStart
    if align in (YGJustify.YGJustifySpaceAround, YGJustify.YGJustifySpaceEvenly):
        return YGJustify.YGJustifyFlexStart
    return align  # type: ignore[return-value]
