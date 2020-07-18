"""
Listing 3.44

While combinations() does not repeat individual input elements,
sometimes it is useful to consider combinations that do include repeated
elements. For those cases, use combinations_with_replacements().
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
    print("Unique pairs:\n")
    show(itertools.combinations_with_replacement("abcd", r=2))


if __name__ == "__main__":
    main()
