import math
import sys

try:
    n = int(input("Number:"))
except Exception:
    print("We want a number.")
    sys.exit()

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
        if k <= 7:
            continue
        else:
            return False
    return True 

print(regular(n))