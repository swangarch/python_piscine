#!/usr/bin/python3

from datetime import datetime


def main():
    """Get current time, and print it in the format, eg:
Seconds since January 1, 1970: 1,756,382,963.6521 or 1.76e+09
in scientific notation Aug 28 2025
    """

    date = datetime.now()
    timestamp = date.timestamp()

    fmt = f"{timestamp:,.4f}"
    scientific_fmt = f"{timestamp:.2e}"

    head = "Seconds since January 1, 1970:"
    end = "in scientific notation"

    print(head, fmt, "or", scientific_fmt, end)
    print(date.strftime("%b %d %Y"))


if __name__ == "__main__":
    main()
