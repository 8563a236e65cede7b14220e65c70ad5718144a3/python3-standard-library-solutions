"""
Listing 3.60

The file class supports the context manager API directly, but some other
objects that represent open handles do not. The example given in the
standard library documentation for contextlib is the object returned from
urllib.urlopen(). Some other legacy classes use a close() method but do
not support the context manager API. To ensure that a handle is closed,
use closing() to create a context manager for it

The handle is closed whether there is an error in the with block or
not
"""
import contextlib


class Door:

    def __init__(self):
        print("  __init__()")
        self.status = "open"

    def close(self):
        print("  close()")
        self.status = "closed"


def main():
    print("Normal Example:")
    with contextlib.closing(Door()) as door:
        print(f"  inside with statement: {door.status}")
    print(f"  outside with statement: {door.status}")

    print("\nError handling example:")
    try:
        with contextlib.closing(Door()) as door:
            print("  raising from inside with statement")
            raise RuntimeError("error message")
    except Exception as err:
        print("  Had an error:", err)


if __name__ == "__main__":
    main()
