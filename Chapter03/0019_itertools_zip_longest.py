"""
Listing 3.18

To process all of the inputs, even if the iterators produce different
numbers of values, use zip_longest()
"""
import itertools


def main():
    r1 = range(3)
    r2 = range(2)

    print("zip stops early:")
    print(list(zip(r1, r2)))

    r1 = range(3)
    r2 = range(2)

    print("\nzip_longest processes all of the values:")
    print(list(itertools.zip_longest(r1, r2)))


if __name__ == "__main__":
    main()
