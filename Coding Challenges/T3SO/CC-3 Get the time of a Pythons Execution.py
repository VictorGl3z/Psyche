import time
def myFunc():
    start = time.time()
    s = 0
    for i in range(1, n+1):
        s += i
    end = time.time()
    return s, end - start
n = 10000
print(myFunc()[1])