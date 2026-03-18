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
