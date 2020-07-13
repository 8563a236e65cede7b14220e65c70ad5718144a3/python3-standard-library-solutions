"""
difflib - Helpers for computing deltas

This module provides classes and functions for comparing sequences. It
can be used for example, for comparing files, and can produce difference
information in various formats, including HTML and context and unified
diffs.

class difflib.SequenceMatcher
    This is a flexible class for comparing pairs of sequences of any type
    so long as the sequence elements are hashable.

class difflib.Differ
    This is a class for comparing sequences of lines of text, and
    producing human-readable differences or deltas. Differ uses
    SequenceMatcher both to compare sequences of lines, and to compare
    sequences of characters within similar (near-matching) lines

    Each line of a Differ delta begins with a two-letter code:
        -       line unique to sequence 1
        +       line unique to sequence 2
                line common to both sequences
        ?       line not present in either input sequence

    Lines beginning with "?" attempt to guide the eye to intraline
    differences, and were not present in either input sequence.

class difflib.HtmlDiff
    This class can be used to create an HTML table (or a complete HTML
    file containing the table) showing a side by side, line by line
    comparison of text with inter-line and intra-line change highlights.
    The table can be generated in either full or contextual difference
    mode

    __init__(tabsize=8, wrapcolumn=None, linejunk=None,
        charjunk=IS_CHARACTER_JUNK)
        Initializes instance of HTMLDiff

        tabsize is an optional keyword argument to specify tab spacing
        and defaults to 8

        wrapcolumn is an optional keyword to specify column number where
        lines are broken and wrapped, defaults to None where lines are
        not wrapped.

        linejunk and charjunk are optional keyword arguments passed into
        ndiff

    The following methods are public:

    make_file(fromlines, tolines, fromdesc="", todesc="",
        context=False, numlines=5, *, charset="utf-8")
        Compares fromlines and tolines (lists of strings) and returns a
        string which is a complete HTML file containing a table showing
        line by line differences with inter-line and intra-line changes
        highlighted.

        fromdesc and todesc are optional keyword arguments to specify
        from/to file column header strings

        context and numlines are both optional keyword arguments. Set
        context to True when contextual differences are to be show, else
        the default is False to show the full files. numlines deaults
        to 5. When context is True, numlines controls the number of
        context lines which surround the difference highlights. When
        context is False, numlines controls the number of lines which
        are show before a difference highlight when using the "next"
        hyperlinks.

    make_table(fromlines, tolines, fromdesc="", todesc="",
        context=False, numlines=5, *, charset="utf-8")
        Compares fromlines and tolines (lists of strings) and returns a
        string which is a complete HTML table showing
        line by line differences with inter-line and intra-line changes
        highlighted.

        The arguments for this method are the same as make_file()


difflib.context_diff(a, b, fromfile="", tofile="",
    fromfiledate="", tofiledate="", n=3, lineterm="\n")
    Compare a and b (lists of strings); return a delta (a generator
    generating the delta lines) in context diff format.

    Context diffs are a compact way of showing just the lines that have
    changes plus a few lines of context. The changes are shown in a
    before/after style. The number of context lines is set by n which
    defaults to 3.

    For inputs that do not have trailing newlines, set the lineterm
    argument to "" so that the output will be uniformly newline free

    The context diff format normall has a header for filenames and
    modification times. Any or all of these may be specified using strings
    for fromfile, tofile, fromfiledate, and tofiledate.
"""
import sys
import difflib

s1 = ["bacon\n", "eggs\n", "ham\n", "guido\n"]
s2 = ["python\n", "eggy\n", "hamster\n", "guido\n"]

sys.stdout.writelines(
    difflib.context_diff(s1, s2, fromfile="before.py", tofile="after.py")
)

"""
difflib.get_close_matches(word, possibilities,
    n=3, cutoff=0.6)
    Return a list of the best "good enough" matches. word is a sequence
    for which close matches are desired (typically a string), and
    possibilities is a list of sequences against which to match
    word (typically a list of strings)
    
    Optional argument n (default 3) is the maximum number of close 
    matches to return. n must be greater than 0.
    
    Optional argument cutoff (default 0.6) is a float in the range [0,1]
    Possibilities that don't score at least that similar to word are
    ignored.
    
    The best (no more than n) matches among the possibilities are 
    returned in a list, sorted by similarity score, most similar first.
"""
difflib.get_close_matches("appel",
                          ["ape", "apple", "peach", "puppy"])

import keyword

difflib.get_close_matches("wheel",
                          keyword.kwlist)
difflib.get_close_matches("pineapple",
                          keyword.kwlist)
difflib.get_close_matches("accept",
                          keyword.kwlist)

"""
difflib.ndiff(a, b, linejunk=None, charjunk=IS_CHARACTER_JUNK)
    Compare a and b (list of strings); return a Differ-style
    delta (a generator generating the delta lines)
    
    Optional keyword parameters linejunk and charjunk are filtering
    functions (or None)
    
    linejunk: A function that accepts a single string argument, and
    returns true if the string is junk, or false if not. The default
    is None.
    
    charjunk: A function that accepts a character (a string of length
    1) and returns true if the character is junk, or false if not.
"""
diff = difflib.ndiff(
    "one\ntwo\nthree\n".splitlines(keepends=True),
    "ore\ntree\nemu\n".splitlines(keepends=True)
)

print(" ".join(diff), end="")

"""
difflib.restore(sequence, which)
    Return one of the two sequences that generated a delta
    
    Given a sequence produced by Differ.compar() or ndiff(), extract
    lines originating from file 1 or 2 (parameter which), stripping off
    line prefixes
"""
diff = difflib.ndiff(
    "one\ntwo\nthree\n".splitlines(keepends=True),
    "ore\ntree\nemu\n".splitlines(keepends=True)
)

diff = list(diff)  # materialize the generated delta into a list
print("".join(difflib.restore(diff, 1)), end="")
print("".join(difflib.restore(diff, 2)), end="")

"""
difflib.unified_diff(a, b, fromfile="", tofile="",
    fromfiledate="", tofiledate="", n=3, lineterm="\n")
    Compare a and b (list of strings); return a delta (a generator
    generating the delta lines) in unified diff format.
    
    Unified diffs are a compact way of showing just the lines that have
    changed plus a few lines of context. The changes are shown in an
    inline style. The number of context lines is set by n which defaults
    to three
"""
s1 = ["bacon\n", "eggs\n", "ham\n", "guido\n"]
s2 = ["python\n", "eggy\n", "hamster\n", "guido\n"]

sys.stdout.writelines(
    difflib.unified_diff(s1, s2, fromfile="before.py", tofile="after.py")
)

"""
difflib.diff_bytes(dfunc, a, b, fromfile=b"", tofile=b"",
fromfiledate=b"", tofiledate=b"", n=3, lineterm=b"\n")
    Compare a and b (list of bytes objects) using dfunct; yield a 
    sequence of delta lines (also bytes) in the format returned by
    dfunc. dunc must be a callable, typically either unified_diff() or
    context_diff()
    
    Allows you to compare data with unknown or inconsistent encoding.
    All inputs except n must be bytes objects, not str.

difflib.IS_LINE_JUNK(line)
    Returns True for ignorable lines. The line line is ignorable if line
    is blank or contains a single "#", otherwise it is not ignorable. 
    Used as default for parameter linejunk in ndiff() in older versions

difflib.IS_CHARACTER_JUNK(ch)
    Returns True for ignorable characters. The character ch is ignorable
    if ch is a space or a tab. Used as a default for charjunk in ndiff()
    
    
SequenceMatcher Objects
The SequenceMatcher class has this constructor:

class difflib.SequenceMatcher(isjunk=None, a="", b="",
    autojunk=True)
    Optional argument isjunk must be None (the default) or a one-argument
    function that takes a sequence element and returns true if and only
    if the element is "junk" and should be ignored. Passing None for 
    isjunk is equivalent to passing lambda x: False; in other words,
    no elements are ignored
    
    E.g.
        lambda x: x in " \t"
        if you are comparing lines as sequences of characters and don't
        want to synch up on blanks or hard tabs.
    
    The optional arguments a and b are sequences to be compared; both
    default to empty strings. The elements of both sequences must be
    hashable.
    
    The optional argument autojunk can be used to disable the automatic
    junk heuristic
    
    SequenceMatcher objects get three data attributes: bjunk is the set
    of elements of b which isjunk is True. bpopular is the set of 
    non-junk elements considered popular by the heuristic (if it is not
    disabled); b2j is a dict mapping the remaining elements of b to a
    list of positions where they occur. All three are reset whenever
    b is reset with set_seqs() or set_seq2()
    
    SequenceMatcher objects have the following methods:
    set_seqs(a, b)
        Set the two sequences to be compared
    
    SequenceMatcher computes and caches detailed information about the
    second sequence, so if you want to compare one sequence against
    many sequences, use set_seq2() to set the commonly used sequence
    once and call set_seq1() repeatedly, once for each of the other
    sequences
    
    set_seq1(a)
        Set the first sequence to be compared. The second sequence
        to be compared is not changed
    set_seq2(b)
        Set the second sequence to be compared. The first sequence
        to be compared is not changed.
        
    find_longest_match(alo, ahi, blo, bhi)
        Find longest matching block in a[alo:ahi] and b[blo:bhi]
        
        If isjunk was omitted or None, find_longest_match() returns
        (i, j, k) such that a[i:i+k] is equal to b[j:j+k] where 
        alo<=i<=i+k<=ahi and blo<=j<=k+k<=bhi. For all (i',j',k')
        meeting those conditions, the additional conditions 
        k >= k', i <= i' and if i == i', j <= j' are also met
        In other words, of all maximal matching blocks, return one
        that starts earliest in a, and of all those maximal matching
        blocks that start earliest in a, return the one that starts
        earliest in b
"""
s = difflib.SequenceMatcher(None, " abcd", "abcd abcd")
s.find_longest_match(0, 5, 0, 9)

"""
        If isjunk was provided, first the longest matching
"""