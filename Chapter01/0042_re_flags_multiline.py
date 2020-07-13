"""
Listing 1.42

Two flags affect how searching in multiline input works: MULTILINE and
DOTALL. The MULTILINE flag controls how the pattern matching code
processes anchoring instructions for text containing newline characters.
When multiline is turned on, the anchor rules for ^ and $ apply at the
beginning and end of each line, in addition to the entire string
"""
import re


def main():
    text = "This is some text -- with punctuation.\nA second line."
    pattern = r"(^\w+)|(\w+\S*$)"
    single_line = re.compile(pattern)
    multiline = re.compile(pattern, re.MULTILINE)

    print(f"Text:\n  {text!r}")
    print(f"Pattern:\n  {pattern}")
    print("Single Line:")
    for match in single_line.findall(text):
        print(f"  {match!r}")
    print("Multiline:")
    for match in multiline.findall(text):
        print(f"  {match!r}")


if __name__ == "__main__":
    main()
