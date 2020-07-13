"""
Listing 1.60

str.split() is one of the most frequently used methods for breaking apart
strings to parse them. It supports only the literal values as separators,
though, and sometimes, a regular expression is necessary if the input is
not consistently formatted.

For example, many plain text markup languages define paragraph separators
as two or more newline (\n) characters. In this case, str.split()
cannot be used, because of the "or more" part of the definition

A strategy for identifying paragraphs using findall() would use a pattern
like (.+?)\n{2,}
"""
import re


def main():
    text = """Paragraph one
on two lines.

Paragraph two.

Paragraph three."""

    for num, para in enumerate(
        re.findall(r"(.+?)\n{2,}", text, flags=re.DOTALL)
    ):
        print(num, repr(para))
        print()


if __name__ == "__main__":
    main()
