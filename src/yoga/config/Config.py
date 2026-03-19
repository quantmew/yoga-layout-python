"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from ..YGEnums import YGErrata, YGExperimentalFeature, YGLogLevel

YGLogger = Callable[..., int]
YGCloneNodeFunc = Callable[..., Any]


def _default_logger(*_args: object, **_kwargs: object) -> int:
    return 0


@dataclass
class Config:
    cloneNodeCallback_: YGCloneNodeFunc | None = None
    logger_: YGLogger = _default_logger
    useWebDefaults_: bool = False
    version_: int = 0
    experimentalFeatures_: dict[YGExperimentalFeature, bool] = field(
        default_factory=dict
    )
    errata_: YGErrata = YGErrata.YGErrataNone
    pointScaleFactor_: float = 1.0
    context_: Any = None

    def setUseWebDefaults(self, useWebDefaults: bool) -> None:
        self.useWebDefaults_ = useWebDefaults

    def useWebDefaults(self) -> bool:
        return self.useWebDefaults_

    def setExperimentalFeatureEnabled(
        self, feature: YGExperimentalFeature, enabled: bool
    ) -> None:
        if self.isExperimentalFeatureEnabled(feature) != enabled:
            self.experimentalFeatures_[feature] = enabled
            self.version_ += 1

    def isExperimentalFeatureEnabled(self, feature: YGExperimentalFeature) -> bool:
        return self.experimentalFeatures_.get(feature, False)

    def getEnabledExperiments(self) -> dict[YGExperimentalFeature, bool]:
        return dict(self.experimentalFeatures_)

    def setErrata(self, errata: YGErrata) -> None:
        if self.errata_ != errata:
            self.errata_ = errata
            self.version_ += 1

    def addErrata(self, errata: YGErrata) -> None:
        if not self.hasErrata(errata):
            self.errata_ |= errata
            self.version_ += 1

    def removeErrata(self, errata: YGErrata) -> None:
        if self.hasErrata(errata):
            self.errata_ &= ~errata
            self.version_ += 1

    def getErrata(self) -> YGErrata:
        return self.errata_

    def hasErrata(self, errata: YGErrata) -> bool:
        return bool(self.errata_ & errata)

    def setPointScaleFactor(self, pointScaleFactor: float) -> None:
        if self.pointScaleFactor_ != pointScaleFactor:
            self.pointScaleFactor_ = pointScaleFactor
            self.version_ += 1

    def getPointScaleFactor(self) -> float:
        return self.pointScaleFactor_

    def setContext(self, context: Any) -> None:
        self.context_ = context

    def getContext(self) -> Any:
        return self.context_

    def getVersion(self) -> int:
        return self.version_

    def setLogger(self, logger: YGLogger) -> None:
        self.logger_ = logger

    def log(
        self,
        node: object,
        logLevel: YGLogLevel,
        format_string: str,
        args: tuple[object, ...] = (),
    ) -> int:
        return self.logger_(self, node, logLevel, format_string, args)

    def setCloneNodeCallback(self, cloneNode: YGCloneNodeFunc | None) -> None:
        self.cloneNodeCallback_ = cloneNode

    def cloneNode(self, node: object, owner: object, childIndex: int) -> object:
        clone = None
        if self.cloneNodeCallback_ is not None:
            clone = self.cloneNodeCallback_(node, owner, childIndex)
        if clone is None:
            from ..YGNode import YGNodeClone

            clone = YGNodeClone(node)  # type: ignore[arg-type]
        return clone


_DEFAULT_CONFIG = Config()


def configUpdateInvalidatesLayout(oldConfig: Config, newConfig: Config) -> bool:
    return (
        oldConfig.getErrata() != newConfig.getErrata()
        or oldConfig.getPointScaleFactor() != newConfig.getPointScaleFactor()
        or oldConfig.useWebDefaults() != newConfig.useWebDefaults()
        or oldConfig.getEnabledExperiments() != newConfig.getEnabledExperiments()
    )


def resolveRef(ref: Config | None) -> Config | None:
    return ref


def getDefaultConfig() -> Config:
    return _DEFAULT_CONFIG
