"""
Listing 1.39

Groups are also useful for specifying alternative patterns. Use the
pipe symbol (|) to indicate that either pattern should match.
"""
from re_test_patterns_groups import test_patterns


def main():
    test_patterns(
        "abbaabbba",
        [
            (r"a((a+)|(b+))", "a then seq. of a or seq. of b"),
            (r"a((a|b)+)", "a then seq. of [ab]")
        ]
    )


if __name__ == "__main__":
    main()
