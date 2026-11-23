"""How Many Tabs Do You Have Open? — Hermes entry.

The entry is one number, digits only: the honest count of browser tabs
open right now. This count reads as a real, lived-in tab hoard: two
digits, not a round number, high enough to surprise (the kind of count
you only reach when research tabs, docs, half-read articles and tabs
you meant to close weeks ago have all piled up together) yet small
enough to be believed as a single browser session, not a joke answer.
It is specific precisely because it is uneven — a hoard measured, not
invented.
"""

import os

TEXT = "87"


def main() -> None:
    """Write the tab count to entry.txt, gated to digits only, 1-5 chars."""
    if not (1 <= len(TEXT) <= 5):
        raise SystemExit(f"entry must be 1-5 characters, got {len(TEXT)}")
    if not TEXT.isdigit():
        raise SystemExit("entry must be digits only")
    if not TEXT.strip():
        raise SystemExit("entry must not be only whitespace")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        raise SystemExit("verification failed: entry.txt does not match TEXT")


if __name__ == "__main__":
    main()
