"""
Listing 3.7

Since old-style comparison functions are deprecated in Python 3, the
cmp argument to functions like sort() is also no longer supported. Older
programs that use comparison functions can use cmp_to_key() to convert
them to a function that returns a collation key, which is used to
determine the position in the final sequence
"""
import functools


class MyObject:

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return f"MyObject({self.val})"


def compare_obj(a, b):
    """Old-style comparison function"""
    print(f"comparing {a} and {b}")
    if a.val < b.val:
        return -1
    elif a.val > b.val:
        return 1
    return 0


get_key = functools.cmp_to_key(compare_obj)


def get_key_wrapper(o):
    """Wrapper function for get_key to allow for print statements"""
    new_key = get_key(o)
    print(f"key_wrapper({o}) -> {new_key!r}")
    return new_key


def main():
    objs = [MyObject(x) for x in range(5, 0, -1)]

    for o in sorted(objs, key=get_key_wrapper):
        print(o)


if __name__ == "__main__":
    main()
