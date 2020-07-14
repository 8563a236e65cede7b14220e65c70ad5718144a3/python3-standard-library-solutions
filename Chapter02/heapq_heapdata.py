"""
Listing 2.46

A heap is a tree-like data structure in which the child nodes have a sort-
order relationship with the parents. Binary heaps can be represented using
an array or list organised so that the children of element N are at
positions 2*N + 1 and 2*N + 2 (for zero-based indexes). This
layout makes it possible to rearrange heaps in place, so it is not
necessary to reallocate as much memory when adding or removing
items

A max-heap ensures that the parent is larger than or equal to both of
its children. A min-heap requires that the parent be less than or equal
to its children. Python's heapq module implement a min-heap
"""
data = [19, 9, 4, 10, 11]
