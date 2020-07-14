"""
Listing 2.20

The elements() method returns an iterator that produces all of the items
known to the Counter

The order of elements is not guaranteed and items with counts less than
or equal to zero are not included
"""
import collections


def main():
    c = collections.Counter("extremely")
    c["z"] = 0
    print(c)
    print(list(c.elements()))


if __name__ == "__main__":
    main()
