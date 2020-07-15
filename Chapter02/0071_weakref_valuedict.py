"""
Listing 2.71

The ref and proxy classes are considered "low level". While they are
useful for maintaining weak references to individual objects and allowing
cycles to be garbage collected, the WeakKeyDictionary and
WeakValueDictionary classes provide a more appropriate API for creating
a cache of several objects

The WeakValueDictionary class uses weak references to the values it holds,
allowing them to be garbage collected when other code is not actually
using them. Using explicit calls to the garbage collector illustrates
the difference between memory handling with a regular dictionary
and a WeakValueDictionary

Any loop variables that refer to the values being cached must be
cleared explicitly so the reference count of the object is decremented.
Otherwise, the garbage collector will not remove the objects and
they will remain in the cache. Similarly, the all_refs variable
is used to hold references to prevent them from being garbage
collected prematurely.
"""
import gc
import pprint
import weakref

gc.set_debug(gc.DEBUG_UNCOLLECTABLE)


class ExpensiveObject:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"ExpensiveObject({self.name})"

    def __del__(self):
        print(f"    (Deleting {self})")


def demo(cache_factory):
    # Hold objects so any weak references
    # are not removed immediately
    all_refs = {}
    print("CACHE TYPE:", cache_factory)
    cache = cache_factory()
    for name in ["one", "two", "three"]:
        o = ExpensiveObject(name)
        cache[name] = o
        all_refs[name] = o
        del o  # decref

    print("   all_refs =", end=" ")
    pprint.pprint(all_refs)
    print("\n  Before, cache contains:", list(cache.keys()))
    for name, value in cache.items():
        print(f"    {name} = {value}")
        del value  # decref

    #Remove all references to the objects except the cache
    print("\n  Cleanup")
    del all_refs
    gc.collect()

    print("\n  After, cache contains:", list(cache.keys()))
    for name, value in cache.items():
        print(f"    {name} = {value}")
    print("  demo returning")
    return

def main():
    demo(dict)
    print()
    demo(weakref.WeakValueDictionary)


if __name__ == "__main__":
    main()
