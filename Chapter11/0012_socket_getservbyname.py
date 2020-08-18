"""
Listing 11.12

The port numbers for network services with standardized names can be
looked up with getservbyname()
"""
import socket
from urllib.parse import urlparse


def main():
    URLS = [
        "http://www.python.org",
        "https://www.mybank.com",
        "ftp://prep.ai.mit.edu",
        "gopher://gopher.micro.umn.edu",
        "smtp://mail.example.com",
        "imap://mail.example.com",
        "imaps://mail.example.com",
        "pop3://pop.example.com",
        "pop3s://pop.example.com"
    ]

    for url in URLS:
        parsed_url = urlparse(url)
        port = socket.getservbyname(parsed_url.scheme)
        print(f"{parsed_url.scheme:>6} : {port}")


if __name__ == "__main__":
    main()
