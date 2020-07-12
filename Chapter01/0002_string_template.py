"""
Listing 1.2

String templates are intended as an alternative to the built-in
interpolation syntax. With string.Template interpolation, variables are
identified by prefixing the name with $ (e.g. $var).

Alternatively, if necessary to set them off from surrounding text, they
can be wrapped with curly braces (e.g. ${var})
"""
import string


def main():
    values = {"var": "foo"}

    t = string.Template("""
    Variable            : $var
    Escape              : $$
    Variable in text    : ${var}iable
    """)

    print("Template: ", t.substitute(values))

    s = """
    Variable            : %(var)s
    Escape              : %%
    Variable in text    : %(var)siable
    """

    print("INTERPOLATION: ", s % values)

    s = """
    Variable            : {var}
    Escape              : {{}}
    Variable in text    : {var}iable
    """

    print("FORMAT: ", s.format(**values))


if __name__ == "__main__":
    main()
