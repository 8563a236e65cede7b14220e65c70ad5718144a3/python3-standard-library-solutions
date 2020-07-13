"""
Listing 1.16

Regular expressions are text matching patterns described with a formal
syntax. The patterns are interpreted as a set of instructions, which are
then executed with a string as input to produce a matching subset or
modified version of the original.

The most common use for re is to search for patterns in text. The search()
function takes the pattern and text to scan, and returns a Match object
when the pattern is found. If the pattern is not found, search() returns
None.

Each match object holds information about the nature of the match,
including the original input string, the regular expression used, and
the location within the original string where the pattern occurs

The start() and end() methods give the indexes into the string showing
where the text matched by the pattern occurs.
"""
import re


def main():
    pattern = "this"
    text = "Does this text match the pattern?"
    match = re.search(pattern, text)

    s = match.start()
    e = match.end()

    print(f"Found '{match.re.pattern}'\n in '{match.string}'\n from"
          f" {s} to {e} ('{text[s:e]}')")


if __name__ == "__main__":
    main()
