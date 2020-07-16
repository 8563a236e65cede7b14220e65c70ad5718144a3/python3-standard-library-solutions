"""
Listing 3.15

When no exact match is found for the type, the inheritance order is
evaluated and the closest matching type is used
"""
import functools


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B):
    pass


class E(C, D):
    pass


@functools.singledispatch
def myfunc(arg):
    print(f"default myfunc({arg.__class__.__name__})")


@myfunc.register(A)
def myfunc_A(arg):
    print(f"myfunc_A({arg.__class__.__name__})")


@myfunc.register(B)
def myfunc_B(arg):
    print(f"myfunc_B({arg.__class__.__name__})")


@myfunc.register(A)
def myfunc_C(arg):
    print(f"myfunc_C({arg.__class__.__name__})")


def main():
    myfunc(A())
    myfunc(B())
    myfunc(C())
    myfunc(D())
    myfunc(E())


if __name__ == "__main__":
    main()
