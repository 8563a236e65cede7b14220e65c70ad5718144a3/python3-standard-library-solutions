"""
Listing 2.38

An OrderedDict is a dictionary subclass that remembers the order in which
its contents are added

A regular dict does not track the insertion order and iterating over it
produces the values in order based on how the keys are stored in the
hash table.

OrderedDict, by contrast, remembers the order of items inserted and
uses it when creating an iterator

** from 3.7, insertion order for python dictionaries is guaranteed
"""
import collections


def main():
    print("Regular dictionary:")
    d = {}
    d["a"] = "A"
    d["b"] = "B"
    d["c"] = "C"

    for k, v in d.items():
        print(k, v)

    print("OrderedDict:")
    d = collections.OrderedDict()
    d["a"] = "A"
    d["b"] = "B"
    d["c"] = "C"

    for k, v in d.items():
        print(k, v)


if __name__ == "__main__":
    main()
