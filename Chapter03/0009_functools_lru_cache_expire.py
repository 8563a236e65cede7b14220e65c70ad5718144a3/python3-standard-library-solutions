"""
Listing 3.9

To prevent the cache from growing without bounds in a long-running process
it is given a maximum size. The default is 128 entries, but that size can
be changed for each cache using the maxsize argument
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
    print("Establish the cache")
    make_call(1, 2)
    make_call(2, 3)

    print("\nUse cached items")
    make_call(1, 2)
    make_call(2, 3)

    print("\nCompute a new value, triggering cache expiration")
    make_call(3, 4)

    print("\nCache still contains one old item")
    make_call(2, 3)

    print("\nOldest item needs to be recomputed")
    make_call(1, 2)


if __name__ == "__main__":
    main()
