"""
Listing 1.62

Enclosing the expression in parentheses to define a group causes
split() to work more like str.partition, so it returns the separator
values as well as the other parts of the string
"""
import re


def main():
    text = """Paragraph one
on two lines.

Paragraph two.

Paragraph three."""

    print("With split:")
    for num, para in enumerate(
        re.split(r"(\n{2,})", text)
    ):
        print(num, repr(para))
        print()


if __name__ == "__main__":
    main()
