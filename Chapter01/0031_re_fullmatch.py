"""
Listing 1.31

The fullmatch() method requires that the entire input string match
the pattern
"""
import re


def main():
    text = "This is some text -- with punctuation"
    pattern = "is"

    print("Text         :", text)
    print("Pattern      :", pattern)

    m = re.search(pattern, text)
    print("Search       :", m)

    s = re.fullmatch(pattern, text)
    print("Full match   :", s)


if __name__ == "__main__":
    main()
