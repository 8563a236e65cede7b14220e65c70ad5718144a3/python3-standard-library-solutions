"""
Listing 3.31

The dropwhile() functions returns an iterator that produces elements of
the input iterator after a condition becomes false for the first time.

dropwhile() does not filter every item of input. After the condition
is false the first time, all of the remaining items in the input
are returned
"""
import itertools


def should_drop(x):
    print("Testing:", x)
    return x < 1


def main():
    for i in itertools.dropwhile(should_drop, [-1, 0, 1, 2, -2]):
        print("Yielding:", i)


if __name__ == "__main__":
    main()
