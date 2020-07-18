"""
Listing 3.34

filterfalse() returns an iterator that includes only items where the
test function returns false
"""
import itertools


def check_item(x):
    print("Testing:", x)
    return x < 1


def main():
    for i in itertools.filterfalse(check_item,  [-1, 0, 1, 2, -2]):
        print("Yielding:", i)


if __name__ == "__main__":
    main()
