"""
Listing 11.16

getaddrinfo() takes several arguments for filtering the result list
"""
import socket


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

    responses = socket.getaddrinfo(
        host="www.python.org",
        port="http",
        family=socket.AF_INET,
        type=socket.SOCK_STREAM,
        proto=socket.IPPROTO_TCP,
        flags=socket.AI_CANONNAME
    )

    for response in responses:

        family, socktype, proto, canonname, sockaddr = response

        print("Family        :", families[family])
        print("Type          :", types[socktype])
        print("Protocol      :", protocols[proto])
        print("Canonical name:", canonname)
        print("Socket address:", sockaddr)
        print()


if __name__ == '__main__':
    main()
