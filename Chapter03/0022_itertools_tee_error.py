"""
Listing 3.22

The new iterators created by tee() share their input, so the original
iterator should not be used after the new ones are created.

If values are consumed from the original input, the new iterators will
not produce those values
"""
import itertools


def main():
    r = itertools.islice(itertools.count(), 5)
    (i1, i2) = itertools.tee(r)

    print("r:", end=" ")
    for i in r:
        print(i, end=" ")
        if i > 1:
            break
    print()

    print("i1:", list(i1))
    print("i2:", list(i2))


if __name__ == "__main__":
    main()
