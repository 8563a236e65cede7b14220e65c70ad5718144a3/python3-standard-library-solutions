"""
Listing 11.34

A selector object provides methods for specifying which events to look
for on a socket and then lets the caller wait for events in a platform-
independent way. Registering interest in an event creates a SelectorKey
which holds the socket, information about the events of interest and
optional application data.

The owner of the selector calls its select() method to learn about
events. The return value is a sequence of key objects, and a bitmask
indicating which events have occurred. A program using a selector should
repeatedly call select() and then handle the events appropriately
"""
import selectors
import socket

mysel = selectors.DefaultSelector()
keep_running = True


def read(connection, mask):
    """Callback for read events"""
    global keep_running

    client_address = connection.getpeername()
    print(f"read({client_address})")
    data = connection.recv(1024)
    if data:
        # A readable client socket has data
        print(f"  received {data!r}")
        connection.sendall(data)
    else:
        # Interpret empty result as closed connection
        print("  closing")
        mysel.unregister(connection)
        connection.close()
        keep_running = False


def accept(sock, mask):
    """Callback for new connections"""
    new_connection, addr = sock.accept()
    print(f"accept({addr})")
    new_connection.setblocking(False)
    mysel.register(new_connection, selectors.EVENT_READ, read)


def main():
    server_address = ("localhost", 10000)
    print("starting up on {} port {}".format(*server_address))
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(False)
    server.bind(server_address)
    server.listen(5)

    mysel.register(server, selectors.EVENT_READ, accept)

    while keep_running:
        print("waiting for I/O")
        for key, mask in mysel.select(timeout=1):
            callback = key.data
            callback(key.fileobj, mask)

    print("shutting down")
    mysel.close()


if __name__ == '__main__':
    main()
