"""
Listing 1.25

As character sets grow larger, typing each character becomes tedious.
You can use chracter ranges as a more compact form
"""
from re_test_patterns import test_patterns


def main():
    test_patterns(
        "This is some text -- with punctuation.",
        [
            (r"[a-z]+", "sequences of lowercase letters"),
            (r"[A-Z]+", "sequences of uppercase letters"),
            (r"[a-zA-Z]+", "sequences of lower- or uppercase letters"),
            (r"[A-Z][a-z]+", "one uppercase followed by lowercase")
        ]
    )


if __name__ == "__main__":
    main()
