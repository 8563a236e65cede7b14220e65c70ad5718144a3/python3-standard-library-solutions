"""
Listing 1.23

A character set is a group of characters, any one of which can match at
that point in the pattern e.g. [ab] would match either a or b
"""
from re_test_patterns import test_patterns


def main():
    test_patterns(
        "abbaabbba",
        [
            ("[ab]", "either a or b"),
            ("a[ab]+", "a followed by one or more a or b"),
            ("a[ab]+?", "a followed by one or more a or b, not greedy")
        ]
    )


if __name__ == "__main__":
    main()
