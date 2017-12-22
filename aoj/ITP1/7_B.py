import itertools

while True:
    n,x = [int(i) for i in input().split()]
    if not(n or x):
        break
    s = list(itertools.combinations(list(range(1,n+1)), 3))
    c = 0
    for i in s:
        if sum(i) == x:
            c += 1
    print(c)