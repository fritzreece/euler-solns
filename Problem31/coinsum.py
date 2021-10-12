
# put (a,b,c,d,e,f,g,h) to be a 2 pound, b 1 pound, c 50p, etc...

def num_ways(denoms, n):
    if n == 0:
        return 1
    if len(denoms) == 0:
        return 0
    if len(denoms) == 1:
        if n % denoms[0] == 0:
            return 1
        return 0
    return sum(num_ways(denoms[1:], n - k * denoms[0]) for k in range(n // denoms[0] + 1))

if __name__ == "__main__":
    print(num_ways((200,100,50,20,10,5,2,1),200))
