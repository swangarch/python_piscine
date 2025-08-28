#!/usr/bin/python3


def NULL_not_found(object: any) -> int:
    """Print the null object type of given object."""

    if object.__class__.__name__ == "NoneType":
        print("Nothing:", object, object.__class__)
    elif object.__class__.__name__ == "float" and object != object:
        print("Cheese:", object, object.__class__)
    elif object.__class__.__name__ == 'int' and object == 0:
        print("Zero:", object, object.__class__)
    elif object == '':
        print("Empty:", object, object.__class__)
    elif object.__class__.__name__ == 'bool' and object is False:
        print("Fake:", object, object.__class__)
    else:
        print("Type not Found")
        return 1
    return 0
