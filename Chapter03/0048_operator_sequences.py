"""
Listing 3.48

The operators for working with sequences can be organized into four
groups: building up sequences, searching for items, accessing contents
and removing items from sequences
"""
import operator


def main():
    a = [1, 2, 3]
    b = ["a", "b", "c"]

    print("a =", a)
    print("b =", b)

    print("\nConstructive:")
    print("  concat(a, b)", operator.concat(a, b))

    print("\nSearching:")
    print("  contains(a, 1)  :", operator.contains(a, 1))
    print("  contains(b, 'd'):", operator.contains(b, "d"))
    print("  countOf(a, 1)   :", operator.countOf(a, 1))
    print("  countOf(b, 'd') :", operator.countOf(b, "d"))
    print("  indexOf(a, 1)   :", operator.indexOf(a, 1))

    print("\nAccess Items:")
    print("  getitem(b, 1)                  :", operator.getitem(b, 1))
    print("  getitem(b, slice(1, 3))        :",
          operator.getitem(b, slice(1, 3)))
    print("  setitem(b, 1, 'd')             :", end=" ")
    operator.setitem(b, 1, "d")
    print(b)
    print("  setitem(a, slice(1, 3), [4,5]):", end=" ")
    operator.setitem(a, slice(1, 3), [4, 5])
    print(a)

    print("\nDestructive:")
    print("  delitem(b, 1)          :", end=" ")
    operator.delitem(b, 1)
    print(b)
    print("  delitem(a, slice(1, 3)):", end=" ")
    operator.delitem(a, slice(1, 3))
    print(a)


if __name__ == "__main__":
    main()
