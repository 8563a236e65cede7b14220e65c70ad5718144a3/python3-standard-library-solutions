"""
Listing 5.7

In contrast to the standard FIFO implementation of Queue, the
LifoQueue uses last-in, first-out orderings (normally associated with
a stack data structure)
"""
import queue


def main():
    q = queue.LifoQueue()

    for i in range(5):
        q.put(i)

    while not q.empty():
        print(q.get(), end=" ")
    print()


if __name__ == "__main__":
    main()
