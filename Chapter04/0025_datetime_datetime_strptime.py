"""
Listing 4.25

The default string representation of a datetime object uses the ISO-8601
format (YYYY-MM-DDTHH:MM:SS.mmmmmm). Alternative formats can be generated
using strftime()

Use datetime.strptime() to convert formatted strings to datetime
instances
"""
import datetime


def main():
    format = "%a %b %d %H:%M:%S %Y"

    today = datetime.datetime.today()
    print("ISO     :", today)

    s = today.strftime(format)
    print("strftime:", s)

    d = datetime.datetime.strptime(s, format)
    print("strptime:", d.strftime(format))


if __name__ == "__main__":
    main()
