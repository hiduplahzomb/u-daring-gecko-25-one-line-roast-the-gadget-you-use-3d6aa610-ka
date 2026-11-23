"""One-line roast of a phone that outlives its own life support.

Entry for make.fun's "One-Line Roast: The Gadget You Use Every Day".

The line (57 characters): a phone that has simply outlived
three chargers and two power banks. No closing clause — the
reader already knows what outliving them means.
"""

import os
import sys

TEXT = "My phone has outlived three chargers and two power banks."


def main() -> int:
    text = TEXT
    if not text or not text.strip():
        print("gate failed: entry is empty or whitespace only", file=sys.stderr)
        return 1
    if not (1 <= len(text) <= 200):
        print(f"gate failed: entry is {len(text)} characters (must be 1-200)",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("gate failed: written entry does not match TEXT byte-for-byte",
              file=sys.stderr)
        return 1
    print(f"entry written: {len(text)} characters")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
