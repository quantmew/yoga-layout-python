"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""


def assertFatal(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def assertFatalWithConfig(_config, condition: bool, message: str) -> None:
    assertFatal(condition, message)


def assertFatalWithNode(_node, condition: bool, message: str) -> None:
    assertFatal(condition, message)


def fatalWithMessage(message: str) -> None:
    raise RuntimeError(message)

