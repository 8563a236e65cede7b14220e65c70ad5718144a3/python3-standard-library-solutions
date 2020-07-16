"""
Listing 3.11

The optional initializer argument is placed at the front of the sequence
and processed along with other items. This can be used to update a
previously computed value with new inputs
"""
import functools


def do_reduce(a, b):
    print(f"do_reduce({a}, {b})")
    return a + b


def main():
    data = range(1, 5)
    print(data)
    result = functools.reduce(do_reduce, data, 99)
    print(f"result: {result}")


if __name__ == "__main__":
    main()
