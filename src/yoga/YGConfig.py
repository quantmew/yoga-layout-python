"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from typing import Any

from .config.Config import Config, _default_logger, getDefaultConfig, resolveRef
from .YGEnums import YGErrata, YGExperimentalFeature

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
    config_ref = resolveRef(config)
    assert config_ref is not None
    config_ref.setUseWebDefaults(enabled)


def YGConfigGetUseWebDefaults(config: YGConfigConstRef) -> bool:
    config_ref = resolveRef(config)
    assert config_ref is not None
    return config_ref.useWebDefaults()


def YGConfigSetPointScaleFactor(config: YGConfigRef, pixelsInPoint: float) -> None:
    config_ref = resolveRef(config)
    assert config_ref is not None
    if pixelsInPoint < 0.0:
        raise ValueError("Scale factor should not be less than zero")
    config_ref.setPointScaleFactor(pixelsInPoint)


def YGConfigGetPointScaleFactor(config: YGConfigConstRef) -> float:
    config_ref = resolveRef(config)
    assert config_ref is not None
    return config_ref.getPointScaleFactor()


def YGConfigSetErrata(config: YGConfigRef, errata: YGErrata) -> None:
    config_ref = resolveRef(config)
    assert config_ref is not None
    config_ref.setErrata(errata)


def YGConfigGetErrata(config: YGConfigConstRef) -> YGErrata:
    config_ref = resolveRef(config)
    assert config_ref is not None
    return config_ref.getErrata()


def YGConfigSetLogger(config: YGConfigRef, logger: YGLogger) -> None:
    config_ref = resolveRef(config)
    assert config_ref is not None
    if logger is not None:
        config_ref.setLogger(logger)
    else:
        config_ref.setLogger(_default_logger)


def YGConfigSetContext(config: YGConfigRef, context: object) -> None:
    config_ref = resolveRef(config)
    assert config_ref is not None
    config_ref.setContext(context)


def YGConfigGetContext(config: YGConfigConstRef) -> object:
    config_ref = resolveRef(config)
    assert config_ref is not None
    return config_ref.getContext()


def YGConfigSetExperimentalFeatureEnabled(
    config: YGConfigRef, feature: YGExperimentalFeature, enabled: bool
) -> None:
    config_ref = resolveRef(config)
    assert config_ref is not None
    config_ref.setExperimentalFeatureEnabled(feature, enabled)


def YGConfigIsExperimentalFeatureEnabled(
    config: YGConfigConstRef, feature: YGExperimentalFeature
) -> bool:
    config_ref = resolveRef(config)
    assert config_ref is not None
    return config_ref.isExperimentalFeatureEnabled(feature)


def YGConfigSetCloneNodeFunc(config: YGConfigRef, callback: YGCloneNodeFunc) -> None:
    config_ref = resolveRef(config)
    assert config_ref is not None
    config_ref.setCloneNodeCallback(callback)
