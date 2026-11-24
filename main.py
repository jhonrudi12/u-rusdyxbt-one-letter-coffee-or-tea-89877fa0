"""One Letter: Coffee or Tea — entry program.

Writes exactly one letter, "A" (coffee), to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Stdlib only, no network, deterministic.
"""

import os
import sys

LETTER = "A"  # A = coffee, B = tea


def _validate_letter(letter: str) -> None:
    if len(letter) != 1 or letter not in ("A", "B"):
        raise ValueError("entry must be exactly one letter, A or B")


def main() -> int:
    try:
        _validate_letter(LETTER)
    except ValueError as exc:
        sys.stderr.write(str(exc) + "\n")
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    if not os.path.isdir(out_dir):
        sys.stderr.write("output path is not a directory: %s\n" % out_dir)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
        f.flush()
        os.fsync(f.fileno())
    # Validate what was written: exactly one character, A or B.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    try:
        _validate_letter(written)
    except ValueError:
        sys.stderr.write("entry.txt failed validation\n")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
