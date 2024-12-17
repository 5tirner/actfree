import random, string

def generateCode():
    code = ''.join(random.choices(string.digits + string.ascii_uppercase + string.ascii_lowercase,k=8))
    return code