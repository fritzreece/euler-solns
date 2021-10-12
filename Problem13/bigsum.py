infile = open("nums.txt")
res = 0
for line in infile:
    res += int(line)
print(res)
