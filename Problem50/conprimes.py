from eratosthenes import eratosthenes
if __name__ == "__main__":
    primes = eratosthenes(10 ** 6)
    pset = set(primes)

    sumprimes = [p for p in primes if p < (10 ** 6) / 10]
    print(len(sumprimes))
    prefix_sums = [0,2]
    for i in range(1,len(sumprimes)):
        prefix_sums.append(prefix_sums[-1] + sumprimes[i])
    print(len(primes))
    m = 0
    mprime = 0
    for i in range(len(prefix_sums)):
        for j in reversed(range(i+1,len(prefix_sums))):
            if prefix_sums[j] - prefix_sums[i] in pset and (j-i) > m:
                print(i,j)
                m = j-i
                mprime = prefix_sums[j] - prefix_sums[i]
    print(mprime)

