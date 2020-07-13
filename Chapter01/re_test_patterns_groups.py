"""
Listing 1.37
"""
import re


def test_patterns(text, patterns):
    """
    Given source text and a list of patterns, look for matches for
    each pattern within the text and print them to stdout
    :param text:
    :param patterns:
    :return:
    """
    # Look for each pattern in the text and print the results
    for pattern, desc in patterns:
        print(f"{pattern!r}  ({desc})")
        print(f"  {text!r}")
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            prefix = " " * (s)
            print(f"  {prefix}{text[s:e]!r}{' ' * (len(text) - e)}  ",
                  end=" ")
            print(match.groups())
            if match.groupdict():
                print(f"{' ' * (len(text) - s)}{match.groupdict()}")
        print()
    return
