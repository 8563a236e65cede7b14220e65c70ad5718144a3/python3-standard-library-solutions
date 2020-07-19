"""
Listing 4.23

Use the datetime class to hold values consisting of both date and time
components. As with date, several convenient class methods are available
for creating datetime instances from other common values
"""
import datetime


def main():
    print("Now    :", datetime.datetime.now())
    print("Today  :", datetime.datetime.today())
    print("UTC Now:", datetime.datetime.utcnow())

    FIELDS = [
        "year", "month", "day",
        "hour", "minute", "second",
        "microsecond"
    ]

    d = datetime.datetime.now()
    for attr in FIELDS:
        print(f"{attr:15}: {getattr(d, attr)}")


if __name__ == "__main__":
    main()
