"""
Listing 4.8

Storing times as elapsed seconds is useful in some situations, but
sometimes a program needs to have access to the individual fields of a
date (e.g year, month). THe time module defines struct_time for holding
date and time values, with the components being broken out so they
are easy to access. Several functions work with struct_time values instead
of floats.

The gmtime() function returns the current time in UTC. localtime()
returns the current time with the current time zone applied. mktime()
takes a struct_time and converts it to the floating-point representation
"""
import time


def show_struct(s):
    print("  tm_year :", s.tm_year)
    print("  tm_mon  :", s.tm_mon)
    print("  tm_mday :", s.tm_mday)
    print("  tm_hour :", s.tm_hour)
    print("  tm_min  :", s.tm_min)
    print("  tm_sec  :", s.tm_sec)
    print("  tm_wday :", s.tm_wday)
    print("  tm_yday :", s.tm_yday)
    print("  tm_isdst:", s.tm_isdst)


def main():
    print("gmtime:")
    show_struct(time.gmtime())
    print("\nlocaltime:")
    show_struct(time.localtime())
    print("\nmktime:", time.mktime(time.localtime()))


if __name__ == "__main__":
    main()
