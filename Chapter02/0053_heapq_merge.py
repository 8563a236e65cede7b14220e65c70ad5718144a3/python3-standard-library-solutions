"""
Listing 2.53

Combining several sorted sequences into one new sequence is easy for
small data sets
    list(sorted(itertoool.chain(*data)))

For larger data sets, this technique can use a considerable amount of
memory. Instead of sorting the entire combined sequence, merge()
uses a heap to generate a new sequence one item at a time, determining
the next item using a fixed amount of memory

Because the implementation of merge uses a heap, it consumes memory based
on the number of sequences being merged, rather than the number of
items in those sequences
"""
import heapq
import random


def main():
    random.seed(2016)

    data = []
    for i in range(4):
        new_data = list(random.sample(range(1, 101), 5))
        new_data.sort()
        data.append(new_data)

    for i, d in enumerate(data):
        print(f"{i}: {d}")

    print("\nMerged:")
    for i in heapq.merge(*data):
        print(i, end=" ")
    print()


if __name__ == "__main__":
    main()
