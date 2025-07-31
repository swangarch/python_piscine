#!/usr/bin/pyton

import sys


def count_char(str1: str):
    """This function count each type of char and print in the command line"""
    total = 0
    up = 0
    low = 0
    punc = 0
    space = 0
    digit = 0
    for c in str1:
        total += 1
        if c.isupper():
            up += 1
        elif c.islower():
            low += 1
        elif c.isdigit():
            digit += 1
        elif c.isspace():
            space += 1
        elif (c >= '!' and c <= '/') or (c >= ':' and c <= '@'):
            punc += 1
        elif (c >= '[' and c <= '`') or (c >= '{' and c <= '~'):
            punc += 1
    print(f"The text contains {total} characters:")
    print(f"{up} upper letters")
    print(f"{low} lower letters")
    print(f"{punc} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


def main():
    """The main function, read either from argv or stdin of """
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
    except AssertionError as e:
        print("AssertionError:", e)
        sys.exit(1)

    if (len(sys.argv) == 2):
        count_char(sys.argv[1])
    else:
        print("What is the text to count?")
        try:
            strin = sys.stdin.read()
            count_char(strin)
        except EOFError:
            pass

if __name__ == "__main__":
    main()
