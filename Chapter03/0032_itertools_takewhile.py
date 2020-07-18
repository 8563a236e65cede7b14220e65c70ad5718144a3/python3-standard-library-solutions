"""
Listing 3.32

The opposite of dropwhile() is takewhile(). It returns an iterator
that itself returns items from the input iterator as long as the test
function returns true
"""
import itertools


def should_take(x):
    print("Testing:", x)
    return x < 2


def main():
    for i in itertools.takewhile(should_take, [-1, 0, 1, 2, -2]):
        print("Yielding:", i)


if __name__ == "__main__":
    main()
