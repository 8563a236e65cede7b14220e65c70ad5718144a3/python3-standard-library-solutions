"""
Listing 2.56

The queue module provides a first-in, first-out data structure suitable
for multi-threaded programming. It can be used to pass messages or other
data between producer and consumer threads safely. Locking is handled for
the caller, so many threads can work with the same Queue instance safely
and easily. The size of a Queue (the number of elements it contains) may
be restricted to throttle memory usage or processing

The Queue class implements a basic first-in, first-out container.
Elements are added to one "end" of the sequence using put(), and
removed from the other end using get()

Elements are removed from the queue in the same order in which they
are inserted
"""
import queue


def main():
    q = queue.Queue()

    for i in range(5):
        q.put(i)

    while not q.empty():
        print(q.get(), end=" ")
    print()


if __name__ == "__main__":
    main()
