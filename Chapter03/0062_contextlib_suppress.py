"""
Listing 3.62

The try:except form can be replaced with contextlib.suppress() to more
explicitly suppress a class of exceptions happening anywhere within
the with block
"""
import contextlib


class NonFatalError(Exception):
    pass


def non_idempotent_operation():
    raise NonFatalError(
        "This operation failed because of existing state"
    )


def main():
    with contextlib.suppress(NonFatalError):
        print("trying non-idempotent operation")
        non_idempotent_operation()
        print("suceeded!")

    print("done")


if __name__ == "__main__":
    main()
