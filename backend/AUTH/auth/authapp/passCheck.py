def checkPassword(key:str):
    if len(key) < 8:
        return False
    upper, lower, digit, symbol = 0, 0, 0, 0
    for i in key:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isdigit():
            digit += 1
        elif i.isprintable():
            symbol += 1
        else:
            return False
    if upper == 0 or lower == 0 or digit == 0 or symbol == 0:
        return False
    return True 
    