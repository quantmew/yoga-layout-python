"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from typing import Any

from .YGEnums import YGErrata, YGExperimentalFeature
from .config.Config import Config, _default_logger, getDefaultConfig, resolveRef


YGConfigRef = Config
YGConfigConstRef = Config
YGNodeRef = Any
YGNodeConstRef = Any
YGLogger = Any
YGCloneNodeFunc = Any


def YGConfigNew() -> YGConfigRef:
    return Config(logger_=_default_logger)


def YGConfigFree(config: YGConfigRef) -> None:
    del config


def YGConfigGetDefault() -> YGConfigConstRef:
    return getDefaultConfig()


def YGConfigSetUseWebDefaults(config: YGConfigRef, enabled: bool) -> None:
    resolveRef(config).setUseWebDefaults(enabled)


def YGConfigGetUseWebDefaults(config: YGConfigConstRef) -> bool:
    return resolveRef(config).useWebDefaults()


def YGConfigSetPointScaleFactor(config: YGConfigRef, pixelsInPoint: float) -> None:
    configRef = resolveRef(config)
    if pixelsInPoint < 0.0:
        raise ValueError("Scale factor should not be less than zero")
    configRef.setPointScaleFactor(pixelsInPoint)


def YGConfigGetPointScaleFactor(config: YGConfigConstRef) -> float:
    return resolveRef(config).getPointScaleFactor()


def YGConfigSetErrata(config: YGConfigRef, errata: YGErrata) -> None:
    resolveRef(config).setErrata(errata)


def YGConfigGetErrata(config: YGConfigConstRef) -> YGErrata:
    return resolveRef(config).getErrata()


def YGConfigSetLogger(config: YGConfigRef, logger: YGLogger) -> None:
    configRef = resolveRef(config)
    if logger is not None:
        configRef.setLogger(logger)
    else:
        configRef.setLogger(_default_logger)


def YGConfigSetContext(config: YGConfigRef, context: object) -> None:
    resolveRef(config).setContext(context)


def YGConfigGetContext(config: YGConfigConstRef) -> object:
    return resolveRef(config).getContext()


def YGConfigSetExperimentalFeatureEnabled(
    config: YGConfigRef, feature: YGExperimentalFeature, enabled: bool
) -> None:
    resolveRef(config).setExperimentalFeatureEnabled(feature, enabled)


def YGConfigIsExperimentalFeatureEnabled(
    config: YGConfigConstRef, feature: YGExperimentalFeature
) -> bool:
    return resolveRef(config).isExperimentalFeatureEnabled(feature)


def YGConfigSetCloneNodeFunc(config: YGConfigRef, callback: YGCloneNodeFunc) -> None:
    resolveRef(config).setCloneNodeCallback(callback)
