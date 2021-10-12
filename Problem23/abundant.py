from amicable import *

def is_abundant(n):
    return sum(proper_divisors(n)) > n

def abundant_nums(bound):
    return {i for i in range(1,bound) if is_abundant(i)}

def sum_of_two(n, abundants):
    for a in abundants:
        if n - a in abundants:
            return True
    return False

if __name__ == "__main__":
    ab = abundant_nums(28124)
    print(sum(x for x in range(28124) if not sum_of_two(x,ab)))
