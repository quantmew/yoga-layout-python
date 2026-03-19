"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass

from .algorithm.Cache import canUseCachedMeasurement
from .algorithm.CalculateLayout import calculateLayout
from .algorithm.SizingMode import sizingMode
from .debug.AssertFatal import assertFatal, assertFatalWithNode
from .event.event import Event, NodeAllocationData, NodeDeallocationData
from .node.LayoutResults import LayoutResults
from .node.Node import Node
from .YGConfig import YGConfigGetDefault
from .YGEnums import YGDirection, YGMeasureMode, YGNodeType

YGNodeRef = Node
YGNodeConstRef = Node


@dataclass
class YGSize:
    width: float
    height: float


def YGNodeNew() -> YGNodeRef:
    return YGNodeNewWithConfig(YGConfigGetDefault())


def YGNodeNewWithConfig(config) -> YGNodeRef:
    assertFatal(config is not None, "Tried to construct YGNode with null config")
    node = Node(config_=config)
    Event.publish(node, Event.NodeAllocation, NodeAllocationData(config))
    return node


def YGNodeClone(oldNodeRef: YGNodeConstRef) -> YGNodeRef:
    oldNode = oldNodeRef
    node = Node(config_=oldNode.getConfig())
    node.hasNewLayout_ = oldNode.hasNewLayout_
    node.isReferenceBaseline_ = oldNode.isReferenceBaseline_
    node.isDirty_ = oldNode.isDirty_
    node.alwaysFormsContainingBlock_ = oldNode.alwaysFormsContainingBlock_
    node.nodeType_ = oldNode.nodeType_
    node.context_ = oldNode.context_
    node.measureFunc_ = oldNode.measureFunc_
    node.baselineFunc_ = oldNode.baselineFunc_
    node.dirtiedFunc_ = oldNode.dirtiedFunc_
    node.style_ = deepcopy(oldNode.style_)
    node.layout_ = deepcopy(oldNode.layout_)
    node.lineIndex_ = oldNode.lineIndex_
    node.setChildren(list(oldNode.children_))
    node.config_ = oldNode.config_
    node.processedDimensions_ = deepcopy(oldNode.processedDimensions_)
    node.owner_ = None
    Event.publish(node, Event.NodeAllocation, NodeAllocationData(node.getConfig()))
    return node


def YGNodeFree(nodeRef: YGNodeRef) -> None:
    node = nodeRef

    owner = node.getOwner()
    if owner is not None:
        owner.removeChild(node)
        node.setOwner(None)

    childCount = node.getChildCount()
    for i in range(childCount):
        child = node.getChild(i)
        child.setOwner(None)

    node.clearChildren()
    Event.publish(node, Event.NodeDeallocation, NodeDeallocationData(YGNodeGetConfig(node)))


def YGNodeFreeRecursive(rootRef: YGNodeRef) -> None:
    root = rootRef

    skipped = 0
    while root.getChildCount() > skipped:
        child = root.getChild(skipped)
        if child.getOwner() != root:
            # Don't free shared nodes that we don't own.
            skipped += 1
        else:
            YGNodeRemoveChild(root, child)
            YGNodeFreeRecursive(child)
    YGNodeFree(root)


def YGNodeFinalize(node: YGNodeRef) -> None:
    Event.publish(node, Event.NodeDeallocation, NodeDeallocationData(YGNodeGetConfig(node)))
    del node


def YGNodeReset(node: YGNodeRef) -> None:
    node.reset()


def YGNodeCalculateLayout(
    node: YGNodeRef, ownerWidth: float, ownerHeight: float, ownerDirection: YGDirection
) -> None:
    calculateLayout(node, ownerWidth, ownerHeight, ownerDirection)


def YGNodeGetHasNewLayout(node: YGNodeConstRef) -> bool:
    return node.getHasNewLayout()


def YGNodeSetHasNewLayout(node: YGNodeRef, hasNewLayout: bool) -> None:
    node.setHasNewLayout(hasNewLayout)


def YGNodeIsDirty(node: YGNodeConstRef) -> bool:
    return node.isDirty()


def YGNodeMarkDirty(nodeRef: YGNodeRef) -> None:
    assertFatalWithNode(
        nodeRef,
        nodeRef.hasMeasureFunc(),
        "Only leaf nodes with custom measure functions should manually mark themselves as dirty",
    )
    nodeRef.markDirtyAndPropagate()


def YGNodeSetDirtiedFunc(node: YGNodeRef, dirtiedFunc) -> None:
    node.setDirtiedFunc(dirtiedFunc)


def YGNodeGetDirtiedFunc(node: YGNodeConstRef):
    return node.getDirtiedFunc()


def YGNodeInsertChild(ownerRef: YGNodeRef, childRef: YGNodeRef, index: int) -> None:
    owner = ownerRef
    child = childRef

    assertFatalWithNode(
        owner,
        child.getOwner() is None,
        "Child already has an owner, it must be removed first.",
    )
    assertFatalWithNode(
        owner,
        not owner.hasMeasureFunc(),
        "Cannot add child: Nodes with measure functions cannot have children.",
    )
    owner.insertChild(child, index)
    child.setOwner(owner)
    owner.markDirtyAndPropagate()


def YGNodeSwapChild(ownerRef: YGNodeRef, childRef: YGNodeRef, index: int) -> None:
    owner = ownerRef
    child = childRef

    owner.replaceChild(child, index)
    child.setOwner(owner)


def YGNodeRemoveChild(ownerRef: YGNodeRef, excludedChildRef: YGNodeRef) -> None:
    owner = ownerRef
    excludedChild = excludedChildRef

    if owner.getChildCount() == 0:
        # This is an empty set. Nothing to remove.
        return

    # Children may be shared between parents, which is indicated by not having an
    # owner. We only want to reset the child completely if it is owned
    # exclusively by one node.
    childOwner = excludedChild.getOwner()
    if owner.removeChild(excludedChild):
        if owner == childOwner:
            excludedChild.setLayout(LayoutResults())
            excludedChild.setOwner(None)
            # Mark dirty to invalidate cache, but suppress the dirtied callback
            # since the node is being detached from the tree and should not
            # propagate dirty signals through external callback mechanisms.
            dirtiedFunc = excludedChild.getDirtiedFunc()
            excludedChild.setDirtiedFunc(None)
            excludedChild.setDirty(True)
            excludedChild.setDirtiedFunc(dirtiedFunc)
        owner.markDirtyAndPropagate()


def YGNodeRemoveAllChildren(ownerRef: YGNodeRef) -> None:
    owner = ownerRef

    childCount = owner.getChildCount()
    if childCount == 0:
        # This is an empty set already. Nothing to do.
        return

    firstChild = owner.getChild(0)
    if firstChild.getOwner() == owner:
        # If the first child has this node as its owner, we assume that this child
        # set is unique.
        for index in range(childCount):
            oldChild = owner.getChild(index)
            oldChild.setLayout(LayoutResults())
            oldChild.setOwner(None)
            # Mark dirty to invalidate cache, but suppress the dirtied callback
            # since the node is being detached from the tree and should not
            # propagate dirty signals through external callback mechanisms.
            dirtiedFunc = oldChild.getDirtiedFunc()
            oldChild.setDirtiedFunc(None)
            oldChild.setDirty(True)
            oldChild.setDirtiedFunc(dirtiedFunc)
        owner.clearChildren()
        owner.markDirtyAndPropagate()
        return

    # Otherwise, we are not the owner of the child set. We don't have to do
    # anything to clear it.
    owner.setChildren([])
    owner.markDirtyAndPropagate()


def YGNodeSetChildren(ownerRef: YGNodeRef, childrenRefs, count: int) -> None:
    owner = ownerRef
    children = [] if childrenRefs is None else list(childrenRefs[:count])

    if owner is None:
        return

    if not children:
        if owner.getChildCount() > 0:
            for child in owner.getChildren():
                child.setLayout(LayoutResults())
                child.setOwner(None)
            owner.setChildren([])
            owner.markDirtyAndPropagate()
    else:
        if owner.getChildCount() > 0:
            for oldChild in owner.getChildren():
                # Our new children may have nodes in common with the old children. We
                # don't reset these common nodes.
                if oldChild not in children:
                    oldChild.setLayout(LayoutResults())
                    oldChild.setOwner(None)
        owner.setChildren(children)
        for child in children:
            child.setOwner(owner)
        owner.markDirtyAndPropagate()


def YGNodeGetChild(nodeRef: YGNodeRef, index: int) -> YGNodeRef | None:
    node = nodeRef

    if index < node.getChildCount():
        return node.getChild(index)
    return None


def YGNodeGetChildCount(node: YGNodeConstRef) -> int:
    return len(node.getChildren())


def YGNodeGetOwner(node: YGNodeRef):
    return node.getOwner()


def YGNodeGetParent(node: YGNodeRef):
    return node.getOwner()


def YGNodeSetConfig(node: YGNodeRef, config) -> None:
    node.setConfig(config)


def YGNodeGetConfig(node: YGNodeRef):
    return node.getConfig()


def YGNodeSetContext(node: YGNodeRef, context: object) -> None:
    node.setContext(context)


def YGNodeGetContext(node: YGNodeConstRef) -> object:
    return node.getContext()


def YGNodeSetMeasureFunc(node: YGNodeRef, measureFunc) -> None:
    node.setMeasureFunc(measureFunc)


def YGNodeHasMeasureFunc(node: YGNodeConstRef) -> bool:
    return node.hasMeasureFunc()


def YGNodeSetBaselineFunc(node: YGNodeRef, baselineFunc) -> None:
    node.setBaselineFunc(baselineFunc)


def YGNodeHasBaselineFunc(node: YGNodeConstRef) -> bool:
    return node.hasBaselineFunc()


def YGNodeSetIsReferenceBaseline(nodeRef: YGNodeRef, isReferenceBaseline: bool) -> None:
    if nodeRef.isReferenceBaseline() != isReferenceBaseline:
        nodeRef.setIsReferenceBaseline(isReferenceBaseline)
        nodeRef.markDirtyAndPropagate()


def YGNodeIsReferenceBaseline(node: YGNodeConstRef) -> bool:
    return node.isReferenceBaseline()


def YGNodeSetNodeType(node: YGNodeRef, nodeType: YGNodeType) -> None:
    node.setNodeType(nodeType)


def YGNodeGetNodeType(node: YGNodeConstRef) -> YGNodeType:
    return node.getNodeType()


def YGNodeSetAlwaysFormsContainingBlock(node: YGNodeRef, alwaysFormsContainingBlock: bool) -> None:
    node.setAlwaysFormsContainingBlock(alwaysFormsContainingBlock)


def YGNodeGetAlwaysFormsContainingBlock(node: YGNodeConstRef) -> bool:
    return node.alwaysFormsContainingBlock()


# TODO: This leaks internal details to the public API. Remove after removing
# ComponentKit usage of it.
def YGNodeCanUseCachedMeasurement(
    widthMode: YGMeasureMode,
    availableWidth: float,
    heightMode: YGMeasureMode,
    availableHeight: float,
    lastWidthMode: YGMeasureMode,
    lastAvailableWidth: float,
    lastHeightMode: YGMeasureMode,
    lastAvailableHeight: float,
    lastComputedWidth: float,
    lastComputedHeight: float,
    marginRow: float,
    marginColumn: float,
    config,
) -> bool:
    return canUseCachedMeasurement(
        sizingMode(widthMode),
        availableWidth,
        sizingMode(heightMode),
        availableHeight,
        sizingMode(lastWidthMode),
        lastAvailableWidth,
        sizingMode(lastHeightMode),
        lastAvailableHeight,
        lastComputedWidth,
        lastComputedHeight,
        marginRow,
        marginColumn,
        config,
    )
