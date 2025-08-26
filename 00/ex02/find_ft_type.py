#!/usr/bin/python3

def all_thing_is_obj(object: any) -> int:
    if object.__class__.__name__ == "list":
        print("List :", object.__class__)
    elif object.__class__.__name__ == "tuple":
        print("Tuple :", object.__class__)
    elif object.__class__.__name__ == "set":
        print("Set :", object.__class__)
    elif object.__class__.__name__ == "dict":
        print("Dict :", object.__class__)
    elif object.__class__.__name__ == "str":
        print(object, "is in the kitchen :", object.__class__)
    else:
        print("Type not found")
    return 42
