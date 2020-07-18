"""
Listing 3.69

Sometimes when building complex contexts, it is useful to be able to
abort an operation if the context cannot be completely constructed,
but to delay the cleanup of all resources until a later time if they can
all be set up properly.

pop_all clears all of the context managers and callbacks from the stack
on which it is called, and returns a new stack prepopulated with those
same context managers and callbacks. The close() method of the new
stack can be invoked later, after the original stack is gone, to clean
up the resources
"""
import contextlib
from contextlib_context_managers import *


def variable_stack(contexts):
    with contextlib.ExitStack() as stack:
        for c in contexts:
            stack.enter_context(c)
        # Return the close() method of a new stack as a clean
        # up function
        return stack.pop_all().close
    # Explicitly return None, indicating that the ExitStack could
    # not be initialized cleanly but that cleanup has
    # already occurred
    return None


def main():
    print("No errors:")
    cleaner = variable_stack([
        HandleError(1),
        HandleError(2)
    ])
    cleaner()

    print("\nHandled error building context manager stack:")
    try:
        cleaner = variable_stack([
            HandleError(1),
            ErrorOnEnter(2)
        ])
    except RuntimeError as err:
        print(f"caught error {err}")
    else:
        if cleaner is not None:
            cleaner()
        else:
            print("no cleaner returned")

    print("\nUnhandled error buildings context manager stack:")
    try:
        cleaner = variable_stack([
            PassError(1),
            ErrorOnEnter(2)
        ])
    except RuntimeError as err:
        print(f"caught error {err}")
    else:
        if cleaner is not None:
            cleaner()
        else:
            print("no cleaner returned")


if __name__ == "__main__":
    main()
