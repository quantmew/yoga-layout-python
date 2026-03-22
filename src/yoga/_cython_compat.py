"""Runtime-safe helpers for Cython pure Python annotations."""

from __future__ import annotations

try:
    import cython as cython  # type: ignore[no-redef]
except ImportError:
    class _DummyCython:
        double = float
        float = float
        int = int
        bint = bool
        Py_ssize_t = int

        @staticmethod
        def locals(**_kwargs):
            def decorator(func):
                return func

            return decorator

        @staticmethod
        def returns(_value):
            def decorator(func):
                return func

            return decorator

    cython = _DummyCython()
