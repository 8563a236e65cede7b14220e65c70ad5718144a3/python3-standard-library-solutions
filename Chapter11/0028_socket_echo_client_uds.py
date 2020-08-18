"""
Listing 11.20

The client should assume that the file system node for the socket
exists, since the server creates it by binding to the address
"""
import socket
import sys


def main():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = "./uds_socket"
    print("connection to {}".format(server_address))
    try:
        sock.connect(server_address)
    except socket.error as msg:
        print(msg)
        sys.exit(1)

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
