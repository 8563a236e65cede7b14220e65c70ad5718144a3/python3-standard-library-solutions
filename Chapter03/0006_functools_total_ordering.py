"""
Listing 3.6

The rich comparison API is designed to allow classes with complex
comparisons to implement each test in the most efficient way possible.
However, for classes where comparison is relatively simple, there is no
point in manually creating each of the rich comparison methods. The
total_ordering() class decorator takes a class that provides some of the
methods and adds the rest of them

The class must provide implementation of __eq__() and one other rich
comparison method. The decorator addes implementations of the rest of
the methods that work by using the comparisons provided. If a comparison
cannot be made, the method should return NotImplemented, so the
comparison can be tried using the reverse comparison operators on
the other object, before failing entirely.
"""
import functools
import inspect
import pprint


@functools.total_ordering
class MyObject:

    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        print(f"  testing __eq__({self.val}, {other.val})")
        return self.val == other.val

    def __gt__(self, other):
        print(f"  testing __gt__({self.val}, {other.val})")
        return self.val > other.val


def main():
    print("Methods:\n")
    pprint.pprint(inspect.getmembers(MyObject, inspect.isfunction))

    a = MyObject(1)
    b = MyObject(2)

    print("\nComparisons:")
    for expr in ["a < b", "a <= b", "a == b", "a >= b", "a > b"]:
        print(f"\n{expr:<6}")
        result = eval(expr)
        print(f"  result of {expr}: {result}")


if __name__ == "__main__":
    main()
