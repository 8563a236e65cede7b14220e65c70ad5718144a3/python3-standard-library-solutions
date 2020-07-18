"""
Listing 3.25

The count() function returns an iterator that produces consecutive
integers, indefinitely. The first number can be passed as an argument
(Default is zero). There is no upper bound argument

This example stops because the list argument is consumed
"""
import itertools


def main():
    for i in zip(itertools.count(1), ["a", "b", "c"]):
        print(i)


if __name__ == "__main__":
    main()
