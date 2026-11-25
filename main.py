#!/usr/bin/env python3
"""One-Line Laugh-Off — make.fun entry.

Writes a single funny line, 1-200 characters, to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only, deterministic, no network.
"""

import os

LINE = "I wrote a test that only passes on my machine, so now my machine is the production server."


def resolve_output_dir() -> str:
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    line = LINE
    if not line or not line.strip():
        raise ValueError("entry line must not be empty")
    if len(line) > 200:
        raise ValueError("entry line must be at most 200 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    out_dir = resolve_output_dir()
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(line)
        print(f"wrote {len(line)} characters to {path}")
    except OSError:
        pass


if __name__ == "__main__":
    main()
