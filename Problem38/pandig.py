
def rep_digits(n):
    s = str(n)
    return any(sum(int(c == d) for d in s) > 1 for c in s)

def is_19_pandig(n):
    s = str(n)
    return not rep_digits(s) and '0' not in s and len(s) == 9

if __name__ == "__main__":
    m = 0
    for n in range(2,10):
        for i in range(1, 10 ** (10 // n)):
            res = int("".join(str(i * k) for k in range(1,n+1)))
            if is_19_pandig(res):
                print(res)
                m = max(m,res)
    print("Answer: " + str(m))

