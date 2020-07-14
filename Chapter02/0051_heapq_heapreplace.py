"""
Listing 2.50

To remove existing elements and replace them with new values in a
single operation, use heapreplace()

Replacing elements in place makes it possible to maintain a fixed-size
heap, such as a queue of jobs ordered by priority
"""
import heapq
from heapq_showtree import show_tree
from heapq_heapdata import data


def main():
    heapq.heapify(data)
    print("start ")
    show_tree(data)

    for n in [0, 13]:
        smallest = heapq.heapreplace(data, n)
        print(f"replace {smallest:>2} with {n:>2}:")
        show_tree(data)


if __name__ == "__main__":
    main()
