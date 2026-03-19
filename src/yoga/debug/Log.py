"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from ..YGEnums import YGLogLevel


def getDefaultLogger():
    """Get the default logger that does nothing."""
    def _logger(*_args: object, **_kwargs: object) -> int:
        return 0
    return _logger


def log(node: object | None, level: YGLogLevel, format_string: str, *args: object) -> int:
    """
    Log a message at the given level.

    Args:
        node: The yoga node (can be None)
        level: The log level
        format_string: The format string
        *args: Arguments to format into the string
    """
    if node is None:
        # Log without node
        return 0

    if hasattr(node, 'getConfig'):
        node.getConfig()  # type: ignore[attr-defined]
    return 0


def logWithConfig(config: object | None, level: YGLogLevel, format_string: str, *args: object) -> int:
    """Log a message with a config but no node."""
    if config is None:
        return 0
    if hasattr(config, 'logger_'):
        pass  # type: ignore[attr-defined]
    return 0

