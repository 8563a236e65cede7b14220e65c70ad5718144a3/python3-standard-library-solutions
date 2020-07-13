"""
Listing 1.40

Defining a group containing a subpattern is also useful in cases where
the string matching subpattern is not part of what should be extracted
from the full text. These kinds of groups are called non-capturing.
Non-capturing groups can be used to describe repetition patterns or
alternatives, without isolating the matching portion of the string in
the value returned.

To create a non-capturing group, use (?:pattern)
"""
from re_test_patterns_groups import test_patterns


def main():
    test_patterns(
        "abbaabbba",
        [
            (r"a((a+)|(b+))", "capturing form"),
            (r"a((?:a+)|(?:b+))", "noncapturing")
        ]
    )


if __name__ == "__main__":
    main()
