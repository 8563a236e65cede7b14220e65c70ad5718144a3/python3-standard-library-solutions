"""
Listing 1.64

The Differ class works on sequences of text lines and produces human-readable
deltas, or change instructions, including differences within individual
lines.

The default output produced by Differ is similar to the diff command-line
tool under Unix. It includes the original input values from both lists,
including common values, and markup data to indicate which changes were
made
    Lines prefixed with - were in the first sequence but not the second
    Lines prefixed with + were in the second sequence but not the first
    If a line has an incremental difference between versions, an extra
    line prefixed with ? is used to highlight the change within the new
    version
    If a line has not changed, it is printed with an extra blank space
    on the left column, so that it is aligned with the other output that
    may have differences

Breaking the text up into a sequence of individual lines before passing it
to compare() produces more readable output than passing in large strings
"""
import difflib
from difflib_data import *


def main():
    d = difflib.Differ()
    diff = d.compare(text1_lines, text2_lines)
    print("\n".join(diff))


if __name__ == "__main__":
    main()
