"""
Listing 3.10

The keys for the cache managed by lru_cache() must be hashable, so all of
the arguments to the function wrapped with the cache lookup must be
hashable
"""
import functools


@functools.lru_cache(maxsize=2)
def expensive(a, b):
    print(f"called expensive({a}, {b})")
    return a * b


def make_call(a, b):
    print(f"({a}, {b})", end=" ")
    pre_hits = expensive.cache_info().hits
    expensive(a, b)
    post_hits = expensive.cache_info().hits
    if post_hits > pre_hits:
        print("cache hit")


def main():
    make_call(1, 2)
    try:
        make_call([1], 2)
    except TypeError as err:
        print(f"ERROR: {err}")

    try:
        make_call(1, {"2": "two"})
    except TypeError as err:
        print(f"ERROR: {err}")


if __name__ == "__main__":
    main()
