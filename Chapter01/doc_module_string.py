"""
string - Common String Operations

String constants
--------------------------------------------------------------------------
string.ascii_letters
    The concatenation of the ascii_lowercase and ascii_uppercase
    constants. Not locale-dependent
--------------------------------------------------------------------------
string.ascii_lowercase
    "abcdefghijklmnopqrstuvwxyz"
--------------------------------------------------------------------------
string.ascii_uppercase
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
--------------------------------------------------------------------------
string.digits
    "0123456789"
--------------------------------------------------------------------------
string.hexdigits
    "0123456789abcdefABCDEF"
--------------------------------------------------------------------------
string.octdigits
    "01234567"
--------------------------------------------------------------------------
string.punctuation
    !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
--------------------------------------------------------------------------
string.printable
    String of ASCII characters which are considered printable. This is
    a combination of digits, ascii_letters, punctuation, and whitespace
--------------------------------------------------------------------------
string.whitespace
    A string containing all ASCII characters that are considered
    whitespace. This includes the characters space, tab, linefeed,
    return, formfeed and vertical tab
--------------------------------------------------------------------------


Custom String Formatting
    The built-in string class provides the ability to do complex variable
    substitutions and value formatting via the format() method.
    The Formatter class in the string module allows you to create
    and customize your own string formatting behaviours using the same
    implementation as the built-in format() method

class string.Formatter
    The Formatter class has the following public methods:
    ----------------------------------------------------------------------
    format(format_string, /, *args, **kwargs_
        Primary API method. Takes a format string and an arbitrary set of
        positional and keyword arguments. It is just a wrapper that calls
        vformat()
        - from version 3.7, format string argument is now positional-only
    ----------------------------------------------------------------------
    vformat(format_string, args, kwargs)
        Does the actual work of formatting. It is exposed as a separate
        function for cases where you want to pass in a predefined
        dictionary of arguments, rather than unpacking and repacking
        the dictionary os individual arguments using *args and **kwargs
        Does the work of breaking up the format string into character data
        and replacement fields. Calls the various methods below
    ----------------------------------------------------------------------

    The Formatter defines a number of methods that are intended to be
    replaced by subclasses:
    ----------------------------------------------------------------------
    parse(format_string)
    Loop over the format_string and return an iterable of tuples
    (literal_text, field_name, format_spec, conversion)
    Values in the tuple conceptually represent a span of literal
    text followed by a single replacement field.
    If there is no literal text, then literal_text will be
    a zero length string. If there is no replacement field, then the
    values of field_name, format_spec and conversion will be None
    ----------------------------------------------------------------------
    get_field(field_name, args, kwargs)
    Given field_name as returned by parse, conver it to an object to be
    formatted. Returns a tuple (obj, used_key).
    Return value used_key has the same meaning as the key parameter to
    get_value()
    ----------------------------------------------------------------------
    get_value(key, args, kwargs)
    Retrieve a given field value. The key value will either be an integer
    or string. If it is an integer, represents the index of the positional
    argument in args. If it is a string, represents named argument in
    kwargs.

    args parameter set to list of positional arguments to vformat(),
    kwargs is set to dictionary of keyword arguments

    For compound field names, these functions are only called for the
    first component of the field name; subsequent components are handled
    through normal attribute and indexing operations.

    If index or keyword refers to an item that does not exist, then an
    IndexError or KeyError should be raised.
    ----------------------------------------------------------------------
    check_unused_args(used_args, args, kwargs)
    Implement checking for unused arguments if desired. check_unused_args()
    is assumed to raise an exception if the check fails
    ----------------------------------------------------------------------
    format_field(value, format_spec)
    simply calls the global format() built-in. This method is provided so
    that subclasses can override it
    ----------------------------------------------------------------------
    convert_field(value, conversion)
    Converts the value (returned by get_field()) given a conversion type
    (as in the tuple returned by the parse() method). The default version
    understands "s" (str), "r" (repr) and "a" (ascii) conversion types
    ----------------------------------------------------------------------


Format String Syntax
    Format strings contain "replacement fields" surrounded by curly
    braces {}. Anything that is not contained in braces is considered
    literal text, which is copied unchanged to the output.
    If you need to include a brace character in the literal text,
    it can be escaped by doubling: {{ and }}

    The field_name itself begins with an arg_name that is either a
    number or a keyword. If its a number, it refers to a positional
    argument. If it's a keyword, refers to a named keyword.

    Grammar for a replacement field:
    replacement_field ::=  "{" [field_name] ["!" conversion] [":" format_spec] "}"
    field_name        ::=  arg_name ("." attribute_name | "[" element_index "]")*
    arg_name          ::=  [identifier | digit+]
    attribute_name    ::=  identifier
    element_index     ::=  digit+ | index_string
    index_string      ::=  <any source character except "]"> +
    conversion        ::=  "r" | "s" | "a"
    format_spec       ::=  <described in the next section>

    An expression of the form ".name" selects the named attribute
    using getattr(), while an expression of the form "[index]" does
    an index lookup using __getitem__()
"""
eg1 = "First, thou shalt count to {0}"  # First positional argument
eg2 = "Bring me a {}"  # Implicitly references first positional argument
eg3 = "From {} to {}"  # Same as "From {0} to {1}"
eg4 = "My quest is {name}"  # References keyword argument
eg5 = "Weight in tons = {0.weight}"  # "weight" attribute of first positional arg
eg6 = "Units destroyed: {players[0]}"  # First element of keyword arg players


class WeightObject:
    def __init__(self, weight):
        self.weight = weight


weight_obj = WeightObject(10)
players = [100, 90, 80]

eg1.format(10)
eg2.format("knife")
eg3.format("A", "B")
eg4.format(name="Python")
eg5.format(weight_obj)
eg6.format(players=players)

"""
    The conversion field causes a type coercion before formatting.
    Normally, the formatting is done by the __format__() method of
    the value itself, however, you can cast to string to override
    the default method.

    Three conversion flags are supported
        "!s" calls str()
        "!r" calls repr()
        "!a" calls ascii()
"""
eg7 = "Harold's a clever {0!s}"  # Calls str()
eg8 = "Bring out the holy {name!r}"  # Calls repr()
eg9 = "More {!a}"  # Calls ascii() on the argument


class PrintObj:
    def __init__(self, init):
        self.attr = init

    def __str__(self):
        return "__str__ " + str(self.attr)

    def __repr__(self):
        return "__repr__\t\n" + str(self.attr)


print_obj = PrintObj(1)
eg7.format(print_obj)
eg8.format(name=print_obj)
eg9.format(print_obj)

"""
    The format_spec field contains a specification of how the value 
    should be presented, including such details as field width,
    alignment, padding, decimal precision and so on.
    Each value type can define its own "formatting mini-language"
    or interpretation of the format_spec
    
    Most built-in types support a common formatting mini-language
    
    A format_spec field can also include nested replacement fields
    within it. These nested replacement fields may contain a field name,
    conversion flag and format specification, but deeper nesting is
    not allowed. Replacement fields are substituted before format_spec
    is interpreted.
    

Format Specification Mini-Language
    "Format specifications" are used within replacement fields contained
    within a format string to define how individual values are 
    presented. They can also be passed directly to the built-in format()
    function.
    
    A general convention is that an empty format specification produces
    the same result as if you had called str() on the value. A non-empty
    format specification typically modifies the result
    
    The general form of a standard format specifier is:
    format_spec     ::=  [[fill]align][sign][#][0][width][grouping_option][.precision][type]
    fill            ::=  <any character>
    align           ::=  "<" | ">" | "=" | "^"
    sign            ::=  "+" | "-" | " "
    width           ::=  digit+
    grouping_option ::=  "_" | ","
    precision       ::=  digit+
    type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
    
    If a valid align value is specified, it can be preceded by a fill
    character that can be any character and defaults to a space if
    omitted. It is not possible to use a literal curly brace ("{" or :}")
    as the fill character in a formatted string literal or when using the
    str.format() method.
    
    < Forces left-alignment within available space
    < Forces right-alignment within available space
    = Forces padding to be placed after the sign (if any) but before
    the digits
    ^ Forces the field to be centered
    
    Unless a minimum field width is defined, the field width will always
    be the same size as the data to fill it, so that the alignment option
    has no meaning in this case.
    
    The sign option is only valid for number types
    + indicates that a sign should be used for both positive as well
    as negative numbers
    - indicated that a signed should be used only for negative numbers
    space indicates that a leading space should be used on positive numbers,
    and a minus sign on negative numbers
    
    "#" option causes the "alternate form" to be used for conversion.
    Only valid for integer, float, complex and Decimal types.
    
    "," signals the use of a comma for a thousands separator.
    
    "_" signals the use of an underscore for a thousands separator
    
    width is a decimal integer defining the minimum total field width,
    including any prefixes, separators and other formatting characters
    
    precision determines how many digits should be displayed after the 
    decimal point for a floating point value. For non number types,
    indicates the maximum field size
    
    type determines how the data should be presented
        string
            "s" String format
            None Same as "s"
        
        integer
            "b" binary
            "c" converts integer to unicode character
            "d" decimal integer
            "o" octal integer
            "x" hex format lowercase
            "X" hex format uppercase
            "n" number
            None Same as "d"
        
        floating point
            "e" Exponent notation lowercase
            "E" Exponent notation uppercase
            "f" Fixed-point notation
            "F" Fixed-point notation but converts nan to NAN and inf to INF
            "g" General format. For precision p>=1, round number to p 
            significant digits
            "G" same as "g" but switches to "E" if the number gets too large
            "n" Number, same as "g"
            "%" Percentage - multiples number by 100 and displays "f"%
            None Similar to g except fixed-point notation will have at least
            one digit past the decimal point


Format Examples
"""
# Accessing argument by position:
"{0}, {1}, {2}".format("a", "b", "c")
"{}, {}, {}".format("a", "b", "c")
"{2}, {1}, {0}".format("a", "b", "c")
"{2}, {1}, {0}".format(*"abc")
"{0}{1}{0}".format("abra", "cad")

# Accessing arguments by name:
"Coordinates: {lattitude}, {longitude}".format(lattitude="37.24N", longitude="-115.81W")
coord = {"lattitude": "37.24N", "longitude": "-115.81W"}
"Coordinates: {lattitude}, {longitude}".format(**coord)

# Accessing arguments' attributes:
c = 3 - 5j
("The complex number {0} if formed from the real part {0.real} "
 "and the imaginary part {0.imag}").format(c)


class Point:
    def __init__(self, x, y):
        (self.x, self.y) = (x, y)

    def __str__(self):
        return "Point({self.x}, {self.y})".format(self=self)


str(Point(4, 2))

# Accessing arguments' items:
coord = (3, 5)
"X: {0[0]}; Y: {0[1]}".format(coord)

# Replacing %s and %r
"repr() shows quotes: {!r}; str() doesn't: {!s}".format("test1", "test2")

# Aligning text and specifying a width:
"{:<30}".format("left aligned")
"{:>30}".format("right aligned")
"{:^30}".format("centered")
"{:*^30}".format("centered")  # use "*" as fill char

# Replacing %=f, %-f and % f and specifying a sign
"{:+f}; {:+f}".format(3.14, -3.14)  # show it always
"{: f}; {: f}".format(3.14, -3.14)  # show space for positive
"{:-f}; {:-f}".format(3.14, -3.14)  # show only minus

# Replacing %x and %o and converting the value to different bases
# format also supports binary numbers
"int: {0:d}; hex: {0:x}; oct: {0:o}; bin: {0:b}".format(42)
"int: {0:d}; hex: {0:#x}; oct: {0:#o}; bin: {0:#b}".format(42)

# Using the comma as a thousands separator:
"{:,}".format(1234567890)

# Expressing a percentage
points = 19
total = 22
"Correct answers: {:.2%}".format(points/total)

# Use type-specific formatting
import datetime

d = datetime.datetime(2010, 7, 4, 12, 15, 58)
'{:%Y-%m-%d %H:%M:%S}'.format(d)

#Nesting arguments and more complex examples
for align, text in zip("<^>", ["left", "center", "right"]):
    print("{0:{fill}{align}16}".format(text, fill=align, align=align))

octets = [192, 168, 0, 1]
"{:02X}{:02X}{:02X}{:02X}".format(*octets)

width = 5
for num in range(5, 12):
    for base in "dXob":
        print("{0:{width}{base}}".format(num, base=base, width=width), end=" ")
    print()

"""
Template strings

Template strings provide simpler string substitutions as described in
PEP292. Primary use case is for internationalization

Template strings support $-based substitutions using the following
rules:
    $$ is an escape
    $identifier names a substitution placeholder
        identifier restricted to any case insensitive ASCII alphanumeric
        string that starts with an underscore or ASCII letter,
    ${identifier} is equivalent to $identifier but required when valid
    identifier characters follow the placeholder but are not part of
    the placeholder e.g. "${noun}ification"
    
Any other appearance of $ results in ValueError being raised

The string module provides a Template class that implements these rules

class string.Template
    The constructor takes a single argument which is the template string
    ----------------------------------------------------------------------
    substitute(mapping={}, /, **kwds)
        Performs the template substitution, returning a new string. 
        mapping is any dictionary-like object with keys that match the
        placeholders in the template.
        Alternatively, you can provide keyword arguments. When both
        mapping and kwds are given, and there are duplicates, the
        placeholders from kwds take precedence.
    safe_substitute(mapping={}, /, **kwds)
        Like substitute(), except that if placeholders are missing from
        mapping and kwds, instead of raising a KeyError exception, the
        original placeholder will appear in the resulting string intact.
        Also, any other appearances of $ will return $ instead of raising
        Value Error
    template
        This is the object passed to the constructor's template argument.
        In general, you shouldn't change it but read-only access is not
        enforced
"""
import string

s = string.Template("$who likes $what")
s.substitute(who="tim", what="kung pao")

d = dict(who="tim")
string.Template("Give $who $100").substitute(d)  # ValueError
string.Template("$who likes $what").substitute(d)  # KeyError
string.Template("$who likes $what").safe_substitute(d)

"""
Advanced usage
    You can derive subclasses of Template to customize the placeholder
    syntax, delimiter character, or the entire regular expression used
    to parse template strings.
    
    To do this, you can override these class attributes
        delimiter 
            This is the literal string describing a placeholder introducing 
            delimiter. Default is $. This should noe be a regular expression
        idpattern
            The regular expression describing the pattern for non-braced 
            placeholders. If given and braceidpattern is None, this pattern
            will also apply to braced placeholders
        braceidpattern
            Like idpattern but describes the pattern for braced placeholders.
            Defaults to None which means fall back to idpattern.
        flags
            regular expression flags that will be applied when compiling
            the regular expression used for recognising substitutions. 
            Default is re.IGNORECASE. re.VERBOSE is always added so that
            custom idpatterns must follow conventions for verbose regular
            expressions.
            
        Alternatively, you can provide the entire regular expression pattern
        by overriding the class attribute pattern. If you do this, the
        regular expression object must have four named capturing groups.
            escaped
                Group matches escape sequence e.g. $$
            named
                Group matches unbraced placeholder name. Should not include
                the delimiter in the capturing group
            braced
                Group matches the brace enclosed placeholder name. Should not
                include either the delimiter or braces in the capturing group
            invalid
                Group matches any other delimiter pattern (usually a single
                delimiter), and it should appear last in the regular expression


Helper Functions
    string.capwords(s, sep=None)
        Split the argument into words using str.split(), capitalize each
        word using str.capitalize(), and join the capitalized words using
        str.join(). If the optional argument sep is absent or None, runs
        of whitespace characters are replaced by a single space and leading
        and trailing whitespace are removed, otherwise sep is used to split
        and join the words

            
                
"""