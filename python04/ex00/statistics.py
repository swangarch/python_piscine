from typing import Any


def quartile(sorted_li: list, quartile_num: int) -> float:
    """Given a list, calculate its quartile"""

    length = len(sorted_li)

    # One definition of quartile
    if quartile_num == 1:
        sub_li_l = sorted_li[0:length // 2 + 1]
        return find_median(sub_li_l)
    elif quartile_num == 3:
        sub_li_r = sorted_li[length // 2:]
        return find_median(sub_li_r)

    # Another definition of quartile
    # if length % 2 == 1:
    #     if quartile_num == 1:
    #         sub_li_l = sorted_li[0:length // 2]
    #         return find_median(sub_li_l)
    #     elif quartile_num == 3:
    #         sub_li_r = sorted_li[length // 2 + 1:]
    #         return find_median(sub_li_r)
    # else:
    #     if quartile_num == 1:
    #         sub_li_l = sorted_li[0:length // 2]
    #         return find_median(sub_li_l)
    #     elif quartile_num == 3:
    #         sub_li_r = sorted_li[length // 2:]
    #         return find_median(sub_li_r)


def find_median(sorted_li: list):
    """Find the median of an array."""

    length = len(sorted_li)
    if length % 2 == 1:
        return sorted_li[int(length / 2)]
    else:
        mi_idx = int(length / 2)
        return (sorted_li[mi_idx - 1] + sorted_li[mi_idx]) / 2.0


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Statistics for the given numbers passed in front, followed
    by the operations passed as key value pair, it can take multiple
    numbers and operations at one time."""

    try:
        for element in args:
            if not isinstance(element, int | float):
                raise TypeError("Positional argument not number type.")

        for k in kwargs:
            if not isinstance(kwargs[k], str):
                raise TypeError("Keyword argument not string type.")

        for k in kwargs:
            if kwargs[k] == "mean":
                if len(args) == 0:
                    print("ERROR")
                else:
                    print("mean :", sum(args) / len(args))

            elif kwargs[k] == "median":
                if len(args) == 0:
                    print("ERROR")
                else:
                    li = sorted(list(args))
                    print("median:", find_median(li))

            elif kwargs[k] == "quartile":
                if len(args) == 0:
                    print("ERROR")
                else:
                    li = sorted(list(args))
                    quartile_1 = float(quartile(li, 1))
                    quartile_3 = float(quartile(li, 3))
                    print(f"quartile : [{quartile_1}, {quartile_3}]")

            elif kwargs[k] == "std":
                if len(args) == 0:
                    print("ERROR")
                else:
                    mean = sum(args) / len(args)
                    var = sum((mean - num) ** 2 for num in args) / len(args)
                    std = var ** 0.5
                    print("std :", std)

            elif kwargs[k] == "var":
                if len(args) == 0:
                    print("ERROR")
                else:
                    mean = sum(args) / len(args)
                    var = sum((mean - num) ** 2 for num in args) / len(args)
                    print("var :", var)

            else:
                pass

    except Exception:
        print("ERROR")
