# Problem Statement
# Write a function that takes the base and height of a triangle and return its area.
# Examples
# tri_area(3,2) -> 3
# tri_area(7,4) -> 14

def tri_area(base, height):
    res = base * height / 2
    return res

while True:
    b = input('Enter your base: ')
    try:
        b = float(b)
        break
    except:
        print('This is not a valid number!')
        continue
    
while True:
    h = input('Enter your height: ')
    try:
        h = float(h)
        break
    except:
        print('This is not a valid number!')
        continue
    
print('The area of the triangle is:', tri_area(b,h))