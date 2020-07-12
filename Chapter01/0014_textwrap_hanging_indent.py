"""
Listing 1.14

In the same way that it is possible to set the width of the output,
the indent of the first line can be controlled independently of subsequent
lines

The indent values can include non-whitespace characters too. The
hanging indent can be prefixed with * to produce bullet points, for
example
"""
import textwrap
from textwrap_example import sample_text


def main():
    dedented_text = textwrap.dedent(sample_text).strip()
    print(textwrap.fill(dedented_text,
                        initial_indent="",
                        subsequent_indent=" " * 4,
                        width=50))


if __name__ == "__main__":
    main()
