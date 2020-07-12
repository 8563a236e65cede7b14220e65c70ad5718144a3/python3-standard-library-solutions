"""
Listing 1.7

The Formatter class implements the same layout specification language
as the format() method of str. Its features include
    type coercion
    alignment
    attribute and field references
    named and positional template arguments
    type-specific formatting options

Most of the time format() is more convenient, but Formatter is provided
as a way to build subclasses, for cases where variations are needed

The string module includes a number of constants related to ASCII
and numerical character sets
"""
import inspect
import string


def is_str(value):
    return isinstance(value, str)


def main():
    for name, value in inspect.getmembers(string, is_str):
        if name.startswith("_"):
            continue
        print(f"{name} = {value}")


if __name__ == "__main__":
    main()
