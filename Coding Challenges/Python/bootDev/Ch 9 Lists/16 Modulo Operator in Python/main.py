def get_odd_numbers(num):
    odd_numbers = []

    for i in range(0, num):
        # don't touch above this line
        number = i % 2
        if number == 1:
            odd_numbers.append(i)

    # don't touch below this line

    return odd_numbers
