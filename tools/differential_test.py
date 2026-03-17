import json
import math
import os
import random
import subprocess
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
CPP_RUNNER = ROOT / "build" / "yoga_cpp_runner"
CPP_SOURCE = ROOT / "tools" / "differential_cpp_runner.cpp"
DOCKERFILE = ROOT / "tools" / "Dockerfile.yoga_cpp_runner"
DOCKER_IMAGE = "yoga-cpp-runner:ubuntu20.04-gcc10-compat"

import sys

sys.path.insert(0, str(SRC))

from yoga import *  # noqa: E402,F403


EDGE_FROM_NAME = {
    "left": YGEdge.YGEdgeLeft,
    "top": YGEdge.YGEdgeTop,
    "right": YGEdge.YGEdgeRight,
    "bottom": YGEdge.YGEdgeBottom,
    "start": YGEdge.YGEdgeStart,
    "end": YGEdge.YGEdgeEnd,
    "horizontal": YGEdge.YGEdgeHorizontal,
    "vertical": YGEdge.YGEdgeVertical,
    "all": YGEdge.YGEdgeAll,
}

FLEX_DIRECTION_FROM_NAME = {
    "row": YGFlexDirection.YGFlexDirectionRow,
    "row-reverse": YGFlexDirection.YGFlexDirectionRowReverse,
    "column": YGFlexDirection.YGFlexDirectionColumn,
    "column-reverse": YGFlexDirection.YGFlexDirectionColumnReverse,
}

JUSTIFY_FROM_NAME = {
    "flex-start": YGJustify.YGJustifyFlexStart,
    "center": YGJustify.YGJustifyCenter,
    "flex-end": YGJustify.YGJustifyFlexEnd,
    "space-between": YGJustify.YGJustifySpaceBetween,
    "space-around": YGJustify.YGJustifySpaceAround,
    "space-evenly": YGJustify.YGJustifySpaceEvenly,
}

ALIGN_FROM_NAME = {
    "auto": YGAlign.YGAlignAuto,
    "flex-start": YGAlign.YGAlignFlexStart,
    "center": YGAlign.YGAlignCenter,
    "flex-end": YGAlign.YGAlignFlexEnd,
    "stretch": YGAlign.YGAlignStretch,
    "baseline": YGAlign.YGAlignBaseline,
    "space-between": YGAlign.YGAlignSpaceBetween,
    "space-around": YGAlign.YGAlignSpaceAround,
    "space-evenly": YGAlign.YGAlignSpaceEvenly,
}

WRAP_FROM_NAME = {
    "no-wrap": YGWrap.YGWrapNoWrap,
    "wrap": YGWrap.YGWrapWrap,
    "wrap-reverse": YGWrap.YGWrapWrapReverse,
}

OVERFLOW_FROM_NAME = {
    "visible": YGOverflow.YGOverflowVisible,
    "hidden": YGOverflow.YGOverflowHidden,
    "scroll": YGOverflow.YGOverflowScroll,
}

DISPLAY_FROM_NAME = {
    "flex": YGDisplay.YGDisplayFlex,
    "none": YGDisplay.YGDisplayNone,
}

POSITION_TYPE_FROM_NAME = {
    "static": YGPositionType.YGPositionTypeStatic,
    "relative": YGPositionType.YGPositionTypeRelative,
    "absolute": YGPositionType.YGPositionTypeAbsolute,
}

DIRECTION_FROM_NAME = {
    "ltr": YGDirection.YGDirectionLTR,
    "rtl": YGDirection.YGDirectionRTL,
    "inherit": YGDirection.YGDirectionInherit,
}

ERRATA_FROM_NAME = {
    "none": YGErrata.YGErrataNone,
    "all": YGErrata.YGErrataAll,
    "classic": YGErrata.YGErrataClassic,
}

EXPERIMENTAL_FEATURE_FROM_NAME = {
    "web-flex-basis": YGExperimentalFeature.YGExperimentalFeatureWebFlexBasis,
}

MEASURE_MODE_FROM_NAME = {
    "undefined": YGMeasureMode.YGMeasureModeUndefined,
    "exactly": YGMeasureMode.YGMeasureModeExactly,
    "at-most": YGMeasureMode.YGMeasureModeAtMost,
}

GUTTER_FROM_NAME = {
    "gap": YGGutter.YGGutterAll,
    "column-gap": YGGutter.YGGutterColumn,
    "row-gap": YGGutter.YGGutterRow,
}

MEASURE_CALLBACKS = {}


@dataclass
class DifferentialFailure:
    name: str
    diff: str
    capture: dict


def ensure_docker_image():
    inspect = subprocess.run(
        ["docker", "image", "inspect", DOCKER_IMAGE],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if inspect.returncode == 0:
        return
    subprocess.run(
        [
            "docker",
            "build",
            "-t",
            DOCKER_IMAGE,
            "-f",
            str(DOCKERFILE),
            ".",
        ],
        cwd=ROOT,
        check=True,
    )


def compile_cpp_runner():
    ensure_docker_image()
    CPP_RUNNER.parent.mkdir(parents=True, exist_ok=True)
    compile_cmd = " ".join(
        [
            "mkdir -p /work/build/lib &&",
            "g++-10",
            "-std=c++20",
            "-O2",
            "-static-libstdc++",
            "-static-libgcc",
            "-include",
            "/work/tools/cpp20_compat.h",
            "-I",
            "/work/yoga-layout",
            "-I",
            "/work/yoga-layout/lib",
            "-o",
            "/work/build/yoga_cpp_runner",
            "/work/tools/differential_cpp_runner.cpp",
            "/work/yoga-layout/benchmark/TreeDeserialization.cpp",
            *(
                str(path.relative_to(ROOT)).replace("\\", "/")
                for path in sorted((ROOT / "yoga-layout" / "yoga").rglob("*.cpp"))
            ),
            "&& true",
        ]
    )
    docker_cmd = [
        "docker",
        "run",
        "--rm",
        "--user",
        f"{os.getuid()}:{os.getgid()}",
        "-v",
        f"{ROOT}:/work",
        "-w",
        "/work",
        DOCKER_IMAGE,
        "bash",
        "-lc",
        compile_cmd,
    ]
    subprocess.run(docker_cmd, check=True, cwd=ROOT)


def cpp_runner_dependencies():
    return [
        CPP_SOURCE,
        DOCKERFILE,
        ROOT / "tools" / "cpp20_compat.h",
        ROOT / "yoga-layout" / "benchmark" / "TreeDeserialization.cpp",
        *sorted((ROOT / "yoga-layout" / "yoga").rglob("*.cpp")),
        *sorted((ROOT / "yoga-layout" / "yoga").rglob("*.h")),
    ]


def ensure_cpp_runner(force_rebuild=False):
    newest_dependency_mtime = max(path.stat().st_mtime for path in cpp_runner_dependencies())
    if (
        force_rebuild
        or
        not CPP_RUNNER.exists()
        or CPP_RUNNER.stat().st_mtime < newest_dependency_mtime
    ):
        compile_cpp_runner()


def is_auto(value):
    return isinstance(value, str) and value == "auto"


def is_undefined(value):
    return isinstance(value, str) and value == "undefined"


def apply_config(config, config_json):
    if not config_json:
        return
    if "use-web-defaults" in config_json:
        YGConfigSetUseWebDefaults(config, config_json["use-web-defaults"])
    if "point-scale-factor" in config_json:
        YGConfigSetPointScaleFactor(config, config_json["point-scale-factor"])
    if "errata" in config_json:
        YGConfigSetErrata(config, ERRATA_FROM_NAME[config_json["errata"]])
    for feature in config_json.get("experimental-features", []):
        YGConfigSetExperimentalFeatureEnabled(
            config, EXPERIMENTAL_FEATURE_FROM_NAME[feature], True
        )


def set_length(style_key, node, value, point_setter, percent_setter, auto_setter=None):
    if is_auto(value):
        if auto_setter is None:
            return
        auto_setter(node)
        return
    if is_undefined(value):
        return
    unit = value["unit"]
    if unit == "px":
        point_setter(node, value["value"])
    elif unit == "pct":
        percent_setter(node, value["value"])
    else:
        raise ValueError(f"unsupported unit for {style_key}: {unit}")


def set_edge_length(style_key, node, value, point_setter, percent_setter=None, auto_setter=None):
    edge_name = style_key.split("-", 1)[1]
    edge = EDGE_FROM_NAME[edge_name]
    if is_auto(value):
        if auto_setter is None:
            return
        auto_setter(node, edge)
        return
    if is_undefined(value):
        return
    unit = value["unit"]
    if unit == "px":
        point_setter(node, edge, value["value"])
    elif unit == "pct" and percent_setter is not None:
        percent_setter(node, edge, value["value"])
    else:
        raise ValueError(f"unsupported unit for {style_key}: {unit}")


def make_measure_callback(serialized_measure_funcs):
    key = json.dumps(serialized_measure_funcs, sort_keys=True)
    if key in MEASURE_CALLBACKS:
        return MEASURE_CALLBACKS[key]

    def callback(node, width, width_mode, height, height_mode):
        for item in serialized_measure_funcs:
            expected_width = item["width"]
            expected_height = item["height"]
            width_matches = (
                (expected_width is None and math.isnan(width))
                or (expected_width is not None and width == expected_width)
            )
            height_matches = (
                (expected_height is None and math.isnan(height))
                or (expected_height is not None and height == expected_height)
            )
            if (
                width_matches
                and height_matches
                and width_mode == MEASURE_MODE_FROM_NAME[item["width-mode"]]
                and height_mode == MEASURE_MODE_FROM_NAME[item["height-mode"]]
            ):
                return YGSize(item["output-width"], item["output-height"])
        return YGSize(10.0, 10.0)

    MEASURE_CALLBACKS[key] = callback
    return callback


def apply_style(node, style_json):
    for key, value in style_json.items():
        if key == "flex-direction":
            YGNodeStyleSetFlexDirection(node, FLEX_DIRECTION_FROM_NAME[value])
        elif key == "justify-content":
            YGNodeStyleSetJustifyContent(node, JUSTIFY_FROM_NAME[value])
        elif key == "align-items":
            YGNodeStyleSetAlignItems(node, ALIGN_FROM_NAME[value])
        elif key == "align-content":
            YGNodeStyleSetAlignContent(node, ALIGN_FROM_NAME[value])
        elif key == "align-self":
            YGNodeStyleSetAlignSelf(node, ALIGN_FROM_NAME[value])
        elif key == "flex-wrap":
            YGNodeStyleSetFlexWrap(node, WRAP_FROM_NAME[value])
        elif key == "overflow":
            YGNodeStyleSetOverflow(node, OVERFLOW_FROM_NAME[value])
        elif key == "display":
            YGNodeStyleSetDisplay(node, DISPLAY_FROM_NAME[value])
        elif key == "position-type":
            YGNodeStyleSetPositionType(node, POSITION_TYPE_FROM_NAME[value])
        elif key == "direction":
            YGNodeStyleSetDirection(node, DIRECTION_FROM_NAME[value])
        elif key == "flex-grow":
            YGNodeStyleSetFlexGrow(node, value)
        elif key == "flex-shrink":
            YGNodeStyleSetFlexShrink(node, value)
        elif key == "flex":
            YGNodeStyleSetFlex(node, value)
        elif key == "flex-basis":
            set_length(
                key,
                node,
                value,
                YGNodeStyleSetFlexBasis,
                YGNodeStyleSetFlexBasisPercent,
                YGNodeStyleSetFlexBasisAuto,
            )
        elif key.startswith("position-"):
            set_edge_length(
                key,
                node,
                value,
                YGNodeStyleSetPosition,
                YGNodeStyleSetPositionPercent,
                YGNodeStyleSetPositionAuto,
            )
        elif key.startswith("padding-"):
            set_edge_length(
                key,
                node,
                value,
                YGNodeStyleSetPadding,
                YGNodeStyleSetPaddingPercent,
            )
        elif key.startswith("border-"):
            set_edge_length(key, node, value, YGNodeStyleSetBorder)
        elif key.startswith("margin-"):
            set_edge_length(
                key,
                node,
                value,
                YGNodeStyleSetMargin,
                YGNodeStyleSetMarginPercent,
                YGNodeStyleSetMarginAuto,
            )
        elif key in GUTTER_FROM_NAME:
            if value["unit"] == "px":
                YGNodeStyleSetGap(node, GUTTER_FROM_NAME[key], value["value"])
            elif value["unit"] == "pct":
                YGNodeStyleSetGapPercent(node, GUTTER_FROM_NAME[key], value["value"])
        elif key == "height":
            set_length(
                key,
                node,
                value,
                YGNodeStyleSetHeight,
                YGNodeStyleSetHeightPercent,
                YGNodeStyleSetHeightAuto,
            )
        elif key == "width":
            set_length(
                key,
                node,
                value,
                YGNodeStyleSetWidth,
                YGNodeStyleSetWidthPercent,
                YGNodeStyleSetWidthAuto,
            )
        elif key == "min-height":
            set_length(
                key,
                node,
                value,
                YGNodeStyleSetMinHeight,
                YGNodeStyleSetMinHeightPercent,
            )
        elif key == "min-width":
            set_length(
                key,
                node,
                value,
                YGNodeStyleSetMinWidth,
                YGNodeStyleSetMinWidthPercent,
            )
        elif key == "max-height":
            set_length(
                key,
                node,
                value,
                YGNodeStyleSetMaxHeight,
                YGNodeStyleSetMaxHeightPercent,
            )
        elif key == "max-width":
            set_length(
                key,
                node,
                value,
                YGNodeStyleSetMaxWidth,
                YGNodeStyleSetMaxWidthPercent,
            )
        else:
            raise ValueError(f"unsupported style key: {key}")


def build_python_tree(tree_json, configs):
    config = YGConfigNew()
    apply_config(config, tree_json.get("config", {}))
    configs.append(config)
    node = YGNodeNewWithConfig(config)

    node_json = tree_json.get("node")
    if node_json and node_json.get("measure-funcs") is not None:
        callback = make_measure_callback(node_json["measure-funcs"])
        YGNodeSetMeasureFunc(node, callback)

    apply_style(node, tree_json.get("style", {}))

    for index, child_json in enumerate(tree_json.get("children", [])):
        child = build_python_tree(child_json, configs)
        YGNodeInsertChild(node, child, index)

    return node


def float_or_none(value):
    return None if value is None or (isinstance(value, float) and math.isnan(value)) else value


def dump_python_layout(node):
    result = {
        "left": float_or_none(YGNodeLayoutGetLeft(node)),
        "top": float_or_none(YGNodeLayoutGetTop(node)),
        "width": float_or_none(YGNodeLayoutGetWidth(node)),
        "height": float_or_none(YGNodeLayoutGetHeight(node)),
        "direction": YGNodeLayoutGetDirection(node).name.replace("YGDirection", "").lower(),
        "had-overflow": YGNodeLayoutGetHadOverflow(node),
        "margin": {
            "left": float_or_none(YGNodeLayoutGetMargin(node, YGEdge.YGEdgeLeft)),
            "top": float_or_none(YGNodeLayoutGetMargin(node, YGEdge.YGEdgeTop)),
            "right": float_or_none(YGNodeLayoutGetMargin(node, YGEdge.YGEdgeRight)),
            "bottom": float_or_none(YGNodeLayoutGetMargin(node, YGEdge.YGEdgeBottom)),
        },
        "padding": {
            "left": float_or_none(YGNodeLayoutGetPadding(node, YGEdge.YGEdgeLeft)),
            "top": float_or_none(YGNodeLayoutGetPadding(node, YGEdge.YGEdgeTop)),
            "right": float_or_none(YGNodeLayoutGetPadding(node, YGEdge.YGEdgeRight)),
            "bottom": float_or_none(YGNodeLayoutGetPadding(node, YGEdge.YGEdgeBottom)),
        },
        "border": {
            "left": float_or_none(YGNodeLayoutGetBorder(node, YGEdge.YGEdgeLeft)),
            "top": float_or_none(YGNodeLayoutGetBorder(node, YGEdge.YGEdgeTop)),
            "right": float_or_none(YGNodeLayoutGetBorder(node, YGEdge.YGEdgeRight)),
            "bottom": float_or_none(YGNodeLayoutGetBorder(node, YGEdge.YGEdgeBottom)),
        },
        "children": [],
    }
    for index in range(YGNodeGetChildCount(node)):
        result["children"].append(dump_python_layout(YGNodeGetChild(node, index)))
    return result


def run_python_capture(capture):
    configs = []
    root = build_python_tree(capture["tree"], configs)
    layout_inputs = capture["layout-inputs"]
    owner_width = math.nan if layout_inputs["available-width"] is None else layout_inputs["available-width"]
    owner_height = math.nan if layout_inputs["available-height"] is None else layout_inputs["available-height"]
    owner_direction = DIRECTION_FROM_NAME[layout_inputs["owner-direction"]]
    try:
        YGNodeCalculateLayout(root, owner_width, owner_height, owner_direction)
        return dump_python_layout(root)
    finally:
        YGNodeFreeRecursive(root)
        for config in configs:
            YGConfigFree(config)


def run_cpp_capture(capture):
    ensure_cpp_runner()
    temp_dir = ROOT / "build" / "differential_tmp"
    temp_dir.mkdir(parents=True, exist_ok=True)
    path = temp_dir / "capture.json"
    path.write_text(json.dumps(capture))
    result = subprocess.run(
        [str(CPP_RUNNER), str(path)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    lines = [line for line in result.stdout.splitlines() if line.strip()]
    if not lines:
        raise ValueError("cpp runner produced no output")
    return json.loads(lines[-1])


def nearly_equal(a, b, tolerance=1e-4):
    if a is None or b is None:
        return a is None and b is None
    return abs(a - b) <= tolerance


def diff_layouts(py_layout, cpp_layout, path="root"):
    for field in ["left", "top", "width", "height"]:
        if not nearly_equal(py_layout[field], cpp_layout[field]):
            return f"{path}.{field}: python={py_layout[field]} cpp={cpp_layout[field]}"
    if py_layout["direction"] != cpp_layout["direction"]:
        return f"{path}.direction: python={py_layout['direction']} cpp={cpp_layout['direction']}"
    if py_layout["had-overflow"] != cpp_layout["had-overflow"]:
        return f"{path}.had-overflow: python={py_layout['had-overflow']} cpp={cpp_layout['had-overflow']}"
    for box in ["margin", "padding", "border"]:
        for edge in ["left", "top", "right", "bottom"]:
            if not nearly_equal(py_layout[box][edge], cpp_layout[box][edge]):
                return (
                    f"{path}.{box}.{edge}: "
                    f"python={py_layout[box][edge]} cpp={cpp_layout[box][edge]}"
                )
    if len(py_layout["children"]) != len(cpp_layout["children"]):
        return (
            f"{path}.children length: "
            f"python={len(py_layout['children'])} cpp={len(cpp_layout['children'])}"
        )
    for index, (py_child, cpp_child) in enumerate(zip(py_layout["children"], cpp_layout["children"])):
        child_diff = diff_layouts(py_child, cpp_child, f"{path}.children[{index}]")
        if child_diff is not None:
            return child_diff
    return None


def px(value):
    return {"unit": "px", "value": value}


def pct(value):
    return {"unit": "pct", "value": value}


def node(style=None, children=None, config=None, node_state=None):
    return {
        "config": config or {},
        "node": node_state,
        "style": style or {},
        "children": children or [],
    }


def systematic_cases():
    return [
        {
            "name": "flex-row-grow",
            "layout-inputs": {
                "available-width": None,
                "available-height": None,
                "owner-direction": "ltr",
            },
            "tree": node(
                style={"width": px(300), "height": px(100), "flex-direction": "row"},
                children=[
                    node(style={"width": px(50), "height": px(100)}),
                    node(style={"flex-grow": 1.0}),
                ],
            ),
        },
        {
            "name": "wrap-gap-margin",
            "layout-inputs": {
                "available-width": None,
                "available-height": None,
                "owner-direction": "ltr",
            },
            "tree": node(
                style={
                    "width": px(140),
                    "height": px(120),
                    "flex-direction": "row",
                    "flex-wrap": "wrap",
                    "row-gap": px(5),
                },
                children=[
                    node(style={"width": px(50), "height": px(10)}),
                    node(style={"width": px(50), "height": px(10)}),
                    node(style={"width": px(50), "height": px(10), "margin-left": px(5)}),
                    node(style={"width": px(50), "height": px(10)}),
                ],
            ),
        },
        {
            "name": "absolute-inset",
            "layout-inputs": {
                "available-width": None,
                "available-height": None,
                "owner-direction": "ltr",
            },
            "tree": node(
                style={"width": px(200), "height": px(150), "position-type": "absolute"},
                children=[
                    node(
                        style={
                            "position-type": "absolute",
                            "position-left": px(40),
                            "position-top": px(20),
                            "width": px(60),
                            "height": px(30),
                        }
                    )
                ],
            ),
        },
        {
            "name": "percent-rtl",
            "layout-inputs": {
                "available-width": None,
                "available-height": None,
                "owner-direction": "rtl",
            },
            "tree": node(
                style={"width": px(300), "height": px(100), "flex-direction": "row"},
                children=[
                    node(style={"width": pct(50), "height": px(30)}),
                    node(style={"flex-grow": 1.0, "margin-start": px(10)}),
                ],
            ),
        },
        {
            "name": "min-max-flex",
            "layout-inputs": {
                "available-width": None,
                "available-height": None,
                "owner-direction": "ltr",
            },
            "tree": node(
                style={"width": px(200), "height": px(100), "flex-direction": "row"},
                children=[
                    node(style={"flex-grow": 1.0, "min-width": px(80), "max-width": px(120)}),
                    node(style={"flex-grow": 1.0, "min-width": px(10), "max-width": px(50)}),
                ],
            ),
        },
        {
            "name": "measure-replay",
            "layout-inputs": {
                "available-width": None,
                "available-height": None,
                "owner-direction": "ltr",
            },
            "tree": node(
                style={"width": px(200), "height": px(100), "align-items": "flex-start"},
                children=[
                    node(
                        style={"flex-direction": "row"},
                        node_state={
                            "measure-funcs": [
                                {
                                    "width": None,
                                    "width-mode": "undefined",
                                    "height": 100.0,
                                    "height-mode": "at-most",
                                    "output-width": 80.0,
                                    "output-height": 20.0,
                                    "duration-ns": 0,
                                }
                            ]
                        },
                    )
                ],
            ),
        },
    ]


def random_length(rng):
    choice = rng.choice(["px", "pct"])
    if choice == "px":
        return px(float(rng.randint(0, 120)))
    return pct(float(rng.randint(10, 100)))


def random_style(rng, depth):
    style = {}
    if depth == 0 or rng.random() < 0.6:
        style["width"] = px(float(rng.randint(40, 260)))
    elif rng.random() < 0.25:
        style["width"] = pct(float(rng.randint(20, 100)))
    if depth == 0 or rng.random() < 0.6:
        style["height"] = px(float(rng.randint(20, 180)))
    elif rng.random() < 0.25:
        style["height"] = pct(float(rng.randint(20, 100)))
    if rng.random() < 0.35:
        style["flex-direction"] = rng.choice(list(FLEX_DIRECTION_FROM_NAME.keys()))
    if rng.random() < 0.25:
        style["justify-content"] = rng.choice(list(JUSTIFY_FROM_NAME.keys()))
    if rng.random() < 0.25:
        style["align-items"] = rng.choice(
            ["flex-start", "center", "flex-end", "stretch"]
        )
    if rng.random() < 0.2:
        style["align-content"] = rng.choice(
            ["flex-start", "center", "flex-end", "stretch", "space-between", "space-around", "space-evenly"]
        )
    if rng.random() < 0.25:
        style["flex-wrap"] = rng.choice(list(WRAP_FROM_NAME.keys()))
    if rng.random() < 0.3:
        style["flex-grow"] = float(rng.randint(0, 3))
    if rng.random() < 0.3:
        style["flex-shrink"] = float(rng.randint(0, 2))
    if rng.random() < 0.2:
        style["position-type"] = "absolute"
        style["position-left"] = px(float(rng.randint(0, 60)))
        style["position-top"] = px(float(rng.randint(0, 60)))
    if rng.random() < 0.2:
        style["min-width"] = px(float(rng.randint(0, 80)))
    if rng.random() < 0.2:
        style["max-width"] = px(float(rng.randint(30, 120)))
    if rng.random() < 0.2:
        style["min-height"] = px(float(rng.randint(0, 80)))
    if rng.random() < 0.2:
        style["max-height"] = px(float(rng.randint(30, 120)))
    for key in ["margin-left", "margin-top", "padding-left", "padding-top", "border-left", "border-top"]:
        if rng.random() < 0.15:
            style[key] = px(float(rng.randint(0, 20)))
    if rng.random() < 0.1:
        style["row-gap"] = px(float(rng.randint(0, 20)))
    if rng.random() < 0.1:
        style["column-gap"] = px(float(rng.randint(0, 20)))
    return style


def random_tree(rng, depth=0):
    style = random_style(rng, depth)
    child_count = 0 if depth >= 3 else rng.randint(0, 3)
    children = [random_tree(rng, depth + 1) for _ in range(child_count)]
    config = {}
    if depth == 0 and rng.random() < 0.25:
        config["use-web-defaults"] = rng.choice([True, False])
    if depth == 0 and rng.random() < 0.2:
        config["point-scale-factor"] = rng.choice([0.0, 1.0, 2.0, 3.0])
    return node(style=style, children=children, config=config)


def random_cases(count, seed=20260317):
    rng = random.Random(seed)
    cases = []
    for index in range(count):
        cases.append(
            {
                "name": f"random-{index:03d}",
                "layout-inputs": {
                    "available-width": None,
                    "available-height": None,
                    "owner-direction": rng.choice(["ltr", "rtl"]),
                },
                "tree": random_tree(rng),
            }
        )
    return cases


def run_case(case):
    capture = {
        "layout-inputs": case["layout-inputs"],
        "tree": case["tree"],
    }
    py_layout = run_python_capture(capture)
    cpp_layout = run_cpp_capture(capture)
    return diff_layouts(py_layout, cpp_layout)


def run_differential_suite(random_count=200, seed=20260317):
    cases = systematic_cases() + random_cases(random_count, seed=seed)
    for case in cases:
        try:
            diff = run_case(case)
        except Exception:
            capture = {
                "layout-inputs": case["layout-inputs"],
                "tree": case["tree"],
            }
            raise
        if diff is not None:
            capture = {
                "layout-inputs": case["layout-inputs"],
                "tree": case["tree"],
            }
            return DifferentialFailure(case["name"], diff, capture)
    return None


def main():
    random_count = 200
    seed = 20260317
    failure = run_differential_suite(random_count=random_count, seed=seed)
    if failure is not None:
        print(f"FAIL: {failure.name}")
        print(failure.diff)
        print(json.dumps({"name": failure.name, **failure.capture}, indent=2))
        raise SystemExit(1)

    print(
        f"differential_test.py: OK "
        f"({len(systematic_cases())} systematic, {random_count} random, total={len(systematic_cases()) + random_count})"
    )


if __name__ == "__main__":
    main()
