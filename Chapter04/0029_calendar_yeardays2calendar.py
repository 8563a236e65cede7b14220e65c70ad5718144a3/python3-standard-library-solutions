"""
Listing 4.29

To produce output in a format other than one of the defaults, use calendar
to calculate the dates and organize the values into weeks and month
ranges, then iterate over the result.

The weekheader(), monthcalendar() and yeardays2calendar() methods
of Calendar are especially useful for this purpose.

Calling yeardays2calendar() produces a sequence of "month row"
lists. Each list of months includes each month as another list of
weeks. The weeks are lists of tuples made up of day number (1-31)
and weekday number (0-6). Days that fall outside of the month have
a day number of 0
"""
import calendar
import pprint


def main():
    cal = calendar.Calendar(calendar.SUNDAY)

    cal_data = cal.yeardays2calendar(2017, 3)
    print("len(cal_data)      :", len(cal_data))

    top_months = cal_data[0]
    print("len(top_months)    :", len(top_months))

    first_month = top_months[0]
    print("len(first_month)   :", len(first_month))

    print("first_month:")
    pprint.pprint(first_month, width=65)


if __name__ == "__main__":
    main()
