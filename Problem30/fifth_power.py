
# note that 6 * (9^5) = 354294, so, 7 * (9^5) is a 6 dig number.
# suffice it to say, we only need to check up thru 6 dig numbers

def quint_sum(n):
    return sum(int(c) ** 5 for c in str(n))

if __name__ == "__main__":
    print(sum(i for i in range(2,7 * (9 ** 5)) if i == quint_sum(i)))
