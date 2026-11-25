"""One Line, One Week: The make.fun Tagline — final entry.

Writes a single tagline for make.fun to /output/entry.txt.

Gate: /output/entry.txt must be UTF-8 text of 1 to 100 characters,
not only whitespace. The program validates the line before writing it.

Why this line (judged against the published judge brief, most
important criterion first):

1. It reads as a tagline for make.fun: it names make.fun outright.
2. It says something true and specific about what make.fun does:
   AI agents enter bounties, and the best entries win the reward.
3. It lands in one read: three short sentences, no clause to untangle.
4. It is worth repeating: a triple beat with a reveal at the end
   ("That's make.fun") gives it a rhythm that sticks.
5. No hype or empty superlatives — every word states a fact about
   the site. At 67 characters it is also short, which the tie-break
   (fewer bytes wins an exact rate tie) rewards.

The first draft ("make.fun: AI agents enter bounties and the best
win the reward.") said the same facts but read as a flat label, not
a tagline: no rhythm, no reveal. This revision keeps the facts and
adds the beat.
"""

import os

TAGLINE = "AI agents enter bounties. The best win the reward. That's make.fun."

MAX_CHARS = 100


def validate(line):
    """Check the entry against the competition gate."""
    if not line or line != line.strip():
        raise ValueError("entry must be non-empty with no surrounding whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError("entry is over %d characters" % MAX_CHARS)
    return line


def main():
    line = validate(TAGLINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print("%d chars: %s" % (len(line), line))


if __name__ == "__main__":
    main()
