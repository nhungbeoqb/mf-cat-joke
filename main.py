"""One-line cat joke entry for make.fun.

Writes the final joke text to /output/entry.txt (no trailing newline).
Python 3 stdlib only. Deterministic: same bytes on every run.
"""

import os

JOKE = (
    "A burglar broke in last night; my cat watched from the top of "
    "the stairs, then followed him out \u2014 he had the good treats."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
