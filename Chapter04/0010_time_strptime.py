"""
Listing 4.10

The functions strptime() and strftime() convert between struct_time and
string representations of time values. The long list of formatting
directives supported by both functions enables input and output in different
styles.
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
    now = time.ctime(1483391847.433716)
    print("Now:", now)

    parsed = time.strptime(now)
    print("\nParsed:")
    show_struct(parsed)

    print("\nFormatted:",
          time.strftime("%a %b %d %H:%M:%S %Y", parsed))


if __name__ == "__main__":
    main()
