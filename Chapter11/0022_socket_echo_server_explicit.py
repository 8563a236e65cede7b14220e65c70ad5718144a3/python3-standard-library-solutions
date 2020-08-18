"""
Listing 11.22

The next example modifies the echo server to list on an address
specified via a command-line argument
"""
import socket
import sys


def main():

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_name = sys.argv[1]
    server_address = (server_name, 10000)
    print("starting up on {} port {}".format(*server_address))
    sock.bind(server_address)

    sock.listen(1)

    while True:
        # Wait for a connection
        print("waiting for a connection")
        connection, client_address = sock.accept()
        try:
            print("connection from ", client_address)

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(16)
                print(f"received {data!r}")
                if data:
                    print("sending data back to the client")
                    connection.sendall(data)
                else:
                    print("no data from ", client_address)
                    break
        finally:
            # Clean up the connection
            connection.close()


if __name__ == '__main__':
    main()
