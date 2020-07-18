"""
Listing 3.65

The context managers given to the ExitStack are treated as though they
appear within a series of nested with statements. Errors that happend
anywhere within the context propagate through the normal error handling of
the context managers.
"""
import contextlib


class Tracker:
    """Base class for noisy context managers"""

    def __init__(self, i):
        self.i = i

    def msg(self, s):
        print(f"  {self.__class__.__name__}({self.i}): {s}")

    def __enter__(self):
        self.msg("entering")


class HandleError(Tracker):
    """If an expression is received, treat it as handled"""

    def __exit__(self, *exc_details):
        received_exc = exc_details[1] is not None
        if received_exc:
            self.msg(f"handling exception {exc_details[1]!r}")
        self.msg(f"exiting {received_exc}")
        # Return a boolean value indicating whether the exception
        # was handled
        return received_exc


class PassError(Tracker):
    """If an exception is received, propagate it"""

    def __exit__(self, *exc_details):
        received_exc = exc_details[1] is not None
        if received_exc:
            self.msg(f"passing exception {exc_details[1]!r}")
        self.msg(f"exiting")
        # Return False, indicating any exception was not handled
        return False


class ErrorOnExit(Tracker):
    """Cause an exception"""

    def __exit__(self, *exc_details):
        self.msg("throwing error")
        raise RuntimeError(f"from {self.i}")


class ErrorOnEnter(Tracker):
    """Cause an exception"""

    def __enter__(self):
        self.msg("throwing error")
        raise RuntimeError(f"from {self.i}")

    def __exit__(self, *exc_info):
        self.msg("exiting")


def main():
    print("No errors:")

