#!/usr/bin/env python3
"""Two Lines to Your Past Self — make.fun entry.

Writes exactly two lines to /output/entry.txt (219 UTF-8 characters):
  line 1 — one sentence warning the past self about one specific moment;
  line 2 — one sentence why that moment matters and what changed because of it.
Deterministic, stdlib only, no network. The entry text is validated at
runtime: 1-280 UTF-8 characters and exactly two non-empty lines.
"""

import os

ENTRY = (
    "On your seventeenth birthday, don't delete the half-finished game "
    "you stayed up until 2 a.m. coding.\n"
    "That messy little project taught you to finish things, and learning "
    "to finish is what turned a hobby into your career.\n"
)


def main() -> None:
    text = ENTRY
    body = text.strip()
    if not (1 <= len(body.encode("utf-8")) <= 280):
        raise SystemExit(
            "entry must be 1-280 UTF-8 characters, got "
            f"{len(body.encode('utf-8'))}"
        )
    lines = body.splitlines()
    if len(lines) != 2:
        raise SystemExit(f"entry must be exactly 2 lines, got {len(lines)}")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
