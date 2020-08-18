"""
Listing 11.8

Use gethostbyname() to consult the operating system hostname resolution
API and convert the name to its numerical address
"""
import socket


def main():
    HOSTS = [
        "debian",
        "pymotw.com",
        "www.python.org",
        "nosuchname"
    ]

    for host in HOSTS:
        try:
            print(f"{host} : {socket.gethostbyname(host)}")
        except socket.error as msg:
            print(f"{host} : {msg}")


if __name__ == "__main__":
    main()
