from math import sqrt
from time import time
def all_perms(string):
    if len(string) < 2:
        return [string]
    res = []
    for i in range(len(string)):
        subperms = all_perms(string[:i] + string[i+1:])
        res.extend(string[i] + p for p in subperms)
    return res

def is_prime(n):
    for i in range(2,int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    start = time()
    ps = "123456789"
    m = 0
    for i in reversed(range(1,11)):
        if m != 0:
            print(m)
            print("Time: " + str(time() - start))
            exit()
        perms = all_perms(ps[:i])
        for p in perms:
            if is_prime(int(p)):
                m = max(int(p),m)
