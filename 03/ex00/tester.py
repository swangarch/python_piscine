#!/usr/bin/python3

from S1E9 import Character, Stark


def main():
    """    Main function to test the abstract class Character and
    its child class Stark, including error handling."""

    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)

    print("-------------------error handle 1---------------------------")
    try:
        hodor1 = Character("hodor")
        print(hodor1)
    except Exception as e:
        print("Error:", e)

    print("-------------------error handle 2---------------------------")
    try:
        hodor2 = Stark()
        print(hodor2)
    except Exception as e:
        print("Error:", e)

    print("-------------------error handle 2---------------------------")
    try:
        hodor3 = Stark("Lyanna", False, False)
        print(hodor3)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
