"""
Listing 1.67

The SequenceMatcher class compares two sequences of any types, as long
as the values are hashable. It uses an algorithm to identify the longest
contiguous matching blocks from the sequences, elimination "junk" values
that do not contribute to the real data.

The function get_opcodes() returns a list of instructions for modifying
the first sequence to make it match the second. The instructions are
encoded as five-element typles, including a single instruction (the
"opcode") and two pairs of start and stop indexes into the sequences,
(denoted as i1, i2, j1, j2)

    Opcode          Definition
    "replace"       Replace a[i1:i2] with b[j1:j2]
    "delete"        Remove a[i1:i2] entirely
    "insert"        Insert b[j1:j2] at a[i1:i2]
    "equal"         The subsequences are already equal

This example compares two lists of integers and uses get_opcodes() to
derive the instructions for converting the original list into the newer
version. The modifications are applied in reverse order so that the
list indexes remain accurate after items are added and removed

Sequence Matcher works with custom classes, as well as built-in types,
as long as they are hashable
"""
import difflib


def main():
    s1 = [1, 2, 3, 5, 6, 4]
    s2 = [2, 3, 5, 4, 6, 1]

    print("Initial data:")
    print("s1 = ", s1)
    print("s2 = ", s2)
    print("s1 == s2: ", s1 == s2)
    print()

    matcher = difflib.SequenceMatcher(None, s1, s2)
    for tag, i1, i2, j1, j2 in reversed(matcher.get_opcodes()):
        if tag == "delete":
            print(f"Remove {s1[i1:i2]} from positions [{i1}:{i2}]")
            print("  before =", s1)
            del s1[i1:i2]
        elif tag == "equal":
            print(f"s1[{i1}:{i2}] and s2[{j1}:{j2}] are the same")
        elif tag == "insert":
            print(f"Insert {s2[j1:j2]} from s2[{j1}:{j2}] into s1 at {i1}")
            print("  before =", s1)
            s1[i1:i2] = s2[j1:j2]
        elif tag == "replace":
            print(f"Replace {s1[i1:i2]} from s1[{i1}:{i2}] with "
                  f"{s2[j1:j2]} from s2[{j1}:{j2}]")
            print("  before =", s1)
            s1[i1:i2] = s2[j1:j2]

        print("   after =", s1, "\n")

    print("s1 == s2:", s1 == s2)


if __name__ == "__main__":
    main()
