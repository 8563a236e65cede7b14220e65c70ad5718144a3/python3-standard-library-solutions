"""
Listing 3.35

compress() offers another way to filter the contents of an iterable.
Instead of calling a function, it uses the values in another iterable
to indicate when to accept a value and when to ignore it.

The first argument is the data iterable to process. The second argument
is a selector iterable that produces boolean values indicating which
elements to take from the data input
"""
import itertools


def main():
    every_third = itertools.cycle([False, False, True])
    data = range(1, 10)

    for i in itertools.compress(data, every_third):
        print(i, end=" ")
    print()


if __name__ == "__main__":
    main()
