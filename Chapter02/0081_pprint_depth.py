"""
Listing 2.81

For very deep data structures, it may not be desireable for the output
to include all of the details. The data may not be formatted properly,
the formatted text might be too large to manage, or some of the data
may be extraneous
"""
import pprint
from pprint_data import data


def main():
    pprint.pprint(data, depth=1)
    pprint.pprint(data, depth=2)
    pprint.pprint(data, depth=3)


if __name__ == "__main__":
    main()
