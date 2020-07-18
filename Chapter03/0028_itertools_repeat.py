"""
Listing 3.28

The repeat() function returns an iterator that produces the same value
each time it is accessed.

The iterator returned by repeat() keeps returning data forever, unless
the optional times argument is provided to limit it
"""
import itertools


def main():
    for i in itertools.repeat("over-and-over", 5):
        print(i)


if __name__ == "__main__":
    main()
