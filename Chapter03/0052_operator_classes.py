"""
Listing 3.52

The functions in the opeartor module work via the standard Python
interfaces when performing their operations. Thus, they work with
user-defined classes as well as the built-in types
"""
import operator


class MyObj:
    """Example for operator overloading"""

    def __init__(self, val):
        super(MyObj, self).__init__()
        self.val = val

    def __str__(self):
        return f"MyObj({self.val})"

    def __lt__(self, other):
        """compare for less-than"""
        print(f"Testing {self} < {other}")
        return self.val < other.val

    def __add__(self, other):
        """add values"""
        print(f"Adding {self} + {other}")
        return MyObj(self.val + other.val)


def main():
    a = MyObj(1)
    b = MyObj(2)

    print("Comparison:")
    print(operator.lt(a, b))

    print("\nArithmetic:")
    print(operator.add(a, b))


if __name__ == "__main__":
    main()
