"""
Listing 2.40

It is possible to change the order of the keys in an OrderedDict by
moving them to either the beginning or the end of the sequence using
move_to_end()

The last argument tells move_to_end() whether to move the item to be
the last item in the key sequence (when True) or the first (when False)
"""
import collections


def main():
    d = collections.OrderedDict(
        [("a", "A"), ("b", "B"), ("c", "C")]
    )
    print("Before:")
    for k, v in d.items():
        print(k, v)

    d.move_to_end("b")

    print("\nmove_to_end():")
    for k, v in d.items():
        print(k, v)

    d.move_to_end("b", last=False)
    print("\nmove_to_end(last=False):")
    for k, v in d.items():
        print(k, v)


if __name__ == "__main__":
    main()
