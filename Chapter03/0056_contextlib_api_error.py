"""
Listing 3.56

The __exit__() method receives arguments containing details of any
exception raised in the with block

If the context manager can handle the exception, __exit__() should
return a true value to indicate that the exception does not need to
be propagated. Returning a false value causes the exception to be
raised again after __exit__() returns
"""


class Context:

    def __init__(self, handle_error):
        print(f"__init__({handle_error})")
        self.handle_error = handle_error

    def __enter__(self):
        print("__enter__()")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__()")
        print("  exc_type =", exc_type)
        print("  exc_val =", exc_val)
        print("  exc_tb =", exc_tb)
        return self.handle_error


def main():
    with Context(True):
        raise RuntimeError("error message handled")

    print()

    with Context(False):
        raise RuntimeError("error message propagated")


if __name__ == "__main__":
    main()
