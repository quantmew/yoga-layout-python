# Translation Checklist

This checklist records the current mechanical 1:1 comparison status between
`src/yoga` and upstream `yoga-layout/yoga`.

## 1. File Mapping

Top-level:

- `src/yoga/YGConfig.py` -> `yoga/YGConfig.cpp`, `yoga/YGConfig.h`
- `src/yoga/YGEnums.py` -> `yoga/YGEnums.cpp`, `yoga/YGEnums.h`
- `src/yoga/YGMacros.py` -> `yoga/YGMacros.h`
- `src/yoga/YGNode.py` -> `yoga/YGNode.cpp`, `yoga/YGNode.h`
- `src/yoga/YGNodeLayout.py` -> `yoga/YGNodeLayout.cpp`, `yoga/YGNodeLayout.h`
- `src/yoga/YGNodeStyle.py` -> `yoga/YGNodeStyle.cpp`, `yoga/YGNodeStyle.h`
- `src/yoga/YGPixelGrid.py` -> `yoga/YGPixelGrid.cpp`, `yoga/YGPixelGrid.h`
- `src/yoga/YGValue.py` -> `yoga/YGValue.cpp`, `yoga/YGValue.h`
- `src/yoga/__init__.py` -> `yoga/Yoga.h`

Algorithm:

- `src/yoga/algorithm/AbsoluteLayout.py` -> `yoga/algorithm/AbsoluteLayout.cpp`, `yoga/algorithm/AbsoluteLayout.h`
- `src/yoga/algorithm/Align.py` -> `yoga/algorithm/Align.h`
- `src/yoga/algorithm/Baseline.py` -> `yoga/algorithm/Baseline.cpp`, `yoga/algorithm/Baseline.h`
- `src/yoga/algorithm/BoundAxis.py` -> `yoga/algorithm/BoundAxis.h`
- `src/yoga/algorithm/Cache.py` -> `yoga/algorithm/Cache.cpp`, `yoga/algorithm/Cache.h`
- `src/yoga/algorithm/CalculateLayout.py` -> `yoga/algorithm/CalculateLayout.cpp`, `yoga/algorithm/CalculateLayout.h`
- `src/yoga/algorithm/FlexDirection.py` -> `yoga/algorithm/FlexDirection.h`
- `src/yoga/algorithm/FlexLine.py` -> `yoga/algorithm/FlexLine.cpp`, `yoga/algorithm/FlexLine.h`
- `src/yoga/algorithm/PixelGrid.py` -> `yoga/algorithm/PixelGrid.cpp`, `yoga/algorithm/PixelGrid.h`
- `src/yoga/algorithm/SizingMode.py` -> `yoga/algorithm/SizingMode.h`
- `src/yoga/algorithm/TrailingPosition.py` -> `yoga/algorithm/TrailingPosition.h`
- `src/yoga/algorithm/__init__.py` -> no direct upstream file

Config / debug / event:

- `src/yoga/config/Config.py` -> `yoga/config/Config.cpp`, `yoga/config/Config.h`
- `src/yoga/config/__init__.py` -> no direct upstream file
- `src/yoga/debug/AssertFatal.py` -> `yoga/debug/AssertFatal.cpp`, `yoga/debug/AssertFatal.h`
- `src/yoga/debug/Log.py` -> `yoga/debug/Log.cpp`, `yoga/debug/Log.h`
- `src/yoga/debug/__init__.py` -> no direct upstream file
- `src/yoga/event/event.py` -> `yoga/event/event.cpp`, `yoga/event/event.h`
- `src/yoga/event/__init__.py` -> no direct upstream file

Node / numeric / style:

- `src/yoga/node/CachedMeasurement.py` -> `yoga/node/CachedMeasurement.h`
- `src/yoga/node/LayoutResults.py` -> `yoga/node/LayoutResults.cpp`, `yoga/node/LayoutResults.h`
- `src/yoga/node/LayoutableChildren.py` -> `yoga/node/LayoutableChildren.h`
- `src/yoga/node/Node.py` -> `yoga/node/Node.cpp`, `yoga/node/Node.h`
- `src/yoga/node/__init__.py` -> no direct upstream file
- `src/yoga/numeric/Comparison.py` -> `yoga/numeric/Comparison.h`
- `src/yoga/numeric/FloatOptional.py` -> `yoga/numeric/FloatOptional.h`
- `src/yoga/numeric/__init__.py` -> no direct upstream file
- `src/yoga/style/GridLine.py` -> `yoga/style/GridLine.h`
- `src/yoga/style/GridTrack.py` -> `yoga/style/GridTrack.h`
- `src/yoga/style/SmallValueBuffer.py` -> `yoga/style/SmallValueBuffer.h`
- `src/yoga/style/Style.py` -> `yoga/style/Style.h`
- `src/yoga/style/StyleLength.py` -> `yoga/style/StyleLength.h`
- `src/yoga/style/StyleSizeLength.py` -> `yoga/style/StyleSizeLength.h`
- `src/yoga/style/StyleValueHandle.py` -> `yoga/style/StyleValueHandle.h`
- `src/yoga/style/StyleValuePool.py` -> `yoga/style/StyleValuePool.h`
- `src/yoga/style/__init__.py` -> no direct upstream file

## 2. Extra Public Symbols

Checked mechanically against upstream declarations and current Python modules.

Current notable extra public Python symbols:

- `src/yoga/config/Config.py:getDefaultConfig`
- `src/yoga/debug/Log.py:logWithConfig`
- `src/yoga/event/event.py` event data classes and enums used as internal
  runtime support

Current status:

- No extra top-level exports were found in `src/yoga/__init__.py` beyond the
  upstream `Yoga.h` aggregation surface.
- Internal helper functions in major public wrappers are mostly underscored and
  no longer leak into the public API surface.

## 3. Old Adapter Naming

Mechanical scan status:

- No remaining `..enums.` or `.enums.` imports are used by active translation
  files under `src/yoga`.
- The legacy `src/yoga/enums/` compatibility package has been removed from the
  tree.

## 4. Comment And Function Order Audit

Audited files:

- `src/yoga/YGConfig.py`
- `src/yoga/YGNode.py`
- `src/yoga/YGNodeStyle.py`
- `src/yoga/YGNodeLayout.py`
- `src/yoga/algorithm/CalculateLayout.py`
- `src/yoga/node/Node.py`
- `src/yoga/style/Style.py`

Current status:

- Public wrapper order is close to upstream for the top-level API files above.
- `Node.py` and `Style.py` have been tightened to better match upstream branch
  order and comments in several hotspots.
- `YGNode.py` now follows upstream allocation / deallocation event paths more
  closely, and `Style.py` uses an explicit equality implementation instead of
  relying on dataclass-generated comparison.
- `CalculateLayout.py` no longer uses Python-only enum-name string checks or
  `width == width` / `height == height` style NaN probes in the flex-basis
  path; those branches now follow upstream enum comparisons and
  `isDefined`/`isUndefined` semantics.
- Remaining gap: internal method ordering inside large Python classes is close
  to upstream, but not yet guaranteed line-for-line identical.
- Remaining gap: some Python implementation files necessarily keep small
  module-level helpers where C++ uses templates or inline private helpers.

## 5. Regression Tests Added For Upstream-Linked Behavior

Added in `tests/test_upstream_regressions.py`:

- invalid measure results are clamped like upstream `Node::measure`
- layout start/end edge getters resolve according to layout direction
- `CachedMeasurement` equality handles undefined numeric fields like upstream
- `LayoutableChildren` skips `display: contents` nodes and yields layoutable
  descendants
- `YGNodeNew` / `YGNodeClone` / `YGNodeFree` publish allocation and
  deallocation events along the same public paths as upstream

## Current Verdict

The translation is executable, current tests pass, and the legacy
`src/yoga/enums/` compatibility layer has been removed. The remaining work is
now mechanical confirmation and final line-level audit, so this checklist marks
the repository as being in a "confirmation / wrap-up" state rather than
"unfinished".
