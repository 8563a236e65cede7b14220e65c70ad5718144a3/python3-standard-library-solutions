"""
Listing 2.78

To format a data structure without writing it directly to a stream
(for example, for logging), use pformat() to build a string representation
"""
import logging
import pprint
from pprint_data import data


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)-8s %(message)s"
    )
    logging.debug("Logging pformatted data")
    formatted = pprint.pformat(data)
    for line in formatted.splitlines():
        logging.debug(line.rstrip())


if __name__ == "__main__":
    main()
