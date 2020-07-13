"""
Listing 1.66

All of the functions that produce difference sequences accept arguments to
indicate which lines should be ignored and which characters within a line
should be ignored. These parameters can be used to skip over markup or
whitespace changes in two versions of a file

The default for Differ is to not ignore any lines or characters explicitly,
but rather to rely on the ability of SequenceMatcher to detect noise. The
default for ndiff() is to ignore space and tab characters
"""
# This example is adapted from the source for difflib.py
import difflib

A = " abcd"
B = "abcd abcd"


def show_results(match):
    print(f"  a    = {match.a}")
    print(f"  b    = {match.b}")
    print(f"  size = {match.size}")
    (i, j, k) = match
    print(f"  A[a:a+size] = {A[i:i+k]!r}")
    print(f"  B[b:b+size] = {B[j:j + k]!r}")


def main():
    print(f"A = {A!r}")
    print(f"B = {B!r}")

    print("\nWithout junk detection:")
    s1 = difflib.SequenceMatcher(None, A, B)
    match1 = s1.find_longest_match(0, len(A), 0, len(B))
    show_results(match1)

    print("\nTreat spaces as junk:")
    s2 = difflib.SequenceMatcher(lambda x: x == " ", A, B)
    match2 = s2.find_longest_match(0, len(A), 0, len(B))
    show_results(match2)


if __name__ == "__main__":
    main()
