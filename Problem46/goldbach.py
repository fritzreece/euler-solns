from math import sqrt
from eratosthenes import eratosthenes
def is_square(n):
    root = sqrt(n)
    return int(root) == root

def test(n, primes):
    i = 0
    while primes[i] < n:
        if is_square((n - primes[i]) // 2):
            return True
        i += 1
    return False

if __name__ == "__main__":
    primes = eratosthenes(10 ** 6)
    pset = set(primes)
    for n in range(3, 10 ** 6, 2):
        if n not in pset and not test(n, primes):
            print(n)
            exit()

