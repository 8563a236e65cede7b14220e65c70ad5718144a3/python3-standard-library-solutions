"""
Listing 11.21

create_connection() is a convenience function that takes one argument, a
two-value tuple containing the address of the server, and derives the
best address to use for the connection
"""
import socket
import sys


def get_constants(prefix):
    """
    Create a dictionary mapping socket module constants
    to their names.
    """
    return {
        getattr(socket, n): n
        for n in dir(socket)
        if n.startswith(prefix)
    }

def main():
    families = get_constants("AF_")
    types = get_constants("SOCK_")
    protocols = get_constants("IPPROTO_")

    sock = socket.create_connection(("localhost", 10000))
    print("Family        :", families[sock.family])
    print("Type          :", types[sock.type])
    print("Protocol      :", protocols[sock.proto])
    print()

    try:
        # Send data
        message = b"This is the message. It will be repeated."
        print(f"sending {message!r}")
        sock.sendall(message)

        # Look for response
        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print(f"received {data!r}")

    finally:
        print("closing socket")
        sock.close()


if __name__ == '__main__':
    main()
