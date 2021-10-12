from fractions import Fraction
from functools import reduce

def funny_cancels(a,b):
    sa = str(a)
    sb = str(b)
    for i in range(len(sa)):
        for j in range(len(sb)):
            num = int(sa[:i] + sa[i+1:])
            den = int(sb[:j] + sb[j+1:])
            if sa[i] != '0' and num < den and sa[i] == sb[j] and Fraction(num,den) == Fraction(a,b):
                return True
    return False

if __name__ == "__main__":
    res = {str(a) + "/" + str(b) for a in range(10,100) for b in range(10,100) if funny_cancels(a,b)}
    print(reduce(lambda a,b: Fraction(a)*Fraction(b), res))
