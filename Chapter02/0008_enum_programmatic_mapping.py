"""
Listing 2.8

For more control over the values associated with members, the names string
can be replaced with a sequence of two-part tuples or a dictionary
mapping names to values.
"""
import enum


def main():
    BugStatus = enum.Enum(
        value="BugStatus",
        names=[
            ("new", 7),
            ("incomplete", 6),
            ("invalid", 5),
            ("wont_fix", 4),
            ("in_progress", 3),
            ("fix_committed", 2),
            ("fix_released", 1)
        ]
    )

    print("All members:")
    for status in BugStatus:
        print(f"{status.name:15} = {status.value}")


if __name__ == "__main__":
    main()
