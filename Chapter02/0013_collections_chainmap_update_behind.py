"""
Listing 2.13

A ChainMap does not cache the values in the child mappings. Thus, if their
contents are modified, the results are reflected when the ChainMap is
accessed.
"""
import collections


def main():
    a = {"a": "A", "c": "C"}
    b = {"b": "B", "c": "D"}

    m = collections.ChainMap(a, b)

    print(f"Before: {m['c']}")
    a["c"] = "E"
    print(f"After: {m['c']}")


if __name__ == "__main__":
    main()
