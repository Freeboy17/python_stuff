import math
from random import randint
import NSD
nsd = NSD.NSD()
#import Crypto.Util.number as num
 # This function check if number is prime
def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True
#KEY GENERATION START
# Generating prime p
while True:
    p = randint(5, 1000)
    if is_prime(p):
        break

"""generates the group <zp*,x>"""
def gen(g, p):
    E = []
    """creating an empty set"""
    my_set = set(E)
    for x in range(1, p):
        """num=g^x mod p"""
        num = pow(g, x, p)
        my_set.add(num)
    return len(my_set)

# inverse number calculator

def modInverse(a, m):
    m0 = m
    y = 0
    x = 1
    if m == 1:
        return 0
    while (a > 1):
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t

    if (x < 0):
        x = x + m0

    return x

if len(bin(p)) < 129:
    for x in range(1, p):
        if gen(x, p) == (p - 1):
            E1 = x
            break
#print("e1(Generator): ", E1)
# Generating private key
while True:
    x = randint(1, p)
    if x <= (p - 2) and x >= 1:
        break

E2 = pow(E1, x, p)

print("public key: (", E1, ",", E2, ",", p, ")")
print("private key(x): ", x)
#KEY GENERATION END

#SIGNATURE GENERATION START
#Generatea random integer k such that 1≤k≤p−2 and gcd(k,p−1)=1.

while 1==1:
    k = randint(1, p-2)
    #temp = nsd.extended_gcd(k, p-1)[0]
    if nsd.extended_gcd(k, p-1)[0] == 1: break
m=40
# Compute r = α**k mod p.
r = pow(E1, k, p)
l = modInverse(k, p-1)
s = l*(m-x*r)%(p-1)

print(f'digital sign: {r}, {s}')
#SIGNATURE GENERATION END
#SIGNATURE VERIFICATION START
def egVer(p, a,	y, r, s, m):
	if r < 1 or r > p-1 : return False
	v1 = pow(y,r,p)%p * pow(r,s,p)%p
	v2 = pow(a,m,p)
	return v1 == v2
#egVer(p, E1, E2, r, s, m)
#SIGNATURE VERIFICATION END
#TEST

print("Message: ", m)
#prime,alpha,private,public = egKey(10)
print("prime,alpha,private,public", p,E1,x,E2)
#rr,ss = egGen(prime,alpha,private, message)
print(f'digital signature: {r}, {s}')
isValid = egVer(p, E1, E2, r, s, m)
print("Valid Signature: " , isValid)
asd = input("press any key to exit")