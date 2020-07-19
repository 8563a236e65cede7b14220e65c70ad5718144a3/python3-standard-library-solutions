"""
Listing 4.18

Future and past dates can be calculated using basic arithmetic on two
datetime objects, or by combining a datetime with a timedelta,
Subtracting dates produces a timedelta, and a timedelta can be also
added or subtracted from a date to produce another date. The internal
values for a timedelta are stored in days, seconds and microseconds
"""
import datetime


def main():
    print("microseconds:", datetime.timedelta(microseconds=1))
    print("milliseconds:", datetime.timedelta(milliseconds=1))
    print("seconds     :", datetime.timedelta(seconds=1))
    print("minutes     :", datetime.timedelta(minutes=1))
    print("hours       :", datetime.timedelta(hours=1))
    print("days        :", datetime.timedelta(days=1))
    print("weeks       :", datetime.timedelta(weeks=1))


if __name__ == "__main__":
    main()
