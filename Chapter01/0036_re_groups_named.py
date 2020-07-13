"""
Listing 1.36

Python extends the basic grouping syntax to add named groups. Using
names to refer to groups makes it easier to modify the pattern over
time, without having to also modify the code using the match results.

To set the name of a group, use the syntax (?P<name>pattern)

Use groupdict() to retrieve the dictionary mapping group names to
substrings from the match. Named patterns are included in the
ordered sequence returned by groups() as well.
"""
import re


def main():
    text = "This is some text -- with punctuation."
    print(text)
    print()

    patterns = [
        r"^(?P<first_word>\w+)",
        r"(?P<last_word>\w+)\S*$",
        r"(?P<t_word>\bt\w+)\W+(?P<other_word>\w+)",
        r"(?P<ends_with_t>\w+t)\b"
    ]

    for pattern in patterns:
        regex = re.compile(pattern)
        match = regex.search(text)
        print(f"'{pattern}'")
        print(f"   ", match.groups())
        print(f"   ", match.groupdict())
        print()


if __name__ == "__main__":
    main()
