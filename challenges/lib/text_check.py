def text_check(text):
    if type(text) != str:
        raise TypeError("Incorrect data type")
    elif "#TODO" in text:
        return True
    else:
        return False
