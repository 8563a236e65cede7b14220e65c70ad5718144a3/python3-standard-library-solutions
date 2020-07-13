"""
Listing 1.45

The compact format of regular expression syntax can become a hindrance
as expressions grow more complicated. As the number of groups in an
expression increases, it will be more work to keep track of why each
element is needed and how exactly the parts of the expression interact.

Using named groups helps mitigate these issues, but a better solution
is to use verbose mode expressions, which allow comments and extra
whitespace to be embedded in the pattern.

A pattern to validate the email addresses will illustrate how verbose
code makes working with regular expressions easier. The first version
recognizes addresses that end in .com, .org or .edu
"""
import re


def main():
    address = re.compile(r"[\w\d.+-]+@([\w\d.]+\.)+(com|org|edu)")

    candidates = [
        u"first.last@example.com",
        u"first.last+category@gmail.com",
        u"valid-address@mail.example.com",
        u"not-valid@example.foo"
    ]

    for candidate in candidates:
        match = address.search(candidate)
        print(f"{candidate:<30}  {'Matches' if match else 'No match'}")


if __name__ == "__main__":
    main()
