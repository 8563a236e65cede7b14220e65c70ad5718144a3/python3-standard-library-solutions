"""
Listing 3.21

The tee() function returns several independent iterators (defaults to
2) based on a single original input

tee() has semantics similar to the Unix tee utility, which repeats
the values it reads from its inputs and writes them to a named file and
standard output. The iterators returned by tee() can be used to feed the
same set of data into multiple algorithms to be processed in parallel
"""
import itertools


def main():
    r = itertools.islice(itertools.count(), 5)

    (i1, i2) = itertools.tee(r)

    print("i1:", list(i1))
    print("i2:", list(i2))


if __name__ == "__main__":
    main()
