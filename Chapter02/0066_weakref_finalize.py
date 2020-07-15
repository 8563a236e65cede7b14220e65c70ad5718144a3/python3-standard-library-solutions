"""
Listing 2.66

For more robust management of resources when weak references are cleaned
up, use finalize to associate callbacks with objects. A finalize instance
is retained until the attached object is deleted, even if the application
does not retain a reference to the finalizer

The arguments to finalize are the object to track, a callable to invoke
when the object is garbage collected, and any positional or named
arguments to pass to the callable
"""
import weakref


class ExpensiveObject:

    def __del__(self):
        print(f"(Deleting {self})")


def on_finalize(*args):
    print(f"on_finalize({args!r})")


def main():
    obj = ExpensiveObject()
    weakref.finalize(obj, on_finalize, "extra argument")

    del obj


if __name__ == "__main__":
    main()
