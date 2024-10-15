def get_champion_slices(champions):
    value1 = champions[2:]
    value2 = champions[:-2]
    value3 = champions[::2]
    return value1, value2, value3
