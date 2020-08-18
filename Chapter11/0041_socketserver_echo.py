"""
Listing 11.41

The socketserver module is a framework for creating network servers.
It defines classes for handling synchronous network requests (the
server request handler blocks until the request is completed) over
TCP, UDP, Unix streams and Unix datagrams. It also provides mix-in
classes for easily converting servers to use a separate thread or
process for each request.

Five server classes are defined in socketserver. BaseServer
defines the API and is not intended to be instantiated and used
directly. TCPServer uses TCP/IP sockets to communicate. UDPServer
uses datagram sockets. UnixStreamServer and UnixDatagramServer use
Unix-domain sockets and are available only on Unix platforms

To construct a server, pass it an address on which to listen for
requests and a request handler class (not instance). The address format
depends on the server type and the socket family used.

Once the server object is instantiated, use either handle_request() or
serve_forever() to produce requests. The serve_forever() method calls
handle_request() in an infinite loop.

BaseServer includes several methods that can be overridden in a
subclass
    verify_request(request, client_address)
        Returns True to process the request or False to ignore it.
    process_request(request, client_address)
        Calls finish_request() to actually do the work of handling
        the request. Can also create a separate thread or process
        as the mix-in classes do
    finish_request(request, client_address)
        Creates a request handler instance using the class given to
        the server's constructor. Calls handle() on the request
        handler to process the request

Request handlers do most of the work of receiving incoming requests
and deciding which action to take. The handler is responsible for
implementing the protocol on top of the socket layer (i.e. HTTP,
XML-RPC or AMQP). The request handler reads the request from the
incoming data channel, processes it, and writes a response back out.
Three methods are available to be overridden
    setup()
        Prepares the request handler for the request. In the
        StreamRequestHandler, the setup() method creates file-like
        objects for reading from and writing to the socket
    handle()
        Does the real work for the request. Parses the incoming request,
        processes the data, and sends a response
    finish()
        Cleans up anything created during setup
"""
import logging
import sys
import socketserver
import socket
import threading

logging.basicConfig(level=logging.DEBUG,
                    format="%(name)s: %(message)s")


class EchoRequestHandler(socketserver.BaseRequestHandler):

    def __init__(self, request, client_address, server):
        self.logger = logging.getLogger("EchoRequestHandler")
        self.logger.debug("__init__")
        socketserver.BaseRequestHandler.__init__(self, request,
                                                 client_address,
                                                 server)
        return

    def setup(self):
        self.logger.debug("setup")
        return socketserver.BaseRequestHandler.setup(self)

    def handle(self):
        self.logger.debug("handle")

        # Echo the data back to the client
        data = self.request.recv(1024)
        self.logger.debug("recv()->'%s'", data)
        self.request.send(data)
        return

    def finish(self):
        self.logger.debug("finish")
        return socketserver.BaseRequestHandler.finish(self)


class EchoServer(socketserver.TCPServer):

    def __init__(self, server_address,
                 handler_class=EchoRequestHandler):
        self.logger = logging.getLogger("EchoServer")
        self.logger.debug("__init__")
        socketserver.TCPServer.__init__(self, server_address,
                                        handler_class)
        return

    def server_activate(self) -> None:
        self.logger.debug("server_activate")
        socketserver.TCPServer.server_activate(self)
        return

    def serve_forever(self, poll_interval=0.5):
        self.logger.debug("waiting for request")
        self.logger.info(
            "Handling request, press <Ctrl-C> to quit"
        )
        socketserver.TCPServer.serve_forever(self, poll_interval)
        return

    def handle_request(self) -> None:
        self.logger.debug("handle_request")
        return socketserver.TCPServer.handle_request(self)

    def verify_request(self, request,
                       client_address) -> bool:
        self.logger.debug("verify_request(%s, %s)",
                          request, client_address)
        return socketserver.TCPServer.verify_request(
            self, request, client_address
        )

    def process_request(self, request, client_address):
        self.logger.debug("process request (%s, %s)",
                          request, client_address)
        return socketserver.TCPServer.process_request(
            self, request, client_address
        )

    def server_close(self):
        self.logger.debug("server_close")
        return socketserver.TCPServer.server_close(self)

    def finish_request(self, request,
                       client_address) -> None:
        self.logger.debug("finish_request(%s, %s)",
                          request, client_address)
        return socketserver.TCPServer.finish_request(
            self, request, client_address
        )

    def close_request(self, request_address):
        self.logger.debug("close_request (%s)",
                          request_address)
        return socketserver.TCPServer.close_request(
            self, request_address
        )

    def shutdown(self):
        self.logger.debug("shutdown()")
        return socketserver.TCPServer.shutdown(self)


def main():
    import socket
    import threading

    address = ("localhost", 0)
    server = EchoServer(address, EchoRequestHandler)
    ip, port = server.server_address

    # Start the server in a thread
    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)
    t.start()

    logger = logging.getLogger("client")
    logger.info("Server on %s:%s", ip, port)

    # Connect to the server
    logger.debug("creating socket")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.debug("connecting to server")
    s.connect((ip, port))

    # Send the data
    message = "Hello, world".encode()
    logger.debug("sending data: %r", message)
    len_sent = s.send(message)

    # Receive a response
    logger.debug("waiting for response")
    response = s.recv(len_sent)
    logger.debug("response from server: %r", response)

    # Clean up
    server.shutdown()
    logger.debug("closing socket")
    s.close()
    logger.debug("done")
    server.socket.close()


if __name__ == '__main__':
    main()
