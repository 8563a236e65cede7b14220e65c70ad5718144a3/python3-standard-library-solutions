"""
Listing 2.18

An empty Counter can be constructed with no arguments and populated via
the update() method

The count values are increased based on the new data, rather than replaced
"""
import collections


def main():
    c = collections.Counter()
    print("Initial :", c)
    c.update("abcdaab")
    print("Sequence:", c)
    c.update({"a": 1, "d": 5})
    print("Dict    :", c)


if __name__ == "__main__":
    main()
