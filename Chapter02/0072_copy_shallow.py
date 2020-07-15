"""
Listing 2.72

The copy module includes two functions, copy() and deepcopy(), for
duplicating existing objects

The shallow copy created by copy() is a new container populated with
references to the contents of the original object. When making a shallow
copy of a list object, a new list is constructed and the elements of the
original list are appended to it

For a shallow copy, the MyClass instance is not duplicated, so the
reference in the dup list is to the same object that is in my_list
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


def main():
    a = MyClass("a")
    my_list = [a]
    dup = copy.copy(my_list)
    print("             my_list:", my_list)
    print("                 dup:", dup)
    print("      dup is my_list:", (dup is my_list))
    print("      dup == my_list:", (dup == my_list))
    print("dup[0] is my_list[0]:", (dup[0] is my_list[0]))
    print("dup[0] == my_list[0]:", (dup[0] == my_list[0]))


if __name__ == "__main__":
    main()
