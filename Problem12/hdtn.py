from eratosthenes import *

PRIMES = eratosthenes(1000)

def num_divisors(n, primes=PRIMES):
    if n == 1:
        return 1
    for p in primes:
        if n % p == 0:
            pwr = 0
            while n%p == 0:
                n /= p
                pwr += 1
            return (pwr+1) * num_divisors(n, primes)
    return 2 # shouldn't get here
