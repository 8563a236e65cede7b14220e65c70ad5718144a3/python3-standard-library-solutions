"""
Listing 2.12

The ChainMap stores the list of mappings over which it searches in a list
in its maps attribute. This list is mutable, so it is possible to add new
mappings directly or to change the order of the elements to control
lookup and update behaviour
"""
import collections


def main():
    a = {"a": "A", "c": "C"}
    b = {"b": "B", "c": "D"}

    m = collections.ChainMap(a, b)

    print(m.maps)
    print(f"c = {m['c']}")

    # Reverse the list
    m.maps = list(reversed(m.maps))

    print(m.maps)
    print(f"c = {m['c']}")


if __name__ == "__main__":
    main()
