from typing import Any


def callLimit(limit: int):
    """A factory function which return a decorator which adds call
    limits on another function."""

    count = 0

    def callLimiter(function):  # decorator
        """Decorator for a function to add a call limit,
        return the wrapper function."""

        def limit_function(*args: Any, **kwds: Any):  # wrapper
            """Wrapper function"""

            nonlocal count
            if count >= limit:
                print(f"Error: {function} call too many times")
                return None
            result = function(*args, **kwds)
            count += 1
            return result

        return limit_function

    return callLimiter
