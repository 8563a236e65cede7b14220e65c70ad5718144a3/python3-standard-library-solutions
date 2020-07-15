"""
Listing 2.63

Working with binary packed data is typically reserved for performance-
sensitive situations, or passing data into and out of extension modules.

These cases can be optimized by avoiding the overhead of allocating a
new buffer for each packed structure. The pack_into() and
unpack_from() methods support writing to pre-allocated buffers directly

The size attribute of the Struct tells us how big the buffer needs to be
"""
import array
import binascii
import ctypes
import struct


def main():
    s = struct.Struct("I 2s f")
    values = (1, "ab".encode("utf-8"), 2.7)
    print("Original:", values)
    print()

    print("ctypes string buffer")
    b = ctypes.create_string_buffer(s.size)
    print("Before  :", binascii.hexlify(b.raw))
    s.pack_into(b, 0, *values)
    print("After   :", binascii.hexlify(b.raw))
    print("Unpacked:", s.unpack_from(b, 0))

    print()
    print("array")

    a = array.array("b", b"\0" * s.size)
    print("Before  :", binascii.hexlify(a))
    s.pack_into(a, 0, *values)
    print("After   :", binascii.hexlify(a))
    print("Unpacked:", s.unpack_from(a, 0))


if __name__ == "__main__":
    main()
