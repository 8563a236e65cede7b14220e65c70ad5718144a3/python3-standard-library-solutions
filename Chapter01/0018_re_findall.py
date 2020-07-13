"""
Listing 1.18

findall() function returns all of the substrings of the input that match
the pattern without overlapping
"""
import re


def main():
    text = "abbaaabbbbaaaaa"
    pattern = "ab"

    for match in re.findall(pattern, text):
        print(f"Found {match!r}")


if __name__ == "__main__":
    main()
