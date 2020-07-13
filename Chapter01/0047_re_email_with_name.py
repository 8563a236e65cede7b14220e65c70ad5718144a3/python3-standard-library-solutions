"""
Listing 1.47

This expanded version parses inputs that include a person's name and email
address, as might appear in an email header. The name comes first and
stands on its own, and the email address follows, surrounded by angle
brackets (< and >)
"""
import re


def main():
    address = re.compile(
        r"""
        # A name is made up of letters and may include "."
        # for title abbreviations and middle initials.
        ((?P<name>
            ([\w.,]+\s+)*[\w.,]+)
            \s*
            # Email addresses are wrapped in angle brackets < >, but
            # only if a name is found, so keep the start bracket in
            # this group
            <
        )? # The entire name is optional
        
        #The address itself: username@domain.tld
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
        u"first.last@example.com",
        u"first.last+category@gmail.com",
        u"valid-address@mail.example.com",
        u"not-valid@example.foo",
        u"First Last <first.last@example.com>",
        u"No Brackets first.last@example.com",
        u"First Last",
        u"First Middle Last <first.last@example.com>",
        u"First M. Last <first.last@example.com>",
        u"<first.last@example.com>"
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
