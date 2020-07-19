"""
Listing 4.28

The calendar module defines the Calendar class, which encapsulates
calculations for values such as the dates of the week in a given month
or year. In addition, the TextCalendar and HTMLCalendar classes can
produce preformatted output

The prmonth() method is a simple function that produces the formatted
text output for a month
"""
import calendar


def main():
    c = calendar.TextCalendar(calendar.SUNDAY)
    c.prmonth(2017, 7)


if __name__ == "__main__":
    main()
