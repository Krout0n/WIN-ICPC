import sys

N, Y = map(int, input().split())
c = [(i, j) for i,j in zip(range(N+1), range(N, -1, -1))]
x = -1
y = -1
z = -1

for i in c:
    if 9000*i[0] + 4000*i[1] + 1000*N == Y and not N - x - y < 0:
        x = i[0]
        y = i[1]
        z = N - x - y
        break
if not(x == y == z == -1):
    print(x,y,z)
    sys.exit(0)

for i in c:
    if -5000*i[0] + -9000*i[1] + 10000*N == Y and not N - z - y  < 0:
        y = i[0]
        z = i[1]
        x = N - z - y
        break

if not(x == y == z == -1):
    print(x,y,z)
    sys.exit(0)

for i in c:
    if 5000*i[0] - 4000*i[1] + 5000*N == Y and not N - x - z < 0:
        x = i[0]
        z = i[1]
        y = N - x - z
        break

print(x,y,z)
