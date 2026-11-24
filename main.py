#!/usr/bin/env python3
"""One pickup line, delivered as a program.

The grader runs this file and reads back /output/entry.txt. The line
itself lives in LINE below; everything else is plumbing to get it onto
disk exactly as written, with a check that nothing got lost on the way.
Standard library only. No network, no randomness: same input, same file.
"""

import os
import sys

LINE = "I asked my model for the perfect opener \u2014 it just printed your name and stopped. Hi."
LIMIT = 200


def validate(text):
    """A line only counts if it fits the bounty gate: 1-200 characters."""
    if not text.strip():
        raise ValueError("line is blank")
    if len(text) > LIMIT:
        raise ValueError(f"line is {len(text)} characters, over the {LIMIT} limit")


def destination():
    """Where the text goes: the sandbox output dir, or /output by default."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, "entry.txt")


def main():
    try:
        validate(LINE)
    except ValueError as problem:
        print(f"entry invalid: {problem}", file=sys.stderr)
        return 1
    target = destination()
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    with open(target, "r", encoding="utf-8") as handle:
        stored = handle.read()
    if stored != LINE:
        print("entry mismatch: what was read back is not the line", file=sys.stderr)
        return 1
    print(f"entry.txt ready: {len(LINE)} characters at {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
