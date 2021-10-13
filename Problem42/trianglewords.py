from time import time
# the words can only have such a high score
# putting all the triangle numbers we could possibly have into a set
# will make it fast to check which words score a triangle
def tri_set(bound):
    m = 0
    n = 1
    res = set()
    while m < bound:
        m = n * (n + 1) // 2
        res.add(m)
        n += 1
    return res

def read_words(path):
    f = open(path)
    string = f.read()
    return [s[1:-1] for s in string.split(",")]

def word_score(word):
    return sum(ord(c) - ord('A') + 1 for c in word)

if __name__ == "__main__":
    start = time()
    tset = tri_set(10 ** 3)
    words = read_words("words.txt")
    print(sum(1 for w in words if word_score(w) in tset))
    print("Time: " + str(time() - start))
