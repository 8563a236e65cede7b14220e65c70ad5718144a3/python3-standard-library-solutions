"""
Listing 3.37

The accumulate() function processes the input iterable, passing the
nth and n+1st item to a function and producing the return value instead
of either input.

The default function used to combine to values adds them, so accumulate()
can be used to produce the cumulative sum of a series of numerical
inputs

When used with a sequence of non-integer values, the results depend on
what it means to "add" two items together. When accumulate() receives
a string input, each response is a progressively longer prefix of that
string
"""
import itertools


def main():
    print(list(itertools.accumulate(range(5))))
    print(list(itertools.accumulate("abcde")))


if __name__ == "__main__":
    main()
