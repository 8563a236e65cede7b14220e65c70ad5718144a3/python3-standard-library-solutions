"""
Listing 3.68

Callbacks offer a convenient way to clearly define cleanup logic without
the overhead of creating a new context manager class. To improve code
readability, that logic can be encapsulated in an inline function, and
callback() can be used as a decorator

There is no way to specify the arguments for functions registered using
the decorator form of callback(). However, if the cleanup callback is
defined inline, scope rules give it access to variables defined in the
calling code
"""
import contextlib


def main():
    with contextlib.ExitStack() as stack:

        @stack.callback
        def inline_cleanup():
            print("inline_cleanup()")
            print(f"local_resource = {local_resource!r}")

        local_resource = "resource created in context"
        print("within the context")


if __name__ == "__main__":
    main()
