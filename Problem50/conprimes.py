from eratosthenes import eratosthenes
if __name__ == "__main__":
    primes = eratosthenes(10 ** 6)
    pset = set(primes)
    prefix_sums = [2]
    for i in range(1,len(primes)):
        prefix_sums.append(prefix_sums[-1] + primes[i])
    print(len(primes))
    m = 0
    # this part is too slow...
    # maybe try to 'pinch' around a number, checking prefix sums bigger and smaller than it?
    # or maybe change what we iterate over entirely... can't be quadratic in # of primes
    for i in range(len(prefix_sums)):
        for j in range(i+21,len(prefix_sums)):
            if (prefix_sums[j] - prefix_sums[i]) in pset:
                m = max(prefix_sums[j] - prefix_sums[i], m)
    print(m)
