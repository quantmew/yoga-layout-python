#include <fstream>
#include <iostream>
#include <memory>
#include <string>

#include <nlohmann/json.hpp>
#include <yoga/Yoga.h>

#define main yoga_benchmark_main
#include "../yoga-layout/benchmark/Benchmark.cpp"
#undef main

using nlohmann::json;

namespace {

json floatOrNull(float value) {
  if (YGFloatIsUndefined(value)) {
    return nullptr;
  }
  return value;
}

std::string directionToString(YGDirection direction) {
  switch (direction) {
    case YGDirectionLTR:
      return "ltr";
    case YGDirectionRTL:
      return "rtl";
    case YGDirectionInherit:
      return "inherit";
  }
  return "inherit";
}

json dumpLayout(YGNodeRef node) {
  json result;
  result["left"] = floatOrNull(YGNodeLayoutGetLeft(node));
  result["top"] = floatOrNull(YGNodeLayoutGetTop(node));
  result["width"] = floatOrNull(YGNodeLayoutGetWidth(node));
  result["height"] = floatOrNull(YGNodeLayoutGetHeight(node));
  result["direction"] = directionToString(YGNodeLayoutGetDirection(node));
  result["had-overflow"] = YGNodeLayoutGetHadOverflow(node);
  result["margin"] = {
      {"left", floatOrNull(YGNodeLayoutGetMargin(node, YGEdgeLeft))},
      {"top", floatOrNull(YGNodeLayoutGetMargin(node, YGEdgeTop))},
      {"right", floatOrNull(YGNodeLayoutGetMargin(node, YGEdgeRight))},
      {"bottom", floatOrNull(YGNodeLayoutGetMargin(node, YGEdgeBottom))},
  };
  result["padding"] = {
      {"left", floatOrNull(YGNodeLayoutGetPadding(node, YGEdgeLeft))},
      {"top", floatOrNull(YGNodeLayoutGetPadding(node, YGEdgeTop))},
      {"right", floatOrNull(YGNodeLayoutGetPadding(node, YGEdgeRight))},
      {"bottom", floatOrNull(YGNodeLayoutGetPadding(node, YGEdgeBottom))},
  };
  result["border"] = {
      {"left", floatOrNull(YGNodeLayoutGetBorder(node, YGEdgeLeft))},
      {"top", floatOrNull(YGNodeLayoutGetBorder(node, YGEdgeTop))},
      {"right", floatOrNull(YGNodeLayoutGetBorder(node, YGEdgeRight))},
      {"bottom", floatOrNull(YGNodeLayoutGetBorder(node, YGEdgeBottom))},
  };

  json children = json::array();
  const uint32_t childCount = YGNodeGetChildCount(node);
  for (uint32_t i = 0; i < childCount; i++) {
    children.push_back(dumpLayout(YGNodeGetChild(node, i)));
  }
  result["children"] = std::move(children);
  return result;
}

float inputValue(const json& j, const char* key) {
  if (!j.contains(key) || j[key].is_null()) {
    return YGUndefined;
  }
  return j[key];
}

} // namespace

int main(int argc, char** argv) {
  if (argc != 2) {
    std::cerr << "usage: yoga_cpp_runner <capture.json>" << std::endl;
    return 2;
  }

  std::ifstream in(argv[1]);
  if (!in) {
    std::cerr << "failed to open input: " << argv[1] << std::endl;
    return 2;
  }

  json capture = json::parse(in);
  auto fns = std::make_shared<facebook::yoga::SerializedMeasureFuncMap>();
  std::shared_ptr<facebook::yoga::YogaNodeAndConfig> root =
      facebook::yoga::buildTreeFromJson(capture["tree"], fns, nullptr, 0);

  json layoutInputs = capture["layout-inputs"];
  const float availableWidth = inputValue(layoutInputs, "available-width");
  const float availableHeight = inputValue(layoutInputs, "available-height");
  const YGDirection ownerDirection =
      facebook::yoga::directionFromString(layoutInputs["owner-direction"]);

  YGNodeCalculateLayout(
      root->node_.get(), availableWidth, availableHeight, ownerDirection);

  json out = dumpLayout(root->node_.get());
  std::cout << out.dump() << std::endl;
  return 0;
}
