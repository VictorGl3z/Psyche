# Problem Statement
# Create a function that takes a base number and an exponent number and returns the calculation
# Examples
# calculate_exponents(5,5) -> 3125
# calculate_exponents(3,3) -> 27

def calculate_exponents(num, exp):
    return num ** exp

while True:
    base = input('Type your base number: ')
    try:
        base = float(base)
        break
    except:
        print('This is not a valid number!')
        continue
    
while True:
    exp = input('Type your exponent: ')
    try:
        exp = float(exp)
        break
    except:
        print('This is not a valid number!')
        continue
    
print('The result of', base, 'to the power of ', exp,'is: ', calculate_exponents(base,exp))

