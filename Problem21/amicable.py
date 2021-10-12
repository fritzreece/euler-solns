from math import *
def divisors(n):
    for i in range(2,ceil(sqrt(n))+1):
        if n % i == 0:
            res = {1,i}
            pwr = 1
            while n % (i ** (pwr+1)) == 0:
                pwr += 1
                res.add(i ** pwr)
            sub = divisors(n // (i ** pwr))
            return {r * s for r in res for s in sub}
    return {1,n}

def proper_divisors(n):
    return divisors(n) - {n}

def amicables(bound):
    res = set()
    for i in range(2, bound):
        di = sum(proper_divisors(i))
        if i != di and i == sum(proper_divisors(di)):
            res |= {i,di}
    return res
