"""
Listing 2.30

The standard tuple uses numerical indexes to access its members. This
makes tuples convenient containers for simple uses.
"""


def main():
    bob = ("Bob", 30, "male")
    print("Representation:", bob)

    jane = ("Jane", 29, "female")
    print("\nField by index:", jane[0])

    print("\nFields by index:")
    for p in [bob, jane]:
        print(f"{p[0]} is a {p[1]} year old {p[2]}")


if __name__ == "__main__":
    main()
