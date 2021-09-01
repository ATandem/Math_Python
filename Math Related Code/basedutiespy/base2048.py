import json
import sys
import re

def b2048(n):
    final = ''
    bn = bin(n)[2:]
 
    with open('basedutiespy\\base2048.json', 'r', encoding='utf-8', newline='') as f:
        lsit = json.load(f)

    if n < 2048: return lsit[n]

    while len(str(bn)) % 11 != 0:
        bn = bn.zfill((len(str(bn)) + 1))

    a = re.findall('.{1,11}', bn)

    for k in a:
        nk = int(k, 2)
        word = lsit[nk]
        a[a.index(k)] = word
        
    final = ' '.join(a)

    return final

try:
    n = int(input("Number:"))
except Exception:
    print("We want a number!")
    sys.exit()

print(b2048(n))
