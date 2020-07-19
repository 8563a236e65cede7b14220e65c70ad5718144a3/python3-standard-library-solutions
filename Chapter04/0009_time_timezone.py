"""
Listing 4.9

The functions for determining the current time depend on having the time
zone set, either by the program or by using a default time zone set for
the system. Changing the time zone does not change the actual time, just
the way it is represented

To change the time zone, set the environment variable TZ and then call
tzset(). The time zone can be specified with a great deal of detail,
right down to the start and stop times for daylight savings time. It is
usually easier to use the time zone name, and let the underlying
libraries derive the other information.
"""
import time
import os


def show_zone_info():
    print("  TZ    :", os.environ.get("TZ", "(not set)"))
    print("  tzname:", time.tzname)
    print(f"  Zone  : {time.timezone} ({time.timezone / 3600})")
    print("  DST   :", time.daylight)
    print("  Time  :", time.ctime())


def main():
    print("Default :")
    show_zone_info()

    ZONES = [
        "GMT",
        "Europe/Amsterdam"
    ]

    for zone in ZONES:
        os.environ["TZ"] = zone
        time.tzset()
        print(zone, ":")
        show_zone_info()


if __name__ == "__main__":
    main()
