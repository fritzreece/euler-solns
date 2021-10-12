
def is_palindrome(n):
    s = str(n)
    for i in range(len(s)//2):
        if s[i] != s[-1-i]:
            return False
    return True

if __name__ == "__main__":
    res = 0
    for i in range(1,10 ** 3):
        for j in range(1, 10 ** 3):
            if is_palindrome(i * j):
                res = max(res, i * j)
    print(res)
