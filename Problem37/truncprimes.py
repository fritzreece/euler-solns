from eratosthenes import *

def truncable(p, pset):
    s = str(p)
    for i in range(len(s)):
        if int(s[i:]) not in pset:
            return False
        if i > 0 and int(s[:(-i)]) not in pset:
            return False
    return True

if __name__ == "__main__":
    pset = set(eratosthenes(10 ** 6))
    tset = {x for x in pset if x > 10 and truncable(x,pset)}
    print(tset)
    print(sum(tset))
