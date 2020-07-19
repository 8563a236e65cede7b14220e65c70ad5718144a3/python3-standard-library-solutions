"""
Listing 4.30

This is equivalent to the data used by formatyear()

The day_name, day_abbr, month_name and month_abbr module attributes are
useful for producing custom-formatted output. They are automatically
configured correctly for the current locale
"""
import calendar


def main():
    cal = calendar.TextCalendar(calendar.SUNDAY)
    print(cal.formatyear(2017, 2, 1, 1, 3))


if __name__ == "__main__":
    main()
