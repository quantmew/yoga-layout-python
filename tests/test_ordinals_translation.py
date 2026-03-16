import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import YGEdge  # noqa: E402


def test_iteration():
    expected_edges = [
        YGEdge.YGEdgeLeft,
        YGEdge.YGEdgeTop,
        YGEdge.YGEdgeRight,
        YGEdge.YGEdgeBottom,
        YGEdge.YGEdgeStart,
        YGEdge.YGEdgeEnd,
        YGEdge.YGEdgeHorizontal,
        YGEdge.YGEdgeVertical,
        YGEdge.YGEdgeAll,
    ]

    assert list(YGEdge) == expected_edges
