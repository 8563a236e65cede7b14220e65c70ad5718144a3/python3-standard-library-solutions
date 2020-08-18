"""
Listing 11.13

To reverse the service port lookup, use getservbyport()
"""
import socket
from urllib.parse import urlunparse


def main():
    for port in [80, 443, 21, 70, 25, 143, 993, 110, 995]:
        url = f"{socket.getservbyport(port)}://example.com"
        print(url)


if __name__ == '__main__':
    main()
