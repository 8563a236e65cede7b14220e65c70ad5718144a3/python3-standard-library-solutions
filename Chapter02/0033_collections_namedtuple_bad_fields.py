"""
Listing 2.33

Field names are invalid if they are repeated or conflict with Python
keywords
"""
import collections


def main():
    try:
        collections.namedtuple("Person", "name class age")
    except ValueError as err:
        print(err)

    try:
        collections.namedtuple("Person", "name age age")
    except ValueError as err:
        print(err)


if __name__ == "__main__":
    main()
