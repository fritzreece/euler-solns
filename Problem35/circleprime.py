from eratosthenes import eratosthenes

PRIMES = set(eratosthenes(10 ** 6))

# rotates a string n steps to the left
# rotate("hello",2) -> "llohe"
def rotate(string, n):
    n = n % len(string)
    return string[n:] + string[:n]

def is_circular(p):
    for n in range(len(str(p))):
        if int(rotate(str(p),n)) not in PRIMES:
            return False
    return True

if __name__ == "__main__":
    print(sum(1 for p in PRIMES if is_circular(p)))
