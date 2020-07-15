"""
Listing 2.61

Use unpack to extract data from its packed representation

Passing the packed value to unpack(), gives basically the same values
back.
"""
import struct
import binascii


def main():
    packed_data = binascii.unhexlify(b'0100000061620000cdcc2c40')

    s = struct.Struct("I 2s f")
    unpacked_data = s.unpack(packed_data)
    print("Unpacked Values:", unpacked_data)


if __name__ == "__main__":
    main()
