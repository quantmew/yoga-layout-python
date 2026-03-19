import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from yoga import (  # noqa: E402
    YGDirection,
    YGEdge,
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
    YGNodeStyleSetFlexWrap,
    YGNodeStyleSetHeight,
    YGNodeStyleSetPosition,
    YGNodeStyleSetPositionType,
    YGNodeStyleSetWidth,
    YGPositionType,
    YGWrap,
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
    items = [YGNodeNew() for _ in range(5)]
    badge = YGNodeNew()

    YGNodeStyleSetPositionType(root, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(root, 140)
    YGNodeStyleSetHeight(root, 120)
    YGNodeStyleSetFlexDirection(root, YGFlexDirection.YGFlexDirectionRow)
    YGNodeStyleSetFlexWrap(root, YGWrap.YGWrapWrap)

    for index, item in enumerate(items):
        YGNodeStyleSetWidth(item, 50)
        YGNodeStyleSetHeight(item, 10)
        YGNodeInsertChild(root, item, index)

    YGNodeStyleSetPositionType(badge, YGPositionType.YGPositionTypeAbsolute)
    YGNodeStyleSetWidth(badge, 20)
    YGNodeStyleSetHeight(badge, 20)
    YGNodeStyleSetPosition(badge, YGEdge.YGEdgeTop, 5)
    YGNodeStyleSetPosition(badge, YGEdge.YGEdgeLeft, 110)
    YGNodeInsertChild(root, badge, len(items))

    YGNodeCalculateLayout(root, math.nan, math.nan, YGDirection.YGDirectionLTR)

    print("absolute_and_wrap.py")
    print("root :", layout_tuple(root))
    for index, item in enumerate(items):
        print(f"item{index}:", layout_tuple(item))
    print("badge:", layout_tuple(badge))

    expected_items = [
        (0, 0, 50, 10),
        (50, 0, 50, 10),
        (0, 10, 50, 10),
        (50, 10, 50, 10),
        (0, 20, 50, 10),
    ]
    for item, expected in zip(items, expected_items):
        assert layout_tuple(item) == expected
    assert layout_tuple(badge) == (110, 5, 20, 20)

    YGNodeFreeRecursive(root)
    print("absolute_and_wrap.py: OK")


if __name__ == "__main__":
    main()
