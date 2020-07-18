"""
Listing 3.50

One of the most unusual features of the operator module is the concept
of getters. These callable objects are constructed at runtime and retrieve
attributes of objects or contents from sequences. Getters are especially
useful when working with iterators or generator sequences, as they incur
less overhead than a lambda or Python function

Attribute getters work like lambda x,n="attrname": getattr(x, n)
"""
import operator


class MyObj:
    """example class for attrgetter"""

    def __init__(self, arg):
        super().__init__()
        self.arg = arg

    def __repr__(self):
        return f"MyObj({self.arg})"


def main():
    l = [MyObj(i) for i in range(5)]
    print("objects   :", l)

    # Extract the "arg" value from each object
    g = operator.attrgetter("arg")
    vals = [g(i) for i in l]
    print("arg values:", vals)

    # Sort using arg
    l.reverse()
    print("reversed  :", l)
    print("sorted    :", sorted(l, key=g))


if __name__ == "__main__":
    main()
