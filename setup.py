from __future__ import annotations

import ast
import os
import shlex
import sys
from pathlib import Path

from setuptools import Extension, setup

ROOT = Path(__file__).parent.resolve()
SRC_ROOT = ROOT / "src"
PACKAGE_ROOT = SRC_ROOT / "yoga"
STAGING_ROOT = ROOT / "build" / "cython_src"


def _is_truthy(value: str | None) -> bool:
    if value is None:
        return False
    return value.strip().lower() in {"1", "true", "yes", "on"}


def _split_csv(value: str | None) -> list[str]:
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def _split_flags(value: str | None) -> list[str]:
    return shlex.split(value) if value else []


def _compiler_directives() -> dict[str, object]:
    return {
        "language_level": "3",
        "boundscheck": _is_truthy(os.getenv("YOGA_CYTHON_BOUNDSCHECK", "0")),
        "wraparound": _is_truthy(os.getenv("YOGA_CYTHON_WRAPAROUND", "0")),
        "initializedcheck": _is_truthy(os.getenv("YOGA_CYTHON_INITIALIZEDCHECK", "0")),
        "nonecheck": _is_truthy(os.getenv("YOGA_CYTHON_NONECHECK", "0")),
        "overflowcheck": _is_truthy(os.getenv("YOGA_CYTHON_OVERFLOWCHECK", "0")),
        "embedsignature": True,
        "cdivision": _is_truthy(os.getenv("YOGA_CYTHON_CDIVISION", "1")),
        "infer_types": _is_truthy(os.getenv("YOGA_CYTHON_INFER_TYPES", "1")),
        "profile": _is_truthy(os.getenv("YOGA_CYTHON_PROFILE", "0")),
        "linetrace": _is_truthy(os.getenv("YOGA_CYTHON_LINETRACE", "0")),
    }


def _iter_module_sources() -> list[Path]:
    include_patterns = _split_csv(os.getenv("YOGA_CYTHON_MODULES")) or [
        "yoga/algorithm/AbsoluteLayout.py",
        "yoga/algorithm/Align.py",
        "yoga/algorithm/Baseline.py",
        "yoga/algorithm/BoundAxis.py",
        "yoga/algorithm/Cache.py",
        "yoga/algorithm/CalculateLayout.py",
        "yoga/algorithm/FlexDirection.py",
        "yoga/algorithm/FlexLine.py",
        "yoga/algorithm/PixelGrid.py",
        "yoga/algorithm/SizingMode.py",
        "yoga/algorithm/TrailingPosition.py",
        "yoga/event/event.py",
        "yoga/numeric/Comparison.py",
        "yoga/numeric/FloatMath.py",
        "yoga/numeric/FloatOptional.py",
    ]
    exclude_patterns = set(
        _split_csv(os.getenv("YOGA_CYTHON_EXCLUDE"))
        or [
            "yoga/__init__.py",
            "yoga/**/__init__.py",
        ]
    )
    selected: list[Path] = []
    seen: set[Path] = set()

    for pattern in include_patterns:
        for path in SRC_ROOT.glob(pattern):
            if not path.is_file():
                continue
            relative = path.relative_to(SRC_ROOT)
            if any(relative.match(exclude) for exclude in exclude_patterns):
                continue
            if path in seen:
                continue
            seen.add(path)
            selected.append(path)

    return sorted(selected)


def _module_name(source_path: Path) -> str:
    return ".".join(source_path.relative_to(SRC_ROOT).with_suffix("").parts)


def _prepare_staging_source(source_path: Path) -> Path:
    relative_path = source_path.relative_to(SRC_ROOT)
    staged_path = STAGING_ROOT / relative_path
    staged_path.parent.mkdir(parents=True, exist_ok=True)

    contents = source_path.read_text(encoding="utf-8")
    module = ast.parse(contents)

    class AnnotationStringifier(ast.NodeTransformer):
        def _stringify(self, node: ast.AST | None) -> ast.AST | None:
            if node is None:
                return None
            return ast.Constant(ast.unparse(node))

        def visit_ImportFrom(self, node: ast.ImportFrom) -> ast.AST | None:
            if node.module == "__future__":
                names = [alias for alias in node.names if alias.name != "annotations"]
                if not names:
                    return None
                node.names = names
            return node

        def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.AST:
            self.generic_visit(node)
            node.returns = self._stringify(node.returns)
            for arg in (
                node.args.posonlyargs
                + node.args.args
                + node.args.kwonlyargs
            ):
                arg.annotation = self._stringify(arg.annotation)
            if node.args.vararg is not None:
                node.args.vararg.annotation = self._stringify(node.args.vararg.annotation)
            if node.args.kwarg is not None:
                node.args.kwarg.annotation = self._stringify(node.args.kwarg.annotation)
            return node

        def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> ast.AST:
            self.generic_visit(node)
            node.returns = self._stringify(node.returns)
            for arg in (
                node.args.posonlyargs
                + node.args.args
                + node.args.kwonlyargs
            ):
                arg.annotation = self._stringify(arg.annotation)
            if node.args.vararg is not None:
                node.args.vararg.annotation = self._stringify(node.args.vararg.annotation)
            if node.args.kwarg is not None:
                node.args.kwarg.annotation = self._stringify(node.args.kwarg.annotation)
            return node

        def visit_AnnAssign(self, node: ast.AnnAssign) -> ast.AST:
            self.generic_visit(node)
            node.annotation = self._stringify(node.annotation)
            return node

    module = AnnotationStringifier().visit(module)
    ast.fix_missing_locations(module)
    contents = ast.unparse(module) + "\n"

    staged_path.write_text(contents, encoding="utf-8")
    return staged_path


def _build_extensions() -> list[Extension]:
    if not PACKAGE_ROOT.exists():
        return []

    return [
        Extension(
            _module_name(source_path),
            [str(_prepare_staging_source(source_path))],
            define_macros=[
                ("CYTHON_TRACE", "1"),
                ("CYTHON_TRACE_NOGIL", "1"),
            ]
            if _is_truthy(os.getenv("YOGA_CYTHON_LINETRACE", "0"))
            else [],
            extra_compile_args=_split_flags(os.getenv("YOGA_CYTHON_CFLAGS")),
            extra_link_args=_split_flags(os.getenv("YOGA_CYTHON_LDFLAGS")),
        )
        for source_path in _iter_module_sources()
    ]


def _should_cythonize() -> bool:
    if _is_truthy(os.getenv("YOGA_CYTHON_BUILD", "0")):
        return True
    return "build_ext" in sys.argv


def _cythonize_extensions() -> list[Extension]:
    if not _should_cythonize():
        return []

    extensions = _build_extensions()
    if not extensions:
        return []

    from Cython.Build import cythonize

    nthreads = int(os.getenv("YOGA_CYTHON_NTHREADS", "0") or "0") or None
    annotate = _is_truthy(os.getenv("YOGA_CYTHON_ANNOTATE", "0"))
    build_dir = os.getenv("YOGA_CYTHON_BUILD_DIR", "build/cython")

    return cythonize(
        extensions,
        compiler_directives=_compiler_directives(),
        annotate=annotate,
        nthreads=nthreads,
        build_dir=build_dir,
    )


setup(ext_modules=_cythonize_extensions())
