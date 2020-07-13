"""
Listing 1.22

When processing a repetition instruction, re will usually consume as much
of the input as possible, while matching the pattern. This so-called
greedy behaviour may result in fewer individual matches, or the matches
may include more of the input text than intended.

Greediness can be turned off by following the repetition instruction
with ?
"""
from re_test_patterns import test_patterns


def main():
    test_patterns(
        "abbaabbba",
        [
            ("ab*?", "a followed by zero or more b"),
            ("ab+?", "a followed by one or more b"),
            ("ab??", "a followed by zero or one b"),
            ("ab{3}?", "a followed by three b"),
            ("ab{2,3}?", "a followed by two to three b")
        ]
    )


if __name__ == "__main__":
    main()
