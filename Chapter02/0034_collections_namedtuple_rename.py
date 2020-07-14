"""
Listing 2.34

In situations where a namedtuple is created based on values outside the
control of the program, the rename option should be set to True so that
the invalid fields are renamed

The new names for the renamed fields depend on their index in the tuple
"""
import collections


def main():
    with_class = collections.namedtuple(
        "Person", "name class age",
        rename=True
    )
    print(with_class._fields)

    two_ages = collections.namedtuple(
        "Person", "name age age",
        rename=True
    )
    print(two_ages._fields)


if __name__ == "__main__":
    main()
