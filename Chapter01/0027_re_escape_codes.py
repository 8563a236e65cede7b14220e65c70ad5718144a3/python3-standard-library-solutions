"""
Listing 1.27

An even more compact representation uses escape codes for several
predefined character sets
    \d  A digit
    \D  A non-digit
    \s  Whitespace (tab, space, newline, etc.)
    \S  Non-whitespace
    \w  Alphanumeric
    \W  Non-Alphanumeric
"""
from re_test_patterns import test_patterns


def main():
    test_patterns(
        "A prime #1 example!",
        [
            (r"\d+", "sequence of digits"),
            (r"\D+", "sequence of non-digits"),
            (r"\s+", "sequence of whitespace"),
            (r"\S+", "sequence of non-whitespace"),
            (r"\w+", "alphanumeric characters"),
            (r"\W+", "non-alphanumeric"),
        ]
    )


if __name__ == "__main__":
    main()
