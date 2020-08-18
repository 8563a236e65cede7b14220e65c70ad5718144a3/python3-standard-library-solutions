"""
Listing 11.10

Use getfqdn() to convert a partial name to a fully qualified domain
name
"""
import socket


def main():
    for host in ["debian", "pymotw.com"]:
        print(f"{host:>10} : {socket.getfqdn(host)}")


if __name__ == "__main__":
    main()
