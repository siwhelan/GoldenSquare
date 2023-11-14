def grammar_check(text):
    if type(text) != str:
        raise TypeError("Incorrect data type")
    elif len(text) > 0 and text[0] == text[0].upper() and text[-1] in "!?.":
        return True

    else:
        return False
