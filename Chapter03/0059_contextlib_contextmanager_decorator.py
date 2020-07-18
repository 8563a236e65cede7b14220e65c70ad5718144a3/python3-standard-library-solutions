"""
Listing 3.59

The context manager returned by contextmanager() is derived from
ContextDecorator so it also works as a function decorator

When the context manager is used as a decorator, the value yielded by
the generator is not available inside the function being
decorated. Arguments passed to the decorated function are still available,
as demonstrated by throw_error()
"""
import contextlib


@contextlib.contextmanager
def make_context():
    print("  entering")
    try:
        # Yield control, but not a value, because any value
        # yielded is not available when the context manager
        # is used as a decorator
        yield
    except RuntimeError as err:
        print("  ERROR:", err)
    finally:
        print("  exiting")


@make_context()
def normal():
    print("  inside with statement")


@make_context()
def throw_error(err):
    raise err


def main():
    print("Normal:")
    normal()

    print("\nHandled error:")
    throw_error(RuntimeError("showing example of handling an error"))

    print("\nUnhandled error")
    throw_error(ValueError("this exception is not handled"))