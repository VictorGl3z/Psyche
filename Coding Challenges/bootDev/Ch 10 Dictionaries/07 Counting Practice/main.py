def count_enemies(enemy_names):
    count = {}
    for name in enemy_names:
        if name in count:
            count[name] += 1
        else:
            count[name] = 1
    return count
