if __name__ == "__main__":
    # lucky guess on the bound...
    tset = {n * (n + 1) // 2 for n in range(1,10 ** 5)}
    pset = {n * (3 * n - 1) // 2 for n in range(1, 10 ** 5)}
    hset = {n * (2 * n - 1) for n in range(1, 10 ** 5)}
    print(tset & pset & hset)
