"""
Listing 2.29

A deque instance cna be configured with a maximum length so that it never
grows beyond that size. When the queue reaches the specified length,
existing items are discarded as new items are added. This behaviour is
useful for finding the last n items in a stream of undetermined length

The deque length is maintained regardless of which end the items are
added to.
"""
import collections
import random


def main():
    # Set the random seed so we see the same output each time
    # the script is run.
    random.seed(1)

    d1 = collections.deque(maxlen=3)
    d2 = collections.deque(maxlen=3)

    for i in range(5):
        n = random.randint(0, 100)
        print("n = ", n)
        d1.append(n)
        d2.appendleft(n)
        print("D1:", d1)
        print("D2:", d2)


if __name__ == "__main__":
    main()
