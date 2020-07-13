"""
Listing 2.3

Because enumeration members are not ordered, they only support comparison
by identity and equality
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
    actual_state = BugStatus.wont_fix
    desired_state = BugStatus.fix_released

    print("Equality:",
          actual_state == desired_state,
          actual_state == BugStatus.wont_fix
          )

    print("Identity:",
          actual_state is desired_state,
          actual_state is BugStatus.wont_fix
          )

    try:
        print("\n".join(" " + s.name for s in sorted(BugStatus)))
    except TypeError as err:
        print(f"  Cannot sort(): {err}")


if __name__ == "__main__":
    main()
