"""
Listing 1.30

In situations where it is known in advance that only a subset of the full
input should be searched, the regular expression match can be further
constrained by telling re to limit the search range.

e.g. if pattern must appear at the front of the input, then using match()
instead of search() will anchor the search without having to explicitly
include an anchor in the search pattern
"""
import re


def main():
    text = "This is some text -- with punctuation"
    pattern = "is"

    print("Text   :", text)
    print("Pattern:", pattern)

    m = re.match(pattern, text)
    print("Match  :", m)
    s = re.search(pattern, text)
    print("Search :", s)


if __name__ == "__main__":
    main()
