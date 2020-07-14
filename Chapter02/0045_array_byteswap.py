"""
Listing 2.45

If the data in the array is not in the native byte order, or if the
data needs to be swapped before being sent to a system with a different
byte order (or over the network), it is possible to convert the entire
array without iterating over the elements from Python.

The byteswap() method switches the byte order of the items in the array
from within C, so it is much more efficient than looping over data in
Python
"""
import array
import binascii


def to_hex(a):
    chars_per_item = a.itemsize * 2  # 2 hex digits
    hex_version = binascii.hexlify(a)
    num_chunks = len(hex_version)  // chars_per_item
    for i in range(num_chunks):
        start = i * chars_per_item
        end = start + chars_per_item
        yield hex_version[start:end]


def main():
    start = int("0x12345678", 16)
    end = start + 5

    a1 = array.array("i", range(start, end))
    a2 = array.array("i", range(start, end))
    a2.byteswap()

    print(f"{'A1 hex':>12} {'A1':>12} {'A2 hex':>12} {'A2':>12}")
    print(f"{'-' * 12} {'-' * 12} {'-' * 12} {'-' * 12}")

    fmt = "{!r:>12} {:12} {!r:>12} {:12}"
    for values in zip(to_hex(a1), a1, to_hex(a2), a2):
        print(fmt.format(*values))


if __name__ == "__main__":
    main()
