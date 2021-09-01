import math
import sys
from sympy.ntheory import *
import moddy as mo
from sympy import *

try:
    nn = int(input("Number:"))
except Exception:
    print("We want a number.")
    sys.exit()

dic = {'prm': '',}
bood = {}

#binary
if nn == abs(nn):
    bood['neg'] = False
    dic["bin"] = f"{nn} in binary is {int(bin(nn)[2:])}"
    b = int(bin(nn)[2:])
else:
    bood['neg'] = True
    dic["bin"] = f" {nn} in binary is {-1 * int(bin(nn)[3:])}"
    b = -1 * int(bin(nn)[3:])

if mo.prime(nn) == 1: 
    if not dic['prm']:
            dic['prm'] = f"{nn} is prime."
            bood['prm'] = True
elif mo.prime(nn) == 0: 
    if not dic['prm']:
            dic['prm'] = f"{nn} is composite."
            bood['prm'] = False
elif mo.prime(nn) == 2: 
    if not dic['prm']:
            dic['prm'] = f"{nn} is neither prime nor composite."
            bood['prm'] = False
elif mo.prime(nn) == 3: 
    if not dic['prm']:
            dic['prm'] = f"{nn} is prime."
            bood['prm'] = True
elif mo.prime(nn) == -1: 
    if not dic['prm']:
            dic['prm'] = f"{nn} is negative."
            bood['prm'] = False

if mo.So2s(nn): dic['so2'] = f'{nn} can be represented by the sum of 2 squares.'; bood['so2'] = True
else: dic['so2'] = f'{nn} cannot be represented by the sum of 2 squares.'; bood['so2'] = False

if mo.evil(nn):  dic['evl'] = f'{nn} is evil.'; bood['evl'] = True
else: dic['evl'] = f'{nn} is odious.'; bood['evl'] = False

if mo.happy(nn): dic['hap'] = f'{nn} is happy.'; bood['hap'] = True
else: dic['hap'] = f'{nn} is sad.'; bood['sad'] = False

if mo.trian(nn): dic['tri'] = f"{nn} is a triangular number."; bood['tri'] = True
else: dic['tri'] = f"{nn} is not a triangular number."; bood['tri'] = False

if mo.square(nn): dic['sqr'] = f"{nn} is a square number."; bood['sqr'] = True
else: dic['sqr'] = f"{nn} is not a square number."; bood['sqr'] = False

if mo.cube(nn): dic['cub'] = f"{nn} is a cube number."; bood['cub'] = True
else: dic['cub'] = f"{nn} is not a cube number."; bood['cub'] = False

if mo.regular(nn): dic['reg'] = f"{nn} is a regular number."; bood['reg'] = True
else: dic['reg'] = f"{nn} is not an regular number."; bood['reg'] = False

if mo.humble(nn): dic['hum'] = f"{nn} is a humble number."; bood['hum'] = True
else: dic['hum'] = f"{nn} is not a humble number."; bood['hum'] = False

if nn > 0:
    dic['sig'] = f"The Divisor Function of {nn} is {divisor_sigma(nn)}"
elif nn < 1: dic['sig'] = ''

if nn > 0:
    dic['tot'] = f"The Euler Totient of {nn} is {totient(nn)}"
elif nn < 1: dic['tot'] = ''

if nn > 0:
    dic['ppi'] = f"The Prime Pi of {nn} is {primepi(nn)}"
elif nn < 1: dic['ppi'] = ''

if nn > 0:
    if nn < 3: dic['pnp'] = f"The prime after {nn} is 3"
    dic['pnp'] = f"The prime before {nn} is {prevprime(nn)}, and the prime after {nn} is {nextprime(nn)}"
elif nn < 1: dic['pnp'] = f"The prime after {nn} is 3"

if nn > 0:
    if is_perfect(nn):
        dic['per'] = f"{nn} is a perfect number."
        bood['per'] = True
    else:
        dic['per'] = f"{nn} is not a perfect number."
        bood['per'] = False
elif nn < 1: dic['per'] = ''; bood['per'] = False

if nn > 0:
    if is_abundant(nn):
        dic['abu'] = f"{nn} is an abundant number."
        bood['abu'] = True
    else:
        dic['abu'] = f"{nn} is not an abundant number."
        bood['abu'] = False
elif nn < 1: dic['abu'] = ''; bood['abu'] = False

if nn > 0:
    if is_deficient(nn):
        dic['def'] = f"{nn} is a deficient number."
        bood['def'] = True
    else:
        dic['def'] = f"{nn} is not a deficient number."
        bood['def'] = False
elif nn < 1: dic['def'] = ''; bood['def'] = False

if is_palindromic(abs(nn)):
    dic['pal'] = f"{nn} is palindromic."
    bood['pal'] = True
else: 
    dic['pal'] = f"{nn} is not palindromic."
    bood['pal'] = False

dic['dgr'] = f"The digital root of {nn} is {mo.digiroot(nn)}."

if not bood['neg']:
    if mo.unusual(nn): dic['unu'] = f"{nn} is unusual."; bood['unu'] = True
    else: dic['unu'] = f"{nn} is not unusual."; bood['unu'] = False

    if mo.powerful(nn): dic['pow'] = f"{nn} is a powerful number."; bood['pow'] = True
    else: dic['pow'] = f"{nn} is not a powerful number."; bood['pow'] = False

    if mo.perfect(nn): dic['ppo'] = f"{nn} is a perfect power."; bood['ppo'] = True
    else: dic['ppo'] = f"{nn} is not a perfect power."; bood['ppo'] = False

    if bood['pow'] and not bood['ppo']: dic['ach'] = f"{nn} is an Achilles number"; bood['ach'] = True
    else: dic['ach'] = f"{nn} is not an Achilles number"; bood['ach'] = False
else:
    dic['pow'] = 'Negative numbers are complex.'
    dic['ppo'] = 'Negative numbers are complex.'
    dic['ach'] = 'Negative numbers are complex.'
    dic['unu'] = 'Negative numbers are complex.'

#digits
dic["dig"] = f"{nn} has {len(str(abs(nn)))} digit(s)."

#check for Power of 2
if nn == abs(nn) and nn > 0:
    j = 0
    for kk in str(abs(int(b))):
        j += int(kk)
    if j == 1:
        dic['pot'] = f"{nn} is a power of 2."; bood['pot'] = True
    else:
        dic['pot'] = f"{nn} is not power of 2"; bood['pot'] = False
        dic['pol'] = f"{nn} is polite."; bood['pol'] = True
else: dic['pot'] = ''; bood['pot'] = False;

#check for mersenne
if nn == abs(nn):
    if is_mersenne_prime(nn):
        mrsprm = '\n It is a mersenne prime.'
    elif math.log2(nn + 1) == math.floor(math.log2(nn + 1)):
        mrsprm = '\n It is a mersenne number.'
    else:
        mrsprm = '' 
else: mrsprm = ''

#Check if it is a Safe or Sophie Germain Prime.
if bood['prm']:
    if nn == 2: sfprm = '\n It is not a safe prime.'; sphprm = 'It is a Sophie Germain prime.'
    elif nn == 3: sfprm = '\n It is not a safe prime.'; sphprm = 'It is a Sophie Germain prime.'
    elif nn == 5: sfprm = '\n It is a safe prime.'; sphprm = 'It is a Sophie Germain prime.'
    elif nn == 7: sfprm = '\n It is a safe prime.'; sphprm = 'It is not a Sophie Germain prime.'
    else:
        if mo.prime((nn - 1) / 2) == 1:
            sfprm = 'It is a safe prime.'
        else: 
            sfprm = 'It is not a safe prime.'
        if mo.prime((2 * nn) + 1) == 1:
            sphprm = 'It is a Sophie Germain prime.'
        else: 
            sphprm = 'It is not a Sophie Germain prime.'
else:
        sfprm = ''
        sphprm = ''

print(f"""{dic['dig']}
    {dic['prm']}
    {dic['bin']}
    {nn} in base 100 is {mo.BoBs.b100(nn)}.
    {nn} in base 1000 is {mo.BoBs.b1000(nn)}.
    {nn} in base 2048 is {mo.BoBs.b2048(nn)}.
    {dic['pot']}{sfprm}{sphprm}{mrsprm}
    {dic['so2']}
    {dic['evl']}
    {dic['hap']}
    {dic['sig']}
    {dic['tot']}
    {dic['ppi']}
    {dic['pnp']}
    {dic['pal']}
    {dic['tri']}
    {dic['sqr']}
    {dic['cub']}
    {dic['pow']}
    {dic['ppo']}
    {dic['ach']}
    {dic['abu']}
    {dic['def']}
    {dic['per']}
    {dic['reg']}
    {dic['hum']}
    {dic['unu']}
    {dic['dgr']}""")