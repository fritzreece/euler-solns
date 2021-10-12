from math import log2

def b_pali(n):
    firstdig = int(log2(n))
    big = 1 << firstdig
    for i in range((firstdig+1) // 2):
        if bool(n & (big >> i)) != bool(n & (1 << i)):
            return False
    return True

def to_pali(string, short=True):
    root = string[:-1] if short else string
    return root + "".join(string[-i] for i in range(1,len(string)+1))

def tps(string):
    return to_pali(string)

def tpl(string):
    return to_pali(string,False)

if __name__ == "__main__":
    s = 0
    for i in range(1,1000):
        if b_pali(int(tps(str(i)))):
            s += int(tps(str(i)))
        if b_pali(int(tpl(str(i)))):
            s += int(tpl(str(i)))
    print(s)
