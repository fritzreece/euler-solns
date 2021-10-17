from eratosthenes import eratosthenes
from math import sqrt

# simple recursive version w/ memoization. since we iterate up it can become quite fast
# worst case O(sqrt(n)) but the answer is around 10^6 anyway so...
MEMO = {}
def pfactors(n):
    if n in MEMO:
        return MEMO[n]
    for i in range(2,int(sqrt(n)) + 1):
        if n % i == 0:
            MEMO[n] = {i} | pfactors(n // i)
            return MEMO[n]
    MEMO[n] = {n}
    return MEMO[n]

# gross main, but pretty fast (~1s)
if __name__ == "__main__":
    x = 2
    found = False
    while not found:
        f1 = len(pfactors(x))
        if f1 == 4:
            f2 = len(pfactors(x+1))
            if f2 == 4:
                f3 = len(pfactors(x+2))
                if f3 == 4:
                    f4 = len(pfactors(x+3))
                    if f4 == 4:
                        found = True
                    else:
                        x += 4
                else:
                    x += 3
            else:
                x += 2
        else:
            x += 1
    print(x)

