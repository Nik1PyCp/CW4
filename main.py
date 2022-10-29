def checker(var_1):
    if type(var_1) != str:
        raise TypeError(
            f"Sorry,"
            f"we can't work with {TypeError},"
            f"we need class str."
        )
    else:
        return var_1

print(checker("10"))