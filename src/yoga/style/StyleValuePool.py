"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

import struct

from ..numeric.FloatOptional import FloatOptional
from .SmallValueBuffer import SmallValueBuffer
from .StyleLength import StyleLength
from .StyleSizeLength import StyleSizeLength
from .StyleValueHandle import StyleValueHandle


class StyleValuePool:
    """
    Pool for compact storage of sparse lengths and numbers.

    Values are referred to using StyleValueHandle. In most cases
    StyleValueHandle can embed the value directly, but if not,
    the value is stored within a buffer provided by the pool.
    """

    # Number of inline slots before falling back to heap allocation
    INLINE_BUFFER_SIZE = 4

    def __init__(self) -> None:
        self._buffer = SmallValueBuffer(buffer_size=self.INLINE_BUFFER_SIZE)

    def store_length(self, handle: StyleValueHandle, length: StyleLength) -> None:
        """Store a StyleLength in the handle."""
        if length.isUndefined():
            handle._set_type(StyleValueHandle.Type.Undefined)
            handle.clearValueIsIndexed()
        elif length.isAuto():
            handle._set_type(StyleValueHandle.Type.Auto)
            handle.clearValueIsIndexed()
        else:
            type_ = (
                StyleValueHandle.Type.Point
                if length.isPoints()
                else StyleValueHandle.Type.Percent
            )
            self._store_value(handle, length.value().unwrap(), type_)

    def store_size(self, handle: StyleValueHandle, size_value: StyleSizeLength) -> None:
        """Store a StyleSizeLength in the handle."""
        if size_value.isUndefined():
            handle._set_type(StyleValueHandle.Type.Undefined)
            handle.clearValueIsIndexed()
        elif size_value.isAuto():
            handle._set_type(StyleValueHandle.Type.Auto)
            handle.clearValueIsIndexed()
        elif size_value.isMaxContent():
            self._store_keyword(handle, StyleValueHandle.Keyword.MaxContent)
        elif size_value.isStretch():
            self._store_keyword(handle, StyleValueHandle.Keyword.Stretch)
        elif size_value.isFitContent():
            self._store_keyword(handle, StyleValueHandle.Keyword.FitContent)
        else:
            type_ = (
                StyleValueHandle.Type.Point
                if size_value.isPoints()
                else StyleValueHandle.Type.Percent
            )
            self._store_value(handle, size_value.value().unwrap(), type_)

    def store_number(
        self, handle: StyleValueHandle, number: FloatOptional
    ) -> None:
        """Store a number in the handle."""
        if number.isUndefined():
            handle._set_type(StyleValueHandle.Type.Undefined)
            handle.clearValueIsIndexed()
        else:
            self._store_value(handle, number.unwrap(), StyleValueHandle.Type.Number)

    def get_length(self, handle: StyleValueHandle) -> StyleLength:
        """Get a StyleLength from the handle."""
        if handle.isUndefined():
            return StyleLength.undefined()
        elif handle.isAuto():
            return StyleLength.ofAuto()
        else:
            value = self._get_float_value(handle)
            if handle._type() == StyleValueHandle.Type.Point:
                return StyleLength.points(value)
            else:
                return StyleLength.percent(value)

    def get_size(self, handle: StyleValueHandle) -> StyleSizeLength:
        """Get a StyleSizeLength from the handle."""
        if handle.isUndefined():
            return StyleSizeLength.undefined()
        elif handle.isAuto():
            return StyleSizeLength.ofAuto()
        elif handle.isKeyword(StyleValueHandle.Keyword.MaxContent):
            return StyleSizeLength.ofMaxContent()
        elif handle.isKeyword(StyleValueHandle.Keyword.FitContent):
            return StyleSizeLength.ofFitContent()
        elif handle.isKeyword(StyleValueHandle.Keyword.Stretch):
            return StyleSizeLength.ofStretch()
        else:
            value = self._get_float_value(handle)
            if handle._type() == StyleValueHandle.Type.Point:
                return StyleSizeLength.points(value)
            else:
                return StyleSizeLength.percent(value)

    def get_number(self, handle: StyleValueHandle) -> FloatOptional:
        """Get a number from the handle."""
        if handle.isUndefined():
            return FloatOptional()
        else:
            value = self._get_float_value(handle)
            return FloatOptional(value)

    def _store_value(
        self, handle: StyleValueHandle, value: float, type_: int
    ) -> None:
        """Store a float value in the handle."""
        handle._set_type(type_)

        if self._is_integer_packable(value):
            if handle.isValueIndexed():
                handle.clearValueIsIndexed()
            handle._set_value(self._pack_inline_integer(value))
        else:
            packed = struct.pack("<f", value)
            int_value = struct.unpack("<I", packed)[0]
            new_index = (
                self._buffer.replace(handle._value(), int_value)
                if handle.isValueIndexed()
                else self._buffer.push(int_value)
            )
            handle._set_value(new_index)
            handle.setValueIsIndexed()

    def _store_keyword(
        self, handle: StyleValueHandle, keyword: int
    ) -> None:
        """Store a keyword in the handle."""
        handle._set_type(StyleValueHandle.Type.Keyword)
        if handle.isValueIndexed():
            new_index = self._buffer.replace(handle._value(), keyword)
            handle._set_value(new_index)
        else:
            handle._set_value(keyword)

    def _get_float_value(self, handle: StyleValueHandle) -> float:
        """Extract a float value from the handle."""
        if handle.isValueIndexed():
            int_value = self._buffer.get32(handle._value())
            result: float = struct.unpack("<f", struct.pack("<I", int_value))[0]
            return result
        else:
            return self._unpack_inline_integer(handle._value())

    @staticmethod
    def _is_integer_packable(f: float) -> bool:
        """Check if a float can be packed as an inline integer."""
        k_max_inline_abs_value = (1 << 11) - 1  # 2047
        i = int(f)
        return float(i) == f and -k_max_inline_abs_value <= i <= k_max_inline_abs_value

    @staticmethod
    def _pack_inline_integer(value: float) -> int:
        """Pack a float as an inline integer."""
        is_negative = 1 if value < 0 else 0
        magnitude = abs(int(value))
        return (is_negative << 11) | magnitude

    @staticmethod
    def _unpack_inline_integer(value: int) -> float:
        """Unpack an inline integer to a float."""
        k_value_sign_mask = 0b0000_1000_0000_0000
        k_value_magnitude_mask = 0b0000_0111_1111_1111

        is_negative = (value & k_value_sign_mask) != 0
        magnitude = value & k_value_magnitude_mask
        return float(-magnitude if is_negative else magnitude)

    def copy(self) -> StyleValuePool:
        """Create a copy of this pool."""
        new_pool = StyleValuePool()
        new_pool._buffer = self._buffer.copy()
        return new_pool
