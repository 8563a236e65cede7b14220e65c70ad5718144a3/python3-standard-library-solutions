"""
Listing 1.50

A negative look ahead assertion ((?!pattern)) says that the pattern
does not match the text following the current point. For example,
the email recognition pattern could be modified to ignore the noreply
mailing address commonly used by automated systems
"""
import re


def main():
    address = re.compile(
        r"""
        ^
        
        # An address: username@domail.tld
        
        #Ignore noreply addresses
        (?!noreply@.*$)
        
        [\w\d.+-]+      # Username
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
