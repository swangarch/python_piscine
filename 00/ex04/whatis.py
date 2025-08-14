#!/usr/bin/python3

import sys

if __name__ == "__main__":
    try:
        assert (len(sys.argv) <= 2 and len(sys.argv) >= 1), "more than one argument is provided"
    except AssertionError as e:
        print("AssertionError:", e)
        sys.exit(1)

    if len(sys.argv) == 2:
        try:
            num = int(sys.argv[1])
            if (num % 2 == 0):
                print("I'm Even.")
            else:
                print("I'm Odd.")
        except:
            print("AssertionError: argument is not an integer")


