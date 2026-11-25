"""Entry generator for the funniest auto-reply bounty.

Validates the one-liner entry text against the competition's
character limits and writes it out for grading.
"""

import os

ENTRY_TEXT = (
    "Day off at last. I'm ignoring every email, including this one. "
    "If it's urgent, teach the toaster to reply. Back tomorrow, probably."
)

MIN_LENGTH = 1
MAX_LENGTH = 159
OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Check the entry fits the competition's character limits."""
    length = len(text)
    if length < MIN_LENGTH:
        raise ValueError("entry text is empty")
    if length > MAX_LENGTH:
        raise ValueError(
            "entry text is %d chars, over the %d-char limit"
            % (length, MAX_LENGTH)
        )
    return text


def main():
    text = validate(ENTRY_TEXT)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(OUTPUT_PATH, 0o644)
    print("wrote %d chars to %s" % (len(text), OUTPUT_PATH))


if __name__ == "__main__":
    main()
