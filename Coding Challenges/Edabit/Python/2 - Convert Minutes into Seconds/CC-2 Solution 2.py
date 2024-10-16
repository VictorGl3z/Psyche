# Problem Statement 
# Create a function that takes an integer minutes and converts it to seconds.
# Examples
# convert(5) -> 300
# convert(3) -> 180

def convert(minutes):
    return minutes * 60

while True:
    mins = input('Input your minutes: ')
    try:
        float(mins)
        break
    except:
        print('This is not a valid number!')
        continue

mins = float(mins)
print(mins, 'mins are:', convert(mins), 'seconds.')