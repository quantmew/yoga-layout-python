"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations


class StyleValueHandle:
    """
    A compact (16-bit) handle to a length or number in a style.

    The value may be embedded directly in the handle if simple,
    or the handle may instead point to an index within a StyleValuePool.
    """

    # Bit masks for handle encoding
    HANDLE_TYPE_MASK = 0b0000_0000_0000_0111
    HANDLE_INDEXED_MASK = 0b0000_0000_0000_1000
    HANDLE_VALUE_MASK = 0b1111_1111_1111_0000

    class Type:
        Undefined = 0
        Point = 1
        Percent = 2
        Number = 3
        Auto = 4
        Keyword = 5

    class Keyword:
        MaxContent = 0
        FitContent = 1
        Stretch = 2

    def __init__(self, repr_: int = 0) -> None:
        self._repr = repr_

    @classmethod
    def ofAuto(cls) -> StyleValueHandle:
        """Create a handle representing 'auto'."""
        handle = cls()
        handle._set_type(cls.Type.Auto)
        return handle

    @classmethod
    def ofUndefined(cls) -> StyleValueHandle:
        """Create a handle representing 'undefined'."""
        handle = cls()
        handle._set_type(cls.Type.Undefined)
        return handle

    def isUndefined(self) -> bool:
        """Check if the handle represents undefined."""
        return self._type() == self.Type.Undefined

    def isDefined(self) -> bool:
        """Check if the handle represents a defined value."""
        return not self.isUndefined()

    def isAuto(self) -> bool:
        """Check if the handle represents 'auto'."""
        return self._type() == self.Type.Auto

    def _type(self) -> int:
        """Get the type encoded in the handle."""
        return self._repr & self.HANDLE_TYPE_MASK

    def _set_type(self, handle_type: int) -> None:
        """Set the type in the handle."""
        self._repr &= ~self.HANDLE_TYPE_MASK
        self._repr |= handle_type

    def _value(self) -> int:
        """Get the value encoded in the handle."""
        return self._repr >> 4

    def _set_value(self, value: int) -> None:
        """Set the value in the handle."""
        self._repr &= ~self.HANDLE_VALUE_MASK
        self._repr |= (value << 4)

    def isValueIndexed(self) -> bool:
        """Check if the value is stored in an index."""
        return (self._repr & self.HANDLE_INDEXED_MASK) != 0

    def setValueIsIndexed(self) -> None:
        """Mark the value as indexed."""
        self._repr |= self.HANDLE_INDEXED_MASK

    def clearValueIsIndexed(self) -> None:
        """Mark the value as inline, not indexed."""
        self._repr &= ~self.HANDLE_INDEXED_MASK

    def isKeyword(self, keyword: int) -> bool:
        """Check if the handle represents a specific keyword."""
        return self._type() == self.Type.Keyword and self._value() == keyword
