"""
Listing 3.39

Nested for loops that iterate over multiple sequences can often be
replaced with product(), which produces a single iterable whose values
are the Cartesian product of the set of input values

The values produced by product() are tuples with members taken from
each of the iterables passed in as arguments in the order they are
passed. The frist tuple returned includes the first value from each
iterable. The last iterable passed to product() is processed first,
followed by next-to-last and so pn. The result is that the return
values are in order based on the first iterable, then the next iterable
and so on.
"""
import itertools


def main():
    FACE_CARDS = ("J", "Q", "K", "A")
    SUITS = ("H", "D", "C", "S")

    DECK = list(
        itertools.product(
            itertools.chain(range(2, 11), FACE_CARDS),
            SUITS
        )
    )

    for card in DECK:
        print(f"{card[0]:>2}{card[1]}", end=" ")
        if card[1] == SUITS[-1]:
            print()


if __name__ == "__main__":
    main()
