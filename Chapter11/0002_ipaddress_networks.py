"""
Listing 11.2

A network is defined by a range of addresses. It is usually expressed
with a base address and a mask indicating which portions of the address
represent the network, and which portions represent addresses on that
network. The mask can be expressed either explicitly or by using
a prefix length value
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
        print("      is private:", net.is_private)
        print("       broadcast:", net.broadcast_address)
        print("      compressed:", net.compressed)
        print("    with netmask:", net.with_netmask)
        print("   with hostmask:", net.with_hostmask)
        print("   num addresses:", net.num_addresses)
        print()


if __name__ == "__main__":
    main()
