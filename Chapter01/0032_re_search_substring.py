"""
Listing 1.32

The search() method of a compiled regular expression accepts optional
start and end position parameters to limit the search to a substring
of the input
"""
import re


def main():
    text = "This is some text -- with punctuation."
    pattern = re.compile(r"\b\w*is\w*\b")

    print("Text:", text)
    print()

    pos = 0
    while True:
        match = pattern.search(text, pos)
        if not match:
            break
        s = match.start()
        e = match.end()
        print("    {:>2d}  :  {:>2d} = '{}'".format(
            s, e-1, text[s:e]
        ))
        pos = e


if __name__ == "__main__":
    main()
