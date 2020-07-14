"""
Listing 2.39

A regular dict looks at its contents when testing for equality. An
OrderedDict also considered the order in which the items were added

In this case, since two ordered dictionaries are created from values
in a different order, they are considered to be different
"""
import collections


def main():
    print("dict       :", end=" ")
    d1 = {}
    d1["a"] = "A"
    d1["b"] = "B"
    d1["c"] = "C"

    d2 = {}
    d2["c"] = "C"
    d2["b"] = "B"
    d2["a"] = "A"

    print(d1 == d2)

    print("OrderedDict:", end=" ")

    d1 = collections.OrderedDict()
    d1["a"] = "A"
    d1["b"] = "B"
    d1["c"] = "C"

    d2 = collections.OrderedDict()
    d2["c"] = "C"
    d2["b"] = "B"
    d2["a"] = "A"

    print(d1 == d2)


if __name__ == "__main__":
    main()
