"""
re - Regular expression operations

Provides regular expression matching operations similar to those found
in Perl

Patterns and strings to be searched can be Unicode strings (str) as well
as 8-bit strings (bytes).
    Unicode and 8-bit cannot be mixed

Regular expressions use the backslash character ("\") to indicate special
forms or to allow special characters to be used without invoking their
special meaning. Use raw string notation to avoid

Regular expression operations are available as module-level functions
and methods on compiled regular expressions. The functions are shortcuts
that don't require you to compile a regex object first, but miss some
fine-tuning parameters.


Regular Expression Syntax

A regular expression specifies a set of strings that matches it; the
functions in this module let you check if a particular string matches
a given regular expression.

TODO: Finish re module documentation
"""