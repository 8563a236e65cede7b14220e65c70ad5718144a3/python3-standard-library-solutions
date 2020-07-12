"""
Listing 1.12

Use the indent() function to add consistent prefix text to all of the
lines in a string.
"""
import textwrap
from textwrap_example import sample_text


def main():
    dedented_text = textwrap.dedent(sample_text)
    wrapped = textwrap.fill(dedented_text, width=50)
    wrapped += "\n\nSecond paragraph after a blank line"
    final = textwrap.indent(wrapped, "> ")

    print("Quoted block:\n")
    print(final)


if __name__ == "__main__":
    main()
