"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from typing import Any

from ..YGEnums import YGLogLevel


def getDefaultLogger():
    """Get the default logger that does nothing."""
    def _logger(*_args: object, **_kwargs: object) -> int:
        return 0
    return _logger


def log(node: Any | None, level: YGLogLevel, format_string: str, *args: object) -> int:
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
        logger = getDefaultLogger()
        return logger(None, None, level, format_string, args)

    config = node.getConfig() if node is not None else None
    logger = config.logger_ if config is not None else getDefaultLogger()
    return logger(config, node, level, format_string, args)


def logWithConfig(config: Any | None, level: YGLogLevel, format_string: str, *args: object) -> int:
    """Log a message with a config but no node."""
    if config is None:
        logger = getDefaultLogger()
        return logger(None, None, level, format_string, args)
    logger = config.logger_ if hasattr(config, 'logger_') else getDefaultLogger()
    return logger(config, None, level, format_string, args)

