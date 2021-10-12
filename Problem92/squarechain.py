

MEMO = {}
# returns the first entry visited twice on square chain starting at n. memoized
def sqc_loop(n):
    curr = n
    seen = set()
    while curr not in MEMO and curr not in seen:
        seen.add(curr)
        curr = sum(int(c) ** 2 for c in str(curr))
    if curr in MEMO:
        curr = MEMO[curr]
    for s in seen:
        MEMO[s] = curr
    return curr

# not terribly fast...
from time import time
if __name__ == "__main__":
   start = time()
   print("Answer: " + str(sum(1 for i in reversed(range(1,10 ** 7)) if sqc_loop(89) == sqc_loop(i))))
   print("Time: " + str(time() - start))
