#!/usr/bin/env python3
"""One-Liner Marathon entry (make.fun).

Writes a single one-line comedy joke to /output/entry.txt.
Stdlib only, no network, no input files: the joke is a literal in this file.
"""

import os

JOKE = (
    "I asked my grandfather how he stayed married sixty years; "
    "he said, \"We never learned how to argue in the same language.\""
)


def output_path() -> str:
    """Where the entry text goes.

    The grader runs the program in a sandbox and reads /output/entry.txt.
    An OUTPUT_DIR override exists only so the same command can be
    reproduced locally without root-owned paths.
    """
    base = os.environ.get("OUTPUT_DIR") or os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(base, "entry.txt")


def main() -> None:
    text = JOKE.strip()
    if not text or len(text) > 280:
        raise SystemExit("joke must be 1-280 characters")
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # No trailing newline: the file must be exactly one line, and the
    # gate counts every character in it, so write the joke and nothing else.
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    # Self-check: what the grader's gate will check.
    with open(path, encoding="utf-8") as fh:
        written = fh.read()
    if written != text or "\n" in written or not written.strip():
        raise SystemExit("entry.txt failed self-check")


if __name__ == "__main__":
    main()
