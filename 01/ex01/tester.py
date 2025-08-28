#!/usr/bin/python3

from array2D import slice_me


def main():
    """    Main function to test if slice_me function works 
    as expected. Also test for error handling."""
    
    family = [[1.80, 78.4],
                [2.15, 102.7],
                [2.10, 98.5],
                [1.88, 75.2]]

    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))

    # Error handle
    print("Error hanle1------------------------------------:")
    print(slice_me(family, 1, -2))



if __name__ == "__main__":
    main()