"""
Listing 11.14

To retrieve the number assigned to a transport protocol, use
getprotobyname()
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
    protocols = get_constants("IPPROTO_")
    print(protocols)

    for name in ["icmp", "udp", "tcp"]:
        proto_num = socket.getprotobyname(name)
        const_name = protocols[proto_num]
        print(f"{name:>4} - {proto_num:2d}"
              f"(socket.{const_name:<12} = "
              f"{getattr(socket, const_name):2d})")


if __name__ == '__main__':
    main()
