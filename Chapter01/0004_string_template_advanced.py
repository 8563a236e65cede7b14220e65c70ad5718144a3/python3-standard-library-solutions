"""
Listing 1.4

The default syntax for string.Template can be changed by adjusting the
regular expression patterns it uses to find the variable names in the
template body. A simple way to do that is to change the delimiter and
idpattern class attributes
"""
import string


class MyTemplate(string.Template):
    delimiter = "%"
    idpattern = "[a-z]+_[a-z]+"


def main():
    template_text = """
        Delimiter   : %%
        Replaced    : %with_underscore
        Ignored     : %notunderscored
    """

    d = {
        "with_underscore": "replaced",
        "notunderscored": "not replaced"
    }

    t = MyTemplate(template_text)
    print("Modified ID pattern: ")
    print(t.safe_substitute(d))


if __name__ == "__main__":
    main()
