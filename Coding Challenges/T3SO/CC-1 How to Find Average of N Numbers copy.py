numlist = []
sum = 0

while True:
    numbers = input("Enter any number: ")
    try:
        val = float(numbers)
        numlist.append(val)
    except:
        print("Number input finished")
        break
    

for i in range(len(numlist)):
    sum += numlist[i]

avg = sum / len(numlist)
print("Average is: ", avg)