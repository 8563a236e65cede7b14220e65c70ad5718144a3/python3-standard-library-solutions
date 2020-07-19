"""
Listing 4.12

A time instance holds only values of time; it does not include a date
associated with the time

The min and max class attributes reflect the valid range of times in
a single day.
"""
import datetime


def main():
    print("Earliest  :", datetime.time.min)
    print("Latest    :", datetime.time.max)
    print("Resolution:", datetime.time.resolution)


if __name__ == "__main__":
    main()
