def reverse_array(items):
    index = range(len(items)-1,-1,-1)
    newList = []
    for i in index:
        newList.append(items[i])
    return newList