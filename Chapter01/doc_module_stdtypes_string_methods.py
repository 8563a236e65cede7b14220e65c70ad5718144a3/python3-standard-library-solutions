"""
String Methods

Strings implement all of the common sequence operations, along with the
additional methods described below.

Strings support two types of string formatting
    str.format(), Format String Syntax, Custom String Formatting
    printf-style formatting

Methods
    ---------------------------------------------------------------------
    str.capitalize()
        Returns a copy of the string with its first character capitalized
        and the rest lowercased.
    ---------------------------------------------------------------------
    str.casefold()
        Returns a casefolded copy of the string. Casefolded strings may
        be used for caseless matching.
        More aggressive than lowercasing, because it removes all case
        distinctions in the string
    ---------------------------------------------------------------------
    str.center(width[,fillchar])
        Returns centered in a string of length width. Padding done using
        specified fillchar. Original string returned if width is less
        than or equal to len(s)
    ---------------------------------------------------------------------
    str.count(sub[,start[,end]])
        Return the number of non-overlapping occurrences of substring
        sub in the range [start, end]. Optional arguments start and
        end are interpreted as in slice notation
    ---------------------------------------------------------------------
    str.encode(encoding="utf-8", errors="strict")
        Return an encoded version of the string as a bytes object.
        errors may be given to set a different error handling scheme.
        Default is "strict" which raises UnicodeError. Other possible
        values are "ignore", "replace", "xmcharrefreplace",
        "backslashreplace" and any other name registered via
        codecs.register_error()
    ---------------------------------------------------------------------
    str.endswith(suffix[,start[,end]])
        Return True if the string ends with the specified suffix,
        otherwise return False. Suffix can also be a tuple of
        suffixes to look for. With optional start, test beginning
        at that position. With optional end, stop comparing at that
        position.
    ---------------------------------------------------------------------
    str.expandtabs(tabsize=8)
        Return a copy of the string where all tab characters are replaced
        by one or more spaces, depending on the current column and the
        given tab size. Tab positions occur ever tabsize characters
        (default is 8 giving tab positions 0, 8, 16, ...)
        To expand the string, the current column is set to zero and
        the string is examined character by character.
            \t is replaced with one or more zeroes
            \n \r reset current column to zero
            any other character unchanged
    ---------------------------------------------------------------------
"""
"01\t012\t0123\t01234".expandtabs()
"01\t012\t0123\t01234".expandtabs(4)

"""
    ---------------------------------------------------------------------
    str.find(sub[,start[,end]])
        Return the lowest index in the string where substring sub is found
        withing the slice s[start:end]. Return -1 if sub is not found.
            Note, use "in" to test if substring occurs, only use find for
            index
    ---------------------------------------------------------------------
    str.format(*args, **kwargs)
        Perform a string formatting operation.
    ---------------------------------------------------------------------
    str.format_map(mapping)
        Similar to str.format(**mapping) except that mapping is used
        directly and not copied to a dict. Useful if for example mapping
        is a dict subclass
    ---------------------------------------------------------------------
"""


class Default(dict):
    def __missing__(self, key):
        return key


"{name} was born in {country}".format_map(Default(name="Guido"))

"""
    ---------------------------------------------------------------------
    str.index(sub[,start[,end]])
        Like find() but raise ValueError when substring is not found
    ---------------------------------------------------------------------
    str.isalnum()
        Return True if all characters in the string are alphanumeric and
        there is at least one character.
        False otherwise.
    ---------------------------------------------------------------------
    str.isalpha()
        Return True if all characters in the string are alphabetic and 
        there is at least one character, False otherwise. 
    ---------------------------------------------------------------------
    str.isascii()
        Returns True if the string is empty or all characters in the string
        are ASCII, False otherwise.
    ---------------------------------------------------------------------
    str.isdecimal()
        Returns True if all characters in the string are decimal characters
        and there is at least one character, False otherwise.
    ---------------------------------------------------------------------
    str.isdigit()
        Returns True if all characters in the string are digits and there
        is at least one character, False otherwise.
    ---------------------------------------------------------------------
    str.isidentifier()
        Returns True if the string is a valid identifier according to
        the language definition.
        Call keyword.iskeyword() to test whether string s is a reserved
        identifier, such as def and class
    ---------------------------------------------------------------------
"""
import keyword

("hello".isidentifier(), keyword.iskeyword("hello"))
("def".isidentifier(), keyword.iskeyword("def"))

"""
    ---------------------------------------------------------------------
    str.islower()
        Returns True if all cased characters in the string are lowercase
        and there is at least one cased character, False otherwise.
    ---------------------------------------------------------------------
    str.isnumeric()
        Returns True if all characters in the string are numeric characters
        and there is at least one character, False otherwise.
    ---------------------------------------------------------------------
    str.isprintable()
        Returns True if all characters in the string are printable or
        the string is empty. False otherwise.
    ---------------------------------------------------------------------
    str.isspace()
        Returns True if there are only whitespace characters in the string
        and there is at least one character, False otherwise.
    ---------------------------------------------------------------------
    str.istitle()
        Returns True if the string is a titlecased string and there is at
        least one character.
    ---------------------------------------------------------------------
    str.isupper()
        Returns True if all cased characters in the string are uppercase
        and there is at least one cased character, False otherwise.
    ---------------------------------------------------------------------
    str.join(iterable)
        Return a string which is the concatenation of the strings in
        iterable. A TypeError will be raised if there are any non-string
        values in iterable, including bytes objects. The separator between
        elements is the string providing this method.
    ---------------------------------------------------------------------
    str.ljust(width[,fillchar])
        Returns the string left justified in a string of length width.
        Padding is done using the specified fillchar.
        Original string is returned if width is less than or equal to
        len(s)
    ---------------------------------------------------------------------
    str.lower()
        Returns a copy of the string with all the cased characters
        converted to lowercase.
    ---------------------------------------------------------------------
    str.lstrip([chars])
        Return a copy of the string with leading characters removed. The
        chars argument is a string specifying the set of characters to be
        removed. If omitted or None, the chars argument defaults to 
        removing whitespace.
"""
"           spacious           ".lstrip()
"www.example.com".lstrip("cmowz.")

"""
    ---------------------------------------------------------------------
    static str.maketrans(x[,y[,z]])
        This static method returns a translation table usable for
        str.translate().
    ---------------------------------------------------------------------
    str.partition(sep)
        Split the string at the first occurrence of sep, and return a
        3-tuple containing the part before the separator, the separator
        itself and the part after the separator. If the separator is
        not found, return a 3-tuple containing the string itself, followed
        by two empty strings
    ---------------------------------------------------------------------
    str.replace(old, new[,count])
        Return a copy of the string with all occurrences of substring old
        replaced by new. If the optional argument count is given, only the
        first count occurrences are replaced.
    ---------------------------------------------------------------------
    str.rfind(sub[,start[,end]])
        Return the highest index in the string where substring sub is
        found, such that sub is contained within s[start:end]. Return -1
        if not found
    ---------------------------------------------------------------------
    str.rindex(sub[,start[,end]])
        Like rfind() but raises ValueError when the substring sub is not
        found.
    ---------------------------------------------------------------------
    str.rjust(width[,fillchar])
        Return the string right justified in a string of length width.
        Padding is done using fillchar. The original string is returned
        if width is less than or equal to len(s)
    ---------------------------------------------------------------------
    str.rpartition(sep)
        Split the string at the last occurrence of sep, and return a
        3-tuple containing the part before the separator, the separator
        itself and the part after the separator. If the separator is
        not found, return a 3-tuple containing the string itself, followed
        by two empty strings
    ---------------------------------------------------------------------
    str.rsplit(sep=None, maxsplit=-1)
        Return a list of the words in the string, using sep as the 
        delimiter string. If maxsplit is given, at most maxsplit splits 
        are done, the rightmost ones. If sep is not specified or None,
        any whitespace string is a separator.
    ---------------------------------------------------------------------
    str.rstrip([chars])
        Return a copy of the string with trailing characters removed. The
        chars argument is a string specifying the set of characters to be
        removed. If omitted or None, the chars argument defaults to 
        removing whitespace.
    ---------------------------------------------------------------------
"""
"           spacious           ".rstrip()
"mississippi".rstrip("ipz")

"""
    ---------------------------------------------------------------------
    str.split(sep=None, maxsplit=-1)
        Return a list of the words in a the string, using sep as the
        delimeter string. If maxsplit is given, at most maxsplit splits
        are done. If maxsplit is not specified or -1, then there is no
        limit on the number of splits (all possible splits are made).
        
        If sep is given, consecutive delimiters are not grouped together
        and are deemed to delimit emtpy strings. The sep argument may
        consist of multiple characters. Splitting an empty string with
        a specified separator returns ['']
        
        If sep is not specified or is None, a different splitting
        algorithm is applied: runs of consecutive whitespace are regarded
        as a single separator and the result will contain no empty strings
        at the start or end of the string if the string has leading or
        trailing whitespace.
        ---------------------------------------------------------------------
"""
"1,2,3".split(",")
"1,2,3".split(",", maxsplit=1)
"1,2,,3".split(",")
"1 2 3".split()
"1 2 3".split(maxsplit=1)
"    1   2    3    ".split()

"""
    ---------------------------------------------------------------------
    str.splitlines([keepends])
        Return a list of lines in the string, breaking at line boundaries.
        Line breaks are not included in the resulting list unless keepends
        is given and true.
        Split at universal newlines
            \n, \r, \r\n, \v or \x0b. \f or \x0c, \x1c, \x1d, \x1e,
            \x85, \u2028, \u2029
    ---------------------------------------------------------------------
"""
"ab c\n\nde fg\rkl\r\n".splitlines()
"ab c\n\nde fg\rkl\r\n".splitlines(keepends=True)
"".splitlines()
"One line\n".splitlines()
"".split("\n")
"Two lines\n".split("\n")

"""
    ---------------------------------------------------------------------
    str.startswith(prefix[,start[,end]])
        Returns True if string starts with the prefix, otherwise return 
        False. prefix can also be a tuple of prefixes to look for
    ---------------------------------------------------------------------
    str.strip([chars])
        Returns a copy of the string with the leading and trailing 
        characters removed. The chars argument is a string specifying the
        set of characters to be removed. If omitted or None, the chars 
        argument defaults to removing whitespace.
    ---------------------------------------------------------------------
"""
"    spacious    ".strip()
"www.example.com".strip("cmowz.")
comment_string = "#...........Section 3.2.1 Issue #32.......... "
comment_string.strip(".#! ")

"""
    ---------------------------------------------------------------------
    str.swapcase()
        Return a copy of the string with uppercase characters converted
        to lowercase and vice versa. Note that it is not necessarily true
        that s.swapcase().swapcase() == s
    ---------------------------------------------------------------------
    str.title()
        Return a titlecased version of the string where words start with an
        uppercase character and the remaining characters are lowercase.
        Note that the algorithm uses a simple definition of a word, thus
        apostrophes in contractions and possessives form word boundaries
        which may not be the desired result. A workaround for apostrophes
        can be constructed using regular expressions
    ---------------------------------------------------------------------
"""
"Hello world".title()
"they're bill's friends from the UK".title()

import re


def titlecase(s):
    return re.sub(r"[A-za-z]+('[A-Za-z]+)?",
                  lambda mo: mo.group(0).capitalize(),
                  s)


titlecase("they're bill's friends.")

"""
    ---------------------------------------------------------------------
    str.translate(table)
        Return a copy of the string in which each character has been mapped
        through the given translation table. The table must be an object that
        implements indexing via __getitem__(), typically a mapping or sequence.
    ---------------------------------------------------------------------
    str.upper()
        Returns a copy of the string with all the cased characters converted
        to uppercase.
        Note s.upper().isupper() might be False if s contains uncased characters
    ---------------------------------------------------------------------
    str.zfill(width)
        Return a copy of the string left filled with ASCII "0" digits to
        make a string of length width. The original string is returned if
        width is less than or equal to len(s)
    ---------------------------------------------------------------------
"""
"42".zfill(5)
"-42".zfill(5)

"""
printf-style String Formatting
    String objects have one unique built-in operation:
    the % operator.
    This is known as the string formatting or interpolation operator.
    Given format % values (where format is a string), % conversion
    specifications in format are replaced with zero or more elements of
    values.
    
    If format requires a single argument, values may be a single
    non-tuple object. Otherwise, values must be a tuple with exactly
    the number of items specified by the format string or a single
    mapping object e.g. dictionary
    
    A conversion specifier contains two or more characters and has
    the following components, which must occur in this order:
        1) %
        2) Mapping key (optional), consisting of a parenthesised 
        sequence of characters
        3) Conversion flags (optional)
        4) Minimum field width (optional)
        5) Precision (optional)
        6) Length Modifier (optional)
        7) Conversion type
        
    When the right argument is a dictionary, then the formats in
    the string must include a parenthesised mapping key into that
    dictionary inserted immediately after the % character. The
    mapping key selects the value to be formatted from the mapping 
"""
print("%(language)s has %(number)03d quote types." %
      {"language": "Python", "number": 2})

"""
    Conversion flag characters:
        #   Alternate form
        0   Zero padded numeric values
        -   Left adjusted
        " " Blank should be left before a positive number
        +   A sign character will precede the conversion
        
    Conversion types
        d   Signed integer decimal
        i   Signed integer decimal
        o   Signed octal value
        u   Obsolete
        x   Signed hexademical (lowercase)
        X   Signed hexademical (uppercase)
        e   Floating point exponential (lowercase)
        E   Floating point exponential (uppercase)
        f   Floating point decimal format
        F   Floating point decimal format
        g   Floating point format
        G   Floating point format
        c   Single character
        r   String (repr)
        s   String (str)
        a   String (ascii)
        %   No argument is converted
"""