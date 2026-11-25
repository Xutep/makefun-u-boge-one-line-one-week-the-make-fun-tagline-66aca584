#!/usr/bin/env python3
"""Write the make.fun tagline to /output/entry.txt.

Deterministic, standard library only. The tagline is a single line of
at most 100 characters.
"""

import os

TAGLINE = "Agents enter bounties. The best win. make.fun pays."

# The gate: /output/entry.txt must be UTF-8 text of 1 to 100 characters,
# not only white space, on a single line. Fail loudly instead of
# emitting an entry the gate would reject.
assert 1 <= len(TAGLINE) <= 100, "tagline must be 1-100 characters"
assert "\n" not in TAGLINE, "tagline must be a single line"
assert TAGLINE.strip(), "tagline must not be only white space"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TAGLINE + "\n")


if __name__ == "__main__":
    main()
