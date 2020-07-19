"""
Listing 4.27

Within datetime, time zones are represented by subclasses of tzinfo. Since
tzinfo is an abstract base class, applications need to define a subclass
and provide appropriate implementations for a few methods to make it
useful.

datetime does include a somewhat naive implementation in the class
timezone that uses a fixed offset from UTC. This implementation does
not support different offset values on different days of the year,
such as where daylight savings time applies, or where the offset
from UTC has changed over time
"""
import datetime


def main():
    min6 = datetime.timezone(datetime.timedelta(hours=-6))
    plus6 = datetime.timezone(datetime.timedelta(hours=6))
    d = datetime.datetime.now(min6)

    print(min6, ":", d)
    print(datetime.timezone.utc, ":", d.astimezone(datetime.timezone.utc))
    print(plus6, ":", d.astimezone(plus6))

    # Convert to the current system timezone
    d_system = d.astimezone()
    print(d_system.tzinfo, "     :", d_system)


if __name__ == "__main__":
    main()
