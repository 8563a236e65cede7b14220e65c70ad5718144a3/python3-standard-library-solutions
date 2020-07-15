"""
Listing 2.67

The finalize instance has a writable property atexist to control whether
the callback is invoked as a program is exiting, if it hasn't already
been called.
"""
import sys
import weakref


class ExpensiveObject:

    def __del__(self):
        print(f"(Deleting {self})")


def on_finalize(*args):
    print(f"on_finalize({args!r})")


def main():
    obj = ExpensiveObject()
    f = weakref.finalize(obj, on_finalize, "extra argument")
    f.atexit = bool(int(sys.argv[1]))

    del obj


if __name__ == "__main__":
    main()
