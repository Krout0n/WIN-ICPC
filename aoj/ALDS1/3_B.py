n, f = map(int, input().split())
d = []

for _ in range(n):
    i = input().split()
    d.append([i[0], int(i[1])])

t = 0
while len(d):
    if d[0][1] > f:
        t += f
        d[0][1] -= f
        d.append(d.pop(0))
    else:
        t += d[0][1]
        a = d.pop(0)
        print(a[0], t)
