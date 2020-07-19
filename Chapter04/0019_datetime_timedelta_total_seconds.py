"""
Listing 4.19

The full duration of a timedelta can be retrieves as a number of
seconds using total_seconds
"""
import datetime


def main():
    for delta in [
        datetime.timedelta(microseconds=1),
        datetime.timedelta(milliseconds=1),
        datetime.timedelta(seconds=1),
        datetime.timedelta(minutes=1),
        datetime.timedelta(hours=1),
        datetime.timedelta(days=1),
        datetime.timedelta(weeks=1)
    ]:
        print(f"{str(delta):15} = {delta.total_seconds():8} seconds")


if __name__ == "__main__":
    main()
