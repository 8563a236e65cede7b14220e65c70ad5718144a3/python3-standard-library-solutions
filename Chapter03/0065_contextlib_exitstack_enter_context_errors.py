"""
Listing 3.65

Context manager error handling
"""
import contextlib
from contextlib_context_managers import *


def variable_stack(contexts):
    with contextlib.ExitStack() as stack:
        for c in contexts:
            stack.enter_context(c)
    print("  outside of stack, any errors were handled")


def main():
    print("No errors:")
    variable_stack([
        HandleError(1),
        PassError(2)
    ])

    print("\nError at the end of the context stack:")
    variable_stack([
        HandleError(1),
        PassError(2),
        ErrorOnExit(3)
    ])

    print("\nError in the middle of the context stack:")
    variable_stack([
        HandleError(1),
        PassError(2),
        ErrorOnExit(3),
        HandleError(4)
    ])

    try:
        print("\nError ignored:")
        variable_stack([
            PassError(1),
            ErrorOnExit(2)
        ])
    except RuntimeError:
        print("error handled outside of context")


if __name__ == "__main__":
    main()
