"""
Listing 1.34

To access the substrings matched by the individual groups within a pattern,
use the groups() method of the Match object

Match.groups() returns a sequence of strings in the order of the groups
within the expression that matches the string.
"""
import re


def main():
    text = "This is some text -- with punctuation."
    print(text)
    print()

    patterns = [
        (r"^(\w+)", "word at start of string"),
        (r"(\w+)\S*$", "word at end with optional punctuation"),
        (r"(\bt\w+)\W+(\w+)", "word starting with t, another word"),
        (r"(\w+t)\b", "word ending with t"),
    ]

    for pattern, desc in patterns:
        regex = re.compile(pattern)
        match = regex.search(text)
        print(f"'{pattern}'   ({desc})\n")
        print("   ", match.groups())
        print()


if __name__ == "__main__":
    main()
