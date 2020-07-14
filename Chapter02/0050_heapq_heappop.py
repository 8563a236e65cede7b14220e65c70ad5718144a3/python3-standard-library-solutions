"""
Listing 2.50

Once the heap is organized correctly, use heappop() to remove the element
with the lowest value
"""
import heapq
from heapq_showtree import show_tree
from heapq_heapdata import data


def main():
    print("random    :", data)
    heapq.heapify(data)
    print("heapified :")
    show_tree(data)
    print

    for i in range(2):
        smallest = heapq.heappop(data)
        print(f"pop    {smallest:>3}:")
        show_tree(data)


if __name__ == "__main__":
    main()
