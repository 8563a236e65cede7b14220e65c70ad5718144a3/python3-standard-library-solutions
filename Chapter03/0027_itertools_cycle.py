"""
Listing 3.27

The cycle() function returns an iterator that repeats the contents of the
arguments it is given indefinitely. Because it has to remember the entire
contents of the input iterator, it may consume quite a bit of memory if
the iterator is long.
"""
import itertools


def main():
    for i in zip(range(7), itertools.cycle(["a", "b", "c"])):
        print(i)


if __name__ == "__main__":
    main()
