import math
from Crypto.Util.number import isPrime
from tqdm import tqdm


def pollard(a, e, n):
    max_iter = 100
    iters = 0

    d = 1
    while d == 1:
        a = pow(a, e, n)
        d = math.gcd(a - 1, n)
        e += 1
        iters += 1

        if d == n:
            return None
        elif iters > max_iter:
            return None

    return d


num = 11 * 23 * 37 * 3 * 13 * 11
factors = []

iter_counts = []

for i in tqdm(range(2, 50)):
    new_num = num
    factors = []
    iter_counts.append(0)
    while not isPrime(new_num):
        factor = pollard(i, 2, new_num)
        if factor is None:
            iter_counts[-1] = 1000
            break
        factors.append(factor)
        new_num //= factor

        if isPrime(new_num):
            factors.append(new_num)

        iter_counts[-1] += 1

    print(factors)

for i, num in enumerate(iter_counts):
    print(i+2, num)
