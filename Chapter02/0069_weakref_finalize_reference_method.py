"""
Listing 2.69

Using a bound method of a tracked object as the callable can also prevent
an object from being finalized properly.

Because the callable given to finalize is a bound method of the instance
obj, the finalize object holds a reference to obj, which cannot be
deleted and garbage collected
"""
import gc
import weakref


class ExpensiveObject:
    def __del__(self):
        print(f"(Deleting {self})")

    def do_finalize(self):
        print("do_finalize")


def main():
    obj = ExpensiveObject()
    obj_id = id(obj)

    f = weakref.finalize(obj, obj.do_finalize)
    f.atexist = False

    del obj

    for o in gc.get_objects():
        if id(o) == obj_id:
            print("found uncollected object in gc")


if __name__ == "__main__":
    main()
