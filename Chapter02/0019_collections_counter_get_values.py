"""
Listing 2.19

Once a Counter is populated, its values can be retrieved using the
dictionary API

Counter does not raise KeyError for unknown items. If a value has not
been seen in the input, its count is 0
"""
import collections


def main():
    c = collections.Counter("abcdaab")

    for letter in "abcde":
        print(f"{letter} : {c[letter]}")


if __name__ == "__main__":
    main()
