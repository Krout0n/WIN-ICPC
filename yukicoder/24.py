import math

d = [0 for i in range(10)]
for _ in range(int(input())):
    _cmd = input().split()
    w,x,y,z = map(int, _cmd[:4])
    cmd = _cmd[-1]
    if cmd == 'NO':
        d[w] = -math.inf
        d[x] = -math.inf
        d[y] = -math.inf
        d[z] = -math.inf
    else:
        d[w] += 1
        d[x] += 1
        d[y] += 1
        d[z] += 1

print(d.index(max(d)))
