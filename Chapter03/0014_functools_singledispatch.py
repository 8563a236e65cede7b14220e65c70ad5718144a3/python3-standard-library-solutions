"""
Listing 3.14

In a dynamically typed language like Python, there is often a need to
perform slightly different operations based on the type of an argument,
especially when dealing with the difference between a list of items and
a single item.

It is simple enough to check the type of an argument directly, but in
cases where the behavioural difference can be isolated into separate
functions, functools provides the singledispatch() decorator to
register a set of generic functions for automatic switching based on
the type of the first argument to a function

The register() attribute of the new function serves as another decorator
for registering alternative implementations. The first function wrapped
with singledispatch() is the default implementation if no other
type-specific function is found, as with the float case in this example.
"""
import functools


@functools.singledispatch
def myfunc(arg):
    print(f"default myfunc({arg!r})")


@myfunc.register(int)
def myfunc_int(arg):
    print(f"myfunc_int({arg})")


@myfunc.register(list)
def myfunc_list(arg):
    print("myfunc_list()")
    for item in arg:
        print(f"  {item}")


def main():
    myfunc("string argument")
    myfunc(1)
    myfunc(2.3)
    myfunc(["a", "b", "c"])


if __name__ == "__main__":
    main()
