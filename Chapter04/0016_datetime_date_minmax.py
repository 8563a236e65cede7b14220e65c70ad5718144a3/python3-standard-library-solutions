"""
Listing 4.16

As is true with the time class, the range of date values supported can
be determined using the min and max attributes
"""
import datetime


def main():
    print("Earliest  :", datetime.date.min)
    print("Latest    :", datetime.date.max)
    print("Resolution:", datetime.date.resolution)


if __name__ == "__main__":
    main()
