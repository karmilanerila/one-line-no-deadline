"""One-line deadline excuse.

The program writes a single joke line to /output/entry.txt.
The line: the deadline ghosted the narrator first, after seeing
forty-seven tabs of 'how to start' and deciding the narrator
wasn't ready for commitment. One sentence, punch at the end.
"""

import os


SETUP = (
    "I didn't miss the deadline \u2014 it ghosted me first, after seeing "
    "my forty-seven tabs of 'how to start'"
)
PUNCH = "and deciding I wasn't ready for commitment."

LINE = SETUP + " " + PUNCH


def check_line(text):
    """Gate check: 1-200 chars, UTF-8, not whitespace-only."""
    if not 1 <= len(text) <= 200:
        raise SystemExit("entry line fails the 1-200 char gate")
    if not text.strip():
        raise SystemExit("entry line is whitespace-only")
    text.encode("utf-8")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = check_line(LINE)
    with open(path, "wb") as f:
        f.write(text.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
