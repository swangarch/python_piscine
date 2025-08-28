#!/usr/bin/python3

from find_ft_type import all_thing_is_obj


def main():
    """The main function to test all_thing_is_obj function in find_ft_type"""

    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello": "titi!"}

    all_thing_is_obj(ft_list)
    all_thing_is_obj(ft_tuple)
    all_thing_is_obj(ft_set)
    all_thing_is_obj(ft_dict)
    all_thing_is_obj("Brian")
    all_thing_is_obj("Toto")
    print(all_thing_is_obj(10))


if __name__ == "__main__":
    main()
