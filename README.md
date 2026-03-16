# yoga-layout-python

`yoga-layout-python` is a pure Python port of Meta's Yoga layout engine.

This repository vendors the upstream Yoga source tree in `yoga-layout/` and mirrors its public C API into Python modules under `src/yoga/`.

## Current Status

- Public enums and value/config primitives are implemented in Python.
- Internal module layout mirrors upstream `yoga/` so the remaining translation can stay file-for-file aligned.
- Layout algorithm parity is in progress - basic flex layouts work, grid and advanced features are being implemented.

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

## Project Structure

```
src/yoga/
├── algorithm/        # Core layout algorithms (CalculateLayout, FlexLine, etc.)
├── config/           # Configuration handling
├── debug/            # Debug utilities (logging, assertions)
├── enums/            # Yoga enum types
├── event/            # Event system
├── node/             # Node class and layout results
├── numeric/          # Numeric utilities (FloatOptional, Comparison)
├── style/            # Style system (Style, StyleLength, etc.)
└── *.py              # Public API modules
```

## License

This project uses the same MIT license as upstream Yoga. See `LICENSE`.

## Contributing

Contributions are welcome! Please see the upstream [Yoga repository](https://github.com/facebook/yoga) for reference.
