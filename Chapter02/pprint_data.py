"""
Listing 2.76

The pprint module contains a "pretty printer" for producing aesthetically
pleasing views of data structures. The formatter produces representations
of data structures that can be parsed correctly by the interpreter,
and that are also easy for a human to read.

The output is kept on a single line, if possible, and indented when split
across multiple lines
"""
data = [
    (1, {"a": "A", "b": "B", "c": "C", "d": "D"}),
    (2, {"e": "E", "f": "F", "g": "G", "h": "H",
         "i": "I", "j": "J", "k": "K", "l": "L"}),
    (3, ["m", "n"]),
    (4, ["o", "p", "q"]),
    (5, ["r", "s", "t" "u", "v", "x", "y", "z"])
]
