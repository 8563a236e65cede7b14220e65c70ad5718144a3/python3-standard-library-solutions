"""
Listing 2.16

For situations where the new context is known or built in advance, it is
also possible to pass a mapping to new_child()

This is the equivalent of
    m2 = collections.ChainMap(c, *m1.maps)
"""
import collections


def main():
    a = {"a": "A", "c": "C"}
    b = {"b": "B", "c": "D"}
    c = {"c": "E"}

    m1 = collections.ChainMap(a, b)
    m2 = m1.new_child(c)

    print(f"m1['c'] = {m1['c']}")
    print(f"m2['c'] = {m2['c']}")


if __name__ == "__main__":
    main()
