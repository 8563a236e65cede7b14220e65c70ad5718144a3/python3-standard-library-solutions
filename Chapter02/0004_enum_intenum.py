"""
Listing 2.4

Use the IntEnum class for enumerations where the members need to behave
more like numbers e.g. to support comparisons
"""
import enum


class BugStatus(enum.IntEnum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1


def main():
    print("Ordered by value:")
    print("\n".join("  " + s.name for s in sorted(BugStatus)))


if __name__ == "__main__":
    main()
