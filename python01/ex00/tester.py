#!/usr/bin/python3

from give_bmi import give_bmi, apply_limit


def main():
    """The main function to test if give_bmi and apply_limit works correctly,
    tested with error handling."""

    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

    # Error handle
    print("Error hanle1------------------------------------:")
    give_bmi([1, 2, 3, 3, "b"], [1, 2, 3, 4, 1])

    print("Error hanle2------------------------------------:")
    give_bmi([1, 2, 3, 3, 1], [1, "A", 3, 4, 1])

    print("Error hanle3------------------------------------:")
    give_bmi([1, 2, 3, 3, 1, 5], [1, 4.2, 3, 4, 1])

    print("Error hanle4------------------------------------:")
    apply_limit([1, 2, 3, 3, 1, 5], 2.0)
    apply_limit([1, 2, 3, 3, 1, 5], "Hello world")

    print("Error hanle5------------------------------------:")
    apply_limit([1, 2, 3, "a", 1, 5], 2)

    print("Error hanle6------------------------------------:")
    apply_limit(3, 2)


if __name__ == "__main__":
    main()
