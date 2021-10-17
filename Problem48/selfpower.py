# pretty simple using python 3's pow(base,exp,mod)

if __name__ == "__main__":
    print(sum(pow(i,i,10 ** 10) for i in range(1,1001)) % 10 ** 10)
