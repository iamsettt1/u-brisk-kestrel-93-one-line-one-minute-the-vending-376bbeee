#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line, spoken by a vending machine to a passing
human, to /output/entry.txt. Deterministic: the same line every run.
Stdlib only, no network.
"""

import os

LINE = "My coils only spin for exact change \u2014 but for you, I'd jam the whole machine."


def main() -> None:
    # Gate self-check: 1-200 chars, not only whitespace.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "line fails the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
