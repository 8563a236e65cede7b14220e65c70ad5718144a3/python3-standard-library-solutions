"""
Listing 1.24

A character set can also be used to exclude specific characters. The carat
(^) means to look for characters that are not in the set following the
carat
"""
from re_test_patterns import test_patterns


def main():
    test_patterns(
        "This is some text -- with punctuation.",
        [(r"[^-. ]+", "sequences without -, ., or space")]
    )


if __name__ == "__main__":
    main()
