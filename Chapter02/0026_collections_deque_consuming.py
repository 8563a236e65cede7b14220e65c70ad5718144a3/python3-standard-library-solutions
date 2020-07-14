"""
Listing 2.26

The elements of the deque can be consumed from both ends or either end,
depending on the algorithm being applied

Use pop() to remove an item from the "right" end of the deque and
popleft() to take an item from the "left" end
"""
import collections


def main():
    print("From the right:")
    d = collections.deque("abcdefg")
    while True:
        try:
            print(d.pop(), end="")
        except IndexError:
            break
    print()

    print("\nFrom the left:")
    d = collections.deque(range(6))
    while True:
        try:
            print(d.popleft(), end="")
        except IndexError:
            break
    print()


if __name__ == "__main__":
    main()
