"""
Listing 1.57

To use named groups in the substitution, use the syntax \g<name>
"""
import re


def main():
    bold = re.compile(r"\*{2}(?P<bold_text>.*?)\*{2}")

    text = "Make this **bold**. This **too**."
    print("Text:", text)
    print("Bold:", bold.sub(r"<b>\g<bold_text></b>", text))


if __name__ == "__main__":
    main()
