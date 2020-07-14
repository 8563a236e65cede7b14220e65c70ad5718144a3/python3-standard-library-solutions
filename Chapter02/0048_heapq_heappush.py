"""
Listing 2.48

There are two basic ways to create a heap: heappush() and heapify()
"""
import heapq
from heapq_showtree import show_tree
from heapq_heapdata import data


def main():
    heap = []
    print("random :", data)
    print()

    for n in data:
        print(f"add {n:3}")
        heapq.heappush(heap, n)
        show_tree(heap)


if __name__ == "__main__":
    main()
