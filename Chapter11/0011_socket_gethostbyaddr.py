"""
Listing 11.11

When the address of a server is available, use gethostbyaddr() to do a
"reverse" lookup for the name
"""
import socket


def main():
    hostname, aliases, addresses = socket.gethostbyaddr("127.0.0.1")

    print("Hostname :", hostname)
    print("Aliases  :", aliases)
    print("Addresses:", addresses)


if __name__ == "__main__":
    main()
