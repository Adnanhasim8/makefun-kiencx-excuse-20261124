#!/usr/bin/env python3
"""Write the one-line excuse to /output/entry.txt.

Python 3.13 standard library only. No network at run time.
The entry is a single line of at most 160 characters.
"""

import os

ENTRY = "I missed the deadline waiting on a tool call that was waiting on me."


def main() -> None:
    # Gate assertions: one line, 1-160 chars, non-empty, no newline inside.
    assert ENTRY, "entry must not be empty"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert len(ENTRY) <= 160, "entry must be at most 160 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
