# yoga-layout-python

`yoga-layout-python` is a pure Python port of Meta's Yoga layout engine.

## Current Status

- Public enums, value/config primitives, and the core layout algorithm are implemented in Python.
- Internal module layout mirrors upstream `yoga/` so translation and parity work can stay file-for-file aligned.
- Upstream test translations pass, and a Python-vs-C++ differential parity harness is available under `tools/`.

## Installation

```bash
pip install -e .
```

For development:

```bash
pip install -e ".[dev]"
```

## Optional Cython Build

The default install remains pure Python. If you want compiled extension modules,
the repository now supports Cython's pure Python mode directly from the existing
`.py` files under `src/yoga/`.

By default, the build now compiles the validated hot-path set:
`AbsoluteLayout.py`, `Align.py`, `Baseline.py`, `BoundAxis.py`, `Cache.py`,
`CalculateLayout.py`, `FlexDirection.py`, `FlexLine.py`, `PixelGrid.py`,
`SizingMode.py`, `TrailingPosition.py`, `event.py`, `Comparison.py`,
`FloatMath.py`, and `FloatOptional.py`.

Build compiled modules in place:

```bash
python setup.py build_ext --inplace
```

Or force cythonization through the PEP 517 build path:

```bash
YOGA_CYTHON_BUILD=1 pip install -e .
```

Useful build parameters are exposed as environment variables:

```bash
YOGA_CYTHON_BUILD=1 \
YOGA_CYTHON_MODULES='yoga/algorithm/AbsoluteLayout.py,yoga/algorithm/Align.py,yoga/algorithm/Baseline.py,yoga/algorithm/BoundAxis.py,yoga/algorithm/Cache.py,yoga/algorithm/CalculateLayout.py,yoga/algorithm/FlexDirection.py,yoga/algorithm/FlexLine.py,yoga/algorithm/PixelGrid.py,yoga/algorithm/SizingMode.py,yoga/algorithm/TrailingPosition.py,yoga/event/event.py,yoga/numeric/Comparison.py,yoga/numeric/FloatMath.py,yoga/numeric/FloatOptional.py' \
YOGA_CYTHON_EXCLUDE='yoga/**/__init__.py' \
YOGA_CYTHON_NTHREADS=8 \
YOGA_CYTHON_ANNOTATE=1 \
YOGA_CYTHON_BOUNDSCHECK=0 \
YOGA_CYTHON_WRAPAROUND=0 \
YOGA_CYTHON_INITIALIZEDCHECK=0 \
YOGA_CYTHON_NONECHECK=0 \
YOGA_CYTHON_INFER_TYPES=1 \
YOGA_CYTHON_CFLAGS='-O3' \
python setup.py build_ext --inplace
```

Supported parameters:

- `YOGA_CYTHON_BUILD=1`: enable cythonization during `pip install` / wheel builds.
- `YOGA_CYTHON_MODULES`: comma-separated glob list under `src/` to compile.
- `YOGA_CYTHON_EXCLUDE`: comma-separated glob list to skip.
- `YOGA_CYTHON_NTHREADS`: parallel cythonization worker count.
- `YOGA_CYTHON_ANNOTATE=1`: emit HTML annotation reports.
- `YOGA_CYTHON_BOUNDSCHECK`, `YOGA_CYTHON_WRAPAROUND`, `YOGA_CYTHON_INITIALIZEDCHECK`, `YOGA_CYTHON_NONECHECK`, `YOGA_CYTHON_OVERFLOWCHECK`: toggle matching Cython directives.
- `YOGA_CYTHON_CDIVISION`, `YOGA_CYTHON_INFER_TYPES`: toggle additional optimization directives.
- `YOGA_CYTHON_PROFILE=1`: keep profiler hooks in generated extensions.
- `YOGA_CYTHON_LINETRACE=1`: enable line tracing macros for coverage/profiling builds.
- `YOGA_CYTHON_CFLAGS`: extra compiler flags passed to the C compiler.
- `YOGA_CYTHON_LDFLAGS`: extra linker flags.
- `YOGA_CYTHON_BUILD_DIR`: intermediate generated C/C++ output directory.

Compiled `.so` modules are written next to the Python sources when using
`--inplace`, and Python will import them automatically in preference to the
`.py` modules.

If you want to go beyond this validated set, expand `YOGA_CYTHON_MODULES`
incrementally and validate with the test suite after each addition.

## API Shape

The Python package keeps Yoga's public naming style:

```python
from yoga import *

config = YGConfigNew()
node = YGNodeNewWithConfig(config)
YGNodeStyleSetWidth(node, 100)
YGNodeStyleSetHeight(node, 50)
YGNodeCalculateLayout(node, YGUndefined, YGUndefined, YGDirectionLTR)

width = YGNodeLayoutGetWidth(node)
height = YGNodeLayoutGetHeight(node)
```

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=yoga --cov-report=term-missing

# Run specific test file
pytest tests/test_smoke.py -v
```

## Differential Parity

The repository includes a differential parity runner that compares Python layout
results against the vendored upstream C++ Yoga engine on the same captured tree.

```bash
# Run the default parity suite
python tools/run_differential_ci.py

# Rebuild the C++ runner first
python tools/run_differential_ci.py --force-rebuild

# Increase the random batch size
python tools/run_differential_ci.py --random-count 1000 --seed 20260317
```

On failure, the script writes a repro capture to
`build/differential_failure_capture.json`.

The lower-level harness remains available if you want the raw output format:

```bash
python tools/differential_test.py
```

## Project Structure

```
src/yoga/
├── algorithm/        # Core layout algorithms (CalculateLayout, FlexLine, etc.)
├── config/           # Configuration handling
├── debug/            # Debug utilities (logging, assertions)
├── event/            # Event system
├── node/             # Node class and layout results
├── numeric/          # Numeric utilities (FloatOptional, Comparison)
├── style/            # Style system (Style, StyleLength, etc.)
└── *.py              # Public API modules

tools/
├── differential_cpp_runner.cpp  # C++ capture runner used for parity checks
├── differential_test.py         # Python/C++ differential harness
└── run_differential_ci.py       # Stable CLI entrypoint for parity checks
```

## License

This project uses the same MIT license as upstream Yoga. See `LICENSE`.

## Contributing

Contributions are welcome! Please see the upstream [Yoga repository](https://github.com/facebook/yoga) for reference.
