"""
Listing 1.56

In addition to searching through text, re supports modifying text using
regular expressions as the search mechanism, and there replacements can
reference groups matched in the pattern as part of the substitution text.
Use sub() to replace all occurrences of a pattern with another string
"""
import re


def main():
    bold = re.compile(r"\*{2}(.*?)\*{2}")

    text = "Make this **bold**. This **too**."
    print("Text:", text)
    print("Bold:", bold.sub(r"<b>\1</b>", text))


if __name__ == "__main__":
    main()
