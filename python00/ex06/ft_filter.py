#!/usr/bin/pyton3

from typing import Callable, Iterable, Iterator, TypeVar

T = TypeVar("T")


def ft_filter(function: Callable[[T], bool] | None, iterable: Iterable[T]) \
        -> Iterator[T]:
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    if function is None:
        return (item for item in iterable if item)
    else:
        return (item for item in iterable if function(item))
