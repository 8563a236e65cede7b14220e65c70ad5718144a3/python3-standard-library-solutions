"""
Listing 1.51

Instead of looking ahead for noreply in the username portion of the
email address, the pattern can alternatively be written using a negative
look behind assertion after the username is matched using the syntax
(?<!pattern)

The expression must use a fixed-length pattern. Repetitions are allowed,
as long as there is a fixed number of them (no wildcards or ranges)
"""
import re


def main():
    address = re.compile(
        r"""
        ^

        # An address: username@domail.tld

        [\w\d.+-]+      # Username
        
        #Ignore noreply addresses
        (?<!noreply)
        
        @
        ([\w\d.]+\.)+   # Domain name prefix
        (com|org|edu)   # Limit the allowed top-level domains

        $
        """,
        re.VERBOSE
    )

    candidates = [
        u"first.last@example.com",
        u"noreply@example.com"
    ]

    for candidate in candidates:
        print(f"Candidate: {candidate}")
        match = address.search(candidate)
        if match:
            print("   Match:", candidate[match.start():match.end()])
        else:
            print("   No match")


if __name__ == "__main__":
    main()
