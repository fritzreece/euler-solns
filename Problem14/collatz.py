memo = {1: 1}

def collatz(n):
    if n in memo:
        return memo[n]
    if n % 2 == 0:
        res = 1 + collatz(n//2)
    else:
        res = 2 + collatz((3*n+1)//2)
    memo[n] = res
    return res

