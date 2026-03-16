import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga.style.SmallValueBuffer import SmallValueBuffer  # noqa: E402


K_BUFFER_SIZE = 4


def test_copy_assignment_with_overflow():
    handles = []
    buffer1 = SmallValueBuffer(buffer_size=K_BUFFER_SIZE)
    for i in range(K_BUFFER_SIZE + 1):
        handles.append(buffer1.push(i))

    buffer2 = buffer1.copy()
    for i, handle in enumerate(handles):
        assert buffer2.get32(handle) == i

    handle = buffer1.push(42)
    assert buffer1.get32(handle) == 42

    with pytest.raises(IndexError):
        buffer2.get32(handle)


def test_push_32():
    magic = 88567114
    buffer = SmallValueBuffer(buffer_size=K_BUFFER_SIZE)
    handle = buffer.push(magic)
    assert buffer.get32(handle) == magic


def test_push_overflow():
    values = [88567114, 351012214, 146122128, 2171092154, 2269016953]
    buffer = SmallValueBuffer(buffer_size=K_BUFFER_SIZE)
    for value in values:
        assert buffer.get32(buffer.push(value)) == value


def test_push_64():
    magic = 118138934255546108
    buffer = SmallValueBuffer(buffer_size=K_BUFFER_SIZE)
    handle = buffer.push(magic)
    assert buffer.get64(handle) == magic


def test_push_64_overflow():
    values = [
        1401612388342512,
        118712305386210,
        752431801563359011,
        118138934255546108,
        237115443124116111,
    ]
    buffer = SmallValueBuffer(buffer_size=K_BUFFER_SIZE)
    for value in values:
        assert buffer.get64(buffer.push(value)) == value


def test_push_64_after_32():
    magic32 = 88567114
    magic64 = 118712305386210
    buffer = SmallValueBuffer(buffer_size=K_BUFFER_SIZE)
    handle32 = buffer.push(magic32)
    assert buffer.get32(handle32) == magic32
    handle64 = buffer.push(magic64)
    assert buffer.get64(handle64) == magic64


def test_push_32_after_64():
    magic32 = 88567114
    magic64 = 118712305386210
    buffer = SmallValueBuffer(buffer_size=K_BUFFER_SIZE)
    handle64 = buffer.push(magic64)
    assert buffer.get64(handle64) == magic64
    handle32 = buffer.push(magic32)
    assert buffer.get32(handle32) == magic32


def test_replace_32_with_32():
    buffer = SmallValueBuffer(buffer_size=K_BUFFER_SIZE)
    handle = buffer.push(88567114)
    assert buffer.get32(buffer.replace(handle, 351012214)) == 351012214


def test_replace_32_with_64():
    buffer = SmallValueBuffer(buffer_size=K_BUFFER_SIZE)
    handle = buffer.push(88567114)
    assert buffer.get64(buffer.replace(handle, 118712305386210)) == 118712305386210


def test_replace_32_with_64_causes_overflow():
    buffer = SmallValueBuffer(buffer_size=K_BUFFER_SIZE)
    handle1 = buffer.push(88567114)
    buffer.push(351012214)
    buffer.push(146122128)
    buffer.push(2171092154)
    assert buffer.get64(buffer.replace(handle1, 118712305386210)) == 118712305386210


def test_replace_64_with_32():
    buffer = SmallValueBuffer(buffer_size=K_BUFFER_SIZE)
    handle = buffer.push(118712305386210)
    assert buffer.get32(buffer.replace(handle, 88567114)) == 88567114


def test_replace_64_with_64():
    buffer = SmallValueBuffer(buffer_size=K_BUFFER_SIZE)
    handle = buffer.push(1401612388342512)
    assert buffer.get64(buffer.replace(handle, 118712305386210)) == 118712305386210
