def all_thing_is_obj(object) -> int:
    if isinstance(object, (int, float, bool)):
        print("Type not found")
    else:
        res = ""
        if isinstance(object, (str)):
            res += object + " is in the kitchen"
        else:
            res += object.__class__.__name__.capitalize()
        res += " : " + str(type(object))
        print(res)
    return 42
