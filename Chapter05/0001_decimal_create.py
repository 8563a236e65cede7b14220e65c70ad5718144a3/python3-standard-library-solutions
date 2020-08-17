"""
Listing 5.1

The decimal module implements fixed- and floating-point arithmetic using
the model familiar to most people, rather than the IEEE floating-point
version. A decimal instance can represent any number exactly, be rounded
up or down, and apply a limit to the number of significant digits

Decimal values are represented as instances of the Decimal class. The
constructor takes one integer or string. Floating-point numbers can
be converted to a string before being used to create a Decimal, thereby
letting the caller explicitly deal with the number of digits for values
that cannot be expressed exactly using the hardware floating-point
representations. Alternatively, the class method from_float() converts
a floating-point number to its exact decimal representation.
"""
import decimal


def main():
    fmt = "{0:<25} {1:<25}"
    print(fmt.format("Input", "Output"))
    print(fmt.format("-" * 25, "-" * 25))

    # Integer
    print(fmt.format(5, decimal.Decimal(5)))

    # String
    print(fmt.format("3.14", decimal.Decimal("3.14")))

    # Float
    f = 0.1
    print(fmt.format(repr(f), decimal.Decimal(str(f))))

    print("{:0.23g} {:<25}".format(
        f,
        str(decimal.Decimal.from_float(f))[:25]
    ))


if __name__ == "__main__":
    main()
