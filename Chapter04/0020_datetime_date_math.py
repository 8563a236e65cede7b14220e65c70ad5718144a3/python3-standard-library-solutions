"""
Listing 4.20

Date math uses the standard arithmetic operators
"""
import datetime


def main():
    today = datetime.date.today()
    print("Today    :", today)

    one_day = datetime.timedelta(days=1)
    print("One day  :", one_day)

    yesterday = today - one_day
    print("Yesterday:", yesterday)

    tomorrow = today + one_day
    print("Tomorrow :", tomorrow)

    print()
    print("tomorrow - yesterday:", tomorrow - yesterday)
    print("yesterday - tomorrow", yesterday - tomorrow)


if __name__ == "__main__":
    main()
