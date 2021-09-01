import json
import re

def b100(n):
    dic = {
        '00': '0',
        '01': '1',
        '02': '2',
        '03': '3',
        '04': '4',
        '05': '5',
        '06': '6',
        '07': '7',
        '08': '8',
        '09': '9',
        '10': '↊',
        '11': '↋',
        '12': 'A',
        '13': 'B',
        '14': 'C',
        '15': 'D',
        '16': 'E',
        '17': 'F',
        '18': 'G',
        '19': 'H',
        '20': 'I',
        '21': 'J',
        '22': 'K',
        '23': 'L',
        '24': 'M',
        '25': 'N',
        '26': 'O',
        '27': 'P',
        '28': 'Q',
        '29': 'R',
        '30': 'S',
        '31': 'T',
        '32': 'U',
        '33': 'V',
        '34': 'W',
        '35': 'X',
        '36': 'Y',
        '37': 'Z',
        '38': 'a',
        '39': 'b',
        '40': 'c',
        '41': 'd',
        '42': 'e',
        '43': 'f',
        '44': 'g',
        '45': 'h',
        '46': 'i',
        '47': 'j',
        '48': 'k',
        '49': 'l',
        '50': 'm',
        '51': 'n',
        '52': 'o',
        '53': 'p',
        '54': 'q',
        '55': 'r',
        '56': 's',
        '57': 't',
        '58': 'u',
        '59': 'v',
        '60': 'w',
        '61': 'x',
        '62': 'y',
        '63': 'z',
        '64': 'Γ',
        '65': 'Δ',
        '66': 'Ϝ',
        '67': 'Θ',
        '68': 'Λ',
        '69': 'Ξ',
        '70': 'Π',
        '71': 'Σ',
        '72': 'Φ',
        '73': 'Ψ',
        '74': 'Ω',
        '75': 'α',
        '76': 'β',
        '77': 'γ',
        '78': 'δ',
        '79': 'ε',
        '80': 'ϝ',
        '81': 'ζ',
        '82': 'η',
        '83': 'θ',
        '84': 'ι',
        '85': 'κ',
        '86': 'λ',
        '87': 'μ',
        '88': 'ν',
        '89': 'ξ',
        '90': 'π',
        '91': 'ρ',
        '92': 'σ',
        '93': 'ς',
        '94': 'τ',
        '95': 'υ',
        '96': 'φ',
        '97': 'χ',
        '98': 'ψ',
        '99': 'ω',
    }
    i = 0
    twobit = ''
    final = ''

    if len(str(n)) < 3: return dic[str(n).zfill(2)]
    if len(str(n)) % 2 == 1:
        f = str(n)[0]
        n = int(str(n)[1:])
    else:
        f = False

    

    for k in str(n):
        if i % 2 == 0:
            twobit = str(k)
        else:
            twobit += str(k)
            final += dic[twobit]
        i += 1

    if f:
        final = f + final

    return final
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
