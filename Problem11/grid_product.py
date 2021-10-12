from functools import reduce
from operator import mul
def build_grid(path):
    res = []
    with open(path) as infile:
        for line in infile:
            res.append([])
            for s in line.split():
                res[-1].append(int(s))
        return res

def print_grid(g):
    for r in g:
        print(r)

def prod(iterable):
    return reduce(mul, iterable, 1)

def max_prod(grid):
    res = 0
    # first pass; vert, horiz, and NW-SE diagonals
    for y in range(len(grid)-4):
        for x in range(len(grid[0])-4):
            vert = prod(grid[y+i][x] for i in range(4))
            hori = prod(grid[y][x+i] for i in range(4))
            diag = prod(grid[y+i][x+i] for i in range(4))
            res = max(res,vert,hori,diag)
    # second pass; NE-SW diagonals
    for y in range(3, len(grid)):
        for x in range(len(grid[0])-4):
            diag2 = prod(grid[y-i][x+i] for i in range(4))
            res = max(res,diag2)
    return res

if __name__ == "__main__":
    print(max_prod(build_grid("grid_text.txt")))
