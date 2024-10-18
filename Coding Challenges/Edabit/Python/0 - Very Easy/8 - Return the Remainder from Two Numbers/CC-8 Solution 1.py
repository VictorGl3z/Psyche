# Problem Statement
# There is a single operator in Python, capable of providing the remainder of a division operation.
# Two numbers are passed as parameters. The first parameter divided by the second parameter will
# have a remainder, possibly zero. Return that value
# Examples
# remainder(1, 3) -> 1
# remainder(3, 4) -> 3

def remainder(x, y):
    return x % y

while True:
    n1 = input('Type your first number: ')
    try:
        n1 = float(n1)
        if n1 > 0:
            break
        else:
            print('Only use positive integers!')
            continue
    except:
        print('That is not a valid number!')
        continue
    
while True:
    n2 = input('Type your second number: ')
    try:
        n2 = float(n2)
        if n2 > 0:
            break
        else:
            print('Only use positive integers!')
            continue
    except:
        print('That is not a valid number!')
        continue
    
print('The remainder of the division between', n1, 'and',n2, 'is:', remainder(n1, n2))
