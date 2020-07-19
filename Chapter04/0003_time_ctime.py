"""
Listing 4.3

The float representation is highly useful when storing or comparing dates,
but less useful for producing human-readable representations. For logging
or printing times, ctime() can be a better choice
"""
import time


def main():
    print("The time is         :", time.ctime())
    later = time.time() + 15
    print("15 seconds from now :", time.ctime(later))


if __name__ == "__main__":
    main()
