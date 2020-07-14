"""
Listing 2.21

Use most_common() to produce a sequence of the n most frequently
encountered input values and their respective counts
"""
import collections


def main():
    c = collections.Counter()
    with open("/usr/share/dict/words", "rt") as f:
        for line in f:
            c.update(line.rstrip().lower())

    print("Most common:")
    for letter, count in c.most_common():
        print(f"{letter}: {count:>7}")


if __name__ == "__main__":
    main()
