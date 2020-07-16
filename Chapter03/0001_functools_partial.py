"""
Listing 3.1

The functools module provides tools for adapting or extending functions
and other callable objects, without completely rewriting them

The primary tool supplied by the functools module is the class partial
which can be used to "wrap" a callable object with default arguments.
The resulting object is itself callable and can be treated as though it
is the original function. It takes all of the same arguments as the
original, and can be invoked with extra positional or named arguments as
well. A partial can be used instead of a lambda to provide default
arguments to a function, while leaving some arguments unspecified.
"""
import functools


def myfunc(a, b=2):
    """Docstring for myfunc()."""
    print("  called myfunc with:", (a, b))


def show_details(name, f, is_partial=False):
    """Show details of a callable object"""
    print(f"{name}")
    print(f"  object:", f)
    if not is_partial:
        print("  __name__:", f.__name__)
    if is_partial:
        print("  func:", f.func)
        print("  args:", f.args)
        print("  keywords:", f.keywords)


def main():
    show_details("myfunc", myfunc)
    myfunc("a", 3)
    print()

    # Set a different value for "b", but require
    # the caller to provide "a"
    p1 = functools.partial(myfunc, b=4)
    show_details("partial with named default", p1, True)
    p1("passing a")
    p1("override b", b=5)
    print()

    # Set a different value for both "a" "b".
    p2 = functools.partial(myfunc, "default a", b=99)
    show_details("partial with defaults", p2, True)
    p2()
    p2(b="override b")
    print()

    print("Insufficient arguments:")
    p1()  # TypeError


if __name__ == "__main__":
    main()
