### Problem Statement ##
# Create a function that takes two numbers as arguments and returns their sum
## Examples
# addition(3,2) -> 5
# addition(-3, 6) -> -9

def addition(a,b):
    sum = a + b
    return sum
n = []

for i in range(0,2):
    while True:
        num = input('Enter your number: ')
        try:
            float(num)
            break
        except:
            print('That is not a valid number!')
            continue
    n.append(float(num))

print('The addition of',n[0], 'and', n[1], 'is:', addition(n[0],n[1]))
