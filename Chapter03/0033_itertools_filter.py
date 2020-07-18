"""
Listing 3.33

The built-in function filter() returns an iterator that includes only
items for which the test function returns true

filter() differs from dropwhile() and takewhile() in that every item
is tested before it is returned
"""


def check_item(x):
    print("Testing:", x)
    return x < 1


def main():
    for i in filter(check_item, [-1, 0, 1, 2, -2]):
        print("Yielding:", i)


if __name__ == "__main__":
    main()
