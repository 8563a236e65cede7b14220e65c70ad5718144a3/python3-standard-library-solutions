"""
Listing 1.10

Use dedent() to produce better results and allow for the use of docstrings
or embedded multiline strings straight from Python code while removing
the formatting of the code itself.

If one line is already indented more than another, some whitespace will
not be removed (only common whitespace from each line is removed)

_Line_One
___Line_two
_Line_three

becomes
Line_One
__Line_two
Line_three
"""
import textwrap
from textwrap_example import sample_text


def main():
    dedented_text = textwrap.dedent(sample_text)
    print("Original:")
    print(sample_text)
    print("Dedented:")
    print(dedented_text)


if __name__ == "__main__":
    main()
