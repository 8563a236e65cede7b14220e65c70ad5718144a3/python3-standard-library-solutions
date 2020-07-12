"""
Listing 1.11

Dedented text can be passed through fill with a few different
width values.
"""
import textwrap
from textwrap_example import sample_text


def main():
    dedented_text = textwrap.dedent(sample_text).strip()
    for width in [45, 60]:
        print("{} Columns:\n".format(width))
        print(textwrap.fill(dedented_text, width=width))
        print()


if __name__ == "__main__":
    main()
