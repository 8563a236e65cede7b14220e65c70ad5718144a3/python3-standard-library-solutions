"""
Listing 11.4

A network instance is iterable and yields the addresses on the
network
"""
import ipaddress


def main():
    NETWORKS = [
        "10.9.0.0/24",
        "fdfd:87b5:b475:5e3e::/64"
    ]

    for n in NETWORKS:
        net = ipaddress.ip_network(n)
        print(f"{net!r}")
        for i, ip in zip(range(3), net.hosts()):
            print(ip)
        print()


if __name__ == "__main__":
    main()
