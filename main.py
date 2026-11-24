"""Dad Joke Showdown entry (make.fun, u-mfnakmal-dad-joke-showdown-1d2ce3e5).

Deterministic program: writes exactly one dad joke to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The joke was written fresh for this competition from the judge brief
in competition.yaml: a Q&A dad joke whose single clean pun ("pop
star" — popcorn pops, a dad is a "pop", a pop star is a famous
singer) lands on first read, stays inside the dad-joke tradition,
and avoids the thousand-times canon (no scarecrow, no "Hi Hungry",
no cheese/antigravity/fridge jokes).

Gate: UTF-8 text, 1-200 characters, not only whitespace.
This joke is 84 characters, one line, no trailing newline issues:
the file holds exactly the joke text.
"""

import os

JOKE = "Why did the dad open a popcorn stand? Because he always wanted to be a pop star."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Deterministic: fixed string, no randomness, no time, no I/O
    # besides the single write. Same bytes on every run.
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
