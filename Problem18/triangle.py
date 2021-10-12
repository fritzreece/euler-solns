def triangle(triarray):
    # maxarray stores the length of longest path ending at that spot in triarray
    maxarray = [[0 for x in a] for a in triarray]
    maxarray[0][0] = triarray[0][0]
    for i in range(1,len(triarray)):
        maxarray[i][0] = maxarray[i-1][0] + triarray[i][0]
        maxarray[i][-1] = maxarray[i-1][-1] + triarray[i][-1]
        for j in range(1,len(triarray[i])-1):
            maxarray[i][j] = triarray[i][j] + max(maxarray[i-1][j-1],
                                                    maxarray[i-1][j])
    return maxarray

def build_triarray(path="tri.txt"):
    inf = open(path)
    res = []
    for line in inf:
        strs = line.split()
        res.append([int(s) for s in strs])
    return res

