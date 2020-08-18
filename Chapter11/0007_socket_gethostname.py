"""
Listing 11.7

The socket module exposes the low-level C API for communicating over
a network using the BSD socket interface. It includes the socket
class, for handling the actual data channel, as well as functions for
network-related tasks such as converting a server's name to an address
and formatting data to be sent across the network.
"""
import socket


def main():
    print(socket.gethostname())


if __name__ == "__main__":
    main()
