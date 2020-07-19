"""
Listing 4.13

The resolution for time is limited to whole microseconds. Floating-
point values for microseconds cause a TypeError
"""
import datetime


def main():
    for m in [1, 0, 0.1, 0.6]:
        try:
            print(f"{m:02.1f} {datetime.time(0, 0, 0, microsecond=m)}")
        except TypeError as err:
            print("ERROR:", err)


if __name__ == "__main__":
    main()
