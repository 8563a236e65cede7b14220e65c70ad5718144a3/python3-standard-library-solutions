"""
Listing 1.19

finditer() returns an iterator that produces Match instances instead of
the strings returned by findall()
"""
import re


def main():
    text = "abbaaabbbbaaaa"
    pattern = "ab"

    for match in re.finditer(pattern, text):
        s = match.start()
        e = match.end()
        print(f"Found {text[s:e]!r} at {s:d}:{e:d}")


if __name__ == "__main__":
    main()
