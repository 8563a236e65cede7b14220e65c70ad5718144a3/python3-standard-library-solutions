"""
Listing 4.15

There are also class methods for creating instances from POSIX timestamps
or integers representing date values from the Gregorian calendar,
where January 1 of the year 1 is designated as having the value 1 and
each subsequent day increments the value by 1
"""
import datetime
import time


def main():
    o = 733114
    print("o               :", o)
    print("fromordinal(o)  :", datetime.date.fromordinal(o))

    t = time.time()
    print("t               :", t)
    print("fromtimestamp(t):", datetime.date.fromtimestamp(t))


if __name__ == "__main__":
    main()
