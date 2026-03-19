import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga.style.Style import Style  # noqa: E402
from yoga.style.StyleLength import StyleLength  # noqa: E402
from yoga.YGEnums import YGDirection, YGEdge, YGFlexDirection, YGGutter  # noqa: E402


def test_computed_padding_is_floored():
    style = Style()
    style.setPadding(YGEdge.YGEdgeAll, StyleLength.points(-1.0))
    padding_start = style.computeInlineStartPadding(
        YGFlexDirection.YGFlexDirectionRow, YGDirection.YGDirectionLTR, 0.0
    )
    assert padding_start == 0.0


def test_computed_border_is_floored():
    style = Style()
    style.setBorder(YGEdge.YGEdgeAll, StyleLength.points(-1.0))
    border_start = style.computeInlineStartBorder(
        YGFlexDirection.YGFlexDirectionRow, YGDirection.YGDirectionLTR
    )
    assert border_start == 0.0


def test_computed_gap_is_floored():
    style = Style()
    style.setGap(YGGutter.YGGutterColumn, StyleLength.points(-1.0))
    gap_between_columns = style.computeGapForAxis(
        YGFlexDirection.YGFlexDirectionRow, 0.0
    )
    assert gap_between_columns == 0.0


def test_computed_margin_is_not_floored():
    style = Style()
    style.setMargin(YGEdge.YGEdgeAll, StyleLength.points(-1.0))
    margin_start = style.computeInlineStartMargin(
        YGFlexDirection.YGFlexDirectionRow, YGDirection.YGDirectionLTR, 0.0
    )
    assert margin_start == -1.0
