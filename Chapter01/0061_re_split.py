"""
Listing 1.61

The previous pattern fails for paragraphs at the end of the input text

Converting to re.split() instead of re.findall() handles the boundary
condition automatically and keeps the pattern simpler
"""
import re


def main():
    text = """Paragraph one
on two lines.

Paragraph two.

Paragraph three."""

    print("With findall:")
    for num, para in enumerate(
        re.findall(r"(.+?)(\n{2,}|$)", text, flags=re.DOTALL)
    ):
        print(num, repr(para))
        print()

    print("With split:")
    for num, para in enumerate(
        re.split(r"\n{2,}", text)
    ):
        print(num, repr(para))
        print()


if __name__ == "__main__":
    main()
