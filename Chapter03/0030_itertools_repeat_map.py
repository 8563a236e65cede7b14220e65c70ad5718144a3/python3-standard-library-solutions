"""
Listing 3.30

This example uses map() to multiply the numbers in the range 0 through 4
by 2

The repeat() iterator does not need to be explicitly limited, since
map() stops processing when any of its input ends, and the range()
returns only five elements
"""
import itertools


def main():
    for i in map(
        lambda x, y: (x, y, x * y),
        itertools.repeat(2),
        range(5)
    ):
        print(f"{i[0]:d} * {i[1]:d} = {i[2]:d}")


if __name__ == "__main__":
    main()
