"""
Listing 2.70

It is sometimes more convenient to use a proxy, rather than a weak
reference. Proxies can be used as though they were the original object
and do not need to be called before the object is accessible. As a
consequence, they can be passed to a library that does not know it is
receiving a reference instead of the real object
"""
import weakref


class ExpensiveObject:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"(Deleting {self})")


def main():
    obj = ExpensiveObject("My Object")
    r = weakref.ref(obj)
    p = weakref.proxy(obj)

    print(f"via obj: {obj.name}")
    print(f"via ref: {r().name}")
    print(f"via proxy: {p.name}")
    del obj
    print(f"via proxy: {p.name}")  # ReferenceError


if __name__ == "__main__":
    main()
