"""
Listing 3.45

Programming using iterators occasionally requires creating small functions
for simple expressions. Sometimes these can be implemented as lambda
functions, but for some operations new functions are not needed at all.
The operator module defines functions that correspond to the built-in
arithmetic, comparison and other operations for the standard object
APIs.

Functions are provided for determining the boolean equivalent for a
value, negating a value to create the opposite boolean value, and
comparing objects to see if they are identical
"""
import operator


def main():
    a = -1
    b = 5

    print("a =", a)
    print("b =", b)

    print("not_(a)     :", operator.not_(a))
    print("truth(a)    :", operator.truth(a))
    print("is_(a, b)   :", operator.is_(a, b))
    print("is_not(a, b):", operator.is_not(a, b))


if __name__ == "__main__":
    main()
