"""
Listing 1.20

Regular expressions support more powerful patterns than simple literal
text strings. Patterns can repeat, can be anchored to different logical
locations within the input, and can be expressed in compact forms that
do nto require every literal character to be present in the pattern.

All of these features are used by combining literal text values with
meta-characters that are part of the regular expression pattern syntax
implemented by re
"""
import re


def test_patterns(text, patterns):
    """
    Given source text and a list of patterns, look for matches for each
    pattern within the text and print them to stdout.
    :param text:
    :param patterns:
    :return:
    """
    # Look for each pattern in the text and print the results
    for pattern, desc in patterns:
        print(f"'{pattern}' ({desc})\n")
        print(f"     '{text}")
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            n_backslashes = text[:s].count("\\")
            prefix = "." * (s + n_backslashes)
            print(f"     {prefix}'{substr}'")
        print()
    return


def main():
    test_patterns("abbaaabbbbaaaaa",
                  [
                      ("ab", "'a' followed by 'b'")
                  ])


if __name__ == "__main__":
    main()
