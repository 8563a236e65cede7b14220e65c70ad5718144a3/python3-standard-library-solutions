"""
Listing 2.54

The bisect module implements an algorithm for inserting elements
into a list while maintaining the list in sorted order

insort() is used to insert items into a list in sorted order

For long lists, significant time and memory savings can be achieved
using an insertion sort algorithm such as this, especially when
the operation to compare two members of the list requires expensive
computation
"""
import bisect


def main():
    values = [14, 85, 77, 26, 50, 45, 66, 79, 10, 3, 84, 77, 1]

    print("New  Pos Contents")
    print("___  ___ ________")

    l = []

    for i in values:
        position = bisect.bisect(l, i)
        bisect.insort(l, i)
        print(f"{i:3}  {position:3} {l}")


if __name__ == "__main__":
    main()
