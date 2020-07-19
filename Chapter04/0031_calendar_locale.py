"""
Listing 4.31

To produce a calendar formatted for a locale other than the current
default, use LocaleTextCalendar or LocaleHTMLCalendar
"""
import calendar


def main():
    c = calendar.LocaleTextCalendar(locale="en_US")
    c.prmonth(2017, 7)

    print()

    c = calendar.LocaleTextCalendar(locale="fr_FR")
    c.prmonth(2017, 7)


if __name__ == "__main__":
    main()
