"""
Listing 1.29

The relative location can be specified in the input text where the pattern
should appear by using anchoring instructions
    ^   Start of string, or line
    $   End of string, or line
    \A  Start of string
    \Z  End of string
    \b  Empty string at the beginning or end of a word
    \B Empty string not at the beginning or end of a word
"""
import re
from re_test_patterns import test_patterns


def main():
    test_patterns(
        "This is some text -- with punctuation.",
        [
            (r"^\w+", "word at start of string"),
            (r"\A\w+", "word at start of string"),
            (r"\w+\S*$", "word near end of string"),
            (r"\w+\S*\Z", "word near end of string"),
            (r"\w*t\w*", "word containing t"),
            (r"\bt\w+", "t at start of word"),
            (r"\w+t\b", "t at end of word"),
            (r"\Bt\B", "t not at start or end of word")
        ]
    )


if __name__ == "__main__":
    main()
