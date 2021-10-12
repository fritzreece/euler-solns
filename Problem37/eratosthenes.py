from math import *

def eratosthenes(bound):
    if bound < 2:
        return []
    primes = [i for i in range(2,bound)]
    for i in range(len(primes)):
        if primes[i] < 0:
            continue
        for j in range(i+primes[i], len(primes), primes[i]):
            primes[j] = -1
    return [x for x in primes if x > 0]
        

