"""
Listing 11.5

Networks support the in operator, which is used to determine whether
an address is part of a network.
"""
import ipaddress


def main():
    NETWORKS = [
        ipaddress.ip_network("10.9.0.0/24"),
        ipaddress.ip_network("fdfd:87b5:b475:5e3e::/64")
    ]

    ADDRESSES = [
        ipaddress.ip_address("10.9.0.6"),
        ipaddress.ip_address("10.7.0.31"),
        ipaddress.ip_address(
            "fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa"
        ),
        ipaddress.ip_address("fe80::3840:c439:b25e:63b0"),
    ]

    for ip in ADDRESSES:
        for net in NETWORKS:
            if ip in net:
                print(f"{ip}\n is on {net}")
                break
        else:
            print(f"{ip}\n is not on a known network")
        print()


if __name__ == "__main__":
    main()
