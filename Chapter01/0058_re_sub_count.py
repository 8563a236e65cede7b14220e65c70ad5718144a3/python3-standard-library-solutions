"""
Listing 1.58

Pass a value to count to limit the number of substitutions performed
"""
import re


def main():
    bold = re.compile(r"\*{2}(.*?)\*{2}")

    text = "Make this **bold**. This **too**."
    print("Text:", text)
    print("Bold:", bold.sub(r"<b>\1</b>", text, count=1))


if __name__ == "__main__":
    main()
