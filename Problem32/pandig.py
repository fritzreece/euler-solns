
def gen_all_perms(string):
    if len(string) == 0:
        return []
    if len(string) == 1:
        return [string]
    subperms = gen_all_perms(string[1:])
    res = []
    for i in range(len(string)):
        res += [s[:i] + string[0] + s[i:] for s in subperms]
    return res


def check_prods(string):
    res = []
    # i is index of character BEFORE which we put the *
    # j is index of char BEFORE which we put the =
    for i in range(1,len(string)-1):
        for j in range(i+1,len(string)):
            if int(string[:i]) * int(string[i:j]) == int(string[j:]):
                res.append(int(string[:i]) * int(string[i:j]))
    return res

if __name__ == "__main__":
    perms = gen_all_perms("123456789")
    res = []
    for p in perms:
        res += check_prods(p)
    res = set(res)
    print(sum(res))

