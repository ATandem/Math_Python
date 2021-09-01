import math

n = int(input("First Number:"))
m = int(input("Second Number:"))

a = abs(2*m*n)
b = abs(m**2 - n**2)
c = abs(m**2 + n**2)

print(f"{a} squared plus {b} squared is equal to {c} squared.\n")
print(f"{a}² + {b}² = {c}²")
