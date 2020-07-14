"""
Listing 2.25

A deque can be populated from either end, termed "left" and "right" in
the Python implementation

The extendleft() function iterates over its input and performs the
equivalent of an appendleft() for each item. The end result is that
deque contains the input sequence in reverse order
"""
import collections


def main():
    # Add to the right.
    d1 = collections.deque()
    d1.extend("abcdefg")
    print("extend    :", d1)
    d1.append("h")
    print("append    :", d1)

    # Add to the left
    d2 = collections.deque()
    d2.extendleft(range(6))
    print("extendleft:", d2)
    d2.appendleft(6)
    print("appendleft:", d2)


if __name__ == "__main__":
    main()

