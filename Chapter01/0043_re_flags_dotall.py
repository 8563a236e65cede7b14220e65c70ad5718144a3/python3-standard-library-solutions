"""
Listing 1.43

DOTALL is the other flag related to multiline text. Normally, the dot
character (.) matches everything in the input text except a newline
character. The flag allows the dot to match newlines as well
"""
import re


def main():
    text = "This is some text -- with punctuation.\nA second line."
    pattern = r".+"
    no_newlines = re.compile(pattern)
    dotall = re.compile(pattern, re.DOTALL)

    print(f"Text:\n  {text!r}")
    print(f"Pattern:\n  {pattern}")
    print("No newlines:")
    for match in no_newlines.findall(text):
        print(f"  {match!r}")
    print("Dotall:")
    for match in dotall.findall(text):
        print(f"  {match!r}")


if __name__ == "__main__":
    main()
