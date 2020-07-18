"""
Listing 3.57

The class ContextDecorator adds support to regular context manager classes
so that they can be used as function decorators as well as context
managers

One difference that arises when using the context manager as a decorator
is that the value returned by __enter__() is not available inside the
function being decorated, unlike the case when with and as are
used. Arguments passed to the decorator function are available in the
usual way
"""
import contextlib


class Context(contextlib.ContextDecorator):

    def __init__(self, how_used):
        self.how_used = how_used
        print(f"__init__({how_used})")

    def __enter__(self):
        print(f"__enter__({self.how_used})")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"__exit__({self.how_used})")


@Context("as decorator")
def func(message):
    print(message)


def main():
    print()
    with Context("as context manager"):
        print("Doing work in the context")

    print()
    func("Doing work in the wrapped function")


if __name__ == "__main__":
    main()
