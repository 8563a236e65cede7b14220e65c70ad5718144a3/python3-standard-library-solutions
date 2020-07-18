"""
Listing 3.63

Poorly designed library code may write directly to sys.stdout or
sys.stderr, without providing arguments to configure different output
destinations. The redirect_stdout() and redirect_stderr() context managers
can be used to capture output from these kinds of functions, for which the
source cannot be changed to accept a new output argument

NOTE: both redirect_stdout() and redirect_stderr() modify the global
state by replacing objects in the sys module; for this reason, they should
be used with care. The functions are not really thread-sage, so calling
them in a multithreaded application will have nondeterministic results.
They also may interfere with other operations that expect the standard
output streams to be attached to terminal devices
"""
import contextlib
import io
import sys


def misbehaving_function(a):
    sys.stdout.write(f"(stdout) A: {a!r}\n")
    sys.stdout.write(f"(stderr) A: {a!r}\n")


def main():
    capture = io.StringIO()
    with contextlib.redirect_stdout(capture), contextlib.redirect_stderr(capture):
        misbehaving_function(5)

    print(capture.getvalue())


if __name__ == "__main__":
    main()
