#!/usr/bin/env python3

import argparse
import json
from pathlib import Path

import differential_test


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--random-count", type=int, default=200)
    parser.add_argument("--seed", type=int, default=20260317)
    parser.add_argument("--force-rebuild", action="store_true")
    parser.add_argument(
        "--failure-capture",
        type=Path,
        default=Path("build/differential_failure_capture.json"),
    )
    args = parser.parse_args()

    differential_test.ensure_cpp_runner(force_rebuild=args.force_rebuild)
    failure = differential_test.run_differential_suite(
        random_count=args.random_count,
        seed=args.seed,
    )
    if failure is None:
        systematic_count = len(differential_test.systematic_cases())
        total = systematic_count + args.random_count
        print(
            f"run_differential_ci.py: OK "
            f"({systematic_count} systematic, {args.random_count} random, total={total})"
        )
        return

    args.failure_capture.parent.mkdir(parents=True, exist_ok=True)
    args.failure_capture.write_text(
        json.dumps({"name": failure.name, **failure.capture}, indent=2)
    )
    print(f"FAIL: {failure.name}")
    print(failure.diff)
    print(f"capture: {args.failure_capture}")
    raise SystemExit(1)


if __name__ == "__main__":
    main()
