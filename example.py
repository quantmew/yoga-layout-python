import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from yoga import (  # noqa: E402
    YGAlign,
    YGConfigFree,
    YGConfigNew,
    YGDirection,
    YGFlexDirection,
    YGJustify,
    YGMeasureMode,
    YGNodeCalculateLayout,
    YGNodeFreeRecursive,
    YGNodeGetContext,
    YGNodeInsertChild,
    YGNodeLayoutGetHeight,
    YGNodeLayoutGetLeft,
    YGNodeLayoutGetTop,
    YGNodeLayoutGetWidth,
    YGNodeNew,
    YGNodeNewWithConfig,
    YGNodeSetContext,
    YGNodeSetMeasureFunc,
    YGNodeStyleGetFlexDirection,
    YGNodeStyleSetAlignItems,
    YGNodeStyleSetFlexDirection,
    YGNodeStyleSetFlexGrow,
    YGNodeStyleSetFlexWrap,
    YGNodeStyleSetHeight,
    YGNodeStyleSetJustifyContent,
    YGNodeStyleSetPositionType,
    YGNodeStyleSetWidth,
    YGPositionType,
    YGSize,
    YGWrap,
)


def assert_layout(node, left, top, width, height):
    actual = (
        YGNodeLayoutGetLeft(node),
        YGNodeLayoutGetTop(node),
        YGNodeLayoutGetWidth(node),
        YGNodeLayoutGetHeight(node),
    )
    expected = (left, top, width, height)
    if actual != expected:
        raise AssertionError(f"layout mismatch: actual={actual}, expected={expected}")


def longest_word_width(text, width_per_char):
    max_length = 0
    current_length = 0
    for char in text:
        if char == " ":
            max_length = max(max_length, current_length)
            current_length = 0
        else:
            current_length += 1
    return max(max_length, current_length) * width_per_char


def calculate_height(text, measured_width, width_per_char, height_per_char):
    if len(text) * width_per_char <= measured_width:
        return height_per_char

    words = text.split(" ")
    lines = 1
    current_line_length = 0
    for word in words:
        word_width = len(word) * width_per_char
        if word_width > measured_width:
            if current_line_length > 0:
                lines += 1
            lines += 1
            current_line_length = 0
        elif current_line_length + word_width <= measured_width:
            current_line_length += word_width + width_per_char
        else:
            lines += 1
            current_line_length = word_width + width_per_char

    return (lines - 1 if current_line_length == 0 else lines) * height_per_char


def intrinsic_size_measure(node, width, width_mode, height, height_mode):
    inner_text = YGNodeGetContext(node)
    height_per_char = 10
    width_per_char = 10

    if width_mode == YGMeasureMode.YGMeasureModeExactly:
        measured_width = width
    elif width_mode == YGMeasureMode.YGMeasureModeAtMost:
        measured_width = min(len(inner_text) * width_per_char, width)
    else:
        measured_width = len(inner_text) * width_per_char

    constrained_width = (
        measured_width
        if YGNodeStyleGetFlexDirection(node) == YGFlexDirection.YGFlexDirectionColumn
        else max(longest_word_width(inner_text, width_per_char), measured_width)
    )

    if height_mode == YGMeasureMode.YGMeasureModeExactly:
        measured_height = height
    elif height_mode == YGMeasureMode.YGMeasureModeAtMost:
        measured_height = min(
            calculate_height(inner_text, constrained_width, width_per_char, height_per_char),
            height,
        )
    else:
        measured_height = calculate_height(
            inner_text, constrained_width, width_per_char, height_per_char
        )

    return YGSize(measured_width, measured_height)


def example_flex_row():
    root = YGNodeNew()
    left = YGNodeNew()
    right = YGNodeNew()

    YGNodeStyleSetWidth(root, 300)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    YGNodeStyleSetWidth(left, 50)
    YGNodeStyleSetHeight(left, 100)
    YGNodeInsertChild(root, left, 0)

    YGNodeStyleSetFlexGrow(right, 1)
    YGNodeInsertChild(root, right, 1)

    YGNodeCalculateLayout(root, math.nan, math.nan, YGDirection.YGDirectionLTR)

    assert_layout(root, 0, 0, 300, 100)
    assert_layout(left, 0, 0, 50, 100)
    assert_layout(right, 50, 0, 250, 100)

    YGNodeFreeRecursive(root)


def example_wrap():
    root = YGNodeNew()
    children = [YGNodeNew() for _ in range(5)]

    YGNodeStyleSetWidth(root, 140)
    YGNodeStyleSetHeight(root, 120)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)

    for index, child in enumerate(children):
        YGNodeStyleSetWidth(child, 50)
        YGNodeStyleSetHeight(child, 10)
        YGNodeInsertChild(root, child, index)

    YGNodeCalculateLayout(root, math.nan, math.nan, YGDirection.YGDirectionLTR)

    expected = [
        (0, 0, 50, 10),
        (50, 0, 50, 10),
        (0, 10, 50, 10),
        (50, 10, 50, 10),
        (0, 20, 50, 10),
    ]
    for child, layout in zip(children, expected):
        assert_layout(child, *layout)

    YGNodeFreeRecursive(root)


def example_absolute():
    root = YGNodeNew()
    child = YGNodeNew()

    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetHeight(root, 200)
    YGNodeStyleSetJustifyContent(root, YGJustify.YGJustifyCenter)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignCenter)

    YGNodeStyleSetPositionType(child, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(child, 50)
    YGNodeStyleSetHeight(child, 40)
    YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, math.nan, math.nan, YGDirection.YGDirectionLTR)

    assert_layout(root, 0, 0, 200, 200)
    assert_layout(child, 75, 80, 50, 40)

    YGNodeFreeRecursive(root)


def example_measure():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    text = YGNodeNewWithConfig(config)

    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 2000)
    YGNodeStyleSetHeight(root, 2000)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)

    YGNodeStyleSetFlexDirection(text, YGFlexDirection.YGFlexDirectionRow)
    YGNodeSetContext(text, "Lorem ipsum")
    YGNodeSetMeasureFunc(text, intrinsic_size_measure)
    YGNodeInsertChild(root, text, 0)

    YGNodeCalculateLayout(root, math.nan, math.nan, YGDirection.YGDirectionLTR)

    assert_layout(text, 0, 0, 110, 10)

    YGNodeFreeRecursive(root)
    YGConfigFree(config)


def main():
    example_flex_row()
    example_wrap()
    example_absolute()
    example_measure()
    print("example.py: OK")


if __name__ == "__main__":
    main()
