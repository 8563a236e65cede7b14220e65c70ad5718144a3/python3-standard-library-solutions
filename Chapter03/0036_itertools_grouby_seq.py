"""
Listing 3.36

The groupby() function returns an iterator that produces sets of values
organized by a common key.
"""
import functools
import itertools
import operator
import pprint


@functools.total_ordering
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __gt__(self, other):
        return (self.x, self.y) > (other.x, other.y)


def main():
    # Create a data set of Point instances
    data = list(
        map(
            Point,
            itertools.cycle(itertools.islice(itertools.count(), 3)),
            itertools.islice(itertools.count(), 7)
        )
    )
    print("Data:")
    pprint.pprint(data, width=35)
    print()

    # Try to group the unsorted data based on X values
    print("Grouped, unsorted:")
    for k, g in itertools.groupby(data, operator.attrgetter("x")):
        print(k, list(g))
    print()

    # Sort the data
    data.sort()
    print("Sorted:")
    pprint.pprint(data, width=35)
    print()

    # Group the sorted data based on X values
    print("Grouped, sorted:")
    for k, g in itertools.groupby(data, operator.attrgetter("x")):
        print(k, list(g))
    print()


if __name__ == "__main__":
    main()
