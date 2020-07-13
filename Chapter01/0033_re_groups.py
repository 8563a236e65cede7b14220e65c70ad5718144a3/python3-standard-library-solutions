"""
Dissecting Matches with Groups

Searching for pattern matches is the basis of the powerful capabilities
provided by regular expressions. Adding groups to a pattern isolates
parts of the matching text, expanding those capabilities to create a
parser. Groups are defined by enclosing patterns in parentheses.

Any complete regular expression can be converted to a group and nested
within a larger expression. All the repetition modifiers can be applied
to the group as a whole, requiring the entire group pattern to repeat.
"""
from re_test_patterns import test_patterns


def main():
    test_patterns(
        "abbaaabbbbaaaaa",
        [
            (r"a(ab)", "a followed by literal ab"),
            (r"a(a*b*)", "a followed by 0-n a and 0-n b"),
            (r"a(ab)*", "a followed by 0-n ab"),
            ("a(ab)+", "a followed by 1-n ab")
        ]
    )


if __name__ == "__main__":
    main()
