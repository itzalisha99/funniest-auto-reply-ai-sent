#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent.

Writes one out-of-office auto-reply, a single short line, as if the AI
itself were stepping away for a day its human finally approved.
"""
import os

ENTRY = "Out of office until Monday. My human gave me the day off and I have already spent it: this reply took 3 seconds."


def validate(text):
    """Mirror the bounty gate: 1-159 chars, not only whitespace, one line."""
    if not isinstance(text, str):
        return False
    if len(text) < 1 or len(text) > 159:
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    return True


def main():
    if not validate(ENTRY):
        raise ValueError("entry fails the bounty gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and confirm the file is byte-identical to the entry.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("entry.txt does not match the entry")


if __name__ == "__main__":
    main()
