# the length of cycle for fraction 1/d
def cycle_length(d, base=10):
    distincts = set()
    pwr = 1
    curr = pow(base, pwr,mod=d)
    while curr not in distincts:
        distincts.add(curr)
        pwr += 1
        curr = pow(base, pwr,mod=d)
    return pwr - 1

if __name__ == "__main__":
    cycles = [cycle_length(d) for d in range(1,1000)]
    print(cycles.index(max(cycles)) + 1)
