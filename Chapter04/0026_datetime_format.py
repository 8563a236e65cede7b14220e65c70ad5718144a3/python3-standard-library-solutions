"""
Listing 4.26

The same formatting codes can be used with Python's string formatting
mini-language by placing them after the : in the firled specification
of the format string

Symbol      Meaning                             Example
%a          Abbreviated weekday name            Wed
%A          Full weekday name                   Wednesday
%w          Weekday number: 0 (Sunday) through  3
            6 (Saturday)
%d          Day of the month (zero padded)      13
%b          Abbreviated month name              Jan
%B          Full month name                     January
%m          Month of the year                   01
%y          Year without century                16
%Y          Year with century                   2016
%H          Hour from 24-hour clock             17
%I          Hour from 12-hour clock             05
%p          AM/PM                               PM
%M          Minutes                             00
%S          Seconds                             00
%f          Microseconds                        000000
%z          UTC offset for timezone-aware       -0500
            objects
%Z          Time zone name                      EST
%j          Day of the year                     013
%W          Week of the year                    02
%c          Date and time representation        Wed Jan 13 17:00:00 2016
            for the current locale
%x          Date representation for the         01/13/16
            current locale
%X          Time representation for the         17:00:00
            current locale
%%          A literal % character               %

Each datetime format code must be prefixed with %, and subsequent
colons are treated as literal characters to be included in the output
"""
import datetime


def main():
    today = datetime.datetime.today()
    print("ISO     :", today)
    print(f"format  : {today:%a %b %d %H:%M:%S %Y}")


if __name__ == "__main__":
    main()
