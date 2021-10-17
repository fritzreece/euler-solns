from eratosthenes import eratosthenes

def all_perms(s):
    if len(s) < 2:
        return {s}
    res = set()
    for i in range(len(s)):
        subperms = all_perms(s[:i] + s[i+1:])
        for p in subperms:
            res.add(s[i] + p)
    return res

# return True iff there exist a,b in nums with b = 2*a
def two_mult(nums):
    for n in nums:
        if 2*n in nums:
            return True
    return False

if __name__ == "__main__":
    primes4 = {p for p in eratosthenes(10 ** 4) if len(str(p)) == 4}
    for p in primes4:
        pmatches = {int(s) for s in all_perms(str(p)) if int(s) in primes4}
        if len(pmatches) > 2 and two_mult({q - p for q in pmatches if q != p}):
            print(pmatches) # not the answer per se, but will print a set of matches that contains the answer
            # easy to solve by inspection after
