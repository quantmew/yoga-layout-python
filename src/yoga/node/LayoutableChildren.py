"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from ..YGEnums import YGDisplay


class LayoutableChildren:
    class Iterator:
        def __init__(self, node=None, childIndex: int = 0, backtrack=None):
            self.node_ = node
            self.childIndex_ = childIndex
            self.backtrack_ = [] if backtrack is None else list(backtrack)

        def __iter__(self):
            return self

        def __next__(self):
            if self.node_ is None:
                raise StopIteration
            current = self.node_.getChild(self.childIndex_)
            self.next()
            return current

        def __eq__(self, other):
            return self.node_ is other.node_ and self.childIndex_ == other.childIndex_

        def __ne__(self, other):
            return not self == other

        def copy(self):
            return LayoutableChildren.Iterator(self.node_, self.childIndex_, self.backtrack_)

        def next(self):
            if self.node_ is None:
                return
            if self.childIndex_ + 1 >= self.node_.getChildCount():
                if not self.backtrack_:
                    self.node_ = None
                    self.childIndex_ = 0
                else:
                    self.node_, self.childIndex_ = self.backtrack_.pop(0)
                    self.next()
            else:
                self.childIndex_ += 1
                if self.node_.getChild(self.childIndex_).style().display() == YGDisplay.YGDisplayContents:
                    self.skipContentsNodes()

        def skipContentsNodes(self):
            currentNode = self.node_.getChild(self.childIndex_)
            while currentNode.style().display() == YGDisplay.YGDisplayContents and currentNode.getChildCount() > 0:
                self.backtrack_.insert(0, (self.node_, self.childIndex_))
                self.node_ = currentNode
                self.childIndex_ = 0
                currentNode = currentNode.getChild(self.childIndex_)
            if currentNode.style().display() == YGDisplay.YGDisplayContents:
                self.next()

    def __init__(self, node):
        self.node_ = node

    def __iter__(self):
        return self.begin()

    def begin(self):
        if self.node_.getChildCount() > 0:
            result = LayoutableChildren.Iterator(self.node_, 0)
            if self.node_.getChild(0).style().display() == YGDisplay.YGDisplayContents:
                result.skipContentsNodes()
            return result
        return self.end()

    def end(self):
        return LayoutableChildren.Iterator()
