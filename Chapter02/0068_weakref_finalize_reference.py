"""
Listing 2.68

Giving the finalize instance a reference to the object it tracks causes a
reference to be retained, so the object is never garbage collected
"""
import gc
import weakref


class ExpensiveObject:

    def __del__(self):
        print(f"(Deleting P{self})")


def on_finalize(*args):
    print(f"on finalize ({args!r})")


def main():
    obj = ExpensiveObject()
    obj_id = id(obj)

    f = weakref.finalize(obj, on_finalize, obj)
    f.atexit = False

    del obj

    for o in gc.get_objects():
        if id(o) == obj_id:
            print("found uncollected object in gc")


if __name__ == "__main__":
    main()
