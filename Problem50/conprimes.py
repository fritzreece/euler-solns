from eratosthenes import eratosthenes
if __name__ == "__main__":
    primes = eratosthenes(10 ** 6)
    pset = set(primes)

    # since we know the biggest sum will have at least 21 terms, we can
    # shrink the set of primes we check as the summand considerably
    # 10 is sort of arbitrary here (you can't necessarily divide by 21
    # since the largest prime could be more than 1/21th of the sum),
    # 10 seems to work, and shrinks our search space 100fold
    sumprimes = [p for p in primes if p < (10 ** 6) / 10]
    print(len(sumprimes))
    # calc prefix sums to find sums of consecutives fast as we search
    prefix_sums = [0,2]
    for i in range(1,len(sumprimes)):
        prefix_sums.append(prefix_sums[-1] + sumprimes[i])
    # print(len(primes))

    # track the max # of terms m, and the prime they sum to mprime
    m = 0
    mprime = 0
    for i in range(len(prefix_sums)):
        for j in reversed(range(i+1,len(prefix_sums))):
            if prefix_sums[j] - prefix_sums[i] in pset and (j-i) > m:
                print(i,j)
                m = j-i
                mprime = prefix_sums[j] - prefix_sums[i]
    print(mprime)

