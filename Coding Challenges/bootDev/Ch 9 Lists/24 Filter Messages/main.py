def filter_messages(messages):
    split = []
    count = []
    filtered = []
    for i in range(len(messages)):
        count.append(0)
        split.append(messages[i].split())
        if "dang" in split[i]:
            for j in range(split[i].count("dang")):
                count[i] += 1
                split[i].pop(split[i].index('dang'))
        filtered.append(" ".join(split[i]))
    return filtered, count

