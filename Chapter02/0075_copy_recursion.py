"""
Listing 2.75

To avoid problems with duplicating recursive data structures, deepcopy()
uses a dictionary to track objects that have already been copied. The
dictionary is passed to the __deepcopy__() method so it can be examined
there as well
"""
import copy


class Graph:

    def __init__(self, name, connections):
        self.name = name
        self.connections = connections

    def add_connection(self, other):
        self.connections.append(other)

    def __repr__(self):
        return f"Graph(name={self.name}, id={id(self)})"

    def __deepcopy__(self, memo):
        print(f"\nCalling __deepcopy__ for {self!r}")
        if self in memo:
            existing = memo.get(self)
            print(f"  Already copied to {existing!r}")
            return existing
        print("  Memo dictionary:")
        if memo:
            for k, v in memo.items():
                print(f"    {k}: {v}")
        else:
            print("    (empty)")

        dup = Graph(copy.deepcopy(self.name, memo), [])
        print(f"  Copying to new object {dup}")
        memo[self] = dup

        for c in self.connections:
            dup.add_connection(copy.deepcopy(c, memo))
        return dup


def main():
    root = Graph("root", [])
    a = Graph("a", [root])
    b = Graph("b", [a, root])
    root.add_connection(a)
    root.add_connection(b)

    dup = copy.deepcopy(root)


if __name__ == "__main__":
    main()
