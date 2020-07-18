"""
Listing 3.54

A context manager is enabled by the with statement, and the API involves
two methods. The __enter__() method is run when the execution flow
enters the code block inside the with statement. It returns an object
to be used within the context. When execution flow leaves the with block,
the __exit__() method of the context manager is called to clean up any
resources that were used

Combining a context manager and the with statement is a more compact
way of writing a try:finally block, since the context manager's
__exit__() method is always called, even if an exception is raised
"""


class Context:

    def __init__(self):
        print("__init__()")

    def __enter__(self):
        print("__enter__()")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__()")


def main():
    with Context():
        print("Doing work in the context")


if __name__ == "__main__":
    main()
