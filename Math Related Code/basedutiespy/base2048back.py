import json
import sys

def b2048b(n):
    li = str(n).split(' ')
    final = []

    fname = 'basedutiespy\\base2048.json'
    with open(fname, 'r', encoding='utf-8', newline='') as f:
        lsit = json.load(f)

    if len(li) == 1:
        return lsit.index(li[0])

    for k in li:
        nnn = lsit.index(k)
        bnn = bin(nnn)[2:]
        final.append(bnn.zfill(11))
        
    return int(''.join(final), 2)



try:
    n = str(input("Number:"))
except Exception:
    print("We want a string!")
    sys.exit()

print(b2048b(n))
