"""
Listing 11.6

A network interface represents a specific address on a network
and can be represented by a host address and a network prefix or
netmask
"""
import ipaddress


def main():
    ADDRESSES = [
        "10.9.0.6/24",
        "fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa/64"
    ]

    for ip in ADDRESSES:
        iface = ipaddress.ip_interface(ip)
        print(f"{iface!r}")
        print("network:\n", iface.network)
        print("ip:\n  ", iface.ip)
        print("IP with prefixlen:\n  ", iface.with_prefixlen)
        print("netmask:\n  ", iface.with_netmask)
        print("hostmask:\n  ", iface.with_hostmask)


if __name__ == "__main__":
    main()
