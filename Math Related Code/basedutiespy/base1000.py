import json
import sys

def b1000(n):
    len2 = len(str(n))
    final = ''
    list = []

    fname = 'basedutiespy\\base1000.json'
    with open(fname, 'r', encoding='utf-8', newline='') as f:
        list = json.load(f)
    
    if len2 == 3:
        return list[int(n)]
    
    if len2 % 3 == 1:
        n = str(n).zfill(len2 + 2)
    elif len2 % 3 == 2:
        n = str(n).zfill(len2 + 1)
 
    a = [str(n)[i:i+3] for i in range(0, len(str(n)), 3)]

    for k in a:
        a[a.index(k)] = list[int(k)]
    final = ''.join(a)

    return final

if __name__ == '__main__':
    try:
        n = int(input("Number:"))
    except Exception:
        print("We want a number!")
        sys.exit()

    print(b1000(n))
