"""
Listing 1.13

To control which lines receive the new prefix, pass a callable as the
predicate argument to indent. The callable will be invoked for each
line of text in turn, and the prefix will be added for lines where the
return value is true
"""
import textwrap
from textwrap_example import sample_text


def should_indent(line):
    print("Indent {!r}?".format(line))
    return len(line.strip()) % 2 == 0


def main():
    dedented_text = textwrap.dedent(sample_text)
    wrapped = textwrap.fill(dedented_text, width=50)
    final = textwrap.indent(wrapped, "EVEN ", predicate=should_indent)
    print("\nQuoted block:\n")
    print(final)


if __name__ == "__main__":
    main()
