def can_withstand_blow(hero_armor, enemy_damage):
    if hero_armor >= enemy_damage:
        return True
    else:
        return False
