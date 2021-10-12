string = open("names.txt").read()
names = string.split(",")
names = ["".join(c for c in n if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ") for n in names]
names.sort()
print(names[0:20])
total = 0
count = 1
for n in names:
    score = sum(ord(c) - ord('A') + 1 for c in n)
    total += score * count
    count += 1
print(total)
