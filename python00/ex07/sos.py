#!/usr/bin/python3

import sys


def check_input(s: str) -> bool:
    """Check if input contain only alphabetic, numeric characters and space."""

    if not isinstance(s, str):
        return False
    try:
        for c in s:
            if not c.isalnum() and c != ' ':
                return False
        return True
    except Exception:
        return False


def main():
    """Program converts input to morse code, print it on the stadard output"""

    NESTED_MORSE = {
        'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
        'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
        'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
        'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
        'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
        'Z': '--..',

        'a': '.-',    'b': '-...',  'c': '-.-.',  'd': '-..',   'e': '.',
        'f': '..-.',  'g': '--.',   'h': '....',  'i': '..',    'j': '.---',
        'k': '-.-',   'l': '.-..',  'm': '--',    'n': '-.',    'o': '---',
        'p': '.--.',  'q': '--.-',  'r': '.-.',   's': '...',   't': '-',
        'u': '..-',   'v': '...-',  'w': '.--',   'x': '-..-',  'y': '-.--',
        'z': '--..',

        '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.',

        ' ': '/'
    }

    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        assert check_input(sys.argv[1]), "the arguments are bad"

        arg1 = sys.argv[1]
        arglen = len(arg1)
        for i in range(arglen):
            if i < arglen - 1:
                print(NESTED_MORSE[arg1[i]], end=" ")
            else:
                print(NESTED_MORSE[arg1[i]])

    except AssertionError as e:
        print("AssertionError:", e)
        sys.exit(1)

    except Exception as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
