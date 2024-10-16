# Problem Statement
# Write a function that converts hours into seconds
# Examples
# how_many_seconds(2) -> 7200
# how_many_seconds(10) -> 36000

def how_many_seconds(hours):
    return hours * 3600

while True:
    hrs = input('Input your hours: ')
    try:
        hrs = float(hrs)
        break
    except:
        print('This is not a valid number!')
        continue
    
print(hrs, 'hours are:', how_many_seconds(hrs), 'seconds.')