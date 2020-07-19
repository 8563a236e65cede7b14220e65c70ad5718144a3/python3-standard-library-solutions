"""
Listing 4.24

Just like date, datetime provides convenient class methods for creating
new instances. It also includes fromordinal() and fromtimestamp()

combine() creates datetime instances from one date and one time instance
"""
import datetime


def main():
    t = datetime.time(1, 2, 3)
    print("t :", t)

    d = datetime.date.today()
    print("d :", d)

    dt = datetime.datetime.combine(d, t)
    print("dt:", dt)


if __name__ == "__main__":
    main()
