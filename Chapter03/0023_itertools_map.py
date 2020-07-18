"""
Listing 3.23

The built-in map() function returns an iterator that calls a function
on the values in the input iterators, and returns the results. It stops
when any input iterator is exhausted.
"""


def times_two(x):
    return 2 * x


def multiply(x, y):
    return (x, y, x * y)


def main():
    print("Doubles:")
    for i in map(times_two, range(5)):
        print(i)

    print("\nMultiples:")
    r1 = range(5)
    r2 = range(5, 10)
    for i in map(multiply, r1, r2):
        print(f"{i[0]:d} * {i[1]:d} = {i[2]:d}")

    print("\nStopping:")
    r1 = range(5)
    r2 = range(2)
    for i in map(multiply, r1, r2):
        print(i)


if __name__ == "__main__":
    main()
