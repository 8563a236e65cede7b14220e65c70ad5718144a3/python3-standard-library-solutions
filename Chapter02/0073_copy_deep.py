"""
Listing 2.73

The deep copy created by deepcopy() is a new container populated with
copies of the contents of the original object. To make a deep copy
of a list, a new list is constructed, the elements of the original list
are copied, and then those copies are appended to the new list
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
    dup = copy.deepcopy(my_list)
    print("             my_list:", my_list)
    print("                 dup:", dup)
    print("      dup is my_list:", (dup is my_list))
    print("      dup == my_list:", (dup == my_list))
    print("dup[0] is my_list[0]:", (dup[0] is my_list[0]))
    print("dup[0] == my_list[0]:", (dup[0] == my_list[0]))


if __name__ == "__main__":
    main()
