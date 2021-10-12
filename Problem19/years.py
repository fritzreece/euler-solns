from datetime import *
count = 0
daynum = 1
d = date(1900,1,1)
delta = timedelta(days=1)
while d < date(1901,1,1):
    d += delta
    daynum += 1
while d <= date(2000,12,31):
    if daynum % 7 == 0 and d.day == 1:
        count += 1
    d += delta
    daynum += 1
print(count)
