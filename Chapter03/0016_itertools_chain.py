"""
Listing 3.16

The itertools module includes a set of functions for working with
sequence data sets. They are intended to be fast and use memory
efficiently. They can also be hooked together to express more complicated
iterations-based algorithms.

Iterator-based code offers better memory consumption characteristics than
code that uses lists. Since data is not produced from the iterator until
it is needed, all of the data does not need to be stored in memory at
the same time.

This "lazy" processing model can reducing swapping and other side effects
of large data sets, improving performance.

The chain() function takes several iterators as arguments and returns
a single iterator that produces the contents of all the inputs as though
they came from a single iterator

chain() makes it easy to process several sequences without constructing
one large list
"""
import itertools


def main():
    for i in itertools.chain([1, 2, 3], ["a", "b", "c"]):
        print(i, end=" ")
    print()


if __name__ == "__main__":
    main()
