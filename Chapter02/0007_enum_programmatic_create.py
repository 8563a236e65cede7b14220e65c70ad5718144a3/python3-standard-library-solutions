"""
Listing 2.7

In some cases, it is more convenient to create enumerations programmatically,
rather than hard-coding them in a class definition. For those situations,
Enum also supports passing the member names and values to the class
constructor.

The value argument is the name of the enumeration, which is used to
build the representation of members. The names argument lists the
members of the enumeration. When a single string is passed, it is
split on whitespace and commas, and the resulting tokens are used as
names for the members, which are automatically assigned values
starting with 1
"""
import enum


def main():
    BugStatus = enum.Enum(
        value="BugStatus",
        names=("fix_released fix_committed in_progress "
               "wont_fix invalid incomplete new")
    )

    print(f"Member: {BugStatus.new}")
    print("\nAll members:")
    for status in BugStatus:
        print(f"{status.name:15} = {status.value}")


if __name__ == "__main__":
    main()
