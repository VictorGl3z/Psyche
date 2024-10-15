def enchant_and_attack(player_health, damage, weapon):
    enchanted_dmg = damage + 10
    new_health = player_health - enchanted_dmg
    enchanted_weapon = "enchanted " + weapon
    return enchanted_weapon, new_health


# Don't modify below this line


def test(player_health, damage, weapon):
    print("The victim has", player_health, "health.")
    print(weapon, "does", damage, "damage. Enchanting and attacking...")
    enchanted_weapon, new_health = enchant_and_attack(player_health, damage, weapon)
    print("The victim has been attacked with the", enchanted_weapon)
    print("The victim has", new_health, "health remaining.")
    print("=====================================")


def main():
    test(100, 50, "sword")
    test(500, 100, "axe")
    test(1000, 250, "bow")


main()
