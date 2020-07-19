"""
Listing 4.32

Although the calendar module focuses mostly on printing full calendars
in various formats, it also provides functions useful for working with
dates in other ways, such as calculating dates for a recurring event.
"""
import calendar
import pprint


def main():
    pprint.pprint(calendar.monthcalendar(2017, 7))


if __name__ == "__main__":
    main()
