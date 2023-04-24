import math
from Crypto.Util.number import isPrime


def pollard(n):
    a = 2
    e = 2

    d = 1
    while d == 1:
        a = pow(a, e, n)
        d = math.gcd(a - 1, n)

        e += 1

    return d


num = 3*7*11
factors = []

while not isPrime(num):
    factor = pollard(num)
    factors.append(factor)
    num //= factor

    if isPrime(num):
        factors.append(num)

print(factors)
