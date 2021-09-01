#This program can check if the input number can be written as the sum of 2 squares.

def So2s(n):
    i = 2
    while i * i <= n:
        count = 0
        if n % i == 0:
            while n % i == 0:
                count += 1
                n = int(n / i)
            if i % 4 == 3 and count % 2 != 0:
                return False
        i += 1
    return n % 4 != 3

nn = int(input("Number:"))
if So2s(nn): print(f"{nn} can be written as the sum of two squares.")
else: print(f"{nn} cannot be written as the sum of two squares.")