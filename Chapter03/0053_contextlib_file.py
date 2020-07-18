"""
Listing 3.53

The contextlib module contains utilities for working with context managers
and the with statement

A context manager is responsible for a resource within a code block,
possibly creating it when the block is entered and then cleaning it up
after the block is exited.
"""


def main():
    with open("/tmp/pymotw.txt", "wt") as f:
        f.write("contents go here")
    # File is automatically closed


if __name__ == "__main__":
    main()
