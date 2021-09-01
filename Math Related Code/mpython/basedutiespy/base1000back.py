import json
import sys

def b1000b(n):
    fname = 'basedutiespy\\base1000.json'
    with open(fname, 'r', encoding='utf-8', newline='') as f:
        list = json.load(f)

    final = []

    for k in str(n):
        i = str(list.index(k)).zfill(3)
        final.append(i)

    return ''.join(final)

try:
    n = input("Number:")
except Exception:
    print("We want a number!")
    sys.exit()

print(b1000b(n))