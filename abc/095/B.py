N, X = map(int, input().split())
m = []
for i in range(N):
    m.append(int(input()))
c = N
X -= sum(m)
print(c + int(X/min(m)))
