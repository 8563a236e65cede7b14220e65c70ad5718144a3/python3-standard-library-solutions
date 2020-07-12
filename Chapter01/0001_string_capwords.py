"""
Listing 1.1

The function capwords() capitalizes all of the words in a string
"""
import string


def main():
    s = "The quick brown fox jumped over the lazy dog."
    print(s)
    print(string.capwords(s))


if __name__ == "__main__":
    main()
