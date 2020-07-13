"""
Listing 1.46

Converting the expression to a more verbose format will make it easier
to extend
"""
import re


def main():
    address = re.compile(
        r"""
        [\w\d.+-]+      # Username
        @
        ([\w\d.]+\.)+   # Domain name prefix
        (com|org|edu)   # TODO: support more top-level domains
        """,
        re.VERBOSE
    )
    
    candidates = [
        u"first.last@example.com",
        u"first.last+category@gmail.com",
        u"valid-address@mail.example.com",
        u"not-valid@example.foo"
    ]

    for candidate in candidates:
        match = address.search(candidate)
        print(f"{candidate:<30}  {'Matches' if match else 'No match'}")


if __name__ == "__main__":
    main()
