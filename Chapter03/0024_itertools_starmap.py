"""
Listing 3.24

The starmap() function is similar to map(), but instead of constructing
a tuple from multiple iterators, it splits up the items in a single
iterator as arguments to the mapping function using the * syntax
"""
import itertools


def main():
    values = [
        (0, 5), (1, 6), (2, 7), (3, 8), (4, 9)
    ]

    for i in itertools.starmap(lambda x, y: (x, y, x * y), values):
        print("{} * {} = {}".format(*i))


if __name__ == "__main__":
    main()
