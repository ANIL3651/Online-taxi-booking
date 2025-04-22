import re

def timeValidation(time):
    regex = re.compile("([01]?[0-9]|2[0-3]):[0-5][0-9]")
    if re.fullmatch(regex, time):
        resultTime = True
    else:
        resultTime=False
    return resultTime

def phoneValidation(phone):
    regex = re.compile("^(?:\d\s?){10,11}$")
    if re.fullmatch(regex, phone):
        resultphone = True
    else:
        resultphone = False
    return resultphone

def emailValidation(email):
    regex = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    if re.fullmatch(regex, email):
        resultemail = True
    else:
        resultemail = False
    return resultemail





