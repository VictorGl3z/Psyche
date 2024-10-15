def get_most_common_enemy(enemies_dict):
    most = -100
    enemy = None
    for name in enemies_dict:
        if enemies_dict[name] > most:
            most = enemies_dict[name]
            enemy = name
    if most != -100:
        return enemy
    else:
        return None
