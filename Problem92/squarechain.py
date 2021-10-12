def sq_sum(n):
    return sum(int(c) * int(c) for c in str(n))

# note that 7 * 9^2 = 567. Therefore, any sum of digit of squares of numbers below 10^7
# will be at most 486, so if we memoize all the values up to that, we can solve bigger numbers in one step
# without using too much time building up a memo of bigger values
# improves runtime ~30%
def memo_up_to(bound=568):
    res = [0 for i in range(bound)]
    res[0] = 1
    res[88] = 89
    for i in range(2, bound):
        temp = i
        while temp != 1 and temp != 89:
            temp = sq_sum(temp)
        res[i-1] = temp
    return res

def sqc_loop(n, memo):
    return memo[sq_sum(n)-1]

# not terribly fast...
from time import time
if __name__ == "__main__":
   start = time()
   memo = memo_up_to()
   print("Memo generated in: " + str(time() - start))
   print("Answer: " + str(sum(1 for x in range(1, 10 ** 7) if sqc_loop(x, memo) == 89)))
   print("Time: " + str(time() - start))
