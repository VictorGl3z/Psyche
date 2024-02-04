def main():
    test(8_000_000, 3_000_000)
    test(10_000_000, 4_500_000)


# Don't edit below this line


def calculate_male_ratio(num_fruit_bats, num_male_bats):
    return num_male_bats / num_fruit_bats


def test(num_fruit_bats, num_male_bats):
    ratio = calculate_male_ratio(num_fruit_bats, num_male_bats)
    print(f"{ratio * 100}% of fruit bats are male")
    print("=====================================")


main()
