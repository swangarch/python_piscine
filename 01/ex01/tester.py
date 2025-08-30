#!/usr/bin/python3

from array2D import slice_me


def main():
    """    Main function to test if slice_me function works
    as expected. Also test for error handling."""

    print("Subject test------------------------------------:")

    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]

    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))

    # Error handle

    print()

    print("Error handle1------------------------------------:")

    family_error1 = [
        [
            [1.80, 78.4],
            [2.15, 102.7],
            [2.10, 98.5],
            [1.88, 75.2]
        ],
        [
            [1.80, 78.4],
            [2.15, 102.7],
            [2.10, 98.5],
            [1.88, 75.2]
        ]]
    print(slice_me(family_error1, 1, 2))

    print("Error handle2------------------------------------:")

    family_error2 = [1.80, 78.4, 2.15, 102.7, 2.10, 98.5, 1.88, 75.2]
    print(slice_me(family_error2, 1, 2))

    print("Error handle3------------------------------------:")
    print(slice_me(family, 1, "-2a"))

    print("Error handle4------------------------------------:")
    print(slice_me(family, "-2a", 5))

    print("Error handle5------------------------------------:")

    family_error3 = [
        [1.80, 78.4, 88.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]

    print(slice_me(family_error3, 0, 2))

    print("Error handle6------------------------------------:")

    family_error4 = [
        [1.80, 78.4],
        "Hello",
        [2.10, 98.5],
        [1.88, 75.2]
    ]

    print(slice_me(family_error4, 0, 2))


if __name__ == "__main__":
    main()
