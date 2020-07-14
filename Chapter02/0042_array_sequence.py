"""
Listing 2.42

An array can be extended and otherwise manipulated in the same ways
as other Python sequences
"""
import array
import pprint


def main():
    a = array.array("i", range(3))
    print("Initial :", a)

    a.extend(range(3))
    print("Extended:", a)

    print("Slice   :", a[2:5])

    print("Iterator:")
    print(list(enumerate(a)))


if __name__ == "__main__":
    main()
