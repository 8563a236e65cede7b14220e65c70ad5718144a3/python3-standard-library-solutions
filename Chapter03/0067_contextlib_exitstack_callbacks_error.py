"""
Listing 3.67

The callbacks are invoked regardless of whether an error occurred, and
they are not given any information about whether an error occurred.
Their return value is ignored.

Because they do not have access to the error, callbacks are unable to
prevent exceptions from propagating through the rest of the stack of
context managers
"""
import contextlib


def callback(*args, **kwds):
    print(f"closing callback({args}, {kwds})")


def main():
    try:
        with contextlib.ExitStack() as stack:
            stack.callback(callback, "arg1", "arg2")
            stack.callback(callback, arg3="val3")
            raise RuntimeError("thrown error")
    except RuntimeError as err:
        print(f"ERROR: {err}")


if __name__ == "__main__":
    main()
