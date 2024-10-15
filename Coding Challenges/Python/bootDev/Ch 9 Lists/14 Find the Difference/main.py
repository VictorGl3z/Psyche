def check_character_levels():
    old_character_levels = [1, 42, 43, 53, 12, 3, 32, 34, 54, 32, 43]
    new_character_levels = [1, 42, 45, 54, 12, 3, 32, 38, 54, 32, 43]

    # don't touch above this line

    for i in range(0, len(old_character_levels)):
        if old_character_levels[i] != new_character_levels[i]:
            print(i)


# don't touch below this line


def test():
    print("Differences found on indexes:")
    check_character_levels()
    print("=====================================")


def main():
    test()


main()
