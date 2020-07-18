"""
Listing 3.41

To compute the product of a sequence with itself, specify how many
times the input should be repeated
"""
import itertools


def show(iterable):
    for i, item in enumerate(iterable, 1):
        print(item, end=" ")
        if (i % 3) == 0:
            print()
    print()


def main():
    print("Repeat 2:\n")
    show(list(itertools.product(range(3), repeat=2)))

    print("Repeat 3:\n")
    show(list(itertools.product(range(3), repeat=3)))


if __name__ == "__main__":
    main()
