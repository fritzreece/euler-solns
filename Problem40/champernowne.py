from time import time
def d(n):
    # first, calculate how many digits come before based on integers w fewer digits
    m = len(str(n)) - 1
    numbefore = m * (10 ** m) - (10 ** m - 1)//9
    # this might be a bit more complicated actually....

# easy baby mode! hooray, computers!!!
if __name__ == "__main__":
    start = time()
    l = []
    for i in range(1,10 ** 6):
        for c in str(i):
            l.append(c)
    prod = 1
    for i in range(7):
        prod *= int(l[10 ** i - 1])
    print("Answer: " + str(prod))
    print("Time: " + str(time() - start))
