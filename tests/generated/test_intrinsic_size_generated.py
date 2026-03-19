import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from yoga import *  # noqa: E402,F403


def _assert_layout(node, left, top, width, height):
    assert YGNodeLayoutGetLeft(node) == left
    assert YGNodeLayoutGetTop(node) == top
    assert YGNodeLayoutGetWidth(node) == width
    assert YGNodeLayoutGetHeight(node) == height



def _longest_word_width(text, width_per_char):
    max_length = 0
    current_length = 0
    for char in text:
        if char == " ":
            max_length = max(current_length, max_length)
            current_length = 0
        else:
            current_length += 1
    return max(current_length, max_length) * width_per_char


def _calculate_height(text, measured_width, width_per_char, height_per_char):
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


def _intrinsic_size_measure(node, width, width_mode, height, height_mode):
    inner_text = YGNodeGetContext(node)
    height_per_char = 10
    width_per_char = 10

    if width_mode == YGMeasureMode.YGMeasureModeExactly:
        measured_width = width
    elif width_mode == YGMeasureMode.YGMeasureModeAtMost:
        measured_width = min(len(inner_text) * width_per_char, width)
    else:
        measured_width = len(inner_text) * width_per_char

    flex_direction = YGNodeStyleGetFlexDirection(node)
    constrained_width = (
        measured_width
        if flex_direction == YGFlexDirection.YGFlexDirectionColumn
        else max(_longest_word_width(inner_text, width_per_char), measured_width)
    )

    if height_mode == YGMeasureMode.YGMeasureModeExactly:
        measured_height = height
    elif height_mode == YGMeasureMode.YGMeasureModeAtMost:
        measured_height = min(
            _calculate_height(inner_text, constrained_width, width_per_char, height_per_char),
            height,
        )
    else:
        measured_height = _calculate_height(
            inner_text, constrained_width, width_per_char, height_per_char
        )

    return YGSize(measured_width, measured_height)

def test_contains_inner_text_long_word():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 2000)
    YGNodeStyleSetHeight(root, 2000)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeSetContext(root_child0, "LoremipsumdolorsitametconsecteturadipiscingelitSedeleifasdfettortoracauctorFuscerhoncusipsumtemporerosaliquamconsequatPraesentsoda")
    YGNodeSetMeasureFunc(root_child0, _intrinsic_size_measure)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 2000
    assert YGNodeLayoutGetHeight(root) == 2000

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 1300
    assert YGNodeLayoutGetHeight(root_child0) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 2000
    assert YGNodeLayoutGetHeight(root) == 2000

    assert YGNodeLayoutGetLeft(root_child0) == 700
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 1300
    assert YGNodeLayoutGetHeight(root_child0) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_contains_inner_text_no_width_no_height():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 2000)
    YGNodeStyleSetHeight(root, 2000)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeSetContext(root_child0, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eleifasd et tortor ac auctor. Integer at volutpat libero, sed elementum dui interdum id. Aliquam consectetur massa vel neque aliquet, quis consequat risus fringilla. Fusce rhoncus ipsum tempor eros aliquam, vel tempus metus ullamcorper. Nam at nulla sed tellus vestibulum fringilla vel sit amet ligula. Proin velit lectus, euismod sit amet quam vel ultricies dolor, vitae finibus lorem ipsum. Pellentesque molestie at mi sit amet dictum. Donec vehicula lacinia felis sit amet consectetur. Praesent sodales enim sapien, sed varius ipsum pellentesque vel. Aenean eu mi eu justo tincidunt finibus vel sit amet ipsum. Sed bibasdum purus vel ipsum sagittis, quis fermentum dolor lobortis. Etiam vulputate eleifasd lectus vel varius. Phasellus imperdiet lectus sit amet ipsum egestas, ut bibasdum ipsum malesuada. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed mollis eros sit amet elit porttitor, vel venenatis turpis venenatis. Nulla tempus tortor at eros efficitur, sit amet dapibus ipsum malesuada. Ut at mauris sed nunc malesuada convallis. Duis id sem vel magna varius eleifasd vel at est. Donec eget orci a ipsum tempor lobortis. Sed at consectetur ipsum.")
    YGNodeSetMeasureFunc(root_child0, _intrinsic_size_measure)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 2000
    assert YGNodeLayoutGetHeight(root) == 2000

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 2000
    assert YGNodeLayoutGetHeight(root_child0) == 70

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 2000
    assert YGNodeLayoutGetHeight(root) == 2000

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 2000
    assert YGNodeLayoutGetHeight(root_child0) == 70

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_contains_inner_text_no_width_no_height_long_word_in_paragraph():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 2000)
    YGNodeStyleSetHeight(root, 2000)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeSetContext(root_child0, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eleifasd et tortor ac auctor. Integer at volutpat libero, sed elementum dui interdum id. Aliquam consectetur massa vel neque aliquet, quis consequat risus fringilla. Fusce rhoncus ipsum tempor eros aliquam, vel tempus metus ullamcorper. Nam at nulla sed tellus vestibulum fringilla vel sit amet ligula. Proin velit lectus, euismod sit amet quam vel ultricies dolor, vitae finibus loremipsumloremipsumloremipsumloremipsumloremipsumloremipsumloremipsumloremipsumloremipsumloremipsumloremipsumloremipsumloremipsumlorem Pellentesque molestie at mi sit amet dictum. Donec vehicula lacinia felis sit amet consectetur. Praesent sodales enim sapien, sed varius ipsum pellentesque vel. Aenean eu mi eu justo tincidunt finibus vel sit amet ipsum. Sed bibasdum purus vel ipsum sagittis, quis fermentum dolor lobortis. Etiam vulputate eleifasd lectus vel varius. Phasellus imperdiet lectus sit amet ipsum egestas, ut bibasdum ipsum malesuada. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed mollis eros sit amet elit porttitor, vel venenatis turpis venenatis. Nulla tempus tortor at eros efficitur, sit amet dapibus ipsum malesuada. Ut at mauris sed nunc malesuada convallis. Duis id sem vel magna varius eleifasd vel at est. Donec eget orci a ipsum tempor lobortis. Sed at consectetur ipsum.")
    YGNodeSetMeasureFunc(root_child0, _intrinsic_size_measure)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 2000
    assert YGNodeLayoutGetHeight(root) == 2000

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 2000
    assert YGNodeLayoutGetHeight(root_child0) == 70

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 2000
    assert YGNodeLayoutGetHeight(root) == 2000

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 2000
    assert YGNodeLayoutGetHeight(root_child0) == 70

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_contains_inner_text_fixed_width():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 2000)
    YGNodeStyleSetHeight(root, 2000)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeSetContext(root_child0, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eleifasd et tortor ac auctor. Integer at volutpat libero, sed elementum dui interdum id. Aliquam consectetur massa vel neque aliquet, quis consequat risus fringilla. Fusce rhoncus ipsum tempor eros aliquam, vel tempus metus ullamcorper. Nam at nulla sed tellus vestibulum fringilla vel sit amet ligula. Proin velit lectus, euismod sit amet quam vel ultricies dolor, vitae finibus lorem ipsum. Pellentesque molestie at mi sit amet dictum. Donec vehicula lacinia felis sit amet consectetur. Praesent sodales enim sapien, sed varius ipsum pellentesque vel. Aenean eu mi eu justo tincidunt finibus vel sit amet ipsum. Sed bibasdum purus vel ipsum sagittis, quis fermentum dolor lobortis. Etiam vulputate eleifasd lectus vel varius. Phasellus imperdiet lectus sit amet ipsum egestas, ut bibasdum ipsum malesuada. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed mollis eros sit amet elit porttitor, vel venenatis turpis venenatis. Nulla tempus tortor at eros efficitur, sit amet dapibus ipsum malesuada. Ut at mauris sed nunc malesuada convallis. Duis id sem vel magna varius eleifasd vel at est. Donec eget orci a ipsum tempor lobortis. Sed at consectetur ipsum.")
    YGNodeSetMeasureFunc(root_child0, _intrinsic_size_measure)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 2000
    assert YGNodeLayoutGetHeight(root) == 2000

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 1290

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 2000
    assert YGNodeLayoutGetHeight(root) == 2000

    assert YGNodeLayoutGetLeft(root_child0) == 1900
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 1290

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_contains_inner_text_no_width_fixed_height():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 2000)
    YGNodeStyleSetHeight(root, 2000)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetHeight(root_child0, 20)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeSetContext(root_child0, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eleifasd et tortor ac auctor. Integer at volutpat libero, sed elementum dui interdum id. Aliquam consectetur massa vel neque aliquet, quis consequat risus fringilla. Fusce rhoncus ipsum tempor eros aliquam, vel tempus metus ullamcorper. Nam at nulla sed tellus vestibulum fringilla vel sit amet ligula. Proin velit lectus, euismod sit amet quam vel ultricies dolor, vitae finibus lorem ipsum. Pellentesque molestie at mi sit amet dictum. Donec vehicula lacinia felis sit amet consectetur. Praesent sodales enim sapien, sed varius ipsum pellentesque vel. Aenean eu mi eu justo tincidunt finibus vel sit amet ipsum. Sed bibasdum purus vel ipsum sagittis, quis fermentum dolor lobortis. Etiam vulputate eleifasd lectus vel varius. Phasellus imperdiet lectus sit amet ipsum egestas, ut bibasdum ipsum malesuada. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed mollis eros sit amet elit porttitor, vel venenatis turpis venenatis. Nulla tempus tortor at eros efficitur, sit amet dapibus ipsum malesuada. Ut at mauris sed nunc malesuada convallis. Duis id sem vel magna varius eleifasd vel at est. Donec eget orci a ipsum tempor lobortis. Sed at consectetur ipsum.")
    YGNodeSetMeasureFunc(root_child0, _intrinsic_size_measure)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 2000
    assert YGNodeLayoutGetHeight(root) == 2000

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 2000
    assert YGNodeLayoutGetHeight(root_child0) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 2000
    assert YGNodeLayoutGetHeight(root) == 2000

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 2000
    assert YGNodeLayoutGetHeight(root_child0) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_contains_inner_text_fixed_width_fixed_height():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 2000)
    YGNodeStyleSetHeight(root, 2000)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 20)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeSetContext(root_child0, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eleifasd et tortor ac auctor. Integer at volutpat libero, sed elementum dui interdum id. Aliquam consectetur massa vel neque aliquet, quis consequat risus fringilla. Fusce rhoncus ipsum tempor eros aliquam, vel tempus metus ullamcorper. Nam at nulla sed tellus vestibulum fringilla vel sit amet ligula. Proin velit lectus, euismod sit amet quam vel ultricies dolor, vitae finibus lorem ipsum. Pellentesque molestie at mi sit amet dictum. Donec vehicula lacinia felis sit amet consectetur. Praesent sodales enim sapien, sed varius ipsum pellentesque vel. Aenean eu mi eu justo tincidunt finibus vel sit amet ipsum. Sed bibasdum purus vel ipsum sagittis, quis fermentum dolor lobortis. Etiam vulputate eleifasd lectus vel varius. Phasellus imperdiet lectus sit amet ipsum egestas, ut bibasdum ipsum malesuada. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed mollis eros sit amet elit porttitor, vel venenatis turpis venenatis. Nulla tempus tortor at eros efficitur, sit amet dapibus ipsum malesuada. Ut at mauris sed nunc malesuada convallis. Duis id sem vel magna varius eleifasd vel at est. Donec eget orci a ipsum tempor lobortis. Sed at consectetur ipsum.")
    YGNodeSetMeasureFunc(root_child0, _intrinsic_size_measure)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 2000
    assert YGNodeLayoutGetHeight(root) == 2000

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 2000
    assert YGNodeLayoutGetHeight(root) == 2000

    assert YGNodeLayoutGetLeft(root_child0) == 1950
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_contains_inner_text_max_width_max_height():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 2000)
    YGNodeStyleSetHeight(root, 2000)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetMaxWidth(root_child0, 50)
    YGNodeStyleSetMaxHeight(root_child0, 20)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeSetContext(root_child0, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eleifasd et tortor ac auctor. Integer at volutpat libero, sed elementum dui interdum id. Aliquam consectetur massa vel neque aliquet, quis consequat risus fringilla. Fusce rhoncus ipsum tempor eros aliquam, vel tempus metus ullamcorper. Nam at nulla sed tellus vestibulum fringilla vel sit amet ligula. Proin velit lectus, euismod sit amet quam vel ultricies dolor, vitae finibus lorem ipsum. Pellentesque molestie at mi sit amet dictum. Donec vehicula lacinia felis sit amet consectetur. Praesent sodales enim sapien, sed varius ipsum pellentesque vel. Aenean eu mi eu justo tincidunt finibus vel sit amet ipsum. Sed bibasdum purus vel ipsum sagittis, quis fermentum dolor lobortis. Etiam vulputate eleifasd lectus vel varius. Phasellus imperdiet lectus sit amet ipsum egestas, ut bibasdum ipsum malesuada. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed mollis eros sit amet elit porttitor, vel venenatis turpis venenatis. Nulla tempus tortor at eros efficitur, sit amet dapibus ipsum malesuada. Ut at mauris sed nunc malesuada convallis. Duis id sem vel magna varius eleifasd vel at est. Donec eget orci a ipsum tempor lobortis. Sed at consectetur ipsum.")
    YGNodeSetMeasureFunc(root_child0, _intrinsic_size_measure)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 2000
    assert YGNodeLayoutGetHeight(root) == 2000

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 2000
    assert YGNodeLayoutGetHeight(root) == 2000

    assert YGNodeLayoutGetLeft(root_child0) == 1950
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_contains_inner_text_max_width_max_height_column():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 2000)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMaxWidth(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeSetContext(root_child0, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eleifasd et tortor ac auctor. Integer at volutpat libero, sed elementum dui interdum id. Aliquam consectetur massa vel neque aliquet, quis consequat risus fringilla. Fusce rhoncus ipsum tempor eros aliquam, vel tempus metus ullamcorper. Nam at nulla sed tellus vestibulum fringilla vel sit amet ligula. Proin velit lectus, euismod sit amet quam vel ultricies dolor, vitae finibus lorem ipsum. Pellentesque molestie at mi sit amet dictum. Donec vehicula lacinia felis sit amet consectetur. Praesent sodales enim sapien, sed varius ipsum pellentesque vel. Aenean eu mi eu justo tincidunt finibus vel sit amet ipsum. Sed bibasdum purus vel ipsum sagittis, quis fermentum dolor lobortis. Etiam vulputate eleifasd lectus vel varius. Phasellus imperdiet lectus sit amet ipsum egestas, ut bibasdum ipsum malesuada. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed mollis eros sit amet elit porttitor, vel venenatis turpis venenatis. Nulla tempus tortor at eros efficitur, sit amet dapibus ipsum malesuada. Ut at mauris sed nunc malesuada convallis. Duis id sem vel magna varius eleifasd vel at est. Donec eget orci a ipsum tempor lobortis. Sed at consectetur ipsum.")
    YGNodeSetMeasureFunc(root_child0, _intrinsic_size_measure)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 2000
    assert YGNodeLayoutGetHeight(root) == 1890

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 1890

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 2000
    assert YGNodeLayoutGetHeight(root) == 1890

    assert YGNodeLayoutGetLeft(root_child0) == 1950
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 1890

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_contains_inner_text_max_width():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 2000)
    YGNodeStyleSetHeight(root, 2000)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetMaxWidth(root_child0, 100)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeSetContext(root_child0, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eleifasd et tortor ac auctor. Integer at volutpat libero, sed elementum dui interdum id. Aliquam consectetur massa vel neque aliquet, quis consequat risus fringilla. Fusce rhoncus ipsum tempor eros aliquam, vel tempus metus ullamcorper. Nam at nulla sed tellus vestibulum fringilla vel sit amet ligula. Proin velit lectus, euismod sit amet quam vel ultricies dolor, vitae finibus lorem ipsum. Pellentesque molestie at mi sit amet dictum. Donec vehicula lacinia felis sit amet consectetur. Praesent sodales enim sapien, sed varius ipsum pellentesque vel. Aenean eu mi eu justo tincidunt finibus vel sit amet ipsum. Sed bibasdum purus vel ipsum sagittis, quis fermentum dolor lobortis. Etiam vulputate eleifasd lectus vel varius. Phasellus imperdiet lectus sit amet ipsum egestas, ut bibasdum ipsum malesuada. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed mollis eros sit amet elit porttitor, vel venenatis turpis venenatis. Nulla tempus tortor at eros efficitur, sit amet dapibus ipsum malesuada. Ut at mauris sed nunc malesuada convallis. Duis id sem vel magna varius eleifasd vel at est. Donec eget orci a ipsum tempor lobortis. Sed at consectetur ipsum.")
    YGNodeSetMeasureFunc(root_child0, _intrinsic_size_measure)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 2000
    assert YGNodeLayoutGetHeight(root) == 2000

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 1290

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 2000
    assert YGNodeLayoutGetHeight(root) == 2000

    assert YGNodeLayoutGetLeft(root_child0) == 1900
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 1290

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_contains_inner_text_fixed_width_shorter_text():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 2000)
    YGNodeStyleSetHeight(root, 2000)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeSetContext(root_child0, "Lorem ipsum")
    YGNodeSetMeasureFunc(root_child0, _intrinsic_size_measure)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 2000
    assert YGNodeLayoutGetHeight(root) == 2000

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 2000
    assert YGNodeLayoutGetHeight(root) == 2000

    assert YGNodeLayoutGetLeft(root_child0) == 1900
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_contains_inner_text_fixed_height_shorter_text():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 2000)
    YGNodeStyleSetHeight(root, 2000)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetHeight(root_child0, 100)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeSetContext(root_child0, "Lorem ipsum")
    YGNodeSetMeasureFunc(root_child0, _intrinsic_size_measure)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 2000
    assert YGNodeLayoutGetHeight(root) == 2000

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 110
    assert YGNodeLayoutGetHeight(root_child0) == 100

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 2000
    assert YGNodeLayoutGetHeight(root) == 2000

    assert YGNodeLayoutGetLeft(root_child0) == 1890
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 110
    assert YGNodeLayoutGetHeight(root_child0) == 100

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_contains_inner_text_max_height():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 2000)
    YGNodeStyleSetHeight(root, 2000)
    YGNodeStyleSetAlignItems(root, YGAlign.YGAlignFlexStart)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetMaxHeight(root_child0, 20)
    YGNodeInsertChild(root, root_child0, 0)
    YGNodeSetContext(root_child0, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eleifasd et tortor ac auctor. Integer at volutpat libero, sed elementum dui interdum id. Aliquam consectetur massa vel neque aliquet, quis consequat risus fringilla. Fusce rhoncus ipsum tempor eros aliquam, vel tempus metus ullamcorper. Nam at nulla sed tellus vestibulum fringilla vel sit amet ligula. Proin velit lectus, euismod sit amet quam vel ultricies dolor, vitae finibus lorem ipsum. Pellentesque molestie at mi sit amet dictum. Donec vehicula lacinia felis sit amet consectetur. Praesent sodales enim sapien, sed varius ipsum pellentesque vel. Aenean eu mi eu justo tincidunt finibus vel sit amet ipsum. Sed bibasdum purus vel ipsum sagittis, quis fermentum dolor lobortis. Etiam vulputate eleifasd lectus vel varius. Phasellus imperdiet lectus sit amet ipsum egestas, ut bibasdum ipsum malesuada. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed mollis eros sit amet elit porttitor, vel venenatis turpis venenatis. Nulla tempus tortor at eros efficitur, sit amet dapibus ipsum malesuada. Ut at mauris sed nunc malesuada convallis. Duis id sem vel magna varius eleifasd vel at est. Donec eget orci a ipsum tempor lobortis. Sed at consectetur ipsum.")
    YGNodeSetMeasureFunc(root_child0, _intrinsic_size_measure)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 2000
    assert YGNodeLayoutGetHeight(root) == 2000

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 2000
    assert YGNodeLayoutGetHeight(root_child0) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 2000
    assert YGNodeLayoutGetHeight(root) == 2000

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 2000
    assert YGNodeLayoutGetHeight(root_child0) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_max_content_width():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidthMaxContent(root)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 100)
    YGNodeStyleSetHeight(root_child1, 50)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 25)
    YGNodeStyleSetHeight(root_child2, 50)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 175
    assert YGNodeLayoutGetHeight(root) == 50

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 50

    assert YGNodeLayoutGetLeft(root_child2) == 150
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 25
    assert YGNodeLayoutGetHeight(root_child2) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 175
    assert YGNodeLayoutGetHeight(root) == 50

    assert YGNodeLayoutGetLeft(root_child0) == 125
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 25
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 50

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 25
    assert YGNodeLayoutGetHeight(root_child2) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_fit_content_width():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 90)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidthFitContent(root_child0)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 50)
    YGNodeStyleSetHeight(root_child0_child0, 50)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 100)
    YGNodeStyleSetHeight(root_child0_child1, 50)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 25)
    YGNodeStyleSetHeight(root_child0_child2, 50)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 90
    assert YGNodeLayoutGetHeight(root) == 150

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 150

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 50
    assert YGNodeLayoutGetWidth(root_child0_child1) == 100
    assert YGNodeLayoutGetHeight(root_child0_child1) == 50

    assert YGNodeLayoutGetLeft(root_child0_child2) == 0
    assert YGNodeLayoutGetTop(root_child0_child2) == 100
    assert YGNodeLayoutGetWidth(root_child0_child2) == 25
    assert YGNodeLayoutGetHeight(root_child0_child2) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 90
    assert YGNodeLayoutGetHeight(root) == 150

    assert YGNodeLayoutGetLeft(root_child0) == -10
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 150

    assert YGNodeLayoutGetLeft(root_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 50
    assert YGNodeLayoutGetWidth(root_child0_child1) == 100
    assert YGNodeLayoutGetHeight(root_child0_child1) == 50

    assert YGNodeLayoutGetLeft(root_child0_child2) == 75
    assert YGNodeLayoutGetTop(root_child0_child2) == 100
    assert YGNodeLayoutGetWidth(root_child0_child2) == 25
    assert YGNodeLayoutGetHeight(root_child0_child2) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_stretch_width():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 500)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetWidthStretch(root_child0)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 50)
    YGNodeStyleSetHeight(root_child0_child0, 50)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 100)
    YGNodeStyleSetHeight(root_child0_child1, 50)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 25)
    YGNodeStyleSetHeight(root_child0_child2, 50)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 50

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 500
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 50
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 100
    assert YGNodeLayoutGetHeight(root_child0_child1) == 50

    assert YGNodeLayoutGetLeft(root_child0_child2) == 150
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 25
    assert YGNodeLayoutGetHeight(root_child0_child2) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 50

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 500
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0) == 450
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 350
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 100
    assert YGNodeLayoutGetHeight(root_child0_child1) == 50

    assert YGNodeLayoutGetLeft(root_child0_child2) == 325
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 25
    assert YGNodeLayoutGetHeight(root_child0_child2) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_max_content_height():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeightMaxContent(root)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 100)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 50)
    YGNodeStyleSetHeight(root_child2, 25)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 50
    assert YGNodeLayoutGetHeight(root) == 175

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 50
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 150
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 25

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 50
    assert YGNodeLayoutGetHeight(root) == 175

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 50
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 150
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 25

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_fit_content_height():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 90)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeightFitContent(root_child0)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 50)
    YGNodeStyleSetHeight(root_child0_child0, 50)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 50)
    YGNodeStyleSetHeight(root_child0_child1, 100)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 50)
    YGNodeStyleSetHeight(root_child0_child2, 25)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 50
    assert YGNodeLayoutGetHeight(root) == 90

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 175

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 50
    assert YGNodeLayoutGetWidth(root_child0_child1) == 50
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 0
    assert YGNodeLayoutGetTop(root_child0_child2) == 150
    assert YGNodeLayoutGetWidth(root_child0_child2) == 50
    assert YGNodeLayoutGetHeight(root_child0_child2) == 25

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 50
    assert YGNodeLayoutGetHeight(root) == 90

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 175

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 50
    assert YGNodeLayoutGetWidth(root_child0_child1) == 50
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 0
    assert YGNodeLayoutGetTop(root_child0_child2) == 150
    assert YGNodeLayoutGetWidth(root_child0_child2) == 50
    assert YGNodeLayoutGetHeight(root_child0_child2) == 25

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_stretch_height():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 500)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetHeightStretch(root_child0)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 50)
    YGNodeStyleSetHeight(root_child0_child0, 50)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 50)
    YGNodeStyleSetHeight(root_child0_child1, 100)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 50)
    YGNodeStyleSetHeight(root_child0_child2, 25)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 50
    assert YGNodeLayoutGetHeight(root) == 500

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 500

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 50
    assert YGNodeLayoutGetWidth(root_child0_child1) == 50
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 0
    assert YGNodeLayoutGetTop(root_child0_child2) == 150
    assert YGNodeLayoutGetWidth(root_child0_child2) == 50
    assert YGNodeLayoutGetHeight(root_child0_child2) == 25

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 50
    assert YGNodeLayoutGetHeight(root) == 500

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 500

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 50
    assert YGNodeLayoutGetWidth(root_child0_child1) == 50
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 0
    assert YGNodeLayoutGetTop(root_child0_child2) == 150
    assert YGNodeLayoutGetWidth(root_child0_child2) == 50
    assert YGNodeLayoutGetHeight(root_child0_child2) == 25

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_max_content_flex_basis_column():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexBasisMaxContent(root)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 100)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 50)
    YGNodeStyleSetHeight(root_child2, 25)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 50
    assert YGNodeLayoutGetHeight(root) == 175

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 50
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 150
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 25

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 50
    assert YGNodeLayoutGetHeight(root) == 175

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 50
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 150
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 25

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_fit_content_flex_basis_column():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 90)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexBasisFitContent(root_child0)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 50)
    YGNodeStyleSetHeight(root_child0_child0, 50)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 50)
    YGNodeStyleSetHeight(root_child0_child1, 100)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 50)
    YGNodeStyleSetHeight(root_child0_child2, 25)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 50
    assert YGNodeLayoutGetHeight(root) == 90

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 175

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 50
    assert YGNodeLayoutGetWidth(root_child0_child1) == 50
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 0
    assert YGNodeLayoutGetTop(root_child0_child2) == 150
    assert YGNodeLayoutGetWidth(root_child0_child2) == 50
    assert YGNodeLayoutGetHeight(root_child0_child2) == 25

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 50
    assert YGNodeLayoutGetHeight(root) == 90

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 175

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 50
    assert YGNodeLayoutGetWidth(root_child0_child1) == 50
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 0
    assert YGNodeLayoutGetTop(root_child0_child2) == 150
    assert YGNodeLayoutGetWidth(root_child0_child2) == 50
    assert YGNodeLayoutGetHeight(root_child0_child2) == 25

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_stretch_flex_basis_column():
    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 500)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexBasisStretch(root_child0)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 50)
    YGNodeStyleSetHeight(root_child0_child0, 50)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 50)
    YGNodeStyleSetHeight(root_child0_child1, 100)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 50)
    YGNodeStyleSetHeight(root_child0_child2, 25)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 50
    assert YGNodeLayoutGetHeight(root) == 500

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 175

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 50
    assert YGNodeLayoutGetWidth(root_child0_child1) == 50
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 0
    assert YGNodeLayoutGetTop(root_child0_child2) == 150
    assert YGNodeLayoutGetWidth(root_child0_child2) == 50
    assert YGNodeLayoutGetHeight(root_child0_child2) == 25

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 50
    assert YGNodeLayoutGetHeight(root) == 500

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 175

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 50
    assert YGNodeLayoutGetWidth(root_child0_child1) == 50
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 0
    assert YGNodeLayoutGetTop(root_child0_child2) == 150
    assert YGNodeLayoutGetWidth(root_child0_child2) == 50
    assert YGNodeLayoutGetHeight(root_child0_child2) == 25

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_max_content_flex_basis_row():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexBasisMaxContent(root)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 100)
    YGNodeStyleSetHeight(root_child1, 500)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 25)
    YGNodeStyleSetHeight(root_child2, 50)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 600

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 50
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 500

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 550
    assert YGNodeLayoutGetWidth(root_child2) == 25
    assert YGNodeLayoutGetHeight(root_child2) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 100
    assert YGNodeLayoutGetHeight(root) == 600

    assert YGNodeLayoutGetLeft(root_child0) == 50
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 50
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 500

    assert YGNodeLayoutGetLeft(root_child2) == 75
    assert YGNodeLayoutGetTop(root_child2) == 550
    assert YGNodeLayoutGetWidth(root_child2) == 25
    assert YGNodeLayoutGetHeight(root_child2) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_fit_content_flex_basis_row():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 90)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexBasisFitContent(root_child0)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 50)
    YGNodeStyleSetHeight(root_child0_child0, 50)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 100)
    YGNodeStyleSetHeight(root_child0_child1, 50)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 25)
    YGNodeStyleSetHeight(root_child0_child2, 50)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 90
    assert YGNodeLayoutGetHeight(root) == 150

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 90
    assert YGNodeLayoutGetHeight(root_child0) == 150

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 50
    assert YGNodeLayoutGetWidth(root_child0_child1) == 100
    assert YGNodeLayoutGetHeight(root_child0_child1) == 50

    assert YGNodeLayoutGetLeft(root_child0_child2) == 0
    assert YGNodeLayoutGetTop(root_child0_child2) == 100
    assert YGNodeLayoutGetWidth(root_child0_child2) == 25
    assert YGNodeLayoutGetHeight(root_child0_child2) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 90
    assert YGNodeLayoutGetHeight(root) == 150

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 90
    assert YGNodeLayoutGetHeight(root_child0) == 150

    assert YGNodeLayoutGetLeft(root_child0_child0) == 40
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == -10
    assert YGNodeLayoutGetTop(root_child0_child1) == 50
    assert YGNodeLayoutGetWidth(root_child0_child1) == 100
    assert YGNodeLayoutGetHeight(root_child0_child1) == 50

    assert YGNodeLayoutGetLeft(root_child0_child2) == 65
    assert YGNodeLayoutGetTop(root_child0_child2) == 100
    assert YGNodeLayoutGetWidth(root_child0_child2) == 25
    assert YGNodeLayoutGetHeight(root_child0_child2) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_stretch_flex_basis_row():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 500)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexBasisStretch(root_child0)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 50)
    YGNodeStyleSetHeight(root_child0_child0, 50)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 100)
    YGNodeStyleSetHeight(root_child0_child1, 50)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 25)
    YGNodeStyleSetHeight(root_child0_child2, 50)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 50

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 500
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 50
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 100
    assert YGNodeLayoutGetHeight(root_child0_child1) == 50

    assert YGNodeLayoutGetLeft(root_child0_child2) == 150
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 25
    assert YGNodeLayoutGetHeight(root_child0_child2) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 50

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 500
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0) == 450
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 350
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 100
    assert YGNodeLayoutGetHeight(root_child0_child1) == 50

    assert YGNodeLayoutGetLeft(root_child0_child2) == 325
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 25
    assert YGNodeLayoutGetHeight(root_child0_child2) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_max_content_max_width():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetMaxWidthMaxContent(root)
    YGNodeStyleSetWidth(root, 200)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 100)
    YGNodeStyleSetHeight(root_child1, 50)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 25)
    YGNodeStyleSetHeight(root_child2, 50)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 175
    assert YGNodeLayoutGetHeight(root) == 50

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 50

    assert YGNodeLayoutGetLeft(root_child2) == 150
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 25
    assert YGNodeLayoutGetHeight(root_child2) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 175
    assert YGNodeLayoutGetHeight(root) == 50

    assert YGNodeLayoutGetLeft(root_child0) == 125
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 25
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 50

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 25
    assert YGNodeLayoutGetHeight(root_child2) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_fit_content_max_width():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 90)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetMaxWidthFitContent(root_child0)
    YGNodeStyleSetWidth(root_child0, 110)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 50)
    YGNodeStyleSetHeight(root_child0_child0, 50)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 100)
    YGNodeStyleSetHeight(root_child0_child1, 50)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 25)
    YGNodeStyleSetHeight(root_child0_child2, 50)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 90
    assert YGNodeLayoutGetHeight(root) == 150

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 150

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 50
    assert YGNodeLayoutGetWidth(root_child0_child1) == 100
    assert YGNodeLayoutGetHeight(root_child0_child1) == 50

    assert YGNodeLayoutGetLeft(root_child0_child2) == 0
    assert YGNodeLayoutGetTop(root_child0_child2) == 100
    assert YGNodeLayoutGetWidth(root_child0_child2) == 25
    assert YGNodeLayoutGetHeight(root_child0_child2) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 90
    assert YGNodeLayoutGetHeight(root) == 150

    assert YGNodeLayoutGetLeft(root_child0) == -10
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 150

    assert YGNodeLayoutGetLeft(root_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 50
    assert YGNodeLayoutGetWidth(root_child0_child1) == 100
    assert YGNodeLayoutGetHeight(root_child0_child1) == 50

    assert YGNodeLayoutGetLeft(root_child0_child2) == 75
    assert YGNodeLayoutGetTop(root_child0_child2) == 100
    assert YGNodeLayoutGetWidth(root_child0_child2) == 25
    assert YGNodeLayoutGetHeight(root_child0_child2) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_stretch_max_width():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 500)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetMaxWidthStretch(root_child0)
    YGNodeStyleSetWidth(root_child0, 600)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 50)
    YGNodeStyleSetHeight(root_child0_child0, 50)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 100)
    YGNodeStyleSetHeight(root_child0_child1, 50)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 25)
    YGNodeStyleSetHeight(root_child0_child2, 50)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 50

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 500
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 50
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 100
    assert YGNodeLayoutGetHeight(root_child0_child1) == 50

    assert YGNodeLayoutGetLeft(root_child0_child2) == 150
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 25
    assert YGNodeLayoutGetHeight(root_child0_child2) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 50

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 500
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0) == 450
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 350
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 100
    assert YGNodeLayoutGetHeight(root_child0_child1) == 50

    assert YGNodeLayoutGetLeft(root_child0_child2) == 325
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 25
    assert YGNodeLayoutGetHeight(root_child0_child2) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_max_content_min_width():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetMinWidthMaxContent(root)
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 100)
    YGNodeStyleSetHeight(root_child1, 50)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 25)
    YGNodeStyleSetHeight(root_child2, 50)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 175
    assert YGNodeLayoutGetHeight(root) == 50

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 50

    assert YGNodeLayoutGetLeft(root_child2) == 150
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 25
    assert YGNodeLayoutGetHeight(root_child2) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 175
    assert YGNodeLayoutGetHeight(root) == 50

    assert YGNodeLayoutGetLeft(root_child0) == 125
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 25
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 100
    assert YGNodeLayoutGetHeight(root_child1) == 50

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 25
    assert YGNodeLayoutGetHeight(root_child2) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_fit_content_min_width():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 90)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetMinWidthFitContent(root_child0)
    YGNodeStyleSetWidth(root_child0, 90)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 50)
    YGNodeStyleSetHeight(root_child0_child0, 50)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 100)
    YGNodeStyleSetHeight(root_child0_child1, 50)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 25)
    YGNodeStyleSetHeight(root_child0_child2, 50)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 90
    assert YGNodeLayoutGetHeight(root) == 150

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 150

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 50
    assert YGNodeLayoutGetWidth(root_child0_child1) == 100
    assert YGNodeLayoutGetHeight(root_child0_child1) == 50

    assert YGNodeLayoutGetLeft(root_child0_child2) == 0
    assert YGNodeLayoutGetTop(root_child0_child2) == 100
    assert YGNodeLayoutGetWidth(root_child0_child2) == 25
    assert YGNodeLayoutGetHeight(root_child0_child2) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 90
    assert YGNodeLayoutGetHeight(root) == 150

    assert YGNodeLayoutGetLeft(root_child0) == -10
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 100
    assert YGNodeLayoutGetHeight(root_child0) == 150

    assert YGNodeLayoutGetLeft(root_child0_child0) == 50
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 50
    assert YGNodeLayoutGetWidth(root_child0_child1) == 100
    assert YGNodeLayoutGetHeight(root_child0_child1) == 50

    assert YGNodeLayoutGetLeft(root_child0_child2) == 75
    assert YGNodeLayoutGetTop(root_child0_child2) == 100
    assert YGNodeLayoutGetWidth(root_child0_child2) == 25
    assert YGNodeLayoutGetHeight(root_child0_child2) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_stretch_min_width():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 500)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetMinWidthStretch(root_child0)
    YGNodeStyleSetWidth(root_child0, 400)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 50)
    YGNodeStyleSetHeight(root_child0_child0, 50)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 100)
    YGNodeStyleSetHeight(root_child0_child1, 50)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 25)
    YGNodeStyleSetHeight(root_child0_child2, 50)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 50

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 500
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 50
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 100
    assert YGNodeLayoutGetHeight(root_child0_child1) == 50

    assert YGNodeLayoutGetLeft(root_child0_child2) == 150
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 25
    assert YGNodeLayoutGetHeight(root_child0_child2) == 50

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 500
    assert YGNodeLayoutGetHeight(root) == 50

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 500
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child0) == 450
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 350
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 100
    assert YGNodeLayoutGetHeight(root_child0_child1) == 50

    assert YGNodeLayoutGetLeft(root_child0_child2) == 325
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 25
    assert YGNodeLayoutGetHeight(root_child0_child2) == 50

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_max_content_max_height():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetMaxHeightMaxContent(root)
    YGNodeStyleSetHeight(root, 200)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 100)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 50)
    YGNodeStyleSetHeight(root_child2, 25)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 50
    assert YGNodeLayoutGetHeight(root) == 175

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 50
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 150
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 25

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 50
    assert YGNodeLayoutGetHeight(root) == 175

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 0
    assert YGNodeLayoutGetTop(root_child1) == 50
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 0
    assert YGNodeLayoutGetTop(root_child2) == 150
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 25

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_fit_content_max_height():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 90)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMaxHeightFitContent(root_child0)
    YGNodeStyleSetHeight(root_child0, 110)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 50)
    YGNodeStyleSetHeight(root_child0_child0, 50)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 50)
    YGNodeStyleSetHeight(root_child0_child1, 100)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 50)
    YGNodeStyleSetHeight(root_child0_child2, 25)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 50
    assert YGNodeLayoutGetHeight(root) == 90

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 50
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 50
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 100
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 50
    assert YGNodeLayoutGetHeight(root_child0_child2) == 25

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 50
    assert YGNodeLayoutGetHeight(root) == 90

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == -50
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 50
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == -100
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 50
    assert YGNodeLayoutGetHeight(root_child0_child2) == 25

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_stretch_max_height():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 500)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMaxHeightStretch(root_child0)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeStyleSetHeight(root_child0, 600)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 50)
    YGNodeStyleSetHeight(root_child0_child0, 50)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 50)
    YGNodeStyleSetHeight(root_child0_child1, 100)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 50)
    YGNodeStyleSetHeight(root_child0_child2, 25)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 50
    assert YGNodeLayoutGetHeight(root) == 500

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 500

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 50
    assert YGNodeLayoutGetWidth(root_child0_child1) == 50
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 0
    assert YGNodeLayoutGetTop(root_child0_child2) == 150
    assert YGNodeLayoutGetWidth(root_child0_child2) == 50
    assert YGNodeLayoutGetHeight(root_child0_child2) == 25

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 50
    assert YGNodeLayoutGetHeight(root) == 500

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 500

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 50
    assert YGNodeLayoutGetWidth(root_child0_child1) == 50
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 0
    assert YGNodeLayoutGetTop(root_child0_child2) == 150
    assert YGNodeLayoutGetWidth(root_child0_child2) == 50
    assert YGNodeLayoutGetHeight(root_child0_child2) == 25

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_max_content_min_height():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetMinHeightMaxContent(root)
    YGNodeStyleSetHeight(root, 100)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0, 50)
    YGNodeStyleSetHeight(root_child0, 50)
    YGNodeInsertChild(root, root_child0, 0)

    root_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child1, 50)
    YGNodeStyleSetHeight(root_child1, 100)
    YGNodeInsertChild(root, root_child1, 1)

    root_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child2, 50)
    YGNodeStyleSetHeight(root_child2, 25)
    YGNodeInsertChild(root, root_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 50
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == 50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == 100
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 25

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 50
    assert YGNodeLayoutGetHeight(root) == 100

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 50

    assert YGNodeLayoutGetLeft(root_child1) == -50
    assert YGNodeLayoutGetTop(root_child1) == 0
    assert YGNodeLayoutGetWidth(root_child1) == 50
    assert YGNodeLayoutGetHeight(root_child1) == 100

    assert YGNodeLayoutGetLeft(root_child2) == -100
    assert YGNodeLayoutGetTop(root_child2) == 0
    assert YGNodeLayoutGetWidth(root_child2) == 50
    assert YGNodeLayoutGetHeight(root_child2) == 25

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_fit_content_min_height():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 90)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMinHeightFitContent(root_child0)
    YGNodeStyleSetHeight(root_child0, 90)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 50)
    YGNodeStyleSetHeight(root_child0_child0, 50)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 50)
    YGNodeStyleSetHeight(root_child0_child1, 100)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 50)
    YGNodeStyleSetHeight(root_child0_child2, 25)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 50
    assert YGNodeLayoutGetHeight(root) == 90

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 50
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 50
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 100
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 50
    assert YGNodeLayoutGetHeight(root_child0_child2) == 25

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 50
    assert YGNodeLayoutGetHeight(root) == 90

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 100

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == -50
    assert YGNodeLayoutGetTop(root_child0_child1) == 0
    assert YGNodeLayoutGetWidth(root_child0_child1) == 50
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == -100
    assert YGNodeLayoutGetTop(root_child0_child2) == 0
    assert YGNodeLayoutGetWidth(root_child0_child2) == 50
    assert YGNodeLayoutGetHeight(root_child0_child2) == 25

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_stretch_min_height():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetHeight(root, 500)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMinHeightStretch(root_child0)
    YGNodeStyleSetFlexWrap(root_child0, YGWrap.YGWrapWrap)
    YGNodeStyleSetHeight(root_child0, 400)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child0, 50)
    YGNodeStyleSetHeight(root_child0_child0, 50)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)

    root_child0_child1 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child1, 50)
    YGNodeStyleSetHeight(root_child0_child1, 100)
    YGNodeInsertChild(root_child0, root_child0_child1, 1)

    root_child0_child2 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidth(root_child0_child2, 50)
    YGNodeStyleSetHeight(root_child0_child2, 25)
    YGNodeInsertChild(root_child0, root_child0_child2, 2)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 50
    assert YGNodeLayoutGetHeight(root) == 500

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 500

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 50
    assert YGNodeLayoutGetWidth(root_child0_child1) == 50
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 0
    assert YGNodeLayoutGetTop(root_child0_child2) == 150
    assert YGNodeLayoutGetWidth(root_child0_child2) == 50
    assert YGNodeLayoutGetHeight(root_child0_child2) == 25

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 50
    assert YGNodeLayoutGetHeight(root) == 500

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0) == 500

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 50
    assert YGNodeLayoutGetHeight(root_child0_child0) == 50

    assert YGNodeLayoutGetLeft(root_child0_child1) == 0
    assert YGNodeLayoutGetTop(root_child0_child1) == 50
    assert YGNodeLayoutGetWidth(root_child0_child1) == 50
    assert YGNodeLayoutGetHeight(root_child0_child1) == 100

    assert YGNodeLayoutGetLeft(root_child0_child2) == 0
    assert YGNodeLayoutGetTop(root_child0_child2) == 150
    assert YGNodeLayoutGetWidth(root_child0_child2) == 50
    assert YGNodeLayoutGetHeight(root_child0_child2) == 25

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_text_max_content_width():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthMaxContent(root_child0)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)
    YGNodeSetContext(root_child0_child0, "Lorem ipsum sdafhasdfkjlasdhlkajsfhasldkfhasdlkahsdflkjasdhflaksdfasdlkjhasdlfjahsdfljkasdhalsdfhas dolor sit amet")
    YGNodeSetMeasureFunc(root_child0_child0, _intrinsic_size_measure)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 10

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 1140
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 1140
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 10

    assert YGNodeLayoutGetLeft(root_child0) == -940
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 1140
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 1140
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_text_stretch_width():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthStretch(root_child0)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)
    YGNodeSetContext(root_child0_child0, "Lorem ipsum dolor sit amet")
    YGNodeSetMeasureFunc(root_child0_child0, _intrinsic_size_measure)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 20

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 20

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_text_fit_content_width():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetWidthFitContent(root_child0)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)
    YGNodeSetContext(root_child0_child0, "Lorem ipsum sdafhasdfkjlasdhlkajsfhasldkfhasdlkahsdflkjasdhflaksdfasdlkjhasdlfjahsdfljkasdhalsdfhas dolor sit amet")
    YGNodeSetMeasureFunc(root_child0_child0, _intrinsic_size_measure)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 30

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 870
    assert YGNodeLayoutGetHeight(root_child0) == 30

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 870
    assert YGNodeLayoutGetHeight(root_child0_child0) == 30

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 30

    assert YGNodeLayoutGetLeft(root_child0) == -670
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 870
    assert YGNodeLayoutGetHeight(root_child0) == 30

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 870
    assert YGNodeLayoutGetHeight(root_child0_child0) == 30

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_text_max_content_min_width():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMinWidthMaxContent(root_child0)
    YGNodeStyleSetWidth(root_child0, 200)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)
    YGNodeSetContext(root_child0_child0, "Lorem ipsum sdafhasdfkjlasdhlkajsfhasldkfhasdlkahsdflkjasdhflaksdfasdlkjhasdlfjahsdfljkasdhalsdfhas dolor sit amet")
    YGNodeSetMeasureFunc(root_child0_child0, _intrinsic_size_measure)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 10

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 1140
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 1140
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 10

    assert YGNodeLayoutGetLeft(root_child0) == -940
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 1140
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 1140
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_text_stretch_min_width():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMinWidthStretch(root_child0)
    YGNodeStyleSetWidth(root_child0, 100)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)
    YGNodeSetContext(root_child0_child0, "Lorem ipsum dolor sit amet")
    YGNodeSetMeasureFunc(root_child0_child0, _intrinsic_size_measure)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 20

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 20

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_text_fit_content_min_width():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMinWidthFitContent(root_child0)
    YGNodeStyleSetWidth(root_child0, 300)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)
    YGNodeSetContext(root_child0_child0, "Lorem ipsum sdafhasdfkjlasdhlkajsfhasldkfhasdlkahsdflkjasdhflaksdfasdlkjhasdlfjahsdfljkasdhalsdfhas dolor sit amet")
    YGNodeSetMeasureFunc(root_child0_child0, _intrinsic_size_measure)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 30

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 870
    assert YGNodeLayoutGetHeight(root_child0) == 30

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 870
    assert YGNodeLayoutGetHeight(root_child0_child0) == 30

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 30

    assert YGNodeLayoutGetLeft(root_child0) == -670
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 870
    assert YGNodeLayoutGetHeight(root_child0) == 30

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 870
    assert YGNodeLayoutGetHeight(root_child0_child0) == 30

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_text_max_content_max_width():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMaxWidthMaxContent(root_child0)
    YGNodeStyleSetWidth(root_child0, 2000)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)
    YGNodeSetContext(root_child0_child0, "Lorem ipsum sdafhasdfkjlasdhlkajsfhasldkfhasdlkahsdflkjasdhflaksdfasdlkjhasdlfjahsdfljkasdhalsdfhas dolor sit amet")
    YGNodeSetMeasureFunc(root_child0_child0, _intrinsic_size_measure)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 10

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 1140
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 1140
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 10

    assert YGNodeLayoutGetLeft(root_child0) == -940
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 1140
    assert YGNodeLayoutGetHeight(root_child0) == 10

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 1140
    assert YGNodeLayoutGetHeight(root_child0_child0) == 10

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_text_stretch_max_width():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMaxWidthStretch(root_child0)
    YGNodeStyleSetWidth(root_child0, 300)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)
    YGNodeSetContext(root_child0_child0, "Lorem ipsum dolor sit amet")
    YGNodeSetMeasureFunc(root_child0_child0, _intrinsic_size_measure)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 20

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 20

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0) == 20

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 200
    assert YGNodeLayoutGetHeight(root_child0_child0) == 20

    YGNodeFreeRecursive(root)

    YGConfigFree(config)

def test_text_fit_content_max_width():
    pytest.skip("Upstream GTEST_SKIP()")

    config = YGConfigNew()

    root = YGNodeNewWithConfig(config)
    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 200)

    root_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetMaxWidthFitContent(root_child0)
    YGNodeStyleSetWidth(root_child0, 1000)
    YGNodeInsertChild(root, root_child0, 0)

    root_child0_child0 = YGNodeNewWithConfig(config)
    YGNodeStyleSetFlexDirection(root_child0_child0, YGFlexDirection.YGFlexDirectionRow)
    YGNodeInsertChild(root_child0, root_child0_child0, 0)
    YGNodeSetContext(root_child0_child0, "Lorem ipsum sdafhasdfkjlasdhlkajsfhasldkfhasdlkahsdflkjasdhflaksdfasdlkjhasdlfjahsdfljkasdhalsdfhas dolor sit amet")
    YGNodeSetMeasureFunc(root_child0_child0, _intrinsic_size_measure)
    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionLTR)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 30

    assert YGNodeLayoutGetLeft(root_child0) == 0
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 870
    assert YGNodeLayoutGetHeight(root_child0) == 30

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 870
    assert YGNodeLayoutGetHeight(root_child0_child0) == 30

    YGNodeCalculateLayout(root, float("nan"), float("nan"), YGDirection.YGDirectionRTL)

    assert YGNodeLayoutGetLeft(root) == 0
    assert YGNodeLayoutGetTop(root) == 0
    assert YGNodeLayoutGetWidth(root) == 200
    assert YGNodeLayoutGetHeight(root) == 30

    assert YGNodeLayoutGetLeft(root_child0) == -670
    assert YGNodeLayoutGetTop(root_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0) == 870
    assert YGNodeLayoutGetHeight(root_child0) == 30

    assert YGNodeLayoutGetLeft(root_child0_child0) == 0
    assert YGNodeLayoutGetTop(root_child0_child0) == 0
    assert YGNodeLayoutGetWidth(root_child0_child0) == 870
    assert YGNodeLayoutGetHeight(root_child0_child0) == 30

    YGNodeFreeRecursive(root)

    YGConfigFree(config)
