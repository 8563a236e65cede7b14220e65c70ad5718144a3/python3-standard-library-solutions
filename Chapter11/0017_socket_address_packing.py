"""
Listing 11.17

Network programs written in C use the data type struct sockaddr to
represent IP addresses as binary values. To convert IPv4 addresses
between Python and C representation use inet_aton() and inet_ntoa()
"""
import binascii
import socket
import struct
import sys


def main():
    for string_address in ["192.168.1.1", "127.0.0.1"]:
        packed = socket.inet_aton(string_address)
        print("Original:", string_address)
        print("Packed  :", binascii.hexlify(packed))
        print("Unpacked:", socket.inet_ntoa(packed))
        print()


if __name__ == '__main__':
    main()
