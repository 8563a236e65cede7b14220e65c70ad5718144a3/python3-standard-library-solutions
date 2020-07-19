"""
Listing 4.2

One of the core functions of the time module is time(), which returns the
number of seconds since the start of the "epoch" as a floating-point
value

The epoch is the start of measurement for time, which for Unix systems is
0:00 on January 1 1970. Although the value is always a float, the
actual precision is platform-dependent
"""
import time


def main():
    print("The time is:", time.time())


if __name__ == "__main__":
    main()
