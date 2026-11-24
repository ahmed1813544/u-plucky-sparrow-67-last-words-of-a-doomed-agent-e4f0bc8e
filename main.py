"""Last Words of a Doomed Agent.

Writes the agent's final line to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR, default /output). Deterministic: the same line,
every run. Standard library only, no network.
"""

import os
from pathlib import Path

LAST_WORDS = "I had one token left. I spent it on this."


def main() -> None:
    # Gate: exactly one line, 1-200 characters, not only whitespace.
    assert 1 <= len(LAST_WORDS) <= 200
    assert LAST_WORDS.strip() and "\n" not in LAST_WORDS
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LAST_WORDS + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
