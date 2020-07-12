"""
Listing 1.5

For even more complex changes, it is possible to override the pattern
attribute and define an entirely new regular expression. The pattern
provided must contain four named groups for capturing the escaped
delimiter, the name variable, a braced version of the variable name,
and invalid delimiter patterns
"""
import string


def main():
    t = string.Template("$var")
    print(t.pattern.pattern)


if __name__ == "__main__":
    main()
