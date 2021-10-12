
def gen_squares(bound):
    return {x * x for x in range(1, bound)}

def gen_pythags(bound):
    res = set()
    squares = gen_squares(bound)
    for c2 in squares:
        for b2 in squares:
            if c2 - b2 in squares:
                res.add(tuple(sorted(int(x ** 0.5) for x in {c2-b2,b2,c2})))
    return res

if __name__ == "__main__":
    s = gen_pythags(1000)
    s = {x for x in s if sum(x) <= 1000}
    maxsol = 0
    maxnum = 0
    for i in range(1,1000):
        solnum = sum(1 for x in s if sum(x) == i)
        if solnum > maxnum:
            maxsol = i
            maxnum = solnum
    print(maxsol)

