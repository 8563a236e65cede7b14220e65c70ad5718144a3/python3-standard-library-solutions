"""
Listing 2.2

Iterating over the enum class produces the individual members of the
enumeration

The members are produced in the order they are declared in the class
definition. The names and values are not used to sort them in any
way
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
    for status in BugStatus:
        print(f"{status.name:15} = {status.value}")


if __name__ == "__main__":
    main()
