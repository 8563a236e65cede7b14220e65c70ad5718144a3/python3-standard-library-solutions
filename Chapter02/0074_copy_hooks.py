"""
Listing 2.74

It is possible to control how copies are made using the __copy__()
and __deepcopy__() special methods

    __copy__() is called without any arguments and should return a
    shallow copy of the object

    __deepcopy__() is called with a memo dictionary and should return
    a deep copy of the object. Any member attributes that need to be
    deep-copied should be passed to copy.deepcopy(), along with the
    memo dictionary, to control for recursion

    The memo dictionary is used to keep track of the values that have
    been copied already, so as to avoid infinite recursion
"""
import copy
import functools


@functools.total_ordering
class MyClass:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.name > other.name

    def __copy__(self):
        print("__copy__()")
        return MyClass(self.name)

    def __deepcopy__(self, memo):
        print(f"__deepcopy__({memo})")
        return MyClass(copy.deepcopy(self.name, memo))


def main():
    a = MyClass("a")
    sc = copy.copy(a)
    dc = copy.deepcopy(a)


if __name__ == "__main__":
    main()
