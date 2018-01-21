f = True
for _ in range(int(input())):
    t, x, y = map(int, input().split())
    if t < abs(x) + abs(y) or t % 2 != abs(c[1] - y + c[0] - x) % 2:
        f = False
print(f and 'Yes' or 'No')
