"""
Listing 1.65

While the Differ class shows all of the input lines, a unified diff
includes only the modified lines and a bit of context. The unified_diff()
function produces this sort of output

The lineterm argument is used to tell unified_diff to skip appending
newlines to the control lines that it returns because the input lines
do not include them. Newlines are added to all the lines when they are
printed.

Using context_diff() produces similar readable output
"""
import difflib
from difflib_data import *


def main():
    diff = difflib.unified_diff(
        text1_lines,
        text2_lines,
        lineterm=""
    )
    print("\n".join(list(diff)))


if __name__ == "__main__":
    main()
