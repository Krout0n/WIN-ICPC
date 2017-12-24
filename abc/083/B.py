x, a, b = [int(i) for i in input().split()]
c = 0
for i in range(x+1):
    s = sum([int(j) for j in list(str(i))])
    if a <= s <= b:
        c += i
print(c)