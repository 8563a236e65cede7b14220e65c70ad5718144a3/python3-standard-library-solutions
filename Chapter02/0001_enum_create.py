"""
Listing 2.1

Python includes several standard programming data structures, such as
list, tuple, dict and set, as part of its built-in types. The standard
library provides powerful and well tested versions of other structures

The enum module defines an enumeration type with iteration and comparison
capabilities. It can be used to create well-defined symbols for values,
instead of using literal integers or strings

A new enumeration is defined using the class syntax by subclassing
Enum and adding class attributes describing the values.
"""
import enum


class BugStatus(enum.Enum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1


def main():
    print(f"\nMember name: {BugStatus.wont_fix.name}")
    print(f"Member value: {BugStatus.wont_fix.value}")


if __name__ == "__main__":
    main()
