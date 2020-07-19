"""
Listing 4.17

Another way to create new date instances is to use the replace() method
of an existing date
"""
import datetime


def main():
    d1 = datetime.date(2008, 3, 29)
    print("d1:", d1.ctime())

    d2 = d1.replace(year=2009)
    print("d2:", d2.ctime())


if __name__ == "__main__":
    main()
