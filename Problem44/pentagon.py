from math import sqrt
def pentagon(n):
    return (n // (2 - n % 2)) * (3 * n - 1) // (1 + n % 2)

def is_pentagonal(k):
    n = (1 + sqrt(1 + 24 * k)) / 6
    return int(n) == n

def inv_penta(k):
    if is_pentagonal(k):
        return (1 + sqrt(1 + 24 * k)) // 6

if __name__ == "__main__":
    pents = [pentagon(n) for n in range(1,5000)]
    maxD = pents[-1] - pents[-2]
    pset = set(pents)
    D = min(abs(x-y) for x in pset for y in pset if (x+y) in pset and (x-y) in pset)
    
    if D < maxD:
        print("Answer: " + str(D))
    else:
        print("Answer: " + str(D) + " (not guaranteed to be minimal)")
