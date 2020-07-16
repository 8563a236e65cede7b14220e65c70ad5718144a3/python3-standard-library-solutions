"""
Listing 3.13

Sequences with a single item automatically reduce to that value when no
initializer is present. Empty lists generate an error, unless an
initializer is provided

Because the initializer argument serves as a default, but is also
combined with the new values if the input sequence is not empty, it is
important to consider carefully whether its use is appropriate. When it
does not make sense to combined with default with new values, it is
better to catch the TypeError rather than passing an initializer
"""
import functools


def do_reduce(a, b):
    print(f"do_reduce({a}, {b})")
    return a + b


def main():
    print("Single item in sequence:",
          functools.reduce(do_reduce, [1]))

    print("Single item in sequence with initializer:",
          functools.reduce(do_reduce, [1], 99))

    print("Empty sequence with initializer:",
          functools.reduce(do_reduce, [], 99))

    try:
        print("Empty sequence:", functools.reduce(do_reduce, []))
    except TypeError as err:
        print(f"ERROR: {err}")


if __name__ == "__main__":
    main()
