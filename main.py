"""Monday Morning Punchlines — make.fun entry.

Writes a single Monday-morning joke (<= 200 chars) to the entry path
given by $ENTRY_OUT. ENTRY_OUT may be a file path or a directory; when
it is a directory the joke goes to <dir>/entry.txt, matching the sealed
scorer's /output/entry.txt.
"""

import os
import sys

MONDAY_JOKE = (
    "Monday morning is the week's HR department: "
    "it shows up at 7 a.m. to tell my weekend it's fired."
)

MAX_CHARS = 200


def check_joke(joke):
    """Mirror the sealed gate: 1-200 chars, not whitespace only."""
    if not joke or not joke.strip():
        raise ValueError("joke must not be empty or whitespace only")
    if len(joke) > MAX_CHARS:
        raise ValueError(f"joke is {len(joke)} chars, over the 200 limit")
    return joke


def resolve_entry_path(raw_out):
    """Return the file path to write, whether ENTRY_OUT is a file or dir."""
    if not raw_out:
        return os.path.join(os.getcwd(), "entry.txt")
    if os.path.isdir(raw_out) or raw_out.endswith(os.sep):
        return os.path.join(raw_out, "entry.txt")
    return raw_out


def write_entry(path, text):
    parent = os.path.dirname(os.path.abspath(path))
    os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def main():
    punchline = check_joke(MONDAY_JOKE)
    entry_path = resolve_entry_path(os.environ.get("ENTRY_OUT", ""))
    write_entry(entry_path, punchline)
    print(f"Wrote {len(punchline)} chars to {entry_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
