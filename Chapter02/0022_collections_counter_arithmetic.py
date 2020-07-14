"""
Listing 2.22

Counter instances support arithmetic and set operations for aggregating
results. This example shows the standard operators for creating new
Counter instances, bu the in-place operators +=, -=, &= and |=
are also supported

Each time a new Counter is produced through an operation, any items
with zero or negative counts are discarded.
"""
import collections


def main():
    c1 = collections.Counter(["a", "b", "c", "a", "b", "b"])
    c2 = collections.Counter("alphabet")

    print("C1:", c1)
    print("C2:", c2)

    print("\nCombined counts:")
    print(c1 + c2)

    print("\nSubtraction:")
    print(c1 - c2)

    print("\nIntersection (taking positive minimums):")
    print(c1 & c2)

    print("\nUnion (taking maximums):")
    print(c1 | c2)


if __name__ == "__main__":
    main()
