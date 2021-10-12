from math import ceil

def factorial(n):
    res = 1
    while n > 0:
        res *= n
        n -= 1
    return res

# assume perms are zero indexed
def nth_perm(string, n):
    string = "".join(sorted(string))
    if n == 0:
        return string

    # the index in the sorted string of the character that will be first in the permutation
    subfac = factorial(len(string)-1) # only calc once
    # current position of character that will be in the front
    pos = n // subfac
    subperm_num = n % subfac
    sub = nth_perm(string[:pos] + string[pos+1:], n % subfac)
    return string[pos] + sub
