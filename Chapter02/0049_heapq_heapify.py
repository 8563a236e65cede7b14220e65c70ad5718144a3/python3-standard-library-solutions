"""
Listing 2.49

If the data is already in memory, it is more efficient to use heapify
to rearrange the items of the list in place

The result of building a list in heap order one item at a time is
the same as building an underordered list and then calling heapify()
"""
import heapq
from heapq_showtree import show_tree
from heapq_heapdata import data


def main():
    print("random    :", data)
    heapq.heapify(data)
    print("heapified :")
    show_tree(data)
    print(data)


if __name__ == "__main__":
    main()
