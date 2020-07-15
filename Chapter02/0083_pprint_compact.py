"""
Listing 2.83

The compact flag tells pprint() to try to fit more data on each individual
line, rather than spreading complex data structures across lines
"""
import pprint
from pprint_data import data


def main():
    print("DEFAULT:")
    pprint.pprint(data, compact=False)
    print("\nCOMPACTS:")
    pprint.pprint(data, compact=True)


if __name__ == "__main__":
    main()
