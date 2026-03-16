import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import YGFloatIsUndefined, YGUndefined  # noqa: E402
from yoga.numeric.FloatOptional import FloatOptional, maxOrDefined  # noqa: E402


empty = FloatOptional()
zero = FloatOptional(0.0)
one = FloatOptional(1.0)
positive = FloatOptional(1234.5)
negative = FloatOptional(-9876.5)


def test_value():
    assert YGFloatIsUndefined(empty.unwrap())
    assert zero.unwrap() == 0.0
    assert one.unwrap() == 1.0
    assert positive.unwrap() == 1234.5
    assert negative.unwrap() == -9876.5

    assert empty.isUndefined()
    assert not zero.isUndefined()
    assert not one.isUndefined()
    assert not positive.isUndefined()
    assert not negative.isUndefined()


def test_equality():
    assert empty == empty
    assert empty == YGUndefined
    assert empty != zero
    assert empty != negative
    assert empty != 12.3

    assert zero == zero
    assert zero == 0.0
    assert zero != positive
    assert zero != -5555.5

    assert one == one
    assert one == 1.0
    assert one != positive

    assert positive == positive
    assert positive == positive.unwrap()
    assert positive != one

    assert negative == negative
    assert negative == negative.unwrap()
    assert negative != zero


def test_inequality():
    assert not (empty != empty)
    assert not (empty != YGUndefined)
    assert empty != zero
    assert empty != negative
    assert empty != 12.3

    assert not (zero != zero)
    assert not (zero != 0.0)
    assert zero != positive
    assert zero != -5555.5

    assert not (one != one)
    assert not (one != 1.0)
    assert one != positive

    assert not (positive != positive)
    assert not (positive != positive.unwrap())
    assert positive != one

    assert not (negative != negative)
    assert not (negative != negative.unwrap())
    assert negative != zero


def test_greater_than_with_undefined():
    assert not (empty > empty)
    assert not (empty > zero)
    assert not (empty > one)
    assert not (empty > positive)
    assert not (empty > negative)
    assert not (zero > empty)
    assert not (one > empty)
    assert not (positive > empty)
    assert not (negative > empty)


def test_greater_than():
    assert zero > negative
    assert not (zero > zero)
    assert not (zero > positive)
    assert not (zero > one)

    assert one > negative
    assert one > zero
    assert not (one > positive)

    assert negative > FloatOptional(float("-inf"))


def test_less_than_with_undefined():
    assert not (empty < empty)
    assert not (zero < empty)
    assert not (one < empty)
    assert not (positive < empty)
    assert not (negative < empty)
    assert not (empty < zero)
    assert not (empty < one)
    assert not (empty < positive)
    assert not (empty < negative)


def test_less_than():
    assert negative < zero
    assert not (zero < zero)
    assert not (positive < zero)
    assert not (one < zero)

    assert negative < one
    assert zero < one
    assert not (positive < one)

    assert FloatOptional(float("-inf")) < negative


def test_greater_than_equals_with_undefined():
    assert empty >= empty
    assert not (empty >= zero)
    assert not (empty >= one)
    assert not (empty >= positive)
    assert not (empty >= negative)
    assert not (zero >= empty)
    assert not (one >= empty)
    assert not (positive >= empty)
    assert not (negative >= empty)


def test_greater_than_equals():
    assert zero >= negative
    assert zero >= zero
    assert not (zero >= positive)
    assert not (zero >= one)

    assert one >= negative
    assert one >= zero
    assert not (one >= positive)

    assert negative >= FloatOptional(float("-inf"))


def test_less_than_equals_with_undefined():
    assert empty <= empty
    assert not (zero <= empty)
    assert not (one <= empty)
    assert not (positive <= empty)
    assert not (negative <= empty)
    assert not (empty <= zero)
    assert not (empty <= one)
    assert not (empty <= positive)
    assert not (empty <= negative)


def test_less_than_equals():
    assert negative <= zero
    assert zero <= zero
    assert not (positive <= zero)
    assert not (one <= zero)

    assert negative <= one
    assert zero <= one
    assert not (positive <= one)

    assert FloatOptional(float("-inf")) <= negative


def test_addition():
    assert zero + one == one
    assert negative + positive == FloatOptional(negative.unwrap() + positive.unwrap())
    assert empty + zero == empty
    assert empty + empty == empty
    assert negative + empty == empty


def test_max_or_defined():
    assert maxOrDefined(empty, empty) == empty
    assert maxOrDefined(empty, positive) == positive
    assert maxOrDefined(negative, empty) == negative
    assert maxOrDefined(negative, FloatOptional(float("-inf"))) == negative
    assert maxOrDefined(FloatOptional(1.0), FloatOptional(1.125)) == FloatOptional(1.125)


def test_unwrap():
    assert YGFloatIsUndefined(empty.unwrap())
    assert zero.unwrap() == 0.0
    assert FloatOptional(123456.78).unwrap() == 123456.78
