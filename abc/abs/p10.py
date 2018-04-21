c = [0, 0]
f = True
for _ in range(int(input())):
    t, x, y = map(int, input().split())
    if sum(c) + t < abs(x) + abs(y):
        f = False
    if t % 2 != abs(c[1] - y + c[0] - x) % 2:
        f = False
print(f and 'Yes' or 'No')

