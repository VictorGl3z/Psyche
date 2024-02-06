def smelt_ore():
    inventory = ["Healing Potion", "Iron Ore", "Bread", "Shortsword"]
    print(f"Inventory: {inventory}")

    # don't touch above this line

    inventory[1] = 'Iron Bar'

    # don't touch below this line

    return inventory


def test():
    inventory = smelt_ore()
    print(f"Smelting ore: {inventory}")
    print("=====================================")


def main():
    test()


main()
