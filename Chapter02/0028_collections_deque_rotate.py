"""
Listing 2.28

Another useful aspect of the deque is the ability to rotate it in either
direction, so as to skip over some items

Rotating the deque to the right (using a positive rotation) takes items
from the right and moves them to the left end. Rotating to the left
(with a negative value) takes items from the left end and moves them to
the right end.
"""
import collections


def main():
    d = collections.deque(range(10))
    print("Normal        :", d)

    d = collections.deque(range(10))
    d.rotate(2)
    print("Right rotation:", d)

    d = collections.deque(range(10))
    d.rotate(-2)
    print("Left rotation :", d)


if __name__ == "__main__":
    main()
