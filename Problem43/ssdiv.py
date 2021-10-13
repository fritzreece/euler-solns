from pandigprime import all_perms
from time import time
def div_rule(n):
    n = str(n)
    primes = [2,3,5,7,11,13,17]
    for i in range(1,8):
        if int(n[i:i+3]) % primes[i-1] != 0:
            return False
    return True

if __name__ == "__main__":
    start = time()
    print(sum(int(s) for s in all_perms("0123456789") if s[0] != '0' and div_rule(s)))
    print("Time: " + str(time() - start))
