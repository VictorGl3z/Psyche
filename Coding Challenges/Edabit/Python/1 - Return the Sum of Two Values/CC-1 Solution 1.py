### Problem Statement ##
# Create a function that takes two numbers as arguments and returns their sum
## Examples
# addition(3,2) -> 5
# addition(-3, 6) -> -9

def addition(a,b):
    sum = a + b
    return sum

n1 = float(input('Input the first number: '))
n2 = float(input('Input the second number: '))

print('The addition of',n1, 'and', n2, 'is:', addition(n1,n2))
