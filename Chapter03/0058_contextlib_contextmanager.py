"""
Listing 3.58

Creating context managers the traditional way - that is, by writing a
class with __enter__() and __exit__() methods - is not difficult.
Nevertheless, writing everything out fully creates extra overhead when
only a trivial bit of context is being managed. In those sorts of
situations, the best approach is to use the contextmanager() decorator to
convert a generator function into a context manager

The generator should initialize the context, invoke yield exactly one
time, and then clean up the context. THe value yielded, if any, is bound
to the variable in the as clause of the with statement. Exceptions
from within the with block are raised again inside the generator, so
they can be handled there
"""
import contextlib


@contextlib.contextmanager
def make_context():
    print("  entering")
    try:
        yield {}
    except RuntimeError as err:
        print("  ERROR:", err)
    finally:
        print("  exiting")


def main():
    print("Normal:")
    with make_context() as value:
        print("  inside with statement: ", value)

    print("\nHandled error:")
    with make_context() as value:
        raise RuntimeError("showing example of handling an error")

    print("\nUnhandled error:")
    with make_context() as value:
        raise ValueError("this exception is not handled")


if __name__ == "__main__":
    main()
