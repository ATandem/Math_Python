import sys
import math

r = range(int(input('Beginning Value:')), int(input('End Value:') + 1))

#exclude the subprimes and neithers
if list(r)[0] <= 3 or list(r)[0] <= -1: print('Subprimes and Neithers are not allowed')

for j in r: 
    n = j

    nag = n

    if n < 0: n = abs(n)

    #check if number is 2 or 3 (subprime) or 0 or 1 (neither). Currently turned off for the loop system. 
    """if n == 1 or n == 0:
        print(f"{nag} is neither.")
        break
    elif n == 2 or n == 3:
        print(f"{nag} is a subprime")
        break"""
    l = int((n/2))


    #go through all numbers bigger than 1 and less than half the original number. (because factors)  
    for k in range(2, l + 1):
        """If number is evenly divisible by the current factor k"""
        if n % k == 0:
            x = 0
            break
        else:
            if k == l:
                x = 1
            elif k < l: 
                continue

    #print the result
    if x == 1:
        print(f"{nag} is prime!")
    elif x == 0:
        print(f"{nag} is composite")