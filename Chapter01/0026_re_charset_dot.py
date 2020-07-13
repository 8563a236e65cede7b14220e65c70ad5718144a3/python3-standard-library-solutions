"""
Listing 1.26

As a special case of a character set, the meta-character dot, or period
indicates that the pattern should match any single character in that
position

Combining the dot with repetition can result in very long matches, unless
the non-greedy form is used.
"""
from re_test_patterns import test_patterns


def main():
    test_patterns(
        "abbaabbba",
        [
            ("a.", "a followed by any one character"),
            ("b.", "b followed by any one character"),
            ("a.*b", "a followed by anything, ending in b"),
            ("a.*?b", "a followed by anything, ending in b, non-greedy")
        ]
    )


if __name__ == "__main__":
    main()
