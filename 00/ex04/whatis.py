#!/usr/bin/python3

import sys


def main():
    """Program that takes an argument, prints it's type if it's a interger, otherwise prints an error."""

    try:
        assert (len(sys.argv) <= 2), "more than one argument is provided"
    except AssertionError as e:
        print("AssertionError:", e)
        sys.exit(1)

    try:
        if len(sys.argv) == 2:
            try:
                num = int(sys.argv[1])
                if num % 2 == 0:
                    print("I'm Even.")
                else:
                    print("I'm Odd.")
            except ValueError:
                raise AssertionError("argument is not an integer")
    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
