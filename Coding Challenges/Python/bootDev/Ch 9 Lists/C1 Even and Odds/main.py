def get_odds_and_evens(numbers):
    num_evens = 0
    num_odds = 0

    # Don't touch above this line
    division = 0
    for i in range(len(numbers)):
        print(numbers[i])
        division = numbers[i] % 2
        if division == 1:
            num_odds += 1
        else:
            num_evens += 1
    return num_odds, num_evens
