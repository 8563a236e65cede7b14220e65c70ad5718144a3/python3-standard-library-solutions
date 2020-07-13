"""
Listing 1.38

Since a group is itself a complete regular expression, groups can be
nested within other groups to build even more complicated expressions
"""
from re_test_patterns_groups import test_patterns


def main():
    test_patterns(
        "abbaabbba",
        [(r"a((a*)(b*))", "a followed by 0-n a and 0-n b")]
    )


if __name__ == "__main__":
    main()
