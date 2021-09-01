import math
import BoBs
from sympy import *
from sympy.ntheory.primetest import *

def prime(n):
    if n < 0: return -1

    if n == 0 or n == 1:
        x = 2
    elif n == 2 or n == 3:
        x = 3

    l = int((sqrt(n)))

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

    #return the result
    return x
def square(n):
    n = abs(n)
    return is_square(n)
def cube(n):
    n = abs(n)
    return int(round(n ** (1. / 3))) ** 3 == n
def So2s(m):
    if square(m) or square(m+1): return True
    i = 2
    while i * i <= m:
        count = 0
        if m % i == 0:
            while m % i == 0:
                count += 1
                m = int(m / i)
            if i % 4 == 3 and count % 2 != 0:
                return False
        i += 1
    return m % 4 != 3
def evil(m):
    b = bin(m)[2:]
    i = 0
    for k in str(b):
        if k == str(1): i += 1
    return i % 2 == 0
def numSquareSum(n):
    squareSum = 0
    while(n):
        squareSum += (n % 10) * (n % 10)
        n = int(n / 10)
    return squareSum
def happy(m):
    # initialize slow and fast by m
    slow = m
    fast = m
    while(True):
        # move slow number by one iteration
        slow = numSquareSum(slow)

        # move fast number by two iteration
        fast = numSquareSum(numSquareSum(fast))
        if(slow != fast):
            continue
        else:
            break
        
    # if both number meet at 1, return true
    return (slow == 1)
def trian(num):
    if (num < 0):
        return False
 
    # Considering the equation n*(n+1)/2 = num
    # The equation is : a(n^2) + bn + c = 0
    c = (-2 * num)
    b, a = 1, 1
    d = (b * b) - (4 * a * c)
 
    if (d < 0):
        return False
 
    # Find roots of equation
    root1 = ( -b + math.sqrt(d)) / (2 * a)
    root2 = ( -b - math.sqrt(d)) / (2 * a)
 
    # checking if root1 is natural
    if (root1 > 0 and math.floor(root1) == root1):
        return True
 
    # checking if root2 is natural
    if (root2 > 0 and math.floor(root2) == root2):
        return True
 
    return False
def powerful(n):
    if n == 0: return False

    # First divide the number repeatedly by 2
    while (n % 2 == 0):
        power = 0
        while (n % 2 == 0):
            n = n//2
            power = power + 1
        # If only 2 ^ 1 divides
        # n (not higher powers),
        # then return false
        if (power == 1):
            return False

    # if n is not a power of 2
    # then this loop will execute
    # repeat above process
    for factor in range(3, int(math.sqrt(abs(n)))+1, 2):
        # Find highest power of
        # "factor" that divides n
        power = 0
        while (n % factor == 0):
            n = n//factor
            power = power + 1
         
        # If only factor ^ 1 divides
        # n (not higher powers),
        # then return false
        if (power == 1):
            return False

     # n must be 1 now if it
     # is not a prime numenr.
     # Since prime numbers are
     # not powerful, we return
     # false if n is not 1.
    return (n == 1)
def perfect(n) :
    
    if (n==1): return True
    if square(n): return True

    # Try all numbers from 2 to sqrt(n) as base
    for x in range(2,(int)(math.sqrt(abs(n)))+1) :
        y = 2
        p = (int)(math.pow(x, y))
  
        # Keep increasing y while power 'p' is smaller
        # than n.
        while (p<=n and p>0) :
            if (p==n) :
                return True
             
            y = y + 1
            p = math.pow(x, y)
    return False
def digiroot(n):
    #ALL ME
    if n < 10: return n 
    ans = 0
    for k in str(n):
        ans += int(k)
    while ans > 9:
        rv = 0
        for k in str(ans):
            rv += int(k)
        ans = rv
    return ans
def regular(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)

    for k in factors:
        if k <= 5:
            continue
        else:
            return False
    return True 
def humble(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)

    for k in factors:
        if k <= 7:
            continue
        else:
            return False
    return True 
def unusual(n):
    if n == 0: return False
    i = 2
    nn = n
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
        
    gpf = max(factors)

    if gpf > math.sqrt(nn):
        return True
    else:
        return False

