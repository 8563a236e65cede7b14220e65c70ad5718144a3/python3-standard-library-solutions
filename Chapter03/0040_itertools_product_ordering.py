"""
Listing 3.40

To change the order of the cards, change the order of the arguments
to product()
"""
import itertools


def main():
    FACE_CARDS = ("J", "Q", "K", "A")
    SUITS = ("H", "D", "C", "S")

    DECK = list(
        itertools.product(
            SUITS,
            itertools.chain(range(2, 11), FACE_CARDS)
        )
    )

    for card in DECK:
        print(f"{card[1]:>2}{card[0]}", end=" ")
        if card[1] == FACE_CARDS[-1]:
            print()


if __name__ == "__main__":
    main()
