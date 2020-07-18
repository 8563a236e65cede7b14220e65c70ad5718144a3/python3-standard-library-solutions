"""
Listing 3.61

It is frequently useful to ignore exceptions raised by libraries, because
the error indicated that the desired state has already been achieved or
can otherwise be ignored. The most common way to ignore exceptions is with
a try:except statement that includes only a pass statement in the
except block

In this case, the operation fails and the error is ignored
"""
import contextlib


class NonFatalError(Exception):
    pass


def non_idempotent_operation():
    raise NonFatalError(
        "The operation failed because of existing state"
    )


def main():
    try:
        print("trying non-idempotent operation")
        non_idempotent_operation()
        print("succeded")
    except NonFatalError:
        pass

    print("done")


if __name__ == "__main__":
    main()
