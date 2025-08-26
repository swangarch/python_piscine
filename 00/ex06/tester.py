#!/usr/bin/pyton3

from ft_filter import ft_filter


def isOdd(num: int) -> bool:
    """Check if a number is odd"""

    if not isinstance(num, int):
        return False
    return (num % 2 == 1)


def lessThanFiveChar(s: str) -> bool:
    """Check if a number is even"""

    if not isinstance(s, str):
        return False
    return len(s) < 5


def main():
    """Tests compare original filter and ft_filter"""

    print(filter.__doc__)

    print("............................................................")

    print(ft_filter.__doc__)

    print("____________________________________________________________")

    list1 = [True, False, True, False, False]
    print(list(filter(None, list1)))
    print(list(ft_filter(None, list1)))

    print("____________________________________________________________")

    list2 = [1, 4, 5, 6, 9]
    print(list(filter(isOdd, list2)))
    print(list(ft_filter(isOdd, list2)))

    print("____________________________________________________________")

    tuple1 = (1, "Hello world", "hello", "hi", "mov", "ecole42", "42", 42)
    print(tuple(filter(lessThanFiveChar, tuple1)))
    print(tuple(ft_filter(lessThanFiveChar, tuple1)))

    print("____________________________________________________________")


if __name__ == "__main__":
    main()
