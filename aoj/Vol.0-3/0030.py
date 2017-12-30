import itertools
while True:
    n,s = map(int, input().split())
    if not(n or s):
        break
    t = 0
    for i in itertools.combinations(range(0,10), n):
        if sum(i) == s:
            t += 1
    print(t)