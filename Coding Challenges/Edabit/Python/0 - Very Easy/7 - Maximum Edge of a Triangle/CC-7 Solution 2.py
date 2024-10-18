# Problem Statement
# Create a function that finds the maximum range of a triangle's third edge,
# where the side lengths are all integers.
# Examples
# next_edge(8, 10) -> 17
# next_edge(5, 7) -> 11

def next_edge(*args):
    return sum(args) - 1

while True:
    side1 = input('Type the first side of the triangle: ')
    try:
        side1 = float(side1)
        if side1 > 0:
            break
        else:
            print('Please only input positive numbers!')
            continue
    except:
        print('That is not a valid number!')
        continue

while True:
    side2 = input('Type the second side of the triangle: ')
    try:
        side2 = float(side2)
        if side2 > 0:
            break
        else:
            print('Please only input positive numbers!')
            continue
    except:
        print('That is not a valid number!')
        continue

print("The maximum range of a triangle's third edge is:", next_edge(side1,side2))

