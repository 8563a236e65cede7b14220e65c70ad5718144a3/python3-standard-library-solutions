"""
Listing 4.22

Both date and time values can be compared using the standard comparison
operators to determine which is earlier or later
"""
import datetime
import time


def main():
    print("Times:")
    t1 = datetime.time(12, 55, 0)
    print("  t1:", t1)
    t2 = datetime.time(13, 5, 0)
    print("  t2:", t2)
    print("  t1 < t2:", t1 < t2)

    print()
    print("Dates:")
    d1 = datetime.date.today()
    print("  d1:", d1)
    d2 = datetime.date.today() + datetime.timedelta(days=1)
    print("  d2:", d2)
    print("  d1 > d2:", d1 > d2)


if __name__ == "__main__":
    main()
