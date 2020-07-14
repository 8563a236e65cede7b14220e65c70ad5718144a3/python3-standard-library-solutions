"""
Listing 2.35

namedtuple provides several useful attributes and methods for working
with subclasses and instances. All of these built-in properties have names
prefixed with an underscore, which protects from name collision with
the user provided attribute names

The names of the fields passed to namedtuple to define the new class
are saved in the _fields attribute.
"""
import collections


def main():
    Person = collections.namedtuple("Person", "name age")
    bob = Person(name="Bob", age=30)
    print("Representation:", bob)
    print("Fields:", bob._fields)


if __name__ == "__main__":
    main()
