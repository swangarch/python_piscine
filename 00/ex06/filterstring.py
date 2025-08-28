#!/usr/bin/pyton3

import sys


def check_str(s: str) -> bool:
    """Check if a string contain only legal characters"""

    try:
        for c in s:
            if not c.isalnum() and c != ' ':
                return False
        return True
    except Exception:
        return False


def check_num(s: str) -> bool:
    """Check if a string contian a valid integer"""

    try:
        for i, c in enumerate(s):
            if i == 0:
                if c != '-' and (not c.isdigit()):
                    return False
            elif not c.isdigit():
                return False
            return True
    except Exception:
        return False


def main():
    """A program that accepts two arguments: a string(S), and an integer(N). The
program should will a list of words from S that have a length greater than N."""

    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        assert check_str(sys.argv[1]), "the arguments are bad"
        assert check_num(sys.argv[2]), "the arguments are bad"
    except AssertionError as e:
        print("AssertionError:", e)
        sys.exit(1)

    try:
        tab = sys.argv[1].split()
        t = int(sys.argv[2])
        print((lambda tab, t: [e for e in tab if len(e) > t])(tab, t))
    except Exception as e:
        print("Error:", e)
        sys.exit(1)


if (__name__ == "__main__"):
    main()
