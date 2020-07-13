"""
Listing 1.35

To ask for the match of a single group, use the group() method. This is
useful when grouping is being used to find parts of the string, but some
of the parts matched by groups are not needed in results

Group 0 represents the string matched by the entire expression, and
subgroups are numbered starting with 1 in the order that their left
parenthesis appears in the expression.
"""
import re


def main():
    text = "This is some text -- with punctuation."

    print("Input text            :", text)

    # Word starting with "t" then another word
    regex = re.compile(r"(\bt\w+)\W+(\w+)")
    print("Pattern               :", regex.pattern)

    match = regex.search(text)
    print("Entire match          :", match.group(0))
    print("Word starting with 't':", match.group(1))
    print("Word after 't' word   :", match.group(2))


if __name__ == "__main__":
    main()
