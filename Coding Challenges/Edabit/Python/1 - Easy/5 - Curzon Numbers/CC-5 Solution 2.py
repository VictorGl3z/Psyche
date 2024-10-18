# Problem Statement
# In this challenge, establish if a given integer num is a Curzon number.
# If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num,
# then num is a Curzon number
# Give a non-negative integer num, implement a function that returns True
# if num is a Curzon number, or False otherwise.
# Examples
# is_curzon(5) -> True
# 2 ** 5 + 1 = 33
# 2 * 5 + 1 = 11
# 33 is multiple of 11
# 
# is curzon(10) -> False
# 2 ** 10 + 1 = 1025
# 2 * 10 + 1 = 21
# 1025 is not a multiple of 21

def is_curzon(num):
	return not (2**num + 1) % (2*num + 1)

while True:
    num = input('Input your number')
    try:
        num = float(num)
        break
    except:
        print('That is not a valid number!')
        continue

print(is_curzon(num))