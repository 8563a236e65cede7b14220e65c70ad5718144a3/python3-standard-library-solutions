"""
Listing 1.17

Although re includes module-level functions for working with regular
expressions as text strings, it is more efficient to compile the
expressions a program uses frequently. The compile() function converts
and expression string into a RegexObject

The module-level functions maintain a cache of compiled expressions, but
the size of the cache is limited and using compiled expressions directly
avoids the overhead associated with cache lookup.

Another advantage of using compiled expressions is that by precompiling
all of the expressions when the module is loaded, the compilation work
is shifted to application start time, instead of occurring at a point
where the program may be responding to a user action
"""
import re


def main():
    regexes = [
        re.compile(p)
        for p in ["this", "that"]
    ]

    text = "Does this text match the pattern?"

    print(f"Text: {text!r}")

    for regex in regexes:
        print(f"Seeking '{regex.pattern}' ->", end=" ")

        if regex.search(text):
            print("match!")
        else:
            print("no match")


if __name__ == "__main__":
    main()
