"""
Listing 3.26

The start and step arguments to count() can be any numerical values that
can be added together
"""
import fractions
import itertools


def main():
    start = fractions.Fraction(1, 3)
    step = fractions.Fraction(1, 3)

    for i in zip(itertools.count(start, step), ["a", "b", "c"]):
        print("{}: {}".format(*i))


if __name__ == "__main__":
    main()
