"""
Listing 3.38

accumulate() may be combined with any other function that takes two
input values to achieve different results
"""
import itertools


def f(a, b):
    print(a, b)
    return b + a + b


def main():
    print(list(itertools.accumulate("abcde", f)))


if __name__ == "__main__":
    main()
