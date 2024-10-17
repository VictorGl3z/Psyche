# Problem Statement
# Given the radius of a circle and the area of a square, return True if the circumference of the circe is greater than the square's perimeter
# and False if the square's perimeter is greater than the circumference of the circle
# Examples
# circle_or_square(16, 625) -> True
# circle_or_square(5, 100) -> false

import math 

def circle_or_square(r_circle, a_square):
    return 2 * math.pi * r_circle > 4 * a_square ** 0.5

while True:
    radius = input('Type the radius of the circle: ')
    try:
        radius = float(radius)
        break
    except:
        print('That is not a valid number!')
        continue

while True:
    area = input('Type the area of the square: ')
    try:
        area = float(area)
        break
    except:
        print('That is not a valid number!')
        continue
    
returned = circle_or_square(radius, area)
if returned:
    print('The circumference of the circle is greater than the perimeter of the square.')
else:
    print('The area of the square is greater than the circumference of the circle.')
    

    