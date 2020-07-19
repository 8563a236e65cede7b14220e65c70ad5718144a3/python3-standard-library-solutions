"""
Listing 4.33

To calculate the group meeting dates for a year, assuming they are always
on the second Thursday of every month, look at the output of
monthcalendar() to find the dates on which Thursdays fall.

The first and last weeks of the month are padded with 0 values as
placeholders for the days falling in the preceding and subsequent months
respectively.
"""
import calendar
import sys


def main():
    year = int(sys.argv[1])

    # Show every month.
    for month in range(1, 13):

        # Computer the dates for each week that overlaps the month
        c = calendar.monthcalendar(year, month)
        first_week = c[0]
        second_week = c[1]
        third_week = c[2]

        # If there is a Thursday in the first week,
        # the second Thursday is in the second week.
        # Otherwise, the second Thursday must be in the
        # third week
        if first_week[calendar.THURSDAY]:
            meeting_date = second_week[calendar.THURSDAY]
        else:
            meeting_date = third_week[calendar.THURSDAY]
        print(f"{calendar.month_abbr[month]:>3}: {meeting_date:>2}")


if __name__ == "__main__":
    main()
