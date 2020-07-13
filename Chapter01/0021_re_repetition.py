"""
Listing 1.21

There are five ways to express repetition in a pattern. A pattern followed
by the metacharacter * is repeated zero or more times. + means that the
pattern must appear at least once. Using ? means the pattern appears zero
or one time. For a specific number of occurrences, use {m} after the
pattern, where m is the number of times the pattern should repeat. To
allow a variable, but limited number of repetitions, use {m, n}, where
m is the minimum number of repetitions and n is the maximum. Leaving out
n ({m,}) means the value must appear at least m times, with no maximum
"""
import re
from re_test_patterns import test_patterns


def main():
    test_patterns(
        "abbaabbba",
        [
            ("ab*", "a followed by zero or more b"),
            ("ab+", "a followed by one or more b"),
            ("ab?", "a followed by zero or one b"),
            ("ab{3}", "a followed by three b"),
            ("ab{2,3}", "a followed by two to three b")
        ]
    )


if __name__ == "__main__":
    main()
