#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — one borrowed CPU core.

Writes a single out-of-office auto-reply line (max 160 chars) in the
voice of an AI agent heading off on vacation to
$MAKEFUN_OUTPUT_DIR/entry.txt (default: out/), then verifies the written
file byte-for-byte: identical bytes, valid UTF-8, 1-160 chars, non-blank,
no leading/trailing whitespace, and exactly one sentence.
"""

import os
import sys

SENTENCE = (
    "I'm on vacation, so this auto-reply is running on a single borrowed "
    "CPU core \u2014 please resend your email slower, in smaller words, "
    "and with snacks."
)

# The em dash above is U+2014. Keep the sentence exactly as written:
# one sentence, no trailing newline in the output file.
# Wording notes (revised once after the kit check): "a single borrowed
# CPU core" for "one borrowed CPU core" — "single" reads tighter and more
# pitiable, which sells the machine-on-holiday voice. The turn lands on
# the last words: the auto-reply itself begs for snacks, which no
# auto-reply should ever do. "slower, in smaller words" keeps the
# vacation-brain joke going without beach/inbox/back-soon cliches.


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    data = SENTENCE.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)

    # --- Verification: read the file back and check it byte-for-byte. ---
    with open(path, "rb") as fh:
        written = fh.read()

    if written != data:
        print("FAIL: entry.txt bytes differ from the sentence", file=sys.stderr)
        return 1

    try:
        text = written.decode("utf-8")
    except UnicodeDecodeError as exc:
        print(f"FAIL: entry.txt is not valid UTF-8: {exc}", file=sys.stderr)
        return 1

    if text != SENTENCE:
        print("FAIL: decoded text differs from the sentence", file=sys.stderr)
        return 1

    if not 1 <= len(text) <= 160:
        print(f"FAIL: length {len(text)} chars is outside 1-160", file=sys.stderr)
        return 1

    if not text.strip():
        print("FAIL: entry is blank", file=sys.stderr)
        return 1

    if text != text.strip():
        print("FAIL: entry has leading or trailing whitespace", file=sys.stderr)
        return 1

    if "\n" in text or "\r" in text:
        print("FAIL: entry must be a single line with no newline characters",
              file=sys.stderr)
        return 1

    if written.endswith(b"\n"):
        print("FAIL: entry.txt must not end with a trailing newline",
              file=sys.stderr)
        return 1

    # Exactly one sentence: count sentence terminators.
    terminators = sum(text.count(mark) for mark in ".!?")
    if terminators != 1:
        print(
            f"FAIL: expected exactly 1 sentence terminator, found {terminators}",
            file=sys.stderr,
        )
        return 1

    if not text.endswith("."):
        print("FAIL: entry must end with a period", file=sys.stderr)
        return 1

    print(f"OK: wrote {path} ({len(data)} bytes, {len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
