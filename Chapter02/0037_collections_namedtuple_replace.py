"""
Listing 2.37

The _replace() method builds a new instance, replacing the values of
some fields in the process

Although the name implies it is modifying the existing object, because
namedtuple instances are immutable, the method actually returns a
new object
"""
import collections


def main():
    Person = collections.namedtuple("Person", "name age")

    bob = Person(name="Bob", age=30)
    print("\nBefore:", bob)
    bob2 = bob._replace(name="Robert")
    print("After:", bob2)
    print("Same?:", bob is bob2)


if __name__ == "__main__":
    main()
