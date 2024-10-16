# Problem Statement
# Create a function that takes an angle in radians and returns the corresponding angle in degrees
# rounded to one decimal place.
# Examples
# radians_to_degrees(1) -> 57.3
# radians_to_degreess(20) -> 1145.9

from math import pi
def radians_to_degrees(angle):
    res = angle * 180 / pi
    return round(res,1)

while True:
    ang = input('Type your angle in radians: ')
    try:
        ang = float(ang)
        break
    except:
        print('Not a valid number!')
        continue
    
print(ang, 'radians are',radians_to_degrees(ang), 'degrees.' )