# Test Translation Matrix

This document records the current test translation status between upstream
`yoga-layout/tests` and this repository's Python test suite.

## Current Status

- Upstream top-level C++ tests: `35`
- Python top-level translated tests: covered
- Upstream generated C++ tests: `25`
- Python generated translated tests: `25`
- Current full-suite result: `824 passed, 46 skipped`
- All `46` skips are explicit translations of upstream `GTEST_SKIP()`

## Top-Level Tests

| Upstream C++ | Python |
| --- | --- |
| `EventsTest.cpp` | `tests/test_events_translation.py` |
| `FlexGapTest.cpp` | `tests/test_flex_gap_translation.py` |
| `FloatOptionalTest.cpp` | `tests/test_float_optional_translation.py` |
| `OrdinalsTest.cpp` | `tests/test_ordinals_translation.py` |
| `SmallValueBufferTest.cpp` | `tests/test_small_value_buffer_translation.py` |
| `StyleTest.cpp` | `tests/test_style_translation.py` |
| `StyleValuePoolTest.cpp` | `tests/test_style_value_pool_translation.py` |
| `YGAlignBaselineTest.cpp` | `tests/test_align_baseline_translation.py` |
| `YGAspectRatioTest.cpp` | `tests/test_aspect_ratio_translation.py` |
| `YGBaselineFuncTest.cpp` | `tests/test_baseline_func_translation.py` |
| `YGCloneNodeTest.cpp` | `tests/test_clone_node_translation.py` |
| `YGComputedMarginTest.cpp` | `tests/test_computed_margin_translation.py` |
| `YGComputedPaddingTest.cpp` | `tests/test_computed_padding_translation.py` |
| `YGConfigTest.cpp` | `tests/test_config_translation.py` |
| `YGDefaultValuesTest.cpp` | `tests/test_default_values_translation.py` |
| `YGDirtiedTest.cpp` | `tests/test_dirtied_translation.py` |
| `YGDirtyMarkingTest.cpp` | `tests/test_dirty_marking_translation.py` |
| `YGEdgeTest.cpp` | `tests/test_edge_translation.py` |
| `YGHadOverflowTest.cpp` | `tests/test_had_overflow_translation.py` |
| `YGLayoutableChildrenTest.cpp` | `tests/test_layoutable_children_translation.py` |
| `YGMeasureCacheTest.cpp` | `tests/test_measure_cache_translation.py` |
| `YGMeasureModeTest.cpp` | `tests/test_measure_mode_translation.py` |
| `YGMeasureTest.cpp` | `tests/test_measure_translation.py` |
| `YGNodeCallbackTest.cpp` | `tests/test_node_callback_translation.py` |
| `YGNodeChildTest.cpp` | `tests/test_node_child_translation.py` |
| `YGPersistenceTest.cpp` | `tests/test_persistence_translation.py` |
| `YGPersistentNodeCloningTest.cpp` | `tests/test_persistent_node_cloning_translation.py` |
| `YGRelayoutTest.cpp` | `tests/test_relayout_translation.py` |
| `YGRoundingFunctionTest.cpp` | `tests/test_rounding_function_translation.py` |
| `YGRoundingMeasureFuncTest.cpp` | `tests/test_rounding_measure_func_translation.py` |
| `YGScaleChangeTest.cpp` | `tests/test_scale_change_translation.py` |
| `YGStyleTest.cpp` | `tests/test_yg_style_translation.py` |
| `YGTreeMutationTest.cpp` | `tests/test_tree_mutation_translation.py` |
| `YGValueTest.cpp` | `tests/test_value_translation.py` |
| `YGZeroOutLayoutRecursivelyTest.cpp` | `tests/test_zero_out_layout_translation.py` |

## Generated Tests

| Upstream Generated C++ | Python |
| --- | --- |
| `YGAbsolutePositionTest.cpp` | `tests/generated/test_absolute_position_generated.py` |
| `YGAlignContentTest.cpp` | `tests/generated/test_align_content_generated.py` |
| `YGAlignItemsTest.cpp` | `tests/generated/test_align_items_generated.py` |
| `YGAlignSelfTest.cpp` | `tests/generated/test_align_self_generated.py` |
| `YGAndroidNewsFeed.cpp` | `tests/generated/test_android_news_feed_generated.py` |
| `YGAspectRatioTest.cpp` | `tests/generated/test_generated_aspect_ratio.py` |
| `YGAutoTest.cpp` | `tests/generated/test_auto_generated.py` |
| `YGBorderTest.cpp` | `tests/generated/test_border_generated.py` |
| `YGBoxSizingTest.cpp` | `tests/generated/test_box_sizing_generated.py` |
| `YGDimensionTest.cpp` | `tests/generated/test_dimension_generated.py` |
| `YGDisplayContentsTest.cpp` | `tests/generated/test_display_contents_generated.py` |
| `YGDisplayTest.cpp` | `tests/generated/test_display_generated.py` |
| `YGFlexDirectionTest.cpp` | `tests/generated/test_flex_direction_generated.py` |
| `YGFlexTest.cpp` | `tests/generated/test_flex_generated.py` |
| `YGFlexWrapTest.cpp` | `tests/generated/test_flex_wrap_generated.py` |
| `YGGapTest.cpp` | `tests/generated/test_gap_generated.py` |
| `YGIntrinsicSizeTest.cpp` | `tests/generated/test_intrinsic_size_generated.py` |
| `YGJustifyContentTest.cpp` | `tests/generated/test_justify_content_generated.py` |
| `YGMarginTest.cpp` | `tests/generated/test_margin_generated.py` |
| `YGMinMaxDimensionTest.cpp` | `tests/generated/test_min_max_dimension_generated.py` |
| `YGPaddingTest.cpp` | `tests/generated/test_padding_generated.py` |
| `YGPercentageTest.cpp` | `tests/generated/test_percentage_generated.py` |
| `YGRoundingTest.cpp` | `tests/generated/test_rounding_generated.py` |
| `YGSizeOverflowTest.cpp` | `tests/generated/test_size_overflow_generated.py` |
| `YGStaticPositionTest.cpp` | `tests/generated/test_static_position_generated.py` |

## Supplemental Tests

These tests are intentionally kept outside the strict upstream 1:1 mapping.
They exist as local smoke tests, focused regression tests, or earlier targeted
layout checks.

- `tests/test_align_items.py`
- `tests/test_align_self.py`
- `tests/test_flex_direction.py`
- `tests/test_flex_layout.py`
- `tests/test_generated_align_items_translation.py`
- `tests/test_justify_content.py`
- `tests/test_margin.py`
- `tests/test_padding.py`
- `tests/test_smoke.py`
- `tests/test_upstream_regressions.py`

## Skip Policy

- Every translated skip now uses `pytest.skip("Upstream GTEST_SKIP()")`
- No local-only skips are currently used in translated upstream tests
- Remaining skipped cases are therefore upstream-authored gaps, not translation
  omissions
