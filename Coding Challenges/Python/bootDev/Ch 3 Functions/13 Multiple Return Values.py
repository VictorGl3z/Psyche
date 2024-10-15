def become_warrior(first_name, last_name, power):
    Title = first_name + " " + last_name + " the warrior"
    Power = power + 1
    return Title, Power


# Don't edit below this line


def main():
    test("Frodo", "Baggins", 5)
    test("Bilbo", "Baggins", 10)
    test("Gandalf", "The Grey", 9000)


def test(first_name, last_name, power_level):
    title_string, power = become_warrior(first_name, last_name, power_level)
    print(title_string, "has a power level of:", power)


main()
