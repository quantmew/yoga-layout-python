import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import (  # noqa: E402
    YGDirection,
    YGFlexDirection,
    YGNodeCalculateLayout,
    YGNodeFreeRecursive,
    YGNodeInsertChild,
    YGNodeLayoutGetHeight,
    YGNodeLayoutGetLeft,
    YGNodeLayoutGetTop,
    YGNodeLayoutGetWidth,
    YGNodeNew,
    YGNodeStyleSetFlexDirection,
    YGNodeStyleSetFlexGrow,
    YGNodeStyleSetHeight,
    YGNodeStyleSetWidth,
)


def layout_tuple(node):
    return (
        YGNodeLayoutGetLeft(node),
        YGNodeLayoutGetTop(node),
        YGNodeLayoutGetWidth(node),
        YGNodeLayoutGetHeight(node),
    )


def main():
    root = YGNodeNew()
    sidebar = YGNodeNew()
    content = YGNodeNew()

    YGNodeStyleSetWidth(root, 800)
    YGNodeStyleSetHeight(root, 200)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)

    YGNodeStyleSetWidth(sidebar, 240)
    YGNodeStyleSetHeight(sidebar, 200)
    YGNodeInsertChild(root, sidebar, 0)

    YGNodeStyleSetFlexGrow(content, 1)
    YGNodeInsertChild(root, content, 1)

    YGNodeCalculateLayout(root, math.nan, math.nan, YGDirection.YGDirectionLTR)

    print("basic_usage.py")
    print("root   :", layout_tuple(root))
    print("sidebar:", layout_tuple(sidebar))
    print("content:", layout_tuple(content))

    assert layout_tuple(root) == (0, 0, 800, 200)
    assert layout_tuple(sidebar) == (0, 0, 240, 200)
    assert layout_tuple(content) == (240, 0, 560, 200)

    YGNodeFreeRecursive(root)
    print("basic_usage.py: OK")


if __name__ == "__main__":
    main()
