"""
Listing 1.48

In situations where flags cannot be added when compiling an expression,
such as when a pattern is passed as an argument to a library function
that will compile it later, the flags can be embedded inside the expression
string itself. For example, to turn case-insensitive matching on,
add (?i) to the beginning of the expression

Because the options control the way the entire expression is evaluated
or parsed, they should always appear at the beginning of the expression

Embedded flags can be combined by placing them within the same group,
for example (?im) turns on case-insensitive matching for multiline
strings
    ASCII       a
    IGNORECASE  i
    MULTILINE   m
    DOTALL      s
    VERBOSE     x
"""
import re


def main():
    text = "This is some text -- with punctuation"
    pattern = r"(?i)\bT\w+"
    regex = re.compile(pattern)
    print(f"Text     : {text}")
    print(f"Pattern  : {pattern}")
    print(f"Matches  : {regex.findall(text)}")


if __name__ == "__main__":
    main()
