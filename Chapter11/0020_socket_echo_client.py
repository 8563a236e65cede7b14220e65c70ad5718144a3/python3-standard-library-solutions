"""
Listing 11.20

Echo client implementation
"""
import socket
import sys


def main():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ("localhost", 10000)
    print("connection to {} port {}".format(*server_address))
    sock.connect(server_address)

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
