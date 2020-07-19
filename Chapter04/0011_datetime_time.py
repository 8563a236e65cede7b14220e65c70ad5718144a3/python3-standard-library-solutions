"""
Listing 4.11

datetime contains functions and classes for date and time parsing,
formatting and arithmetic.

Time values are represented with the time class. A time instance has
attributes for hour, minute, second and microsecond; it can also include
time zone information
"""
import datetime


def main():
    t = datetime.time(1, 2, 3)
    print(t)
    print("hour       :", t.hour)
    print("minute     :", t.minute)
    print("second     :", t.second)
    print("microsecond:", t.microsecond)
    print("tzinfo     :", t.tzinfo)


if __name__ == "__main__":
    main()
