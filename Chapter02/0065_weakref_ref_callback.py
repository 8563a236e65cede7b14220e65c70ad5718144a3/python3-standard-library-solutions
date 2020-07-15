"""
Listing 2.65

The ref constructor accepts an optional callback function that is invoked
when the referenced object is deleted
"""
import weakref


class ExpensiveObject:

    def __del__(self):
        print(f"(Deleting {self})")


def callback(reference):
    """Invoked when referenced object is deleted"""
    print(f"callback({reference!r})")


def main():
    obj = ExpensiveObject()
    r = weakref.ref(obj, callback)

    print("obj:", obj)
    print("ref:", r)
    print("r():", r())

    print("deleting obj")
    del obj
    print("r():", r())


if __name__ == "__main__":
    main()
