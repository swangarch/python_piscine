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
        if (c >= 'A' and c <= 'Z'):
            up += 1
        elif (c >= 'a' and c <= 'z'):
            low += 1
        elif (c >= '0' and c <= '9'):
            digit += 1
        elif c == ' ' or (c >= '\t' and c <= '\r'):
            space += 1
        elif (c >= '!' and c <= '/') or (c >= ':' and c <= '@') or (c >= '[' and c <= '`') or (c >= '{' and c <= '~'):
            punc += 1
    print(f"The text contains {total} characters:")
    print(f"{up} upper letters")
    print(f"{low} lower letters")
    print(f"{punc} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")



if __name__ == "__main__":
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
    except AssertionError as e:
        print("AssertionError:", e)
        sys.exit(1)

    if (len(sys.argv) == 2):
        count_char(sys.argv[1])
    else:
        try:
            strin = input("What is the text to count?\n")
            count_char(strin + '\n')
        except EOFError:
            pass
