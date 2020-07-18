"""
Listing 3.28

It is useful to combine repeat() with zip() or map() when invariant
values should be included with the values from other iterators
"""
import itertools


def main():
    for i, s in zip(
            itertools.count(),
            itertools.repeat("over-and-over", 5)):
        print(i, s)


if __name__ == "__main__":
    main()
