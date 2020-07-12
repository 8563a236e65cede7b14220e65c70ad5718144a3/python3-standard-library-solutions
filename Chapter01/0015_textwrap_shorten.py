"""
Listing 1.15

To truncate text to create a summary or preview, use shorten(). All
existing whitespace, such as tabs, newlines and series of multiple
spaces, will be standardized to a single space. Then the text
will be truncated to a length less than or equal to what is requested,
between word boundaries so that no partial words are included

If non-whitespace text is removed from the original text as part of the
truncation, it is replaced with a placeholder value [...] by default.
Default can be changed by supplying placeholder argument to shorten()
"""
import textwrap
from textwrap_example import sample_text


def main():
    dedented_text = textwrap.dedent(sample_text)
    original = textwrap.fill(dedented_text, width=50)

    print("Original:\n")
    print(original)

    shortened = textwrap.shorten(original, 100)
    shortened_wrapped = textwrap.fill(shortened, width=50)

    print("\nShortened:\n")
    print(shortened_wrapped)


if __name__ == "__main__":
    main()
