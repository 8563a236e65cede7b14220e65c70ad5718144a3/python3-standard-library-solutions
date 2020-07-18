"""
Listing 3.51

Item getters work like lambda x,y=5: x[y]:
"""
import operator

def main():
    l = [dict(val=-1 * i) for i in range(4)]
    print("Dictionaries:")
    print("  original:", l)
    g = operator.itemgetter("val")
    vals = [g(i) for i in l]
    print("   values:", vals)
    print("   sorted:", sorted(l, key=g))

    print()
    l = [(i, i * -2) for i in range(4)]
    print("\nTuples:")
    print("  original:", l)
    g = operator.itemgetter(1)
    vals = [g(i) for i in l]
    print("   values:", vals)
    print("   sorted:", sorted(l, key=g))


if __name__ == "__main__":
    main()
