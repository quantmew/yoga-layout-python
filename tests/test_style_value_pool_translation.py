import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga.numeric.FloatOptional import FloatOptional  # noqa: E402
from yoga.style.StyleLength import StyleLength  # noqa: E402
from yoga.style.StyleSizeLength import StyleSizeLength  # noqa: E402
from yoga.style.StyleValueHandle import StyleValueHandle  # noqa: E402
from yoga.style.StyleValuePool import StyleValuePool  # noqa: E402


def test_undefined_at_init():
    pool = StyleValuePool()
    handle = StyleValueHandle()
    assert handle.isUndefined()
    assert not handle.isDefined()
    assert pool.get_length(handle) == StyleLength.undefined()
    assert pool.get_number(handle) == FloatOptional()


def test_auto_at_init():
    pool = StyleValuePool()
    handle = StyleValueHandle.ofAuto()
    assert handle.isAuto()
    assert pool.get_length(handle) == StyleLength.ofAuto()


def test_store_small_int_points():
    pool = StyleValuePool()
    handle = StyleValueHandle()
    pool.store_length(handle, StyleLength.points(10))
    assert pool.get_length(handle) == StyleLength.points(10)


def test_store_small_negative_int_points():
    pool = StyleValuePool()
    handle = StyleValueHandle()
    pool.store_length(handle, StyleLength.points(-10))
    assert pool.get_length(handle) == StyleLength.points(-10)


def test_store_small_int_percent():
    pool = StyleValuePool()
    handle = StyleValueHandle()
    pool.store_length(handle, StyleLength.percent(10))
    assert pool.get_length(handle) == StyleLength.percent(10)


def test_store_large_int_percent():
    pool = StyleValuePool()
    handle = StyleValueHandle()
    pool.store_length(handle, StyleLength.percent(262144))
    assert pool.get_length(handle) == StyleLength.percent(262144)


def test_store_large_int_after_small_int():
    pool = StyleValuePool()
    handle = StyleValueHandle()
    pool.store_length(handle, StyleLength.percent(10))
    pool.store_length(handle, StyleLength.percent(262144))
    assert pool.get_length(handle) == StyleLength.percent(262144)


def test_store_small_int_after_large_int():
    pool = StyleValuePool()
    handle = StyleValueHandle()
    pool.store_length(handle, StyleLength.percent(262144))
    pool.store_length(handle, StyleLength.percent(10))
    assert pool.get_length(handle) == StyleLength.percent(10)


def test_store_small_int_number():
    pool = StyleValuePool()
    handle = StyleValueHandle()
    pool.store_number(handle, FloatOptional(10.0))
    assert pool.get_number(handle) == FloatOptional(10.0)


def test_store_undefined():
    pool = StyleValuePool()
    handle = StyleValueHandle()
    pool.store_length(handle, StyleLength.undefined())
    assert handle.isUndefined()
    assert not handle.isDefined()
    assert pool.get_length(handle) == StyleLength.undefined()


def test_store_undefined_after_small_int():
    pool = StyleValuePool()
    handle = StyleValueHandle()
    pool.store_length(handle, StyleLength.points(10))
    pool.store_length(handle, StyleLength.undefined())
    assert handle.isUndefined()
    assert not handle.isDefined()
    assert pool.get_length(handle) == StyleLength.undefined()


def test_store_undefined_after_large_int():
    pool = StyleValuePool()
    handle = StyleValueHandle()
    pool.store_length(handle, StyleLength.points(262144))
    pool.store_length(handle, StyleLength.undefined())
    assert handle.isUndefined()
    assert not handle.isDefined()
    assert pool.get_length(handle) == StyleLength.undefined()


def test_store_keywords():
    pool = StyleValuePool()
    handle_max_content = StyleValueHandle()
    handle_fit_content = StyleValueHandle()
    handle_stretch = StyleValueHandle()

    pool.store_size(handle_max_content, StyleSizeLength.ofMaxContent())
    pool.store_size(handle_fit_content, StyleSizeLength.ofFitContent())
    pool.store_size(handle_stretch, StyleSizeLength.ofStretch())

    assert pool.get_size(handle_max_content) == StyleSizeLength.ofMaxContent()
    assert pool.get_size(handle_fit_content) == StyleSizeLength.ofFitContent()
    assert pool.get_size(handle_stretch) == StyleSizeLength.ofStretch()
