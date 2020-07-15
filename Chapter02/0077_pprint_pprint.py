"""
Listing 2.77

The simplest way to use the module is through the pprint() function
"""
import pprint
from pprint_data import data


def main():
    print("PRINT:")
    print(data)
    print("PPRINT:")
    pprint.pprint(data)


if __name__ == "__main__":
    main()
