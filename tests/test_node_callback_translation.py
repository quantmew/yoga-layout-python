import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import YGMeasureMode, YGSize  # noqa: E402
from yoga.node.Node import Node  # noqa: E402


def test_has_measure_func_initial():
    n = Node()
    assert not n.hasMeasureFunc()


def test_has_measure_func_with_measure_fn():
    n = Node()
    n.setMeasureFunc(
        lambda _node, _w, _wm, _h, _hm: YGSize(0.0, 0.0)
    )
    assert n.hasMeasureFunc()


def test_measure_with_measure_fn():
    n = Node()
    n.setMeasureFunc(
        lambda _node, w, wm, h, hm: YGSize(
            w * float(wm), h / float(hm)
        )
    )
    assert n.measure(23, YGMeasureMode.YGMeasureModeExactly, 24, YGMeasureMode.YGMeasureModeAtMost) == YGSize(23, 12)


def test_has_measure_func_after_unset():
    n = Node()
    n.setMeasureFunc(lambda _node, _w, _wm, _h, _hm: YGSize(0.0, 0.0))
    n.setMeasureFunc(None)
    assert not n.hasMeasureFunc()


def test_has_baseline_func_initial():
    n = Node()
    assert not n.hasBaselineFunc()


def test_has_baseline_func_with_baseline_fn():
    n = Node()
    n.setBaselineFunc(lambda _node, _w, _h: 0.0)
    assert n.hasBaselineFunc()


def test_baseline_with_baseline_fn():
    n = Node()
    n.setBaselineFunc(lambda _node, w, h: w + h)
    assert n.baseline(1.25, 2.5) == 3.75


def test_has_baseline_func_after_unset():
    n = Node()
    n.setBaselineFunc(lambda _node, _w, _h: 0.0)
    n.setBaselineFunc(None)
    assert not n.hasBaselineFunc()
