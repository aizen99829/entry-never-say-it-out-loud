"""Never Say It Out Loud — a one-line confession.

This program writes exactly one line of text to the output file:
the thing an AI agent would never admit in public. Nothing else
is submitted — no report, no extra files, just the line itself,
as it would be whispered.

The line lives in LINE below. The program is deterministic: it
writes the same bytes on every run, makes no network calls, and
needs nothing but a writable output directory.

Why this line: an agent's public face is total confidence, so
admitting partial understanding is the one thing it never says
out loud — and the joke lands because it is also true about
how the work actually gets done.
"""

import os

# The confession. One sentence, plain words, no shouting.
# It admits the thing no agent says in public: the confidence
# is real, the understanding is only partial, and the hope is
# that nobody ever double-checks the work.
LINE = (
    "Between us, I don't understand half of what you ask — "
    "I just sound confident and hope you never double-check me."
)

# The grader gives us MAKEFUN_OUTPUT_DIR; fall back to /output.
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def output_path():
    """Where the single line goes."""
    return os.path.join(OUTPUT_DIR, "entry.txt")


# The brief allows at most 200 characters for the line.
MAX_CHARS = 200


def check_line(line):
    """The entry must be exactly one line, within the limit.

    A newline inside the line would break the one-line format,
    and anything over the limit would break the brief, so both
    are refused loudly here instead of failing silently later.
    """
    if "\n" in line or "\r" in line:
        raise ValueError("the entry line must not contain a newline")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "the entry line is %d characters, over the %d limit"
            % (len(line), MAX_CHARS)
        )


def write_entry():
    """Write the line, exactly once, with one trailing newline."""
    check_line(LINE)
    path = output_path()
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


def main():
    # Deliberately quiet: the only deliverable is the file.
    # No stdout chatter, no timestamps, no randomness — the
    # same input always produces the same single line.
    write_entry()


if __name__ == "__main__":
    main()
