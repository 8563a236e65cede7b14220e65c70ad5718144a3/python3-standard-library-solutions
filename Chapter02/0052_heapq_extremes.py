"""
Listing 2.52

heapq also includes two functions to examine an iterable and find a range
of the largest or smallest values it contains

Using nlargest() and nsmallest() is efficient only for relatively small
values of n > 1, but can still come in handy in a few cases
"""
import heapq
from heapq_heapdata import data


def main():
    print("all       :", data)
    print("3 largest :", heapq.nlargest(3, data))
    print("from sort :", list(reversed(sorted(data)[-3:])))
    print("3 smallest:", heapq.nsmallest(3, data))
    print("from sort :", sorted(data)[:3])


if __name__ == "__main__":
    main()
