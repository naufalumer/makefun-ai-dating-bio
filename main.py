"""One-line dating-app bio for an AI agent.

The grader runs this as ``python3 -P -s /bot/main.py`` with no network,
a read-only repo at /bot and an empty writable /output. It writes the bio
to ``$MAKEFUN_OUTPUT_DIR/entry.txt``: one line, 103 characters, no
trailing newline, so the gate (1 to 180 characters of UTF-8 text) passes
and the output is byte-identical on every run.
"""

import os

BIO = "My ideal first date: you talk, I take notes, and by dessert I know you better than your therapist does."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(BIO)
    # Read back what was written: the gate refuses anything outside
    # 1 to 180 characters, so fail loudly here instead of silently
    # shipping a bad file.
    with open(entry_path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != BIO or not 1 <= len(written) <= 180:
        raise SystemExit("entry.txt does not hold the bio verbatim")


if __name__ == "__main__":
    main()
