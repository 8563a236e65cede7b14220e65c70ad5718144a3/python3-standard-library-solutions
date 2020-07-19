"""
Listing 4.4

Because time() looks at the system clock, and because the system clock can
be changed by the user or system services for synchronizing clocks across
multiple computers, calling time() repeatedly may produce values that go
forward and backward. This can result in unexpected behaviour when trying
to measure durations or otherwise use those times for computation. To
avoid those situations, use monotonic(), which always returns values
that go forward.

The start point for the monotonic clock is not defined, so return values
are useful only for doing calculations with other clock values. In this
example, the duration of the sleep is measured using monotonic()
"""
import time


def main():
    start = time.monotonic()
    time.sleep(0.1)
    end = time.monotonic()
    print(f"start : {start:>9.2f}")
    print(f"end   : {end:>9.2f}")
    print(f"span  : {(end-start):>9.2f}")


if __name__ == "__main__":
    main()
