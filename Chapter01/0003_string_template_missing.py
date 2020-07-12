"""
Listing 1.3

One key difference between templates and string interpolation or formatting
is that the type of the arguments is not taken into account. The values
are converted to strings, and the strings are inserted into the result.
No formatting options are available e.g. digits of floating-point value

safe_substitute() makes it possible to avoid exceptions if not all the
values needed by the template are provided as arguments
"""
import string


def main():
    values = {"var": "foo"}

    t = string.Template("$var is here but $missing is not provided")

    try:
        print("substitute(): ", t.substitute(values))
    except KeyError as err:
        print("ERROR: ", str(err))

    print("safe_substitute(): ", t.safe_substitute(values))


if __name__ == "__main__":
    main()
