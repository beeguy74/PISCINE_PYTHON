def NULL_not_found(obj) -> int:
    dictNones = {
      "<class 'NoneType'>": "Nothing",
      "<class 'float'>": "Cheese",
      "<class 'int'>": "Zero",
      "<class 'str'>": "Empty",
      "<class 'bool'>": "Fake",
    }

    if not obj or not obj == obj:
        myType = str(type(obj))
        res = dictNones[myType]
        res += f": {obj}"
        res += "" if obj == "" else " "
        res += myType
        print(res)
    else:
        print("Type not found")
        return 1
    return 0
