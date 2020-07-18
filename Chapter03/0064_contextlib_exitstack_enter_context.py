"""
Listing 3.64

Most context managers operate on one object at at time, such as
a single file or database handle. In these cases, the object is known
in advance and the code using the context manager can be build around that
one object.

In other cases, a program may need to create an unknown number of objects
within a context, with all of those objects expected to be cleaned
up when control flow exits the context. ExitStack was created to handle
these more dynamic cases.

An ExitStack instance maintains a stack data structure of cleanup
callbacks. The callbacks are populated explicitly within the context, and
any registered callbacks are called in the reverse order when control
flow exits the context. The result is similar to having multiple
nested with statement, except they are established dynamically

Several approaches may be used to populate the ExitStack. This example
uses enter_context() to add a new context manager to the stack

enter_context() first calls __enter__() on the context manager. It then
registers its __exit__() method as a callback to be invoked as the
stack is undone
"""
import contextlib


@contextlib.contextmanager
def make_context(i):
    print(f"{i} entering")
    yield {}
    print(f"{i} exiting")


def variable_stack(n, msg):
    with contextlib.ExitStack() as stack:
        for i in range(n):
            stack.enter_context(make_context(i))
        print(msg)


def main():
    variable_stack(2, "inside context")


if __name__ == "__main__":
    main()
