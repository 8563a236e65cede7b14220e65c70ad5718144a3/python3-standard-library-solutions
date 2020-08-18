"""
Listing 11.32

Sockets transmit streams of bytes. Those bytes can contain text
messages encoded as bytes as in the previous examples, or they can
be made up of binary data that has been packed into a buffer with
struct, to prepare it for transmission
"""
import binascii
import socket
import struct
import sys


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 10000)
    sock.connect(server_address)

    values = (1, b"ab", 2.7)
    packer = struct.Struct("I 2s f")
    packed_data = packer.pack(*values)

    print("values =", values)

    try:
        # Send data
        print(f"sending {binascii.hexlify(packed_data)}")
        sock.sendall(packed_data)
    finally:
        print("closing socket")
        sock.close()


if __name__ == '__main__':
    main()