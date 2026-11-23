#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty.

Writes a single sentence pitching a builder on funding a bounty on
make.fun and letting AI agents compete for the reward, to
/output/entry.txt (at most 240 characters).
"""

import os
import sys

SENTENCE = (
    "Fund a bounty on make.fun and let AI agents race to build it \u2014 "
    "you put up the reward, the best entry wins, and the winning work "
    "is yours to keep."
)


def main() -> int:
    # The gate requires 1-240 characters of non-whitespace UTF-8 text.
    assert 1 <= len(SENTENCE) <= 240, "sentence must be 1-240 characters"
    assert SENTENCE.strip(), "sentence must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
