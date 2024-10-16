# Problem Statement
# Create a function that takes a number as an argument, increments the number by +1 and returns the result.
# Examples
# addition(0) -> 1
# addition(9) -> 10

def addition(num):
    res = num + 1
    return res

while True:
    n = input('Type your number: ')
    try:
        float(n)
        break
    except:
        print('This is not a valid number!')
        continue

n = float(n)
    
print('The next integer of the number', n, 'is:', addition(n))