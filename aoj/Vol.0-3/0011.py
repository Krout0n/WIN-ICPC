a = list(map(lambda x: x+1, range(int(input()))))
for _ in range(int(input())):
    m,n = map(lambda x: int(x)-1, input().split(','))
    a[m], a[n] = a[n],a[m]
for i in a:
    print(i)