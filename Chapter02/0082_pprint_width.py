"""
Listing 2.82

The default output width for the formatted text is 80 columns. To adjust
that width, use the width argument to pprint()
"""
import pprint
from pprint_data import data


def main():
    for width in [80, 5]:
        print(f"WIDTH = {width}")
        pprint.pprint(data, width=width)
        print()


if __name__ == "__main__":
    main()
