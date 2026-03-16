import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import YGUndefined, YGUnit, YGValue  # noqa: E402


def test_supports_equality():
    assert YGValue(12.5, YGUnit.YGUnitPercent) == YGValue(12.5, YGUnit.YGUnitPercent)
    assert YGValue(12.5, YGUnit.YGUnitPercent) != YGValue(56.7, YGUnit.YGUnitPercent)
    assert YGValue(12.5, YGUnit.YGUnitPercent) != YGValue(12.5, YGUnit.YGUnitPoint)
    assert YGValue(12.5, YGUnit.YGUnitPercent) != YGValue(12.5, YGUnit.YGUnitAuto)
    assert YGValue(12.5, YGUnit.YGUnitPercent) != YGValue(
        12.5, YGUnit.YGUnitUndefined
    )

    undefined_value = YGValue(12.5, YGUnit.YGUnitUndefined)
    nan_undefined_value = YGValue(YGUndefined, YGUnit.YGUnitUndefined)
    assert undefined_value == nan_undefined_value
    assert math.isnan(nan_undefined_value.value)

    assert YGValue(0, YGUnit.YGUnitAuto) == YGValue(-1, YGUnit.YGUnitAuto)
