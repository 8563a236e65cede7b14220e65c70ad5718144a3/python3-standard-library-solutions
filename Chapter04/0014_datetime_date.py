"""
Listing 4.14

Calendar date values are represented with the date class. Instances have
attributes for year, month and day. It is easy to create a date
representing the current date using the today() class method
"""
import datetime


def main():
    today = datetime.date.today()
    print(today)
    print("ctime  :", today.ctime())
    tt = today.timetuple()
    members = [
        "tm_year",
        "tm_mon",
        "tm_mday",
        "tm_hour",
        "tm_min",
        "tm_sec",
        "tm_wday",
        "tm_yday",
        "tm_isdst"
    ]

    print("tuple  : ", end="")
    for i in members:
        if i == "tm_year":
            print(f"{i}  =", eval("tt." + i))
        else:
            print(f"         {i}  =", eval("tt." + i))

    print("ordinal:", today.toordinal())
    print("Year   :", today.year)
    print("Mon    :", today.month)
    print("Day    :", today.day)


if __name__ == "__main__":
    main()
