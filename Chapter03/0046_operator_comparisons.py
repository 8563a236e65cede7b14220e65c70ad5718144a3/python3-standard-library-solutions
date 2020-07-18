"""
Listing 3.46

All of the rich comparison operators are supported
"""
import operator


def main():
    a = 1
    b = 5.0

    print("a =", a)
    print("b =", b)

    for func in (operator.lt, operator.le, operator.eq,
                operator.ne, operator.ge, operator.gt):
        print(f"{func.__name__}(a, b): {func(a, b)}")


if __name__ == "__main__":
    main()
