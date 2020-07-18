"""
Listing 3.17

If the iterables to be combined are not all know in advance, or if they
need to be evaluated lazily, chain.from_iterable() can be used to
construct the chain instead
"""
import itertools


def make_iterables_to_chain():
    yield [1, 2, 3]
    yield ["a", "b", "c"]


def main():
    for i in itertools.chain.from_iterable(make_iterables_to_chain()):
        print(i, end=" ")
    print()


if __name__ == "__main__":
    main()
