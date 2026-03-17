import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import (  # noqa: E402
    YGAlign,
    YGConfigFree,
    YGConfigNew,
    YGDirection,
    YGFlexDirection,
    YGMeasureMode,
    YGNodeCalculateLayout,
    YGNodeFreeRecursive,
    YGNodeGetContext,
    YGNodeInsertChild,
    YGNodeLayoutGetHeight,
    YGNodeLayoutGetLeft,
    YGNodeLayoutGetTop,
    YGNodeLayoutGetWidth,
    YGNodeNewWithConfig,
    YGNodeSetContext,
    YGNodeSetMeasureFunc,
    YGNodeStyleGetFlexDirection,
    YGNodeStyleSetAlignItems,
    YGNodeStyleSetFlexDirection,
    YGNodeStyleSetHeight,
    YGNodeStyleSetPositionType,
    YGNodeStyleSetWidth,
    YGPositionType,
    YGSize,
)


def layout_tuple(node):
    return (
        YGNodeLayoutGetLeft(node),
        YGNodeLayoutGetTop(node),
        YGNodeLayoutGetWidth(node),
        YGNodeLayoutGetHeight(node),
    )


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


def main():
    config = YGConfigNew()
    root = YGNodeNewWithConfig(config)
    text = YGNodeNewWithConfig(config)

    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 300)
    YGNodeStyleSetHeight(root, 200)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)

    YGNodeStyleSetFlexDirection(text, YGFlexDirection.YGFlexDirectionRow)
    YGNodeSetContext(text, "Yoga layout measure function example")
    YGNodeSetMeasureFunc(text, intrinsic_size_measure)
    YGNodeInsertChild(root, text, 0)

    YGNodeCalculateLayout(root, math.nan, math.nan, YGDirection.YGDirectionLTR)

    print("text_measure.py")
    print("root:", layout_tuple(root))
    print("text:", layout_tuple(text))

    assert layout_tuple(root) == (0, 0, 300, 200)
    assert layout_tuple(text) == (0, 0, 350, 10)

    YGNodeFreeRecursive(root)
    YGConfigFree(config)
    print("text_measure.py: OK")


if __name__ == "__main__":
    main()
