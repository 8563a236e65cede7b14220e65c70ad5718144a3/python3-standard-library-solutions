"""
Listing 1.6

This example defines a new patterns to create a new type of template,
using {{var}} as the variable syntax
"""
import re
import string


class MyTemplate(string.Template):
    delimiter = "{{"
    pattern = r"""
    \{\{(?:
    (?P<escaped>\{\{) |
    (?P<named>[_a-z][_a-z0-9]*)\}\} |
    (?P<braced>[a-z][_a-z09]*)\}\} |
    (?P<invalid>)
    )
    """


def main():
    t = MyTemplate("""
    {{{{
    {{var}}
    """)

    print("MATCHES: ", t.pattern.findall(t.template))
    print("SUBSTITUTED: ", t.safe_substitute(var="replacement"))


if __name__ == "__main__":
    main()
