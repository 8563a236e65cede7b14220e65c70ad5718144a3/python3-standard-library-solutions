"""
Listing 1.54

Python's expression parser includes an extension that uses (?P=name) to
refer to the value of a named group matched earlier in the expression.
"""
import re


def main():
    address = re.compile(
        r"""

        # The regular name
        (?P<first_name>\w+)           # First name
        \s+
        (([\w.]+)\s+)?  # Optional middle name or initial
        (?P<last_name>\w+)           # Last name

        \s+

        <

        # The address: first_name.last_name@domain.tld
        (?P<email>
            (?P=first_name)
            \.
            (?P=last_name)
            @
            ([\w\d.]+\.)+   # Domain name prefix
            (com|org|edu)   # Limit the allowed top-level domains
        )

        >
        """,
        re.VERBOSE | re.IGNORECASE
    )

    candidates = [
        u"First Last <first.last@example.com>",
        u"Different Name <first.last@example.com>",
        u"First Middle Last <first.last@example.com>",
        u"First M. Last <first.last@example.com>"
    ]

    for candidate in candidates:
        print(f"Candidate: {candidate}")
        match = address.search(candidate)
        if match:
            print("  Match name :", match.groupdict()["first_name"], end=" ")
            print(match.groupdict()["last_name"])
            print("  Match email:", match.groupdict()["email"])
        else:
            print("  No match")


if __name__ == "__main__":
    main()
