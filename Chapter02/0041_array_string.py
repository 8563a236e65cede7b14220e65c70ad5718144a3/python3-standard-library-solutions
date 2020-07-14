"""
Listing 2.41

The array module defines a sequence data structure that looks very much
like a list, except that all of the members have to be of the same
primitive type.

The types supported are all numeric or other fixed-size primitive types
such as bytes

Code        Type                Minimum Size (Bytes)
b           Int                 1
B           Int                 1
h           Signed short        1
H           Unsigned short      1
i           Signed int          1
I           Unsigned int        1
l           Signed long         1
L           Unsigned long       1
q           Signed long long    1
Q           Unsigned long long  1
f           Float               1
d           Double float        1

An array is instantiated with an argument describing the type of data
to be allowed, and possibly an initial sequence of data to store
in the array
"""
import array
import binascii


def main():
    s = b"This is the array"
    a = array.array("b", s)

    print("As byte string:", s)
    print("As array      :", a)
    print("As hex        :", binascii.hexlify(a))


if __name__ == "__main__":
    main()
