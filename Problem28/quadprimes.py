from eratosthenes import *
from fractions import Fraction

PRIMES = eratosthenes(11 ** 6)
PRIMESET = set(PRIMES)
MAXPRIME = PRIMES[-1]

def num_quads(a,b):
    n = 0
    while q_eval(1,a,b,n).denominator == 1 and int(q_eval(1,a,b,n)) in PRIMESET:
        n += 1
    if q_eval(1,a,b,n) > MAXPRIME:
        print("UH OH!")
    return n

# get coefficients (k,a,b) where f(n) = kn^2 + an + b is the unique quadratic
# where f(0) = t0, f(1) = t1, f(2) = t2
def solve_quad(t0,t1,t2):
    h = Fraction(1,2)
    return h * (t0 - 2*t1 + t2), h * (-3 * t0 + 4 * t1 - t2), t0

def q_eval(k,a,b,n):
    return k * n * n + n * a + b

def check_quads():
    max_a = 0
    max_b = 0
    m = 0
    bdex = 0
    while PRIMES[bdex] <= 1000:
        a = Fraction(-1999,2)
        while a < 1000:
            nq = num_quads(a,PRIMES[bdex])
            if nq > m:
                m = nq
                max_a = a
                max_b = PRIMES[bdex]
            a += Fraction(1,2)
        bdex += 1
    return max_a, max_b, m

