import math


def g(x, n):
    return pow(x, 2, n) + 1


def factor(num):
    x = 2
    y = 2
    d = 1

    while d == 1:
        x = g(x, num)
        y = g(g(y, num), num)
        d = math.gcd(abs(x - y), num)
    if d == num:
        return None
    else:
        return d


num = 1506565219
print(factor(num))
