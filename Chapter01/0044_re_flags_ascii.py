"""
Listing 1.44

Under Python 3, str objects use the full Unicode character set, and
regular expression processing on a str assumes that the pattern and
input text are both Unicode.

Those assumptions mean that the pattern \w+ will match both the words
"French" and "Français". To restrict escape codes to the ASCII character
set, as was the default in Python2, use the ASCII flag when compiling
the pattern or when calling the module level functions search() and
match()
"""
import re


def main():
    text = u"Français łzoty Österreich"
    pattern = r"\w+"
    ascii_pattern = re.compile(pattern, re.ASCII)
    unicode_pattern = re.compile(pattern)

    print("Text    :", text)
    print("Pattern :", pattern)
    print("ASCII   :", list(ascii_pattern.findall(text)))
    print("Unicode :", list(unicode_pattern.findall(text)))


if __name__ == "__main__":
    main()
