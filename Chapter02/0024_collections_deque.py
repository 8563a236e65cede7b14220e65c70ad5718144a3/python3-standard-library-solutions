"""
Listing 2.24

A double-ended queue or deque supports adding and removing elements from
either end of the queue. The more commonly used stacks and queues are
degenerate forms of deques where the inputs and outputs are restricted
to a single end

Since deques are a type of sequence container, they support some of
the same operations as list, such as examining the contents with
__getitem__(), determining the length and removing elements from
the middle of the queue by matching identity
"""
import collections


def main():
    d = collections.deque("abcdefg")
    print("Deque:", d)
    print("Length:", len(d))
    print("Left end:", d[0])
    print("Right end:", d[-1])

    d.remove("c")
    print("remove(c):", d)


if __name__ == "__main__":
    main()
