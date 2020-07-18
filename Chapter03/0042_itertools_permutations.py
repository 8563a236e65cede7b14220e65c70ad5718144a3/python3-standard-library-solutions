"""
Listing 3.42

The permutations() function produces items from the input iterable
combined in the possible permutations of the given length. It defaults
to producing the full set of all permutations

Use the r argument to limit the length and number of the individual
permuations returned
"""
import itertools


def show(iterable):
    first = None
    for i, item in enumerate(iterable, 1):
        if first != item[0]:
            if first is not None:
                print()
            first = item[0]
        print("".join(item), end=" ")
    print()


def main():
    print("All permutations:\n")
    show(itertools.permutations("abcd"))

    print("\nPairs:\n")
    show(itertools.permutations("abcd", r=2))


if __name__ == "__main__":
    main()
