def double_string(string):
    newString = ""
    for i in string:
        for j in i:
            newString += j*2
    return newString
