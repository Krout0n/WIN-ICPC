n, p = [int(i) for i in input().split()]
a = [[] for _ in range(p+1)]

for _ in range(n):
    l = [int(i) for i in input().split()]
    l.append(sum(l))
    [a[i].append(j) for i, j in enumerate(l)]
    print(*l)

for h,i in enumerate(a):
    if h == len(a) - 1:
        print(sum(i))
    else:
        print(sum(i),end=' ')