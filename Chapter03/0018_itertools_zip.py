"""
Listing 3.18

The built-in function zip() returns an iterator that combines the elements
of several iterators into tuples

zip() stops when the first input iterator is exhausted.
"""


def main():
    for i in zip([1, 2, 3], ["a", "b", "c"]):
        print(i)


if __name__ == "__main__":
    main()
