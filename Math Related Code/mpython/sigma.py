import sys
from sympy import *

try:
    n = int(input("Number:"))
except Exception:
    print("We want a number.")
    sys.exit()

print(divisor_sigma(n))

print(totient(n))