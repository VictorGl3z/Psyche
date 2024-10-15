def is_prime(number):
    count = 0
    for i in range(1,number+1):
        division = number % i
        if division == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False
            
        
    
