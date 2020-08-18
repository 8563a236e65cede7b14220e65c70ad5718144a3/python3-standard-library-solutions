"""
Listing 11.33

Binary server implementation
"""
import binascii
import socket
import struct
import sys


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 10000)
    sock.bind(server_address)
    sock.listen(1)

    unpacker = struct.Struct("I 2s f")

    while True:
        print("\nwaiting for a connection")
        connection, client_address = sock.accept()
        try:
            data = connection.recv(unpacker.size)
            print(f"received {binascii.hexlify(data)}")

            unpacked_data = unpacker.unpack(data)
            print("unpacked:", unpacked_data)
        finally:
            connection.close()


if __name__ == '__main__':
    main()
