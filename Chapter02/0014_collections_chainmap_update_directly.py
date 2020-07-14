"""
Listing 2.14

It is also possible to set values through the ChainMap directly,
although only the first mapping in the chain is actually modified

When the new value is stored using m, the a mapping is updated
"""
import collections


def main():
    a = {"a": "A", "c": "C"}
    b = {"b": "B", "c": "D"}

    m = collections.ChainMap(a, b)

    print("Before:", m)
    m["c"] = "E"
    print("After:", m)
    print("a:", a)


if __name__ == "__main__":
    main()
