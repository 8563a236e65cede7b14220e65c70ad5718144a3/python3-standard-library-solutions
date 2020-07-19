"""
Listing 4.1

The time module provides provides access to several of clocks, each
useful for different purposes. The standard system calls such as time()
report the system "wall clock" time. The monotonic() clock can be used to
measure elapsed time in a long-running process because it is guaranteed
never to move backward, even if the system time is changed. For
performance testing, perf_counter() provides access to the clock with the
highest available resolution, which makes short time measurements more
accurate. The CPU time is available through clock(), and process_time()
returns the combined processor time and system time.

Implementation details for the clocks vary by platform. Use
get_clock_info() to access basic information about the current
implementation, including the clock's resolution
"""
import textwrap
import time


def main():
    available_clocks = [
        ("clock", time.clock),
        ("monotonic", time.monotonic),
        ("perf_counter", time.perf_counter),
        ("process_time", time.process_time),
        ("time", time.time)
    ]

    for clock_name, func in available_clocks:
        name = clock_name
        info = time.get_clock_info(clock_name)
        current = func()
        print(textwrap.dedent(f"""\
        {name}:
            adjustable    : {info.adjustable}
            implementation: {info.implementation}
            monotonic     : {info.monotonic}
            resolution    : {info.resolution}
            current       : {current}
        """))
    print()


if __name__ == "__main__":
    main()
