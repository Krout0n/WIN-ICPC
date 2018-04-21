s = 0
n, a, b = map(int, input().split())
for i in range(n+1):
    if i < 10:
        h = i
    else:
        h = sum(list(map(int, list(str(i)))))
    if a <= h <=b:
        s += i
print(s)