"""
Listing 1.49

In many cases, it is useful to match a part of a pattern only if some
other part will also match.

For example, in the email parsing expression, the angle brackets were
marked as optional.

Realistically, the brackets should be paired, and the expression should
match only if both are present, or neither is. This modified version
of the expression uses a positive look ahead assertion to match
the pair.

The look ahead assertion syntax is (?=pattern)
"""
import re


def main():
    address = re.compile(
        r"""
        # A name is made up of letters and may include "."
        # for title abbreviations and middle initials.
        ((?P<name>
            ([\w.,]+\s+)*[\w.,]+)
            \s+
        ) # The name is no longer optional
        
        # LOOKAHEAD
        # Email addresses are wrapped in angle brackets, but only
        # if both are present or neither is
        (?= (<.*>$)         # Remainder wrapped in angle brackets
            |
            ([^<].*[^>]$)   # Remainder *not wrapped in angle brackets 
        )
        
        <? # Optional opening angle bracket
        
        # The address itself: username@domain.tld
        (?P<email>
            [\w\d.+-]+      # Username
            @
            ([\w\d.]+\.)+   # Domain name prefix
            (com|org|edu)   # Limit the allowed top-level domains
        )

        >? # Optional closing angle bracket.
        """,
        re.VERBOSE
    )

    candidates = [
        u"First Last <first.last@example.com>",
        u"No Brackets first.last@example.com",
        u"Open Bracket <first.last@example.com",
        u"Close Bracket first.last@example.com>",
    ]

    for candidate in candidates:
        print("Candidate: ", candidate)
        match = address.search(candidate)
        if match:
            print("   Name :", match.groupdict()["name"])
            print("   Email:", match.groupdict()["email"])
        else:
            print("   No Match")


if __name__ == "__main__":
    main()
