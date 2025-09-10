def square(x: int | float) -> int | float:
    """Return the correspond square of input number, take int or
    float as parameters."""

    if not (isinstance(x, int) or isinstance(x, float)):
        print("Error: wrong input type.")
        return None
    return x ** 2


def pow(x: int | float) -> int | float:
    """Return the correspond exponentiation of itself of an input number,
    take int or float as parameters."""

    if not (isinstance(x, int) or isinstance(x, float)):
        print("Error: wrong input type.")
        return None

    return x ** x


def outer(x: int | float, function) -> object:
    """Return a closure function that when called returns the result of
    the argument calculation."""

    count = 0

    def inner() -> float:
        """Closure function, which uses count variable of outer funciton
        and keep the result. When first call, it uses parameters of
        outer function, after it will use result of previous call."""

        nonlocal count
        try:
            if count == 0:
                count = function(x)
            else:
                count = function(count)
            return count
        except Exception as e:
            print("Error:", e)
            return None
    return inner
