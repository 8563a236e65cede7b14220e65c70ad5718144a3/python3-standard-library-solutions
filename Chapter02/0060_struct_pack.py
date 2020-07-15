"""
Listing 2.60

The struct module includes functions for converting between strings
of bytes and native Python data types such as numbers and strings.

A set of module-level functions is available for working with structured
values, as well as the Struct class. Format specifiers are converted from
their string format to a compiled representation, similar to the way
regular expressions are handles. The conversion takes some resources,
so it is typically more efficient to do it once when creating a Struct
instance and call methods on the instance, instead of using the module-
level functions.

Structs support packing data into strings, and upacking data from strings
using format specifiers made up of characters representing the type of
the data and optional count and endianness indicators.
"""
import struct
import binascii


def main():
    values = (1, "ab".encode("utf-8"), 2.7)
    s = struct.Struct("I 2s f")
    packed_data = s.pack(*values)

    print("Original values:", values)
    print("Format string  :", s.format)
    print("Uses           :", s.size, "bytes")
    print("Packed Value   :", binascii.hexlify(packed_data))


if __name__ == "__main__":
    main()
