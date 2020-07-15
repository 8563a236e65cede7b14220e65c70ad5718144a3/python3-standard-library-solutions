"""
Listing 2.62

By default, values are encoded using the native C library notion of
endianness. It is easy to override that choice by providing an explicit
endianness directive in the format string

    Code        Meaning
    @           Native oder
    =           Native standard
    <           Little-endian
    >           Big-endian
    !           Network order
"""
import struct
import binascii


def main():
    values = (1, "ab".encode("utf-8"), 2.7)
    print("Original values: ", values)

    endianness = [
        ("@", "native, native"),
        ("=", "native, standard"),
        ("<", "little-endian"),
        (">", "big-endian"),
        ("!", "network")
    ]

    for code, name in endianness:
        s = struct.Struct(code + " I 2s f")
        packed_data = s.pack(*values)
        print()
        print("Format string  :", s.format, "for", name)
        print("Uses           :", s.size, "bytes")
        print("Packed Value   :", binascii.hexlify(packed_data))
        print("Unpacked Value :", s.unpack(packed_data))


if __name__ == "__main__":
    main()
