"""
Listing 2.36

namedtuple instances can be converted to OrderedDict instances using
_asdict()
"""
import collections


def main():
    Person = collections.namedtuple("Person", "name age")
    bob = Person(name="Bob", age=30)
    print("Representation:", bob)
    print("As Dictionary:", bob._asdict())


if __name__ == "__main__":
    main()
