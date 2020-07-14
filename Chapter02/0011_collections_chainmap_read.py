"""
Listing 2.11

The collections module includes container data types beyond the built-in
types list, dict and tuple.

The ChainMap class manages a sequence of dictionaries, and searches
through them in the order that they appear to find values associated with
keys.

A ChainMap makes a good "context" container, since it can be treated as
a stack for which changes happen as the stack grows, with these
changes being discarded again as the stack shrinks.

The ChainMap supports the same API as a regular dictionary for accessing
existing values
"""
import collections


def main():
    a = {"a": "A", "c": "C"}
    b = {"b": "B", "c": "D"}

    m = collections.ChainMap(a, b)
    print("Individual Values")
    print(f"a = {m['a']}")
    print(f"b = {m['b']}")
    print(f"c = {m['c']}")

    print(f"Keys = {list(m.keys())}")
    print(f"Values = {list(m.values())}")

    print("Items:")
    for k, v in m.items():
        print(f"{k} = {v}")
    print()

    print(f"'d' in m: {'d' in m}")


if __name__ == "__main__":
    main()
