"""
Listing 4.21

A timedelta object also supports arithmetic with integers, floats and
other timedelta instances
"""
import datetime


def main():
    one_day = datetime.timedelta(days=1)
    print("1 day    :", one_day)
    print("5 days   :", one_day * 5)
    print("1.5 days :", one_day * 1.5)
    print("1/4 day  :", one_day / 4)

    # Assume an hour for lunch
    work_day = datetime.timedelta(hours=7)
    meeting_length = datetime.timedelta(hours=1)
    print("meetings per day :", work_day / meeting_length)


if __name__ == "__main__":
    main()
