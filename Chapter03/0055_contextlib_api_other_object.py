"""
Listing 3.55

The __enter__() method can return any object to be associated with a name
specified in the as clause of the with statement.

The value associated with the variable c is the object returned by
__enter__(), which is not necessarily the Context instance created
in the with statement
"""


class WithinContext:

    def __init__(self, context):
        print(f"WithinContext.__init__({context})")

    def do_something(self):
        print(f"WithinContext.do_something()")

    def __del__(self):
        print("WithinContext.__del__")


class Context:

    def __init__(self):
        print(f"Context.__init__()")

    def __enter__(self):
        print("Context.__enter__()")
        return WithinContext(self)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Context.__exit__()")


def main():
    with Context() as c:
        c.do_something()


if __name__ == "__main__":
    main()
