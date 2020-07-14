"""
Listing 2.15

ChainMap provides a convenience method for creating a new instance with
one extra mapping at the front of the maps list to make it easy to avoid
modifying the existing underlying data structures

This stacking behaviour is what makes it convenient to use ChainMap
instances as template or application contexts. Specifically, it is
easy to add or update values in one iteration, then discard the changes
for the next iteration
"""
import collections


def main():
    a = {"a": "A", "c": "C"}
    b = {"b": "B", "c": "D"}

    m1 = collections.ChainMap(a, b)
    m2 = m1.new_child()

    print("m1 before:", m1)
    print("m2 before:", m2)

    m2["c"] = "E"

    print("m1 after:", m1)
    print("m2 after:", m2)


if __name__ == "__main__":
    main()
