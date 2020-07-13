"""
Listing 1.41

Option flags are used to change the way the matching engine processes an
expression. The flags can be combined using a bitwise OR operation, then
passed to compile(), search(), match() and other functions that accept a
pattern for searching

IGNORECASE causes literal characters and character ranges in the pattern
to match both uppercase and lowercase characters
"""
import re


def main():
    text = "This is some text -- with punctuation."
    pattern = r"\bT\w+"
    with_case = re.compile(pattern)
    without_case = re.compile(pattern, re.IGNORECASE)

    print(f"Text:\n  {text!r}")
    print(f"Pattern:\n  {pattern}")
    print("Case-sensitive:")
    for match in with_case.findall(text):
        print(f"  {match!r}")
    print("Case-insensitive:")
    for match in without_case.findall(text):
        print(f"  {match!r}")


if __name__ == "__main__":
    main()
