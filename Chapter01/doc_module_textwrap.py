"""
textwrap - Text wrapping and filling

The textwrap module provides some convenience functions, as well as
TextWrapper, the class that does all the work

Use TextWrapper if filling or wrapping multiple strings for efficiency
------------------------------------------------------------------------
textwrap.wrap(text, width=70, **kwargs)
    Wraps the single paragraph in text (a string) so that every line is
    at most width characters long. Returns a list of output lines,
    without final newlines.

    Optional keyword arguments correspond to the instance attributes of
    TextWrapper. width defaults to 70
------------------------------------------------------------------------
textwrap.fill(text, width=70, **kwargs)
    Wraps the single paragraph in text, and returns a single string
    containing the wrapped paragraph. fill() is shorthand for
        "\n".join(wrap(text, ...
    Accepts exactly the same keyword arguments as wrap()
------------------------------------------------------------------------
textwrap.shorten(text, width, **kwargs)
    Collapse and truncate the given text to fit the given width.

    First the whitespace in text is collapsed (all whitespace is replaced
    by single spaces). If the result fits in the width, it is returned.
    Otherwise, enough words are dropped from the end so that the remaining
    words plus the placeholder fit within width

    Optional keyword arguments correspond to the instance attributes of
    TextWrapper.
------------------------------------------------------------------------
"""
import textwrap

textwrap.shorten("Hello world!", width=12)
textwrap.shorten("Hello world!", width=11)
textwrap.shorten("Hello world!", width=10, placeholder="...")

"""
------------------------------------------------------------------------
textwrap.dedent(text)
    Removes any common leading whitespace from every line in text.
    
    This can be used to make triple_quoted strings line up with the left
    edge of the display, while still presenting them in source code
    indented form.
    
    Both tabs and spaces are both treated as whitespace, but they are
    not equal "  hello" and "\thello" are considered to have no common
    leading whitespace
    
    Lines containing only whitespace are ignored in the input and 
    normalized to a single newline character in the output.
------------------------------------------------------------------------
"""


def test():
    s = """\
    hello
        world
    """
    print(repr(s))
    print(repr(textwrap.dedent(s)))


test()

"""
------------------------------------------------------------------------
textwrap.indent(text, prefix, predicate=None)
    Add prefix to the beginning of selected lines in text
    
    Lines are serparated by calling text.splitlines(True)
    
    By default, prefix is added to all lines that do not consist solely
    of whitespace (including any line endings)
    
    The optional predicate argument can be used to control which lines
    are indented.
------------------------------------------------------------------------
"""
s = "hello\n\n \nworld"
textwrap.indent(s, "    ")

print(textwrap.indent(s, "+ ", lambda line: True))

"""
wrap(), fill() and shorten() work by creating a TextWrapper instance and
calling a single method on it. That instance is not reused, so for
applications that process many text strings using wrap() and/or fill(),
it may be more efficient to create your own TextWrapper object.

Text is preferably wrapped on whitespaces and right after the hyphens in
hyphenated words; only then will long words be broken if necessary, unless
TextWrapper.break_long_words is set to false

class textwrap.TextWrapper(**kwargs)
    The TextWRapper constructor accepts a number of optional keyword
    arguments. Each keyword argument corresponds to an instance
    attribute, so for example
"""
wrapper = textwrap.TextWrapper(initial_indent="* ")
#is the same as
wrapper = textwrap.TextWrapper()
wrapper.initial_indent = "* "

"""
    You can re-use the same TextWrapper object many times, and you can
    change any of its options through direct assignment to instance
    attributes between uses.
    
    The textwrapper instance attributes are as follows
    --------------------------------------------------------------------
    width
        (default: 70) The maximum length of wrapped lines. As long
        as there are no individual words in the input text longer than
        width, TextWrapper guarantees that no output line will be longer
        than width characters
    --------------------------------------------------------------------
    expand_tabs
        (default: True) If true, then all tab characters in text will be
        expanded to spaces using the expandtabs() method of text
    --------------------------------------------------------------------
    tabsize
        (default: 8) If expand_tabs is true, then all tab characters in 
        text will be expanded to zero or more spaces, depending on the
        current columnb and the given tab size
    --------------------------------------------------------------------
    replace_whitespace
        (default: True) If true, after tab expansion, but before wrapping,
        the wrap() method will replace each whitespace character with a
        single space. The whitespace characters replaced are: tab, newline,
        vertical tab, formfeed and carriage return ("\t\n\v\f\r")
    --------------------------------------------------------------------
    drop_whitespace
        (default: True) If true, whitespace at the beginning and ending of
        every line (after wrapping but before indenting) is dropped. 
        Whitespace at the beginning of the paragraph, however, is not dropped
        if non-whitespace follows it. If whitespace being dropped takes up
        and entire line, the whole line is dropped
    --------------------------------------------------------------------
    initial_indent
        (default: "") String that will be prepended to the first line of
        wrapped output. Counts towards the length of the first line. The
        empty string is not indented
    --------------------------------------------------------------------
    subsequent_indent
        (default: "") String that will be prepended to all lines of wrapped
        output except the first. Counts towards the length of each line
        except the first
    --------------------------------------------------------------------
    fix_sentence_endings
        (default: False) If true, TextWrapper attempts to detect sentence
        endings and ensure that sentences are always separated by exactly
        two spaces. This is generally desired for text in a monospaced font.
        However, the sentence detection algorithm is imperfect. 
        Assumes that a sentence ending consists of lowercase letter followed
        by ".", "!" or "?", possibly followed by one of '"' or "'", followed
        by a space.
        Specific to English language texts
    --------------------------------------------------------------------
    break_long_words
        (default: True) If true, wrapping will occur preferably on 
        whitespaces and right after hyphens in compound words, as is
        customary in English. If false, only whitespaces will be considered
        as potentially good places for line breaks, but you need to set
        break_long_words to false if you want truly insecable words.
    --------------------------------------------------------------------
    max_lines
        (default: None) If not None, then the output will contain at most
        max_lines lines, with placeholder appearing at the end of the
        output
    --------------------------------------------------------------------
    palceholder
        (default: " [...]") String that will appear at the end of the output
        text if it has been truncated.
    --------------------------------------------------------------------
    
    TextWrapper Public methods:
    --------------------------------------------------------------------
    wrap(text)
        Wraps the single paragraph in text (a string) so every line is at
        most width characters long. All wrapping options are taken from
        instance attributes of the TextWrapper instance. Returns a list
        of output lines, without final newlines. If the wrapped output
        has no content, the returned list is empty.
    --------------------------------------------------------------------
    fill(text)
        Wraps the single paragraph in text and returns a single string
        containing the wrapped paragraph
    --------------------------------------------------------------------
"""
