"""
Listing 1.52

A positive look behind assertion can be used to find text following a
pattern using the syntax (?<=pattern).

In the following example, the expression finds Twitter handles
"""
import re


def main():
    twitter = re.compile(
        r"""
        # A twitter handle: @username
        (?<=@)
        ([\w\d_]+)  # Username
        """,
        re.VERBOSE
    )

    text = """This text includes two Twitter handles.
    One for @ThePSF, and one for the author, @doughellmann
    """

    print(text)
    for match in twitter.findall(text):
        print(f"Handle: {match}")


if __name__ == "__main__":
    main()
