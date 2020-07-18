"""
Listing 3.49

In addition to the standard operators, many types of objects support
"in-place" modification through special operators such as +=. Equivalent
functions are available for in-place modifications as well
"""
import operator


def main():
    a = -1
    b = 5.0
    c = [1, 2, 3]
    d = ["a", "b", "c"]
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)
    print("d = ", d)
    print()

    a = operator.iadd(a, b)
    print("a = iadd(a, b) =>", a)
    print()

    c = operator.iconcat(c, d)
    print("c = iconcat(c, d) =>", c)


if __name__ == "__main__":
    main()
