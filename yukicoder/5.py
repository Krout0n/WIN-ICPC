L = int(input())
input()
W = sorted([int(i) for i in input().split()])
c = 0
s = 0
for i in W:
    s += i
    if s <= L:
        c += 1
    else:
        break
print(c)
