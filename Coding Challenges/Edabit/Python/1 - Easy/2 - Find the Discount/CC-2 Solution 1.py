# Problem Statement
# Create a function that takes two arguments: The original price and the discount percentage as integers
# and returns the final price after the discount.
# Examples
# dis(1500,50) -> 750
# dis(100,75) -> 25

def dis(price, discount):
    total = price * (1 - discount / 100)
    return round(total,2)
    
while True:
    og = input('Type the original price of the product: ')
    try:
        og = int(og)
        break
    except:
        print('Please type a valid number!')
        continue

while True:
    perc = input('Type the discount percentage: ')
    try:
        perc = int(perc)
        break
    except:
        print('Please type a valid number!')
        continue


print('The final price after the discount is:',dis(og,perc))