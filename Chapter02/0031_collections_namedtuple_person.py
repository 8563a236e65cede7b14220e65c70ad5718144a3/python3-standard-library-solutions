"""
Listing 2.31

In contrast, remembering which index should be used for each value can
lead to errors, especially if the tuple has a lot of fields and is
constructed far from where it is used. A namedtuple assigns names,
as well as the numerical index, to each member.

namedtuple instances are just as memory efficient as regular tuples because
they do not have per-instance dictionaries. Each kind of namedtuple is
represented by its own class, which is created by using the namedtuple()
factory function. The arguments are the name of the new class and a
string containing the names of the elements

It is possible to access the fields of the namedtuple by name using
dotted notation (obj.attr) as well as by using the position indexes of
standard tuples
"""
import collections


def main():
    Person = collections.namedtuple("Person", "name age")

    bob = Person(name="Bob", age=30)
    print("\nRepresentation:", bob)

    jane = Person(name="Jane", age=29)
    print("\nField by name", jane.name)

    print("\nFields by index:")
    for p in [bob, jane]:
        print(f"{p[0]} is {p[1]} years old")


if __name__ == "__main__":
    main()
