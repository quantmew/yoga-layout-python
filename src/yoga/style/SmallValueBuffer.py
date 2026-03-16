"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class SmallValueBuffer:
    """
    Container for storing 32 or 64 bit integer values with stable indices.

    Values are first stored in a fixed buffer, before falling back to heap allocation.
    """

    buffer_size: int
    buffer: list[int] = field(default_factory=list)
    wide_elements: list[bool] = field(default_factory=list)
    overflow_buffer: list[int] = field(default_factory=list)
    overflow_wide_elements: list[bool] = field(default_factory=list)
    count: int = 0

    def __post_init__(self) -> None:
        if not self.buffer:
            self.buffer = [0] * self.buffer_size
        if not self.wide_elements:
            self.wide_elements = [False] * self.buffer_size

    def push(self, value: int) -> int:
        """
        Add a new element to the buffer, returning the index.

        Supports both 32-bit and 64-bit values.
        """
        if isinstance(value, int) and value > 0xFFFFFFFF:
            # 64-bit value - split into LSB and MSB
            lsb = value & 0xFFFFFFFF
            msb = value >> 32

            lsb_index = self._push_internal(lsb)
            msb_index = self._push_internal(msb)

            # Mark the LSB as wide
            if lsb_index < self.buffer_size:
                self.wide_elements[lsb_index] = True
            else:
                overflow_index = lsb_index - self.buffer_size
                self.overflow_wide_elements[overflow_index] = True

            return lsb_index
        else:
            return self._push_internal(value & 0xFFFFFFFF)

    def _push_internal(self, value: int) -> int:
        """Internal push for a 32-bit value."""
        index = self.count
        self.count += 1

        if index < self.buffer_size:
            self.buffer[index] = value
            return index
        else:
            self.overflow_buffer.append(value)
            self.overflow_wide_elements.append(False)
            return index

    def replace(self, index: int, value: int) -> int:
        """
        Replace an existing element with a new value.

        Returns the (possibly new) index.
        """
        if isinstance(value, int) and value > 0xFFFFFFFF:
            # 64-bit value
            is_wide = self._is_wide(index)
            if is_wide:
                lsb = value & 0xFFFFFFFF
                msb = value >> 32
                self._set_at(index, lsb)
                self._set_at(index + 1, msb)
                return index
            else:
                # Need to push new values
                return self.push(value)
        else:
            self._set_at(index, value & 0xFFFFFFFF)
            return index

    def _set_at(self, index: int, value: int) -> None:
        """Set a value at the given index."""
        if index < self.buffer_size:
            self.buffer[index] = value
        else:
            overflow_index = index - self.buffer_size
            self.overflow_buffer[overflow_index] = value

    def _is_wide(self, index: int) -> bool:
        """Check if the value at index is wide (64-bit)."""
        if index < self.buffer_size:
            return self.wide_elements[index]
        else:
            overflow_index = index - self.buffer_size
            return self.overflow_wide_elements[overflow_index]

    def get32(self, index: int) -> int:
        """Get a 32-bit value at the given index."""
        if index < self.buffer_size:
            return self.buffer[index]
        else:
            overflow_index = index - self.buffer_size
            return self.overflow_buffer[overflow_index]

    def get64(self, index: int) -> int:
        """Get a 64-bit value at the given index."""
        lsb = self.get32(index)
        msb = self.get32(index + 1)
        return (msb << 32) | lsb

    def copy(self) -> "SmallValueBuffer":
        """Create a copy of this buffer."""
        new_buffer = SmallValueBuffer(buffer_size=self.buffer_size)
        new_buffer.buffer = self.buffer.copy()
        new_buffer.wide_elements = self.wide_elements.copy()
        new_buffer.overflow_buffer = self.overflow_buffer.copy()
        new_buffer.overflow_wide_elements = self.overflow_wide_elements.copy()
        new_buffer.count = self.count
        return new_buffer
